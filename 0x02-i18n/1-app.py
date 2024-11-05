#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """
    Config class
    """
    LANGUAGEES = ["en", "fr"]


@app.route('/', strict_slashes=False)
def index():
    """
    Index page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
