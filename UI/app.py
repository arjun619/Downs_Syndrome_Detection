from flask import Flask,render_template,request
from flask import *

app= Flask("yourweb")


@app.route("/second")
def secondpage():
    return render_template("htform.html")

@app.route("/detector",methods=["POST"])

#takes the file upload variable from html form and saves the image in local directory
def thirdpage():
    #return request.form.get("myimage")
    f= request.files['fileToUpload']
     
    f.save(f.filename)  
    
    return "success"
    
app.run(debug=True)
