# Taking limit as input from user.
limit = int(input('Enter the limit of dictionary to be generated: '))
# Making an object of dictionary.
sampleDict = dict()
# Generating the dictionary.
for i in range(1, limit + 1):
    sampleDict[i] = i * i
print(f'Generated dictionary is: {sampleDict}')
