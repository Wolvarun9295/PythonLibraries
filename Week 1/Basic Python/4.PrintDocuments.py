# Documentation of a function is given by function.__doc__.
print(f'The documentation of abs:\n{abs.__doc__}\n')
try:
    # Taking user input.
    number = int(input('Enter the number (+ve or -ve) to get the absolute number: '))
    # Printing the absolute value.
    print(abs(number))
except:
    print('Invalid Input! Try Again!')
