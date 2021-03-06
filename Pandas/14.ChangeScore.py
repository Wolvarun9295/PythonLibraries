import pandas as pd
import numpy as np

examData = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

sampleFrame = pd.DataFrame(examData, index=labels)
print('Original DataFrame:')
print(sampleFrame)
print()
print("After changing the score in row 'd' to 11.5:")
sampleFrame.loc['d', 'score'] = 11.5
print(sampleFrame)
