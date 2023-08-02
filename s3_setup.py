import os
import sys
from zipfile import ZipFile
import shutil
from xray.exception import XrayException
from xray.logger import logging

class DataStore:
    def __init__(self,):
        self.root = os.path.join(os.getcwd(),'data')
        self.zip = os.path.join(self.root, 'archive.zip')
        self.images = os.path.join(self.root, 'Dataset')
        self.list_unwanted = ['Prediction']

    def prepare_data(self,):
        try:
            logging.info('Extracting Data')
            with ZipFile(self.zip,'r') as file:
                file.extractall(path=self.root)
            file.close()
        except Exception as e:
            raise  XrayException(e,sys)
        
    def remove_unwanted(self,):
        try:
            for unwanted in self.list_unwanted:
                path = os.path.join(self.images,unwanted)
                shutil.rmtree(path, ignore_errors=True)
        except Exception as e:
            raise XrayException(e,sys)
        
    def sync_data(self,):
        try:
            logging.info('--------starting data sync-----------')
            os.system(f'aws s3 sync {self.images} s3://xray11/Dataset/')
            logging.info('ending the sync')
        except Exception as e:
            raise XrayException(e,sys)

s = DataStore()
s.prepare_data()
s.remove_unwanted()
s.sync_data()
