#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
	"""Displays 'Hello HBNB!'"""
	return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
	"""Displays 'HBNB'"""
	return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def hbnb_c(text):
	"""display 'C' followed by the value of the text variable"""
	new_text = text.replace("_", " ")
	return "C {}".format(new_text)


if __name__ == "__main__":
	app.run(host='0.0.0.0')
