from xray.exception import XrayException
from xray.logger import logging
from xray.entity.artifact_entity import ClassificationArtifact
from sklearn.metrics import f1_score,precision_score,recall_score,accuracy_score
import os,sys

def get_classification_score(y_true, y_pred):
    try:
        logging.info('Getting Classification Score')
        model_f1_score=  f1_score(y_true, y_pred)
        model_precision_score = precision_score(y_true, y_pred)
        model_recall_score = recall_score(y_true, y_pred)
        model_accuracy = accuracy_score(y_true, y_pred)
        classification_artifact = ClassificationArtifact(model_f1_score=model_f1_score,model_precision_score=model_precision_score, model_recall_score=model_recall_score, model_accuracy=model_accuracy)
        return classification_artifact
    except Exception as e:
        raise XrayException(e,sys)