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
