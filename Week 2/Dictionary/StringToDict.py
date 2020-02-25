# Taking input from user.
string = input('Enter something: ')
# Initializing a blank dictionary.
sampleDict = {}
# Adding string values to dictionary.
for i in string:
    sampleDict[i] = sampleDict.get(i, 0) + 1
print(sampleDict)
