import yaml
from xray.exception import XrayException
from xray.logger import logging
import os,sys
import numpy as np


def read_yaml_file(file_path: str)->dict:
    try:
        logging.info('Reading Yaml File')
        with open(file_path, 'r') as stream:
            return yaml.safe_load(stream)
    except Exception as e:
        raise XrayException(e,sys)

def write_yaml_file(file_path: str, content: object, replace:bool=False)->None:
    try: 
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            yaml.dump(content, file)
    except Exception as e:
        raise XrayException(e,sys)


