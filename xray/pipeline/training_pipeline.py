from xray.exception import XrayException
from xray.logger import logging
from xray.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig
from xray.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
import os, sys
from xray.components.data_ingestion import DataIngestion
from xray.components.data_validation import DataValidation


class  Trainipipeline:
    def __init__(self,):
        self.training_pipeline_config = TrainingPipelineConfig()
    
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact
        except XrayException as e:
            raise XrayException(e,sys)
        
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact)->DataValidationArtifact:
         try:
            logging.info("Starting data validation")
            self.data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_validation_config=self.data_validation_config,data_ingestion_artifact= data_ingestion_artifact )
            data_validation_artifact = data_validation.initiate_data_validation()

         except XrayException as e:
                     raise XrayException(e,sys)
         
    def run_pieline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact)

        except XrayException as e:
                raise XrayException(e,sys)