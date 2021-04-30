# experiment_of_light
from math import*
data_experiment = []
data_nubuda = []
d = 3331.700    # 已知的光栅常数
degree_zero = 170 + 9 / 60  # 零级光谱对应角度
data_experiment_preHg = [(190, 28), (190, 22), (149, 48), (149, 45)]    # 预读数据
nubuda_pre = 577.000    # 已知汞灯黄色谱线波长
print("实验9汞灯黄色谱线波长计算")
nubuda = 0


def data_load():
    "实验数据读取，且固定为4组"
    i = 1
    while i != 5:
        data_experiment.append(eval(input("请输入第%d组实验数据:" % i)))
        i += 1


def calulate_of_nubuda(du, fen):
    "输入实验记录所得的角度，计算数据对应波长"
    degree = du + fen / 60 - degree_zero  # 衍射角
    radian = radians(degree)    # 衍射角对应弧度
    if degree > 0:
        k = round(degree // 10)
    else:
        k = -round(-degree // 10)  # 对应级数
    sins = sin(radian)
    nubuda = d * sins / k
    data_nubuda.append(nubuda)
    print("%d级光谱数据对应的波长为%.3fnm(保留三位小数)" % (k, nubuda))


def result_print(data_experiment):
    "输出所得的4组波长值并求平均数"
    i = 1
    for du, fen in data_experiment:
        calulate_of_nubuda(du, fen)
    average = sum(data_nubuda) / 4
    print("Hg黄色光谱波长nubuda的平均值为%.3fnm" % (average))
    print("相对误差为%.2f%%" % ((average - nubuda_pre) / nubuda_pre * 100))


def main():
    # data_load()
    result_print(data_experiment_preHg)


main()
