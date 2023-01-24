from tensorflow import keras
import numpy as np
import model as md

def load_model():
    return keras.models.load_model("./models/model.h5")

def get_class(y_pred):
    return md.class_names[np.argmax(y_pred[0])]

def get_score(y_pred):
    return "{:.2f}%".format(y_pred[0][np.argmax(y_pred[0])] * 100)

def parse_query(input_img):
    return np.array([np.fromstring(input_img.replace("[", "").replace("]", "").replace(" ", ""), sep=";").reshape(28,28)])
