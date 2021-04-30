import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager  # 导入字体管理模块


x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2
font = font_manager.FontProperties(
    fname="C:\\Users\\Hedge\\Documents\\Fonts\\msyh.ttf")


plt.figure(figsize=(8, 5))
# figure3图像绘制
plt.plot(x, y1, color='r', linewidth=2, linestyle='--')
plt.plot(x, y2)
# x,y取值范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))
# x,y轴标签
plt.xlabel("x轴", fontproperties=font)
plt.ylabel("y轴", fontproperties=font)
# x,y轴节点
plt.xticks([1, 2, 3])
plt.yticks([-2, -1.8, -1, 1.22, 3],
           ['really bad', 'bad', 'normal', 'good', 'really good'])
# 其中空格需要反斜杠，此外，对于数学表达式需要使用r'$LaTe X$'，其中r表示正则表达。

# 坐标轴设置
ax = plt.gca()
# 取消上侧及右侧边框线
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
# x,y轴坐标轴设置
ax.spines['bottom'].set_position(('data', -1))  # x轴位于y=-1处
ax.spines['left'].set_position(('data', 1))


plt.show()
