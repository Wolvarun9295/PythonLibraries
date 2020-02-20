from itertools import groupby
from operator import itemgetter

animalList = ['cat', 'dog', 'rabbit', 'pig', 'bat', 'monkey', 'snake', 'crocodile']

for letter, animals in groupby(sorted(animalList), key=itemgetter(0)):
    print(letter)
    for animal in animals:
        print(animal)
