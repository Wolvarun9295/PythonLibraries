inputString = input('Enter something: ')
length = len(inputString)
reversedString = ""
while length != 0:
    reversedString += inputString[length - 1]
    length -= 1
print(f'The String reversed is: {reversedString}')
