#!/usr/bin/python3
"""
    A python script that starts a Flask web application
    must listen on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return 'C %s' % text.replace("_", " ")


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number_only(n):
    return '%s is a number' % n


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
