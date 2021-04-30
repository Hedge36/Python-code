import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

"""
# method1
plt.figure()
plt.title("method1")
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])
# 尤其注意subplot中的index参数，此处应为4！
plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 3])
# subplot中参数可省略“，”
plt.subplot(235)
plt.plot([0, 1], [0, 2])

plt.subplot(236)
plt.plot([0, 1], [0, 4])
"""

"""
# method2
plt.figure()
plt.title("method subpot2grid")
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
ax1.plot([1, 2], [1, 2])
ax1.set_title("ax1")

ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax2.plot([1, 2], [1, 2])
ax2.set_title("ax2")

ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax3.plot([1, 2], [1, 2])
ax3.set_title("ax3")

ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.plot([1, 2], [1, 2])
ax4.set_title("ax4")

ax5 = plt.subplot2grid((3, 3), (2, 1))
ax5.plot([1, 2], [1, 2])
ax5.set_title("ax5")
"""

"""
# method3
plt.figure()
gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, :2])
ax3 = plt.subplot(gs[1:, 2])
ax4 = plt.subplot(gs[-1, 0])
ax5 = plt.subplot(gs[-1, -2])
"""

# method4
# 最简洁，但是如何不均等分配？
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(
    2, 2, sharex=True, sharey=True)
ax11.scatter([1, 2], [2, 1])


plt.tight_layout()
plt.show()
