try:
    # Taking input from user.
    numberOfElements = int(input('Enter the number of elements you want: '))
    # Creating an empty list to store items.
    storeList = []
    print('Enter the elements: ')
    for item in range(numberOfElements):
        addThis = input('> ')
        storeList.append(addThis)
    print('List of items in List: ', storeList)
    print('List of items in Tuple: ', tuple(storeList))
except:
    print('Invalid Input! Try Again!')
