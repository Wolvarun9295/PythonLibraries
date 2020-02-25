import numpy as np

arr1 = np.array([1, 2])
arr2 = np.array([4, 5])
print(f'Array1 : {arr1}')
print(f'Array2 : {arr2}')
print(f'a > b? : {np.greater(arr1, arr2)}')
print(f'a >= b? : {np.greater_equal(arr1, arr2)}')
print(f'a < b? : {np.less(arr1, arr2)}')
print(f'a <= b? : {np.less_equal(arr1, arr2)}')
