import os,sys
from xray.exception import XrayException
from xray.logger import logging
from xray.cnn.model.Model_Resolver import ModelResolver
import pandas as pd
import tensorflow as tf
from datetime import datetime
PREDICTION_DIR = 'prediction'

# def start_bluk_prediction(directory: str):
