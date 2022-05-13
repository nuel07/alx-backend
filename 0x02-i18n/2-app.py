#!/usr/bin/env python3
"""basic flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
app.url_map_strict_slashes = False
babel = Babel(app)


class Config:
    """babel configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """determines best match with supported languages"""
    return request.accept_languages.best_match(app.config('LANGUAGES'))


@app.route("/", methods=["GET"])
def hello():
    """ render template """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
