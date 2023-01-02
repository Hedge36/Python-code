# Physical experiment 12 error calculate
cmc = __import__("common math calculate")
import matplotlib.pyplot as plt
from pylab import mpl
import pandas as pd


def print_R_Pt(data_temperature):
    "铂电阻对应温度结果打印"
    for temper in data_temperature:
        #print("当温度为%.1f°C时，铂100电阻值为%.2f Ω。" % (temper, R0 * (1 + A * temper)))
        data_Rt.append(R0 * (1 + A * temper))


def y_xcorr_calculate(data_x, data_y):
    "求y关于x的相关系数"
    series_x = pd.Series(data_x)
    series_y = pd.Series(data_y)
    corr_gust = round(series_x.corr(series_y), 4)
    return corr_gust


def mini_two_mulitip(data_x, data_y):
    "计算x，y的拟合系数"
    return cmc.liner_fitting(data_x, data_y)


R0 = 100  # 铂初始电阻
A = 3.90802E-3  # 铂的温度系数
data_temperature = [1.4] + [10 * i for i in range(1, 11)]   # 待测温度组值数组
data_Rt = []  # Pt100的实验数据值组
data_voltage = [0.056, 0.138, 0.203, 0.309, 0.353,
                0.449, 0.532, 0.622, 0.702, 0.795, 0.884]   # LM35测定的电压值数组

print_R_Pt(data_temperature)
print("铂100对应温度系数A为%.4f,相关系数r为%.4f。" % (mini_two_mulitip(
    data_temperature, data_Rt)[0] * 10, y_xcorr_calculate(data_temperature, data_Rt)))
print("LM35对应系数A为%.2f,相关系数r为%.4f。" % (mini_two_mulitip(
    data_temperature, data_voltage)[0] * 1000, y_xcorr_calculate(data_temperature, data_voltage)))
#mini.main(data_temperature, data_Rt)
data_temperature.remove(40)   # 修正待测温度组值数组
data_temperature.remove(10)   # 修正待测温度组值数组
data_voltage = [0.056, 0.203, 0.309,
                0.449, 0.532, 0.622, 0.702, 0.795, 0.884]   # 修正后的LM35测定的电压值数组
print("修正后的LM35对应系数A为%.2f,相关系数r为%.4f。" % (mini_two_mulitip(
    data_temperature, data_voltage)[0] * 1000, y_xcorr_calculate(data_temperature, data_voltage)))
