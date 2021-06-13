import matplotlib
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2
# 多窗口绘图
plt.figure(num=2)
# figure2图像绘制
plt.plot(x, y1)

plt.figure(figsize=(8, 5))
# figure3图像绘制
plt.plot(x, y1, linewidth=2, linestyle='--')
plt.plot(x, y2)

plt.show()
