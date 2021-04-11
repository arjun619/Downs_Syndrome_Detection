import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img

def predict(image):
    #return tf.keras.preprocessing.image.img_to_array(load_img("C:\\Users\\arjun\\Desktop\pics\\2nddec.PNG"))
    return tf.keras.preprocessing.image.img_to_array(load_img(image))
    
