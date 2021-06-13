import matplotlib
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2


plt.figure(figsize=(8, 5))
# figure3图像绘制
l1, = plt.plot(x, y1, linewidth=2, linestyle='--', label='line1')
l2, = plt.plot(x, y2, label='line2')
# 作为handle句柄的变量末必须加","!
plt.legend(handles=(l1, l2), labels=['a', 'b'], loc="best")
# 图例操作，handles操作对象，labels标签，loc图例位置，更多参数见kite。
plt.show()
