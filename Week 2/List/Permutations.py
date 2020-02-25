import itertools

size = int(input('Enter how many value you need to put: '))
numberList = []
print('Enter {size} items to generate permutations:')
for i in range(size):
    item = int(input('> '))
    numberList.append(item)
print(f'Permutations of given values: {list(itertools.permutations(numberList))}')
