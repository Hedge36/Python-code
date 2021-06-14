import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))
# "，"表示返回长度为1的元组


def animate(i):
    line.set_ydata(np.sin(x+i/10))
    return line,


def init():
    line.set_ydata(np.sin(x))
    return line,


# frames帧数,interval更新频率,blit是否对所有点更新,init_func表示起始状态,func动画函数
ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init,
                              interval=20, blit=False)
plt.show()
