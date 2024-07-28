#!/usr/bin/python3
"""
Start a Flask web application
"""

from flask import Flask, render_template
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
    return (f"C {text}")


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Display python text """
    text = escape(text).replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """n is a number"""
    return (f"{n} is a number")


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display html page"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
