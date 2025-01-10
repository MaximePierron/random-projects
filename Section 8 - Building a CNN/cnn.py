# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:11:08 2024

@author: MPEIRRON
"""

#Build the CNN
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D, Dropout, Flatten, Dense

#Initialise CNN
classifier = Sequential()

#Add Convolution layer
classifier.add(
    Convolution2D(
        filters=32,
        kernel_size=3,
        input_shape=(64, 64, 3),
        activation='relu'
    )
)

#Add Convolution layer
classifier.add(
    Convolution2D(
        filters=32,
        kernel_size=3,
        activation='relu'
    )
)

#Add Convolution layer
classifier.add(
    Convolution2D(
        filters=32,
        kernel_size=3,
        activation='relu'
    )
)

#Add Convolution layer
classifier.add(
    Convolution2D(
        filters=32,
        kernel_size=3,
        activation='relu'
    )
)

#Pooling
classifier.add(MaxPooling2D())

#Flattening
classifier.add(Flatten())

#Fully connected layer
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dropout(0.3))
classifier.add(Dense(units=1, activation='sigmoid'))

#The CNN structure is set
#Compile the CNN
classifier.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

#Fit CNN on pictures
# this is the augmentation configuration we will use for training
from keras.preprocessing.image import ImageDataGenerator

batch_size = 32

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1./255)

# this is a generator that will read pictures found in
# subfolers of 'data/train', and indefinitely generate
# batches of augmented image data
training_set = train_datagen.flow_from_directory(
        'dataset/training_set',  # this is the target directory
        target_size=(64, 64),  # all images will be resized to 150x150
        batch_size=batch_size,
        class_mode='binary')  # since we use binary_crossentropy loss, we need binary labels

# this is a similar generator, for validation data
test_set = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(64, 64),
        batch_size=batch_size,
        class_mode='binary')

classifier.fit_generator(
        training_set,
        steps_per_epoch=8000 // batch_size,
        epochs=75,
        validation_data=test_set,
        validation_steps=2000 // batch_size)

classifier.save_weights('third_try.h5')  # always save your weights after training or during training

#Train a single image

from keras.preprocessing import image
import numpy as np

# Load the image
test_image = image.load_img('dataset/single_prediction/cat_or_dog_1.jpg', target_size=(64, 64))

# Convert the image to an array
test_image = image.img_to_array(test_image)

# Rescale the image
test_image = test_image / 255.0

# Expand the dimensions of the array
test_image = np.expand_dims(test_image, axis=0)

# Predict the class of the image
result = classifier.predict(test_image)

# Get the class indices
training_set.class_indices

# Interpret the result
if result[0][0] == 1:
    prediction = 'Dog'
else:
    prediction = 'Cat'

print(prediction)