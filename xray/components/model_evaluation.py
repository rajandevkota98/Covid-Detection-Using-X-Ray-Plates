from xray.exception import XrayException
from xray.logger import logging
from xray.entity.artifact_entity import DataIngestionArtifact, ModelTrainerArtifact, ModelEvaluationArtifact
from xray.entity.config_entity import ModelEvaluationConfig
import os, sys
from xray.utils.common import write_yaml_file, read_yaml_file
from xray.constants.training_pipeline import PARAMS_FILE_PATH
import tensorflow as tf
from xray.cnn.model.Model_Resolver import ModelResolver


class ModelEvaluation:
    def __init__(self, model_evaluation_config: ModelEvaluationConfig, data_ingestion_artifact: DataIngestionArtifact, model_trainer_artifact: ModelTrainerArtifact):
        try:
            self.model_evaluation_config = model_evaluation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self._params_schema = read_yaml_file(PARAMS_FILE_PATH)

        except Exception as e:
            raise XrayException(e,sys)
        
    
    def initiate_model_evaluation(self,):
        try:
            test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0 / 255)
            test_data = test_datagen.flow_from_directory(
                    self.data_ingestion_artifact.test_file_path,
                    target_size=self._params_schema['TARGET_SIZE'],
                    batch_size=self._params_schema['BATCH_SIZE'],
                    class_mode='binary')
            
            logging.info('Getting Recently Trained Model')
            trained_model_file_path = self.model_trainer_artifact.trained_model_file_path
            model_resolver = ModelResolver()
            is_model_accepted = True

            if not model_resolver.is_model_exists():
                 logging.info('No saved model found')
                 model_evaluation_artifact = ModelEvaluationArtifact(is_model_accepted= is_model_accepted,improved_accuracy= None,
                                                                      best_model_file_path=None, trained_model_file_path=trained_model_file_path)
                 return model_evaluation_artifact

            
            logging.info('Best model found')
            best_model_file_path =model_resolver.SOTA_model()
            best_model = tf.keras.models.load_model(best_model_file_path)

            _,best_model_accuracy = best_model.evaluate(test_data,steps = len(test_data))
            logging.info(f"best_model_accuracy: {best_model_accuracy}")


            recent_trained_model = tf.keras.models.load_model(trained_model_file_path)
            _,recent_model_accuracy = recent_trained_model.evaluate(test_data,steps = len(test_data))
            logging.info(f"recent_model_accuracy: {recent_model_accuracy}")

            improved_accuracy = recent_model_accuracy - best_model_accuracy
            logging.info(f'improved_accuracy: {improved_accuracy}')

            if self.model_evaluation_config.model_evaluation_threshold < improved_accuracy:
                 is_model_accepted = True
            else:
                 is_model_accepted = False
            
            model_evaluation_arifact = ModelEvaluationArtifact(is_model_accepted=is_model_accepted, improved_accuracy=improved_accuracy,trained_model_file_path=trained_model_file_path, best_model_file_path=best_model_file_path)
            logging.info(f'model_evaluation_arifact:{model_evaluation_arifact}')
            model_evalutaion_report = model_evaluation_arifact.__dict__
            report_file_path = self.model_evaluation_config.model_evaluation_report_path
            dir_path = os.path.dirname(report_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info('writing model evaluation report')
            write_yaml_file(self.model_evaluation_config.model_evaluation_report_path,model_evalutaion_report)
            return model_evaluation_arifact

        except Exception as e:
                raise XrayException(e,sys)

 