# Storing a string in replaceThis variable to change the <<UserName>>
# with the Username supplied by user.
replaceThis = "Hello <<UserName>>, how are you?"
# Storing the user input in name variable.
name = input('Enter Username: ')
# Logic for replacing the <<UserName>> with user input.
if len(name) < 3:
    print('Please enter username greater than 3 characters.')
else:
    print(replaceThis.replace('<<UserName>>', name))
