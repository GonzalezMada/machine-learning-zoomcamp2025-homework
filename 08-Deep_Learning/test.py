import numpy as np
import os
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.preprocessing.image import load_img, img_to_array

print(os.getcwd())
model = keras.models.load_model('/workspaces/machine-learning-zoomcamp2025-homework/08-Deep_Learning/clothes_classification_model.h5')


image_path = '/workspaces/machine-learning-zoomcamp2025-homework/08-Deep_Learning/image_t-shirt.jpg'
img = load_img(image_path, target_size=(150, 150))
img_array = img_to_array(img)
print(img_array.shape)
img_array = np.expand_dims(img_array, axis=0)

predictions = model.predict(img_array)
predicted_class = np.argmax(predictions, axis=1)
labels = ['dress', 'hat', 'longsleeve', 'outwear', 'pants', 'shirt', 'shoes', 'shorts', 'skirt', 't-shirt']
print(f'The predicted class is: {labels[predicted_class[0]]}')


