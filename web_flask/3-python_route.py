#!/usr/bin/python3
"""A script that starts a flask web application
web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Returns Hello HBNB!"""
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Returns HBNB"""
    return ("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Returns “C ” followed by the value of the text variable"""
    return f'C {text.replace("_", " ")}'

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Returns “Python ”, followed by the value of the text variable"""
    return f'C {text.replace("_", " ")}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
