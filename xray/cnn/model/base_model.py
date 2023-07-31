import os,sys
from xray.exception import XrayException
from xray.logger import logging
from xray.utils.common import read_yaml_file
from xray.entity.config_entity import BaseModelConfig
from xray.entity.artifact_entity import BaseModelArtifact
from xray.constants.training_pipeline import PARAMS_FILE_PATH
import tensorflow as tf



class BaseModel:
    def __init__(self, base_model_config: BaseModelConfig):
        try:
            self.base_model_config = base_model_config
            self._params_config = read_yaml_file(PARAMS_FILE_PATH)
        except Exception as e:
                raise XrayException(e)
        
    
    def get_base_model(self,):
        try:
            self.model = tf.keras.applications.vgg16.VGG16(
                input_shape=self._params_config["IMAGE_SIZE"],
                weights=self._params_config['WEIGHTS'],
                include_top=self._params_config['INCLUDE_TOP']
            )
            os.makedirs(os.path.dirname(self.base_model_config.base_model_path), exist_ok=True)
            self.model.save(self.base_model_config.base_model_path, overwrite= True)
            base_model_artifact = BaseModelArtifact(base_model_path=self.base_model_config.base_model_path)
            return base_model_artifact
        except Exception as e:
             raise XrayException(e,sys)





