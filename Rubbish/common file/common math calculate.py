# 常用数学计算
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import pandas as pd
'''
直接引用
cmc = __import__("common math calculate")  

间接引用
import sys
sys.path.insert(0,'D:\\Study\\2019-2020\\Python\\resource code\\resource code\\rubbish')
cmc = __import__("common math calculate") 

'''

# 统计数据类


def average(data):
    "计算数组data的平均数并返回平均数,计算如下：N/(1/x1+1/x2+...+1/xn)"
    return sum(data) / len(data)


def absulate_subtract(data):
    "返回数组data的绝对误差"
    average_of_data = average(data)
    size = len(data)
    temp = []
    for i in range(size):
        temp.append(abs(data[i] - average_of_data))
    absulate_subtract_of_data = sum(temp)
    return absulate_subtract_of_data


def average_absulate_subtract(data):
    "返回数组的平均绝对差"
    size = len(data)
    aver_sub = absulate_subtract(data) / size
    return aver_sub


def subtract_square(data):
    "返回数组data的差平方"
    data_temp = []
    size = len(data)  # 元素个数
    average_data = average(data)  # 平均值
    for i in range(size):
        square_subtract = (data[i] - average_data)**2  # 平方差
        data_temp.append(square_subtract)
    return sum(data_temp)


def relative_error(L0, L):
    "计算L与L0相对误差，返回百分数，其中L为测量值，L0为理论值"
    error = round(abs(L - L0) / L0 * 100, 2)
    return str(error) + "%"


def y_x_corr(data_x, data_y):
    "返回y关于x的相关系数"
    series_x = pd.Series(data_x)
    series_y = pd.Series(data_y)
    corr_gust = round(series_x.corr(series_y), 4)
    return corr_gust


def standard_error(data):
    "测量误差计算,返回实验标准差及平均值的实验标准差"
    subtract_square_of_data = subtract_square(data)
    size = len(data)
    s1 = (subtract_square_of_data / (size - 1))**0.5  # 实验标准差
    s2 = (subtract_square_of_data / size / (size - 1))**0.5    # 平均值的实验标准差
    return s1, s2


def uncertainty_calculation(data, Δ, measure_type):
    '''返回直接测量量（data,Δ,measure_type）对应的不确定度，其中data为测量数据，Δ为测量
    最小分度值，measure_type为测量方式,measure_type对应参数：
    0未知 1游标卡尺 2螺旋测微仪'''
    size = len(data)
    if size == 1:
        SA = 0  # A类不确定度
    else:
        SA = standard_error[1]
    if measure_type == '1':
        SB = Δ / (3 ** 0.5)

    print("A类不确定度为%.2f\nB类不确定度为%.2f" % (SA, SB))


def liner_fitting(data_x, data_y):
    "根据最小二乘法计算，返回拟合后的斜率及截距"
    size = len(data_x)
    i = 0
    sum_xy = 0
    sum_y = 0
    sum_x = 0
    sum_sqare_x = 0
    while i < size:
        sum_xy += data_x[i] * data_y[i]
        sum_y += data_y[i]
        sum_x += data_x[i]
        sum_sqare_x += data_x[i] * data_x[i]
        i += 1
    average_x = average(data_x)
    average_y = average(data_y)
    return_k = (size * sum_xy - sum_x * sum_y) / \
        (size * sum_sqare_x - sum_x * sum_x)
    return_b = average_y - average_x * return_k
    '''print(sum_xy, sum_x, sum_y, sum_sqare_x,
        average_x, average_y, return_k, return_b)
    '''
    return return_k, return_b


def calculate_y(data_x, k, b):
    "最小二乘法作图用，计算出关于y的修正值"
    datay = []
    for x in data_x:
        datay.append(k * x + b)
    return datay


def draw(data_x, data_y_new, data_y_old, title, xlabel, ylabel):
    "做出关于x，y的最小二乘法拟合图形"
    plt.plot(data_x, data_y_new, label="拟合曲线", color="c")
    plt.scatter(data_x, data_y_old, label="离散数据")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title(title)
    plt.legend(loc="upper left")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def Least_squares(x, y, mod=0, title='一元线性拟合', xlabel="$x$", ylabel="$y$"):
    '''根据最小二乘法作y关于x的拟合直线图，此外，该函数包含两种模式，输出第三参数时会返回
    拟合直线的斜率及截距,不输入则默认不返回，此外，图形标题，x轴标签及y轴标签为可选参量。'''
    parameter = liner_fitting(x, y)
    draw_data = calculate_y(x, parameter[0], parameter[1])
    draw(x, draw_data, y, title, xlabel, ylabel)
    if mod != 0:
        return parameter


def smooth_curve(data_x, data_y, title='曲线拟合', xlabel='$x$', ylabel='$y$'):
    '根据数组x，y绘制平滑的拟合曲线,其中，图形标题，x轴标签及y轴标签为可选参量。'
    from scipy.interpolate import make_interp_spline
    x = np.array(data_x)
    y = np.array(data_y)
    x_smooth = np.linspace(x.min(), x.max(), 300)
    y_smooth = make_interp_spline(x, y)(x_smooth)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.plot(x_smooth, y_smooth)
    plt.scatter(x, y, c='c', marker='o')
    labels = '拟合曲线', '实际值'
    plt.legend(labels)
    plt.show()

    # 数学计算类


def distance(A, B):
    '计算同一维度内A,B两点之间的距离，维度不限'
    if len(A) == len(B):
        dimension = len(A)
        subt = [(A[i]-B[i])**2 for i in range(dimension)]
        dist = sum(subt)**0.5
        print(dist)
    else:
        print("A and B are not the same dimension!")
