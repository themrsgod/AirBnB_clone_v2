#!/usr/bin/python3
"""
    script that starts a Flask web application
    must listen on 0.0.0.0, port 5000
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return 'C %s' % text.replace("_", " ")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
