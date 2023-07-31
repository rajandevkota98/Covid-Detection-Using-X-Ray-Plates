import os
from xray.constants.s3_bucket import TRAINING_BUCKET_NAME


####
PIPELINE_NAME = 'xray'
SAVED_MODEL_DIR = os.path.join('saved_models')
ARTIFACT_DIR: str = 'artifact'
FILE_NAME: str ='Dataset'
TRAIN_FILE_NAME: str ='Train'
TEST_FILE_NAME: str ='Val'
MODEL_FILE_NAME: str = 'model.h5'
PARAMS_FILE_PATH: str ='params/params.yaml'
CONFIG_FILE_PATH: str = 'config/config.yaml'

"""Data ingestion constant"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"


"""Data Validation Constant"""
DATA_VALIDATION_DIR_NAME:str = 'data_validation'
DATA_VALIDATION_VALID_DIR:str = 'validated'
DATA_VALIDATION_DATA_REPORT_DIR:str = 'data_report'
DATA_VALIDATION_DATA_REPORT_FILE_NAME:str = 'report.yaml'


"""Base Model"""
BASE_MODEL_DIR_NAME:str = 'base_models'
BASE_MODEL_NAME: str = 'base_model.h5'

