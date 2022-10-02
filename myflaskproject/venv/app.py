from flask import Flask, render_template, request
from markupsafe import escape
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route("/home/<name>")
def home(name):
    return render_template("home.html", name=name)

@app.route("/<name>")
def hell(name):
    return f"Hello, {escape(name)}!"

@app.route("/home/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join(app.instance_path, "../../templates/upload.png"))
        return "success"
