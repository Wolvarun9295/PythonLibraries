from MyPack import wordLength

try:
    inputString = input('Enter something: ')
    largerThan = int(input('Check words greater than?: '))
    print(wordLength.spiltNCheck(largerThan, inputString))
except Exception:
    print('Invalid Input! Try Again!')
