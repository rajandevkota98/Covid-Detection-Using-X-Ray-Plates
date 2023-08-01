from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str


@dataclass
class DataValidationArtifact:
    valid_test_file_path: str
    valid_train_file_path: str
    report_file_path:str


@dataclass
class BaseModelArtifact:
    base_model_path:str


@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str


@dataclass
class ModelEvaluationArtifact:
    is_model_accepted: bool
    improved_accuracy:float
    best_model_file_path: str
    trained_model_file_path: str
    
@dataclass
class ModelPusherArtifact:
    saved_model_path:str
    model_file_path:str




