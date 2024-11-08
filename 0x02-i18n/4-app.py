#!/usr/bin/env python3
"""
Force locale with URL parameter
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """
    Initialize Config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    determines the best match with our supported languages
    """
    query = request.query_string.decode('utf-8').split('&')
    is_locale = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        query,
    ))
    if 'locale' in is_locale:
        if is_locale['locale'] in app.config["LANGUAGES"]:
            return is_locale['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """
    Index page.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
