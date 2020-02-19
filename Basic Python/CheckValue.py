# Imported valueChecker module from MyPack.
from MyPack import valueChecker

try:
    # Initializing a blank list.
    storeList = []
    # Taking size as input from user.
    size = int(input('Enter number of elements you want to enter in list: '))
    # Taking elements from user.
    for item in range(size):
        element = int(input('> '))
        storeList.append(element)

    print(storeList)
    # Taking user input to check the value in list.
    checkThis = int(input('Enter the element you want to search: '))
    print(valueChecker.checkValue(storeList, checkThis))
except Exception:
    print('Invalid Input! Try Again!')
