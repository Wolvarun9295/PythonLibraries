# Imported OS module for os related operations.
import os

# Input taken from user.
checkThis = input('Enter the absolute path of file: ')
# os.path.exists(arg) checks if the the file exists.
print(os.path.exists(checkThis))
