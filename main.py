from flask import Flask

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

@app.route('/celsius_to_fahrenheit/<celsius_str>')
def convert_celsius_to_fahrenheit(celsius_str):
    try:
        celsius = float(celsius_str)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return f"The Fahrenheit value of {celsius}°C is {fahrenheit}°F."
    except ValueError:
        return "Invalid input. Please provide a valid Celsius value."

if __name__ == '__main__':
    app.run()
