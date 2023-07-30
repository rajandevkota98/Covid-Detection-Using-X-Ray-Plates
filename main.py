import os, sys
from xray.exception  import XrayException
from xray.logger import logging
from xray.pipeline.training_pipeline import Trainipipeline


train_pipeline = Trainipipeline()

if __name__ == "__main__":
    try:
        train_pipeline.run_pieline()
    except Exception as e:
        raise XrayException(e,sys)            