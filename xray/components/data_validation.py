from xray.exception import XrayException
from xray.logger import logging
from xray.utils.common import read_yaml_file,write_yaml_file
from xray.entity.config_entity import DataValidationConfig
from xray.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
import os, sys
from xray.constants.training_pipeline import CONFIG_FILE_PATH
from PIL import Image

class DataValidation:
    def __init__(self, data_ingestion_artifact:DataIngestionArtifact, data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._config = read_yaml_file(CONFIG_FILE_PATH)
            self.report = {}
        except Exception as e:
            raise XrayException(e,sys)
        
    def check_label(self,dir_path:str):
        try:
            num_directory = 0
            label =self._config['label']
            logging.info('checking label')
            for entry in os.scandir(dir_path):
                if entry.is_dir():
                    num_directory += 1
            if num_directory == label:
                self.report['number_of_labels'] =num_directory
                logging.info('checking labels done')
                return True
            else:
                raise Exception(f'{dir_path} Label are distrubed')
        except Exception as e:
            raise XrayException(e,sys)
        

    def check_if_valid(self,image_path:str):

        """
        To check if the path is image or not.
        
        """
        try:
            image = Image.open(image_path)
            image.verify()
            return True
        except Exception as e:
            raise XrayException(e,sys)


    def check_image_or_not(self, image_dir:str):

        """
        To check if the directory contain only image or not
        """
        try:
            logging.info('checking images')
            labels = ['Covid', 'Normal']
            for label in labels:
                num_image = 0
                label_dir = os.path.join(image_dir, label)
                if not os.path.exists(label_dir):
                    raise Exception(f'{label_dir} doesn;t exist')

                for image in os.listdir(label_dir):
                    image_path = os.path.join(label_dir,image)
                    if self.check_if_valid(image_path):
                        num_image += 1
                    else:
                        raise Exception(f'{image_path} is not a valid image in the {label} directory')
                self.report[f"No of images on {image_dir}"]= num_image
            return True 
        except Exception as e:
            raise XrayException(e,sys)
    
    def write_report(self,):
        logging.info("Writing report")
        report_file_path = self.data_validation_config.data_report_file_path
        dir_path = os.path.dirname(report_file_path)
        os.makedirs(dir_path, exist_ok=True)
        write_yaml_file(file_path=report_file_path, content=self.report)

    def initiate_data_validation(self,):
        try:
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            self.check_label(train_file_path)
            self.check_label(test_file_path)
            self.check_image_or_not(train_file_path)
            self.check_image_or_not(test_file_path)
            self.write_report()

            data_validation_artifact = DataValidationArtifact(valid_test_file_path=self.data_ingestion_artifact.test_file_path, valid_train_file_path= self.data_ingestion_artifact.trained_file_path,report_file_path= self.data_validation_config.data_report_file_path)
            logging.info('Validated Successfully')
            logging.info(f'Data Validation artifact {data_validation_artifact}')
            return data_validation_artifact

        except Exception as e:
            raise XrayException(e,sys)



