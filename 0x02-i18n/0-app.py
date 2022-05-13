#!/usr/bin/env python3
"""basic Flask app """

from flask import Flask
from flask import render_template
app = Flask(__name__)
app.url_map_strict_slashes = False


@app.route("/", methods=["GET"])
def hello():
    """return Hello World"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
