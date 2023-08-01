import os,sys
from xray.exception import XrayException
from xray.logger import logging
from xray.cnn.model.Model_Resolver import ModelResolver
import pandas as pd
import tensorflow as tf
from datetime import datetime
from zipfile import ZipFile
import cv2
import shutil
from xray.constants.training_pipeline import PARAMS_FILE_PATH
from xray.utils.common import read_yaml_file, write_yaml_file
from xray.constants.training_pipeline import SAVED_MODEL_DIR
import numpy as np
from xray.constants.prediction_pipeline import PREDICTION_DIR, PREDICTED_DIR,REPORT_NAME
os.makedirs(PREDICTION_DIR, exist_ok=True)
os.makedirs(PREDICTED_DIR, exist_ok=True)
zip_file_save = 'zip_archieve'
os.makedirs(zip_file_save, exist_ok=True)



from xray.cnn.model.mapping import TargetMapping
target_size = read_yaml_file(PARAMS_FILE_PATH)["TARGET_SIZE"]
target_map = TargetMapping()

def preprocess_image(image_path, target_size = target_size):
    img = cv2.imread(image_path)
    img = cv2.imread(image_path)
    if img is None:
        raise Exception(f"Error: Unable to read image at '{image_path}'")
    img = cv2.resize(img, target_size)
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)  
    return img




def bulk_prediction(zip_file, save_path=PREDICTION_DIR):
    dict_ = {}
    with ZipFile(zip_file, 'r') as file:
        file.extractall(save_path)
    logging.info('Getting the Test file location')
    file_path = os.path.join(save_path, os.listdir(save_path)[0])

    logging.info('Loading the model')
    model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
    best_model_path = model_resolver.SOTA_model()
    model = tf.keras.models.load_model(best_model_path)

    for image in os.listdir(file_path):
        image_path = os.path.join(file_path, image)
        print(f"Processing image: {image_path}")
        try:
            img = preprocess_image(image_path, target_size)
            prediction = model.predict(img)
            class_index = 0 if prediction[0][0] < 0.5 else 1
            logging.info('Prediction')
            predicted_class = target_map.reverse_mapping()[class_index]
            dict_[image] = f"{predicted_class}"
            predicted_file_path = os.path.join(PREDICTED_DIR, predicted_class)
            os.makedirs(predicted_file_path, exist_ok=True)
            shutil.copy(image_path, predicted_file_path)
        except Exception as e:
            raise XrayException(e, sys)
    report_file_path = os.path.join(PREDICTED_DIR, REPORT_NAME)
    write_yaml_file(report_file_path, dict_)
    shutil.rmtree(file_path)
    zip_file_path=shutil.make_archive(base_name='predicted1', format='zip', root_dir=PREDICTED_DIR)
    print(zip_file_path)
    return zip_file_path
    




    

def single_prediction(image_path):
    img = preprocess_image(image_path)
    model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
    best_model_path = model_resolver.SOTA_model()
    model = tf.keras.models.load_model(best_model_path)
    prediction = model.predict(img)
    class_index = 0 if prediction[0][0] < 0.5 else 1
    predicted_class = target_map.reverse_mapping()[class_index]
    return predicted_class    
    

bulk_prediction('test.zip')





    
