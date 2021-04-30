import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure(num=1, figsize=(8, 5))
plt.plot(x, y, lw=10, zorder=2)
# zorder 图层排列顺序，去除后期backgroundbox背景框

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(("data", 0))
ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data", 0))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.7))

plt.show()
