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
PARAMS_FILE_NAME: str ='params.yaml'

"""Data ingestion constant"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"


