import pandas as pd

sampleArray = pd.Series([2, 4, 6, 8, 10])
print("Pandas Array:")
print(sampleArray)
print(f'Type of Array: {type(sampleArray)}')
print("Converted to list:")
print(sampleArray.tolist())
print(f'Type of converted list: {type(sampleArray.tolist())}')
