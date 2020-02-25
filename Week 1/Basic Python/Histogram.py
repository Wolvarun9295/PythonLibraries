# Taking size of list as input from user.
size = int(input('Enter size: '))
# Initializing a blank list.
plottingList = []

print('Enter elements in list: ')
# Adding elements in list.
for item in range(size):
    element = int(input('> '))
    plottingList.append(element)
# Printing the Histogram of given data.
print('Histogram for given data:')
for everyItem in plottingList:
    print('#' * everyItem)
