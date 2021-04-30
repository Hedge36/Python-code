# rubbish1 学年绩点饼图
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import math

font1 = matplotlib.font_manager.FontProperties(
    fname="C:/Users/Hedge/Documents/Fonts/msyh.ttf")

labels = '<60', '<70', '<80', '<90', '<100'
sizes = [0, 1, 2, 8, 3]
colors = ['r', 'm', 'yellow', 'b', 'c']

explode = (0, 0.2, 0, 0, 0)  # 对应饼块突出的距离
matplotlib.rcParams['font.family'] = 'STSong'
plt.title("2019-2020学年学科绩点分布饼状图", fontproperties=font1, fontsize=15)
plt.axis('equal')
patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels,
                                  autopct='%d%%', shadow=False, colors=colors,
                                  startangle=170)
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
plt.xticks(())
plt.yticks(())
plt.show()
