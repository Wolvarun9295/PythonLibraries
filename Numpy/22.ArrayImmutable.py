import numpy as np

arr = np.zeros(10)
arr.flags.writeable = False
print("Test the array is read-only or not: ")
print("Try to change the value of the first element: ")
arr[0] = 1
