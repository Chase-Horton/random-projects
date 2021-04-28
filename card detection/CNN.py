# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:49:47 2020

@author: Chase
"""

import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import cv2
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import matplotlib.pyplot as plt
batch_size = 32

trainGen = ImageDataGenerator().flow_from_directory('pictures/train', target_size = (635, 850), batch_size = batch_size, class_mode =  'categorical', color_mode = "grayscale")

testGen = ImageDataGenerator().flow_from_directory('pictures/test', target_size = (635, 850), batch_size = batch_size, class_mode =  'categorical', color_mode = "grayscale")
model = Sequential()
model.add(Conv2D(64, kernel_size = 3, activation="relu", input_shape = (635, 850, 1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit_generator(
        trainGen,
        steps_per_epoch=1500 // batch_size,
        epochs=10,
        validation_data=testGen,
        validation_steps=500 // batch_size)
model.save_weights('first_try.h5')

