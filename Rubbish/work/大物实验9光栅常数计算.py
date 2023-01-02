# experiment_of_light
from math import*
data_experiment = []
data_d = []
nubada = 589.3
degree_zero = 170
data_experiment_preNa = [(190, 40), (180, 12), (159, 48), (149, 17)]
#data_experiment_preHg = [(190, 38), (190, 22), (149, 48), (149, 45)]
print("实验9光栅常数计算")


def data_load():
    i = 1
    while i != 5:
        data_experiment.append(eval(input("请输入第%d组实验数据:" % i)))
        i += 1


def calulate_of_d(du, fen):
    "输入录入的角度，自动计算对应光栅常数"
    degree = du + fen / 60 - degree_zero  # 衍射角
    radian = radians(degree)    # 衍射角对应弧度
    if degree > 0:
        k = round(degree // 10)
    else:
        k = -round(-degree // 10)  # 对应级数
    sins = sin(radian)
    d = k * nubada / sins
    data_d.append(d)
    print("%d级光谱对应的光栅常数为%.3fnm(保留三位小数)" % (k, d))


def result_print(data_experiment):
    i = 1
    for du, fen in data_experiment:
        calulate_of_d(du, fen)
    average = sum(data_d) / 4
    print("光栅常数d的平均值为%.3fnm" % (average))


def main():
    # data_load()
    result_print(data_experiment_preNa)
    # result_print(data_experiment_preHg)


main()
