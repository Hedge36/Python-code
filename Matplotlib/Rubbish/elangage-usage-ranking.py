import matplotlib.pyplot as plt
import matplotlib.font_manager as fm  # 字体管理器

# 准备字体
my_font = fm.FontProperties(fname="C:/Users/Hedge/Documents/Fonts/msyh.ttf")
# 准备数据
data = [0.16881, 0.14966, 0.07471, 0.06992, 0.04762,
        0.03541, 0.02925, 0.02411, 0.02316, 0.01409, 0.36326]
# 准备标签
labels = ['Java', 'C', 'C++', 'Python', 'Visual Basic.NET',
          'C#', 'PHP', 'JavaScript', 'SQL', 'Assembly langugage', '其他']
# 将排列在第4位的语言(Python)分离出来
explode = [0, 0, 0, 0.3, 0, 0, 0, 0, 0, 0, 0]
# 使用自定义颜色
colors = ['red', 'pink', 'magenta', 'purple', 'orange']
# 将横、纵坐标轴标准化处理,保证饼图是一个正圆,否则为椭圆
plt.axes(aspect='equal')
# 控制X轴和Y轴的范围(用于控制饼图的圆心、半径)
plt.xlim(0, 8)
plt.ylim(0, 8)
# 不显示边框
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['left'].set_color('none')
plt.gca().spines['bottom'].set_color('none')
# 绘制饼图
plt.pie(x=data,  # 绘制数据
        labels=labels,  # 添加编程语言标签
        explode=explode,  # 突出显示Python
        colors=colors,  # 设置自定义填充色
        autopct='%.3f%%',  # 设置百分比的格式,保留3位小数
        pctdistance=0.7,  # 设置百分比标签和圆心的距离
        labeldistance=1.1,  # 设置标签和圆心的距离
        startangle=180,  # 设置饼图的初始角度
        center=(4, 4),  # 设置饼图的圆心(相当于X轴和Y轴的范围)
        radius=3.8,  # 设置饼图的半径(相当于X轴和Y轴的范围)
        counterclock=False,  # 是否为逆时针方向,False表示顺时针方向
        wedgeprops={'linewidth': 1, 'edgecolor': 'green'},  # 设置饼图内外边界的属性值
        textprops={'fontsize': 12, 'color': 'black',
                   'fontproperties': my_font},  # 设置文本标签的属性值
        frame=1)  # 是否显示饼图的圆圈,1为显示
# 不显示X轴、Y轴的刻度值
plt.xticks(())
plt.yticks(())
# 添加图形标题
plt.title('2018年8月的编程语言指数排行榜', fontproperties=my_font)
# 显示图形
plt.show()
