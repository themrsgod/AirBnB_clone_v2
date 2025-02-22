#!/usr/bin/python3
"""
A script that starts a Flask web application:
"""

from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception=None):
    """
    After each request remove the current SQLAlchemy Session:
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    List cities of states: display a HTML page:
    Returns:
        html: template that lists states, cities & amenity sort by name A->Z
    """
    data = {
        "states": storage.all("State").values(),
        "amenities": storage.all("Amenity").values()
    }
    return render_template("10-hbnb_filters.html", models=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)