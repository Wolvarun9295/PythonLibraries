# Taking string as user input.
string = input('Enter a number: ')
# Taking the count from user.
countOfZeros = int(input('Enter number of zeros to be added after it: '))
# Using zfill to append the 0's to the string.
# NOTE: len(string) is added to countOfZeros to avoid the error of skipping positions when adding 0 after string.
string = string.zfill(countOfZeros + len(string))
print(string)
