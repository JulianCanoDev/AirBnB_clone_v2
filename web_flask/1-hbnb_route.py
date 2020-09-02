#!/usr/bin/python3
"""Flash app"""
from flask import Flask
app = Flask('web_flask')


@app.route('/', strict_slashes=False)
def hello_route1():
    """Return string 1"""
    return 'Hello HBNB!'


@app.route('/', strict_slashes=False)
def hello_route2():
    """Return string 2"""
    return 'HBNB!'


if __name__ == "__main__":
    """Running point"""
    app.run(host='0.0.0.0', port=5000)
