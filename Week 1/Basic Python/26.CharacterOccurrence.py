# Taking the string as input from user.
string = input('Enter a string: ')
# Taking user input of character to be found.
findThis = input("Enter a character to find out it's occurrence in the String: ")
# Printing the number of occurrences in the string.
print(f'{findThis} occurs {string.count(findThis)} times in the {string}')
