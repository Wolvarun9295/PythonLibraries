# Defining two functions in class TemperatureConvertor.
class TemperatureConvertor:
    # Function to convert Celsius to Fahrenheit.
    def celsiusToFahrenheit(self, temperature):
        fahrenheit = (temperature * (9 / 5)) + 32
        print(f'{temperature} Celsius is {round(fahrenheit, 2)} Fahrenheit')

    # Function to convert Fahrenheit to Celsius.
    def fahrenheitToCelsius(self, temperature):
        celsius = (temperature - 32) * (5 / 9)
        print(f'{temperature} Fahrenheit is {round(celsius, 2)} Celsius')


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
            convert.celsiusToFahrenheit(temperature)
        elif degree.upper() == "F":
            convert.fahrenheitToCelsius(temperature)
except Exception:
    print('Invalid Input! Try Again!')
