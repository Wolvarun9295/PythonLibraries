import numpy as np

arr1 = np.array([0, 10, 20, 40, 60])
arr2 = np.array([10, 30, 40])
print(f'Common elements in Array1 and Array2 are: {np.intersect1d(arr1, arr2)}')
