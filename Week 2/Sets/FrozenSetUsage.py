setA = frozenset([1, 2, 3, 4])
setB = frozenset([3, 4, 5, 6])
setC = setA.isdisjoint(setB)
print(f'Are these sets disjoint?: {setC}')
setC = setA.difference(setB)
print(f'Difference of sets: {setC}')
print(f'Union: {setA | setB}')