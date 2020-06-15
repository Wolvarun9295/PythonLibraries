import matplotlib.pyplot as plt

x1 = [10, 20, 30]
y1 = [20, 40, 10]
x2 = [10, 20, 30]
y2 = [40, 10, 30]
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines with different widths and colors with suitable legends ')
plt.plot(x1, y1, color='blue', linewidth=3, label='line1-width-3')
plt.plot(x2, y2, color='red', linewidth=5, label='line2-width-5')
plt.legend()
plt.show()
