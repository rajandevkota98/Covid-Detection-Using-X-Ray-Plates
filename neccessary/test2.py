from xray.entity.artifact_entity import BaseModelArtifact
import tensorflow as tf
import numpy as np
import tensorflow as tf

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 8
NUM_EPOCHS = 1

conv_base = tf.keras.models.load_model('base_models/base_model.h5')
conv_base.trainable = True
set_trainable = False
for layer in conv_base.layers:
  print(layer.name)
for layer in conv_base.layers:
  if layer.name=='block5_conv1':
    set_trainable= True
  if set_trainable:
    layer.trainable = True
  else:
    layer.trainable= False


for layer in conv_base.layers:
  print(layer.name, layer.trainable)

x = conv_base.get_layer('block5_conv1').output

x = tf.keras.layers.Conv2D(32, (3, 3), activation='relu')(x)
x = tf.keras.layers.Conv2D(32, (3, 3), activation='relu')(x)
x = tf.keras.layers.Conv2D(32, (3, 3), activation='relu')(x)
x = tf.keras.layers.Conv2D(8, (1, 1), activation='relu')(x)
x = tf.keras.layers.GlobalAveragePooling2D()(x)
predictions = tf.keras.layers.Dense(1, activation='sigmoid')(x)

model = tf.keras.Model(inputs=conv_base.input, outputs=predictions)
model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1.0 / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)


test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0 / 255)


train_data = train_datagen.flow_from_directory(
    'artifact/2023_07_30_14_41_26/data_ingestion/ingested/Train',
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary'
)
test_data = test_datagen.flow_from_directory(
    'artifact/2023_07_30_14_41_26/data_ingestion/ingested/Val',
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

model.fit(
    train_data,
    steps_per_epoch=len(train_data),
    epochs=NUM_EPOCHS,
    validation_data=test_data,
    validation_steps=len(test_data)
)
