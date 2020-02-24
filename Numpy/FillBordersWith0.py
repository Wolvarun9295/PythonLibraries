import numpy as np

arr = np.zeros((5, 5))
print(arr)
print()
arr[1:-1, 1:-1] = 1
print(arr)
