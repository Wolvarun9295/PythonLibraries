import matplotlib.pyplot as plt

x = range(1, 50)
y = [value * 3 for value in x]
print('Value of x:')
print(*x)
print('Values of y (thrice of x):')
print(y)
plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Draw a line')
plt.show()
