import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    # calculate height
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
# 8表示8+2个颜色层数
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)
C = plt.contour(X, Y, f(X, Y), 8, colors='b', linewidths=0.5)
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.xticks(())
plt.show()
