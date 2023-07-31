from xray.exception import XrayException
from xray.logger import logging
from xray.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from xray.entity.artifact_entity import DataIngestionArtifact
import os, sys
from xray.constants.training_pipeline import TEST_FILE_NAME, TRAIN_FILE_NAME, FILE_NAME
import shutil

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            self.test_file_name  = TEST_FILE_NAME
            self.train_file_name = TRAIN_FILE_NAME
            self.file_name = FILE_NAME
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
            logging.info('Syncing data to directory')
            os.system(f"aws s3 sync s3://xray11/Dataset/ {data_path} --no-progress")

        except Exception as e:
                raise XrayException(e,sys)
        
    
    def preparing_data(self,):
         try:
              training_data_file_path = self.data_ingestion_config.training_data_file_path
              test_data_file_path = self.data_ingestion_config.test_data_file_path

              source_training_data_file_path = os.path.join(self.data_ingestion_config.feature_store_file_path, self.train_file_name)
              source_test_data_file_path = os.path.join(self.data_ingestion_config.feature_store_file_path, self.test_file_name)
              logging.info('copying training data')
              shutil.copytree(source_training_data_file_path,training_data_file_path)
              logging.info('completed copying training data')
              logging.info('copying test data')
              shutil.copytree(source_test_data_file_path,test_data_file_path)
              logging.info('completed copying test data')


         except Exception as e:
                raise XrayException(e,sys)
    

    def initiate_data_ingestion(self,):
        try:
            data = self.data_download()
            self.preparing_data()
            data_ingestion_artifact =DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_data_file_path, test_file_path=self.data_ingestion_config.test_data_file_path)
            logging.info('data ingestion completed successfully')
            logging.info(f'data ingestion artifact: {data_ingestion_artifact}')
            return data_ingestion_artifact
        except Exception as e:
                    raise XrayException(e,sys)

