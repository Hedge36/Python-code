import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X / float(12)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(12)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, + Y1, facecolor='r', edgecolor='white')
plt.bar(X, - Y2, facecolor='b', edgecolor='white')
# 给每一个柱子注上大小
for x, y in zip(X, Y1):
    plt.text(x, y + 0.01, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    plt.text(x, - y - 0.12, '%.2f' % y, ha='center', va='bottom')
plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()
