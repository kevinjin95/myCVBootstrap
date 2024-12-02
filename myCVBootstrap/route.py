from flask import render_template, url_for
from myCVBootstrap import app
@app.route("/")
@app.route("/home")
def home_page():
    return render_template('index.html')