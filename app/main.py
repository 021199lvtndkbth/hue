from app import app
from flask import render_template
from app.models import *

@app.route("/")
def index():
    return render_template("hue.html")


if __name__ == "__main__":
    app.run(debug=True)