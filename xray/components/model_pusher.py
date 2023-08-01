import os,sys
from xray.exception import XrayException
from xray.logger import logging
from xray.entity.artifact_entity import ModelPusherArtifact, ModelEvaluationArtifact, ModelTrainerArtifact
from xray.entity.config_entity import ModelPusherConfig
import shutil
import tensorflow as tf

class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig, model_evaluation_artifact: ModelEvaluationArtifact, model_trainer_artifact: ModelTrainerArtifact):
        try:
            self.model_pusher_config = model_pusher_config
            self.model_evaluation_artifact = model_evaluation_artifact
            self.model_trainer_artifact = model_trainer_artifact
        except Exception as e:
            raise XrayException(e, sys)
        
    def sync_data(self):
        try:
            logging.info('--------starting data sync-----------')
            trained_model_path = self.model_trainer_artifact.trained_model_file_path
            os.system(f'aws s3 sync {trained_model_path} s3://xraymodel11/Model/')  
            logging.info('ending the sync')
        except Exception as e:
            raise XrayException(e, sys)
        

    def initiate_model_pusher(self):
        try:
            trained_model_path = self.model_trainer_artifact.trained_model_file_path

            model_file_path = self.model_pusher_config.model_file_path
            os.makedirs(os.path.dirname(model_file_path), exist_ok=True)
            shutil.copyfile(trained_model_path, model_file_path)

            saved_model_path = self.model_pusher_config.saved_model_path
            os.makedirs(os.path.dirname(saved_model_path), exist_ok=True)
            shutil.copy(src=trained_model_path, dst=saved_model_path)

            model = tf.keras.models.load_model(model_file_path)

            model_pusher_artifact = ModelPusherArtifact(saved_model_path=saved_model_path, model_file_path=model_file_path)

            self.sync_data()

            return model, model_pusher_artifact

        except Exception as e:
            raise XrayException(e, sys)
