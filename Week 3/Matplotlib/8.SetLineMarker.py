import matplotlib.pyplot as plt

x = [1, 4, 5, 6, 7]
y = [2, 6, 3, 6, 3]

plt.plot(x, y, color='red', linestyle='dashdot', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)
plt.ylim(1, 8)
plt.xlim(1, 8)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Display marker')
plt.show()
