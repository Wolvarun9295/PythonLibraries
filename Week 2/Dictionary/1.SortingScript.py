# Imported operator module.
import operator

# Initialized a dictionary.
dictionarySample = {3: 4, 1: 2, 7: 8, 5: 6, 0: 0}
print(f'Dictionary: {dictionarySample}')
# Sorting in Ascending.
sortedDictionary = sorted(dictionarySample.items(), key=operator.itemgetter(1))
print(f'Dictionary values sorted in Ascending: {sortedDictionary}')
# Sorting in Descending.
sortedDictionary = sorted(dictionarySample.items(), key=operator.itemgetter(1), reverse=True)
print(f'Dictionary values sorted in Descending: {sortedDictionary}')
