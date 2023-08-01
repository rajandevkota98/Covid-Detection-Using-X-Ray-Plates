from datetime import datetime
import os, sys
from xray.constants import training_pipeline

class TrainingPipelineConfig:
    def __init__(self, timestamp = datetime.now()):
        timestamp = timestamp.strftime('%Y_%m_%d_%H_%M_%S')
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_dir: str = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp)
        self.timestamp = timestamp


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path: str = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME)
        self.training_data_file_path: str = os.path.join(self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_NAME)
        self.test_data_file_path :str = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME)

class DataValidationConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.valid_train_file_path: str = os.path.join(self.valid_data_dir, training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path: str = os.path.join(self.valid_data_dir, training_pipeline.TEST_FILE_NAME)
        self.data_report_file_path:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_DATA_REPORT_DIR, training_pipeline.DATA_VALIDATION_DATA_REPORT_FILE_NAME)


class BaseModelConfig:
    def __init__(self,):
        self.base_model_dir_name:str = os.path.join(training_pipeline.BASE_MODEL_DIR_NAME)
        self.base_model_path: str = os.path.join(self.base_model_dir_name,training_pipeline.BASE_MODEL_NAME )


class ModelTrainerConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.trained_model_dir_name: str = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.MODEL_TRAINER_DIR_NAME)
        self.trained_model_file_path:str = os.path.join(self.trained_model_dir_name, training_pipeline.MODEL_TRAINER_MODEL_NAME)
        self.expected_accuracy = training_pipeline.EXPECTED_ACCURACY
        self.overfit_threshold = training_pipeline.OVERFIT_THRESHOLD

        
class ModelEvaluationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.model_evaluation_dir_name: str =os.path.join(training_pipeline_config.artifact_dir, training_pipeline.MODEL_EVALUATION_DIR_NAME)
        self.model_evaluation_threshold = training_pipeline.MODEL_EVALUATION_CHANGED_THRESHOLD
        self.model_evaluation_report_path = os.path.join(self.model_evaluation_dir_name,training_pipeline.MODEL_EVALUATION_REPORT_NAME)
    
        

class ModelPusherConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.model_pusher_dir = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.MODEL_PUSHER_DIR_NAME)
        self.model_file_path = os.path.join(self.model_pusher_dir, training_pipeline.MODEL_FILE_NAME)
        timestamp = round(datetime.now().timestamp())
        self.saved_model_path = os.path.join(training_pipeline.SAVED_MODEL_DIR,f"{timestamp}",training_pipeline.MODEL_FILE_NAME)