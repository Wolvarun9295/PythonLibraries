import numpy as np

arr = np.array([[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]])
index = [0, 3, 4]
newArr = np.delete(arr, index)
print(newArr)
