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
class ClassificationArtifact:
    model_f1_score:int
    model_precision_score:int
    model_recall_score:int
    model_accuracy:int
