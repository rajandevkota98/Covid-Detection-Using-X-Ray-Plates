from xray.exception import XrayException
from xray.logger import logging
from xray.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from xray.entity.artifact_entity import DataIngestionArtifact
import os, sys

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise XrayException(e,sys)
        

    def data_download(self,):
        """
        It downloads images from the S3 bucket.
        
        """
        try:
            data_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(data_path)
            os.makedirs(dir_path,exist_ok=True)
            os.system(f"aws s3 sync s3://xray11/Dataset/ {data_path} --no-progress")

        except Exception as e:
                raise XrayException(e,sys)
    

    def initiate_data_ingestion(self,):
        try:
            data = self.data_download()
            data_ingestion_artifact =DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_data_file_path, test_file_path=self.data_ingestion_config.test_data_file_path)
            return data_ingestion_artifact
        except Exception as e:
                    raise XrayException(e,sys)

