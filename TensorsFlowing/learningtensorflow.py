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

