from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


if __name__ == '__main__':
    app.run()


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/temperature')
@app.route('/temperature/<celsius>')
def temperature(celsius=0):
    return "{:.2f}".format(calculate_fahrenheit(celsius))


def calculate_fahrenheit(celsius):
    result = float(celsius) * 9.0 / 5 + 32
    return result
