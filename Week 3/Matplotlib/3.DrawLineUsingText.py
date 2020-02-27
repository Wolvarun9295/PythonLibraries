import matplotlib.pyplot as plt
import csv

x = []
y = []
with open("/home/bridgelabz/Desktop/test.txt", 'r') as f:
    data = csv.reader(f, delimiter=',')
    for row in data:
        x.append(int(row[0]))
        y.append(int(row[1]))
plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')
plt.show()
