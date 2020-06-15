import numpy as np

arr1 = np.array([[10, 20, 30], [40, 50, 60]])
arr2 = np.array([[100], [200]])
print(np.append(arr1, arr2, axis=1))
