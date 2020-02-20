inputString = input('Enter something: ')
sampleDict = {}
for char in inputString:
    keys = sampleDict.keys()
    if char in keys:
        sampleDict[char] += 1
    else:
        sampleDict[char] = 1
print(sampleDict)
