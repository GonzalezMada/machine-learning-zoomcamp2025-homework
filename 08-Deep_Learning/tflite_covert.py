from tensorflow import keras
import tensorflow as tf
model = keras.models.load_model('/workspaces/machine-learning-zoomcamp2025-homework/08-Deep_Learning/clothes_classification_model.h5')

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with open('/workspaces/machine-learning-zoomcamp2025-homework/08-Deep_Learning/clothes_classification_model.tflite', 'wb') as f:
    f.write(tflite_model)