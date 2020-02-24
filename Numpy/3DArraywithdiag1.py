import numpy as np

arr = np.zeros((3, 3))
print(arr)
print()
arr[0:1, 0] = 1
arr[1:2, 1] = 1
arr[2:, 2] = 1
print(arr)
