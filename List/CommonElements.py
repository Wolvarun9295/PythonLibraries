sampleList1 = [1, 2, 3, 4]
sampleList2 = [3, 4, 5, 6]
print(f'List 1: {sampleList1}')
print(f'List 2: {sampleList2}')
sampleList3 = set(sampleList1) & set(sampleList2)
print(f'The common elements from both List: {list(sampleList3)}')
