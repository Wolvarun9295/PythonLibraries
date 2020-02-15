# Defining two functions in class TemperatureConvertor.
class TemperatureConvertor:
    # Function to convert Celsius to Fahrenheit.
    def celsiusToFahrenheit(self, temperature):
        fahrenheit = (temperature * (9 / 5)) + 32
        return fahrenheit

    # Function to convert Fahrenheit to Celsius.
    def fahrenheitToCelsius(self, temperature):
        celsius = (temperature - 32) * (5 / 9)
        return celsius


try:
    # Taking temperature as input from user.
    temperature = int(input('Enter temperature: '))
    # Initializing degree variable to further store character input.
    degree = ''
    # Creating object convert of TemperatureConvertor class.
    convert = TemperatureConvertor()

    print('''Make your choice:
    1. (C)elsius to Fahrenheit
    2. (F)ahrenheit to Celsius
    3. (Q)uit
    ''')
    # Calculating the temperature by function calling.
    while degree.upper() != "Q":
        degree = input('>')
        if degree.upper() == "C":
            print(f'{temperature} Celsius is {round(convert.celsiusToFahrenheit(temperature), 2)} Fahrenheit')
        elif degree.upper() == "F":
            print(f'{temperature} Fahrenheit is {round(convert.fahrenheitToCelsius(temperature), 2)} Celsius')
except Exception:
    print('Invalid Input! Try Again!')
