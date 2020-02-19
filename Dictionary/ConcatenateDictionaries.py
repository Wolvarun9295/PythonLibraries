# Initialized 3 dictionaries and 1 blank dictionary for concatenation.
sampleDict1 = {1: 10, 2: 20}
print(f'Dictionary 1: {sampleDict1}')
sampleDict2 = {3: 30, 4: 40}
print(f'Dictionary 2: {sampleDict2}')
sampleDict3 = {5: 50, 6: 60}
print(f'Dictionary 3: {sampleDict3}')
sampleDict4 = {}
# Using for loop to concatenate the dictionaries.
for i in (sampleDict1, sampleDict2, sampleDict3):
    sampleDict4.update(i)
print(f'The concatenated dictionary is: {sampleDict4}')
