# Imported subprocess module.
import subprocess

try:
    # Taking size of list to store the command.
    size = int(input('Enter number of words in command: '))
    # Initializing a blank list.
    commandStore = []
    print('Enter a command and divide it into line if it contains spaces: ')
    # Storing the command in list.
    for item in range(size):
        command = input('> ')
        commandStore.append(command)
    # Calling the command.
    subprocess.call(commandStore)
except:
    print('Invalid Input! Try Again!')
