#!/usr/bin/env python3
""" basic flask app """

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.url_map_strict_slashes = False
babel = Babel(app)


class Config:
    """class to configure available languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", methods=["GET"])
def hello():
    """ render template and return Hello world """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
