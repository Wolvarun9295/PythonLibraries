try:
    print("Enter 3 numbers: ")
    # Initializing a blank variable for input.
    number = ""
    # Initializing a blank list.
    sortThis = []
    # Taking input from user.
    # NOTE: This loop is just for taking user input and not for sorting.
    for i in range(3):
        number = int(input('> '))
        sortThis.append(number)
    # Sorting the values.
    sortThis.sort()
    print(sortThis)
except Exception:
    print('Invalid Input! Try Again!')
