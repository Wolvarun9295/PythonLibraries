# Imported OS module.
import os

try:
    # Taking user input. NOTE: Input should be given in all caps! Ex. HOME or PATH.
    accessThis = input('Enter to access the environment variables of any file: ')
    # Printing the environmental path.
    print(os.environ[accessThis])
except:
    print('Invalid Input! Try Again!')
