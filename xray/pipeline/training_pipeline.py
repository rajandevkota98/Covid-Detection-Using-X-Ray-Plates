from xray.exception import XrayException
from xray.logger import logging
from xray.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from xray.entity.artifact_entity import DataIngestionArtifact
import os, sys
from xray.components.data_ingestion import DataIngestion


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
        
    def run_pieline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except XrayException as e:
                raise XrayException(e,sys)