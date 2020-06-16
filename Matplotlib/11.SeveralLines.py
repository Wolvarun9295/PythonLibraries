import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'g--', t, t ** 2, 'bs', t, t ** 3, 'r^')
plt.show()
