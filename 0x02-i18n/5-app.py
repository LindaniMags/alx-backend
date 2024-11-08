#!/usr/bin/env python3
"""
Mock logging in
"""
from typing import Union, Dict
from flask_babel import Babel
from flask import Flask, render_template, request, g


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
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    returns a user dictionary or None
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """
    uses get_user to find a user if any, and set it as a globa
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    determines the best match with our supported languages
    """
    is_locale = request.args.get('locale', '')
    if is_locale in app.config["LANGUAGES"]:
        return is_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """
    Index page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
