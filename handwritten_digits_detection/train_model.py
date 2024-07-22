import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Input, Conv2D, MaxPool2D, Dropout, Activation, Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# Loading MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# One-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

_,X_train_th = cv2.threshold(x_train,127,255,cv2.THRESH_BINARY)
_,X_test_th = cv2.threshold(x_test,127,255,cv2.THRESH_BINARY)

x_train = X_train_th/255
x_test = X_test_th/255

x_test = x_test.reshape(-1,28,28,1)
x_test = x_test.reshape(-1,28,28,1)

model = Sequential([
    Input(shape=(28, 28,1)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

model.save('model/digit_recognition_model.keras') 