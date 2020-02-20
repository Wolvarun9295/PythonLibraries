import itertools

listOfLists = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print(f'List: {listOfLists}')
listOfLists.sort()
newList = list(i for i, j in itertools.groupby(listOfLists))
print(f'New List: {newList}')
