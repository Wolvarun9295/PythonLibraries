try:
    # Initializing a blank list.
    listStore = []
    # Taking input from user for size.
    size = int(input('Enter the size of array: '))
    # Taking elements input from user.
    for i in range(size):
        element = int(input('> '))
        listStore.append(element)
    print(f'The items in array are: {listStore}')
    # Taking the user input of index value to be accessed.
    indexInput = int(input('Enter the index you want to access: '))
    # Accessing the element by index.
    for i in listStore:
        if indexInput == i:
            print(f'The item on index {indexInput} is: {listStore[i]}')
except Exception:
    print('Invalid Input! Try Again!')
