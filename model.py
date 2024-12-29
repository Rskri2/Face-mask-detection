import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
model = load_model('model.h5')

def prepare_image(file):
    img = image.load_img(file, target_size = (224, 224))
    img_array = image.img_to_array(img)
    return tensorflow.keras.applications.mobilenet.preprocess_input(img_array)

def predict_output(img):
    pred = model.predict(img.reshape(1, 224, 224, 3))
    return pred[0]

