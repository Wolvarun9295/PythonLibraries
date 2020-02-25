import numpy as np

arr = np.array([1, 2, 3], dtype=np.float64)
print(f'Size of array: {arr.size}')
print(f'Length of one array element in bytes: {arr.itemsize}')
print(f'Total bytes consumed by the elements of array: {arr.nbytes}')
