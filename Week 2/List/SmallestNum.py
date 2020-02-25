sampleList = [4, 2, 5, 1, 3]
print(f'List: {sampleList}')
small = sampleList[0]
for i in sampleList:
    if small > i:
        small = i
print(f'The smallest item in List is: {small}')
