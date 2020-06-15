import matplotlib.pyplot as plt

X = range(1, 50)
Y = [value * 3 for value in X]
plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
print(plt.axis())
plt.axis([0, 100, 0, 200])
plt.show()
