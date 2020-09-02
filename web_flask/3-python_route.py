#!/usr/bin/python3
"""Flash app"""
from flask import Flask
app = Flask('web_flask')


@app.route('/', strict_slashes=False)
def hello_route_1():
    """Return string 1"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_route_2():
    """Return string 2"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_route_3(text):
    """Return string 3"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/(<text>)', strict_slashes=False)
def hello_route_4(text="is cool"):
    """Return string 4"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    """Running point"""
    app.run(host='0.0.0.0', port=5000)
