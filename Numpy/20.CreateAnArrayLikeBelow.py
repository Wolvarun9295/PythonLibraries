import numpy as np

arr = np.zeros((4, 3))
print(arr)
print()
arr[1:2, 0] = 1
arr[2:3, 0:2] = 1
arr[3:, 0:] = 1
print(arr)
