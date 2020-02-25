import numpy as np

arr = np.zeros((8, 8), dtype='int')
print(arr)
print()
arr[1::2, ::2] = 1
arr[::2, 1::2] = 1
print(arr)
