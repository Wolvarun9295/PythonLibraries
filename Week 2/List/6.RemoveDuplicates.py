numberList = [1, 2, 3, 2, 1, 5, 6, 4, 8, 5, 4]
uniques = set()
for num in numberList:
    if num not in uniques:
        uniques.add(num)
print(f'List after removing duplicates: {uniques}')
