from flask import Flask,jsonify, render_template, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from model import prepare_image, predict_output

app = Flask(__name__)
CORS(app)
@app.route("/")

def predict(filename):
    img = prepare_image('images/'+filename)
    output = predict_output(img)
    return output
    
def welcome():
    return render_template("index.html")

@app.route('/submit', methods = ["POST"])
def submit():
    if 'file' not in request.files:
        return jsonify({"message":"File not uploaded"}), 400
    
    file = request.files["file"]
    if file.filename == ' ':
        return jsonify({"message":"File not uploaded"}), 400
    filename = secure_filename(file.filename)
    file.save('images/'+filename)
    
    output = predict(filename)
    
    if output >= 0.5:
        return jsonify({"message":"Not wearing the mask"}), 201
    else :
        return jsonify({"message":"Wearing the mask"}), 201

if __name__ == "__main__":
    app.run(debug=True)