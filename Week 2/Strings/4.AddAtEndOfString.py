inputString = input('Enter something: ')
length = len(inputString)
if length > 2:
    if inputString[-3:] == 'ing':
        inputString += 'ly'
    else:
        inputString += 'ing'
print(inputString)
