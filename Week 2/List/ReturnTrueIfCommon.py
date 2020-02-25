from MyPack import commonChecker

try:
    list1 = []
    list2 = []
    size = int(input('How many elements do you want to add?: '))
    print('Enter elements in list 1:')
    for i in range(size):
        element = int(input('> '))
        list1.append(element)

    print('Enter elements in list 2:')
    for i in range(size):
        element = int(input('> '))
        list2.append(element)
    print(list1)
    print(list2)
    print(f'Are there common elements in List1 and List2?: {commonChecker.checkThese(list1, list2)}')
except Exception:
    print('Invalid Input! Try Again!')
