# experiment_of_light
from math import*
data_experiment = []
data_nubuda = []
d = 3331.700    # 已知的光栅常数
degree_zero = 170 + 9 / 60  # 零级光谱对应角度
data_experiment_preHg = [(190, 28), (190, 22), (149, 48), (149, 45)]    # 预读数据
nubuda_pre = 577.000    # 已知汞灯黄色谱线波长
print("实验9角色散率计算")


def cos_x(x, y):
    degree = x + y / 60  # 衍射角
    radian = radians(degree)    # 衍射角对应弧度
    cos_x = cos(radian)
    # print(degree, radian, cos_x)
    return cos_x


D1 = (-2) / d / cos_x(0, 6)
D2 = 2 / d / cos_x(0, 3)
D = (D1 + D2) / 2
print(D1, D2, D)
