import os
import sys
from xray.exception import XrayException
from xray.logger import logging
from xray.cnn.model.Model_Resolver import ModelResolver
import pandas as pd
from datetime import datetime
from zipfile import ZipFile
import tensorflow as tf


PREDICTION_DIR = 'prediction'
PREDICTED_DIR = 'predicted'
from xray.constants.training_pipeline import SAVED_MODEL_DIR
os.makedirs(PREDICTION_DIR, exist_ok=True)
os.makedirs(PREDICTED_DIR, exist_ok=True)


def bulk_prediction(zip_file, save_path=PREDICTION_DIR):
    with ZipFile(zip_file, 'r') as file:
        file.extractall(save_path)
        file.close()
    test_data_file = os.path.join(save_path,os.listdir(save_path)[0])

    model_resolver = ModelResolver(SAVED_MODEL_DIR)
    model_path = model_resolver.SOTA_model()
    model = tf.keras.models.load_model(model_path)
    


bulk_prediction('archive.zip')