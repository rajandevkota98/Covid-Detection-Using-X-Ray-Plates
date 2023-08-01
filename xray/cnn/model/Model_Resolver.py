from xray.exception import XrayException
from xray.logger import logging
from xray.constants.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME
import os,sys

class ModelResolver:

    def __init__(self, model_dir = SAVED_MODEL_DIR):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise XrayException(e,sys)
    
    def SOTA_model(self,):
        try:
            timestamp = list(map(int, os.listdir(self.model_dir)))
            latest_timestamp = max(timestamp)
            latest_model_path = os.path.join(self.model_dir, f"{latest_timestamp}",MODEL_FILE_NAME)
            return latest_model_path
        except Exception as e:
            raise XrayException(e,sys)
        

    def is_model_exists(self):
        try:
            if not os.path.exists(self.model_dir):
                return False
            timestamp = os.listdir(self.model_dir)
            if len(timestamp) == 0:
                return False
            latest_model_path = self.SOTA_model()
            if not os.path.exists(latest_model_path):
                return False
            return True
        except Exception as e:
            raise XrayException(e,sys)