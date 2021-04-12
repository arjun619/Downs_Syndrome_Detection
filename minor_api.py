from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow import keras
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/')
def fun():
    return render_template("check.html")

@app.route('/c', methods=['GET', 'POST'])
def fun2():
    file = request.files['fileToUpload']
    if file.filename == '':
            flash('No selected file')
            return redirect(url_for('fun'))
    file.filename = "kapil.jpg"
    file.save(file.filename)
    #image = Image.open('kapil.jpg')
    #image = image.resize((224, 224))
    #image.save('kapil.jpg')
    arr=tf.keras.preprocessing.image.img_to_array(load_img("kapil.jpg",target_size=(224,224)))
    arr = arr.reshape(1,224,224,3)
    print(arr)
    model = keras.models.load_model('facedetect.h5')
    result = model.predict(arr)
    if(result[0][0]==1.):
            return("negative")
    else:
            return("positive")

if __name__ == "__main__":
    app.run(debug=True)