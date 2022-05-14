#!/usr/bin/env python3
''' A basic Flask app '''

from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)
app.url_map_strict_slashes = False
babel = Babel(app)


class Config:
    ''' babel configuration '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    ''' determines best match for supported languages '''
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"])
def hello_world():
    ''' render the template '''
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
