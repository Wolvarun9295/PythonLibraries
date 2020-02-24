import numpy as np

arr = np.arange(1.0, 2.0, 36.2)
np.savetxt('File.out', arr, delimiter=',')
