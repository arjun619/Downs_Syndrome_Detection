from flask import Flask,render_template,request
from flask import *

app = Flask("yourweb")
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/second")
def secondpage():
    return render_template("upload.html")

@app.route("/negative")
def negativepage():
    return render_template("negative.html")

@app.route("/positive")
def positivepage():
    return render_template("positive.html")

@app.route("/detector",methods=["POST"])
#takes the file upload variable from html form and saves the image in local directory
def thirdpage():
    #return request.form.get("myimage")
    try:
        f = request.files['file']
    except IOError:
        return "Failure"
    f.save(f.filename)

    return "success"
app.run(debug=True)
