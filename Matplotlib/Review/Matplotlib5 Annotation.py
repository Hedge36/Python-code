import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure(num=1, figsize=(8, 5))
plt.plot(x, y)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(("data", 0))
ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data", 0))


x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, color='b')
# 两点间连线，k表示黑色， lw表示线宽
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)

# method 1
plt.annotate(r"$y=2x+1$", xy=(x0, y0), xycoords='data', xytext=(+2, -2),
             fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
"""
xy 为被注释的坐标点

xytext 为注释文字的坐标位置

xycoords 参数如下:
figure points：图左下角的点
figure pixels：图左下角的像素
figure fraction：图的左下部分
axes points：坐标轴左下角的点
axes pixels：坐标轴左下角的像素
axes fraction：左下轴的分数
data：使用被注释对象的坐标系统(默认)
polar(theta,r)：if not native ‘data’ coordinates t

arrowprops #箭头参数,参数类型为字典dict
width：箭头的宽度(以点为单位)
headwidth：箭头底部以点为单位的宽度
headlength：箭头的长度(以点为单位)
shrink：总长度的一部分，从两端“收缩”
facecolor：箭头颜色

bbox给标题增加外框 ，常用参数如下：
boxstyle：方框外形
facecolor：(简写fc)背景颜色
edgecolor：(简写ec)边框线条颜色
edgewidth：边框线条大小
"""

# method 2
"""
plt.text(-3.7, 3, r"$This\ is\ text.$",
    fontdict={size:16, color:"r"})
"""
plt.show()
