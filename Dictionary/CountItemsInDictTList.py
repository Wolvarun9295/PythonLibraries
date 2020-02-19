sampleDict = {'Varun': ['subj1', 'subj2', 'subj3'], 'Golu': ['subj1', 'subj2']}
ctr = sum(map(len, sampleDict.values()))
print(f'Number of items in Dictionary that are List: {ctr}')
