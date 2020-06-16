import math
import random
import matplotlib.pyplot as plt

numberOfBalls = 25
x = [random.triangular() for i in range(numberOfBalls)]
y = [random.gauss(0.5, 0.25) for i in range(numberOfBalls)]
colors = [random.randint(1, 4) for i in range(numberOfBalls)]
areas = [math.pi * random.randint(5, 15) ** 2 for i in range(numberOfBalls)]
plt.figure()
plt.scatter(x, y, s=areas, c=colors, alpha=0.85)
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
