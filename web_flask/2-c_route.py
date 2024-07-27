#!/usr/bin/python3
"""
Start a Flask web application
"""

from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display Hello HBNB! """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display HBNB! """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display c text"""
    text = escape(text).replace('_', ' ')
    return (f"c {text}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
