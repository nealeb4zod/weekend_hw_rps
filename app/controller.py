from flask import render_template
from app import app
from app.models.


@app.route("/")
def index():
    return render_template("index.html", title="Home")
