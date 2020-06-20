# basic tensorflow example from tensorflow.org tutorial (with added comments to help me learn)

# Tensorflow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

# returns training set (the data the model uses to learn), and is tested against the test set
# images are 28x28 NumPy arrays, with pixel values ranging from 0 to 255, labels are ints 0-9,
# corresponding to the class of clothing the image represents
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# these are the labels, the index corresponds to the label
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# scale values of images from 0-255 to 0-1
train_images = train_images / 255.0
test_images = test_images / 255.0

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    # cmap=plt.cm.binary is what turns it to grayscale
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    # plt.colorbar() can show colorbar next to each if want to
    plt.xlabel(class_names[train_labels[i]])
plt.show()

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)), # flatten 2d array into 1d array
    keras.layers.Dense(128, activation='relu'), # first neural layer
    keras.layers.Dense(10) # second (last) neural layer, each node containing score of belonging to one of 10 classes
])

# model compilation with loss function, optimizer, and metrics (set to check accuracy)
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# fits the training data to the created model, starts training 10 times
model.fit(train_images, train_labels, epochs=10)

# compare how the model performs on the test dataset
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)