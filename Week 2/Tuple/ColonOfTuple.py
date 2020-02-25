from copy import deepcopy

sampleTuple = ("Varun", 7.6, [], True)
print(sampleTuple)
colonTuple = deepcopy(sampleTuple)
colonTuple[2].append(100)
print(colonTuple)
