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


@app.route('/python/<text>')
@app.route('/python/', defaults={'text': 'is cool'})
def hello_route_4(text):
    """Return string 4"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def hello_route_5(n):
    """Return number 5"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>')
def hello_route6(n):
    """Return number 6"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    """Running point"""
    app.run(host='0.0.0.0', port=5000)
