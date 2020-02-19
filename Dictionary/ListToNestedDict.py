sampleList = [1, 2, 3, 4]
sampleDict = current = {}
for item in sampleList:
    current[item] = {}
    current = current[item]
print(sampleDict)
