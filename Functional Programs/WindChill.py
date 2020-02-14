try:
    # Taking the values of temperature and speed from the user.
    temperature = float(input('Enter the temperature in Fahrenheit: '))
    speed = float(input('Enter the speed in MPH: '))
    # Calculating the WindChill.
    # NOTE: Windchill is only calculated if the temperature is less than 50 and
    # if the speed is less than 110 or greater than 3.
    if temperature <= 50 and speed >= 3 or speed <= 110:
        windChill = 35.74 + (0.6215 * temperature) - (35.75 * (speed ** 0.16)) + (
                (0.4275 * temperature) * (speed ** 0.16))
        print(f'The WindChill with temperature {temperature} F and speed {speed} MPH is: {round(windChill, 2)} F')
    else:
        print('Please make sure the temperature is less than 50 degree fahrenheit and speed above 3 MPH!')
except Exception:
    print('Invalid Input! Try Again!')
