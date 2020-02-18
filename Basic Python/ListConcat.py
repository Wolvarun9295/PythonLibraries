try:
    # Taking size of list from user.
    size = int(input('Enter the size of list: '))
    # Initializing a blank list.
    stringList = []
    # Taking user input of elements and putting them in list.
    print('Enter elements in the list: ')
    for i in range(size):
        item = input('> ')
        stringList.append(item)
    # Concatenating the list into a String.
    for i in range(len(stringList)):
        print(stringList[i], end=" ")
except:
    print('Invalid Input! Try Again!')
