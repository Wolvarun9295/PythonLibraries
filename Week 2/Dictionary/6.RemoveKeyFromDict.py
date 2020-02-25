try:
    # Initializing a dictionary.
    sampleDict = {1: 10, 2: 20, 3: 30, 4: 40}
    print(f'Dictionary: {sampleDict}')
    # Taking the key to be deleted as input from user.
    delThis = int(input('Enter the key you want to delete: '))
    # Deleting the key.
    del sampleDict[delThis]
    print(f'After deleting the key {delThis} from dictionary:')
    print(sampleDict)
except Exception:
    print('Invalid Input! Try Again!')
