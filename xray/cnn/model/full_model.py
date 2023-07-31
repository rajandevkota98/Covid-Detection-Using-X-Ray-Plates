from xray.exception import XrayException
from xray.logger import logging
from xray.entity.artifact_entity import BaseModelArtifact
from xray.entity.config_entity import BaseModelConfig
import tensorflow as tf
import os, sys
from xray.cnn.model.base_model import BaseModel




class XrayModel:
    def __init__(self,base_model_path):
        self.base_model_path = base_model_path
        self.base_model = tf.keras.models.load_model(self.base_model_path)
        self.conv1 = tf.keras.layers.Conv2D(32, (3,3), activation='relu')
        self.conv2 = tf.keras.layers.Conv2D(32, (3,3), activation = 'relu')
        self.conv3 = tf.keras.layers.Conv2D(32, (3,3), activation = 'relu')
        self.conv4 = tf.keras.layers.Conv2D(8, (1,1), activation ='relu')
        self.global_avg_pool = tf.keras.layers.GlobalAveragePooling2D()
        self.output_layer = tf.keras.layers.Dense(1, activation='sigmoid')
        

    def create_model(self,):
        try:
            self.base_model.trainable = True
            set_trainable = False
            for layer in self.base_model.layers:
                if layer.name=='block5_conv1':
                    set_trainable= True
                if set_trainable:
                    layer.trainable = True
                else:
                    layer.trainable= False
            x = self.base_model.get_layer('block5_conv1').output
            x = self.conv1(x)
            x = self.conv2(x)
            x = self.conv3(x)
            x = self.conv4(x)
            x = self.global_avg_pool(x)
            pred = self.output_layer(x)
            model = tf.keras.Model(inputs = self.base_model.input, outputs = pred )
            return model

        except Exception as e:
            raise XrayException(e,sys)





