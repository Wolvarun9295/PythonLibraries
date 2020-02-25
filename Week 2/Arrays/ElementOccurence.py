try:
    # Initialize a blank list.
    listStore = []
    # Taking the size of list from user.
    size = int(input('Enter the size of array: '))
    # Taking the items from user.
    for i in range(size):
        element = int(input('> '))
        listStore.append(element)
    # Taking user input of the item to be counted.
    countThis = int(input('Enter the number you want to find the occurrences of: '))
    print(f'{countThis} occurs {listStore.count(countThis)} times.')
except Exception:
    print('Invalid Input! Try Again!')
