# 大物实验1数据分析
cmc = __import__("common math calculate")
import math

d_boa = [5.226, 5.215, 5.277, 5.285, 5.242]  # 金属薄板的厚度/mm
D_wir = [1.334, 1.316, 1.350, 1.278, 1.315,

         1.233, 1.329, 1.304, 1.302, 1.323]  # 金属丝直径/mm

D_cup = [3.000, 3.001, 3.000, 3.000, 2.999]  # 铜杯外径/cm

d_cup = [2.370, 2.400, 2.374, 2.380, 2.380]  # 铜杯内径/cm

H_cup = [4.706, 4.710, 4.710, 4.712, 4.715]  # 铜杯高度/cm

h_cup = [4.178, 4.184, 4.188, 4.190, 4.186]  # 铜杯深度/cm

m_bal = [121.6, 122.0, 121.8, 122.1, 121.8]  # 物理天平称重/g

m_ele = [119.12, 119.12, 119.12, 119.11, 119.12]  # 电子天平称重/g

T = 25.5  # 水温/℃
ρ_water = 0.996944  # 对应温度下水的密度
m_inwater = [105.2, 105.1, 105.2, 105.3, 105.4]  # 物理天平测出在水中质量/g
# zip待使用序列包
cup = zip(D_cup, d_cup, H_cup, h_cup, m_bal)
cup_vol = zip(D_cup, d_cup, H_cup, h_cup)
# 推导式计算
m_water = [m1 - m2 for m1, m2 in zip(m_bal, m_inwater)]  # 排开水的质量
temp_vol = [m / ρ_water for m in m_water]   # 阿基米德法测量金属杯体积
temp_ρ = [m / vol for vol, m in zip(temp_vol, m_bal)]    # 阿基米德法测量金属杯密度
# 金属杯各参数对应平均值的标准误差及平均值对应偏导
dV_dD = 88.8
dV_dd = -70.178
dV_dH = 28.274
dV_dh = -17.81
sitaD = 0
sitad = 0.005
sitaH = 0.001
sitah = 0.002
sitam = 0.087
V_average = 58.662 / 4


def experiencement(data):
    average = cmc.average(data)
    sums = sum(data)
    s1, s2 = cmc.standard_error(data)
    s0 = cmc.subtract_square(data)
    print("参考数据：\n和:%.3f\n平均值：%.3f" % (sums, average))
    print("差平方:%.3f\n标准误差：%.3f。" % (s0, s2))
    return average


def volume(D, d, H, h):
    "由已测得数据计算金属杯体积"
    vol = math.pi * (D ** 2 - d ** 2) * h / 4 + \
        math.pi * (D ** 2) * (H - h) / 4
    return vol


def cup_expe(data_group):
    "实验二物理天平物理间接测量密度实验各参数计算"
    statement = ['金属杯外径', '金属杯内径', '金属杯高度', '金属杯深度', '金属杯质量']
    for state, data in zip(statement, data_group):
        print()
        print(state)
        experiencement(data)


def volume_calculate():
    temp = []
    print("实验二物理天平金属杯的体积计算")
    for D, d, H, h in cup_vol:
        vol = volume(D, d, H, h)
        temp.append(vol)
    experiencement(temp)


def density_calculate():
    "实验二物理天平间接测量金属杯的密度"
    temp = []
    print("金属杯的密度计算")
    for D, d, H, h, m in cup:
        vol = volume(D, d, H, h)
        temp.append(m / vol)
    experiencement(temp)


def standard_error_V():
    "实验二物理天平金属杯体积平均值的标准差"
    sitaV = ((dV_dD * sitaD)**2 + (dV_dd * sitad)**2 +
             (dV_dH * sitaH)**2 + (dV_dh * sitah)**2)**0.5
    SA = (sitam**2 + (sitaV / V_average)**2)**0.5   # 密度第一类不确定度分量
    SB = 0.115  # 密度第二类不确定度分量
    S = (SA**2 + SB ** 2)**0.5  # 密度合成不确定度
    ΔN = 1.96 * S  # 扩展不确定度
    print("金属杯体积平均值得实验标准差为%.3f,金属杯密度平均值第一类不确定度分量为%.3f,第二类不确定度分量为%.3f,合成不确定度为%.3f,扩展不确定度为%.3f。"
          % (sitaV, SA, SB, S, ΔN))


def volume_ajimide():
    "实验三阿基米德排水法计算金属杯密度"
    average = cmc.average(temp_ρ)   # 密度平均值
    SA = cmc.standard_error(temp_ρ)[1]  # 第一类不确定度
    SB = 0.001 / (3**0.5)   # 第二类不确定度
    S = (SA ** 2 + SB ** 2)**0.5  # 密度合成不确定度
    ΔN = 1.96 * S  # 扩展不确定度
    print("金属杯密度平均值为%.3f,金属杯密度平均值第一类不确定度分量为%.3f,第二类不确定度分量为%.3f,合成不确定度为%.3f,扩展不确定度为%.3f。"
          % (average, SA, SB, S, ΔN))


# experiencement(d_boa)
# experiencement(D_wir)
# cup_expe(cup)
# volume_calculate()
# standard_error_V()
# density_calculate()
volume_ajimide()
