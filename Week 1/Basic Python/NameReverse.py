# Imported welcomeUSer module from MyPack.
from MyPack import welcomeUser

# Taking input from user and storing in variables.
firstName = input('Enter your first name: ')
lastName = input('Enter your last name: ')
# Calling the welcome function.
print(welcomeUser.welcome(firstName, lastName))
