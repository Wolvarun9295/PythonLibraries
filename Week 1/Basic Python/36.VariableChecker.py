# Initialize or remove variable to check the output.
variable = 0
try:
    variable
except NameError:
    print("Variable NOT Defined!")
else:
    print('Variable Defined!')
