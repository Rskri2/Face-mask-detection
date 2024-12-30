from flask import Flask, render_template, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from helper import prepare_image, predict_output

app = Flask(__name__)
CORS(app)

def predict_val(filename):
    img = prepare_image('images/'+filename)
    output = predict_output(img)
    return output

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route('/submit', methods = ["POST"])
def submit():
    if 'file' not in request.files:
        return "File not uploaded"
    
    file = request.files["file"]
    if file.filename == ' ':
        return "File not uploaded"
    filename = secure_filename(file.filename)
    file.save('images/'+filename)
    
    output = predict_val(filename)
    
    if output >= 0.5:
        return render_template('mask.html', Mask = "Not Wearing mask")
    else :
        return render_template('mask.html', Mask = "Wearing Mask")


if __name__ == "__main__":
    app.run(debug=True)