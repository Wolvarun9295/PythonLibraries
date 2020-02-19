try:
    # Taking size from user.
    size = int(input('Enter the size of list: '))
    # Initializing a blank list.
    numbers = []
    print(f'Enter {size} elements in list: ')
    # Getting the elements in list from user.
    for i in range(size):
        element = int(input('> '))
        numbers.append(element)
    print(numbers)
    # Assigning the numbers[0] to minimum and numbers[len(numbers)-1] to maximum.
    minimum = numbers[0]
    maximum = numbers[len(numbers) - 1]
    # Logic for getting the smallest and largest number from list.
    for items in numbers:
        if minimum > items:
            minimum = items
        elif maximum < items:
            maximum = items
    print(f'Minimum number: {minimum}')
    print(f'Maximum number: {maximum}')

except Exception:
    print('Invalid Input! Try Again!')
