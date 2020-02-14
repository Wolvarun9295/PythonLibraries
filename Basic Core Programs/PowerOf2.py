try:
    # Taking the Nth term from user.
    Nth_Term = int(input('Enter Nth value: '))
    # Initializing exponent for getting the Power of 2.
    exponent = 0
    # Logic for generating the Power of 2 table and
    # checking the generated values are LEAP YEAR or NOT.
    while exponent != Nth_Term:
        power = 2 ** exponent
        if power % 400 == 0:
            print(str(power) + 'is Leap year')
        elif power % 100 == 0:
            print(str(power) + ' is NOT Leap Year')
        elif power % 4 == 0:
            print(str(power) + ' is Leap Year')
        else:
            print(str(power) + ' is NOT Leap Year')

        exponent += 1
except Exception:
    print("Invalid Input! Try Again!")
