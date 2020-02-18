# Imported abspath from os.path.
from os.path import abspath

# Getting input from user.
getThisFile = input("Enter the filename you want path of: ")
print(abspath(f'{getThisFile}'))
