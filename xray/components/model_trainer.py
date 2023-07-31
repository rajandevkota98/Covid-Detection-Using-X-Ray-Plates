from xray.exception import XrayException
from xray.logger import logging
from xray.cnn.model.full_model import XrayModel
from xray.entity.artifact_entity import ModelTrainerArtifact, BaseModelArtifact, DataIngestionArtifact
from xray.entity.config_entity import ModelTrainerConfig
from xray.cnn.model.full_model import XrayModel
import os, sys
from utils.common import read_yaml_file
from xray.constants.training_pipeline import PARAMS_FILE_PATH
import tensorflow as tf

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig, base_model_artifact: BaseModelArtifact, data_ingestion_artifact: DataIngestionArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.base_model_artifact = base_model_artifact
            self.data_ingestion_artifact = data_ingestion_artifact
            self._params_schema = read_yaml_file(PARAMS_FILE_PATH)
        except Exception  as e:
            raise XrayException(e,sys)        
        
    def model_training(self,) -> None:
        try:
            xraymodel = XrayModel(base_model_path= self.base_model_artifact)
            self.model = xraymodel.create_model()

            self.model.compile(optimizer=self._params_schema['OPTIMIZER'], loss= self._params_schema['LOSS'],metrics=self._params_schema['METRICS'])
            train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1.0 / 255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)

            test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0 / 255)

            train_data = train_datagen.flow_from_directory(
            self.data_ingestion_artifact.trained_file_path,
            target_size=self._params_schema['IMAGE_SIZE'],
            batch_size=self._params_schema['BATCH_SIZE'],
            class_mode='binary')


            test_data = test_datagen.flow_from_directory(
            self.data_ingestion_artifact.trained_file_path,
            target_size=self._params_schema['IMAGE_SIZE'],
            batch_size=self._params_schema['BATCH_SIZE'],
            class_mode='binary')

            self.model.fit(
                train_data,
                steps_per_epoch=len(train_data),
                epochs=self._params_schema['EPOCHS'],
                validation_data=test_data,
                validation_steps=len(test_data)
            )
            


            os.makedirs(os.path.dirname(self.model_trainer_config.trained_model_file_path), exist_ok=True)
            self.model.save(self.model_trainer_config.trained_model_dir_name, overwrite= True)





            
        except Exception as e:
            raise XrayException(e,sys)

