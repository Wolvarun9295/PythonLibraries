size = int(input('Enter size of list: '))
sampleList = []
print('Enter Something:')
for i in range(size):
    element = input('> ')
    sampleList.append(element)
print(f'List: {sampleList}')

for i in sampleList:
    sampleList.sort()
print(f'The longest word in String List is: {sampleList[-1]}')
