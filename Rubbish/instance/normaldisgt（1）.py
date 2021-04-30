import numpy as np
import os
import matplotlib.pyplot as plt


def main_draw(n):
    k = []
    x, y = [], []
    # z1x,z1y = [],[]
    # z2x,z2y = [],[]
    for data in open("random_couple.txt", "r"):
        x1, y1 = data.split(",")
        x.append(float(x1))
        y.append(float(y1))

    # 构造区分条件
    for i in range(len(x)):
        k.append(y[i] / x[i])

    # 生成区分数据集
    # for i in range(len(x)):
    #     if k[i] >= 0.006:
    #         z1x.append(x[i])
    #         z1y.append(y[i])
    #     else:
    #         z2x.append(x[i])
    #         z2y.append(y[i])
    # #划分类
    x_max = max(x)
    y_max = max(y)
    plt.figure()
    plt.axis([0, x_max, 0, y_max])
    plt.xticks(range(0, int(x_max*1.2), 250))
    plt.yticks(range(0, int(y_max*1.2), 250))
    for i in range(len(x)):
        if k[i] >= 1:
            plt.scatter(x[i], y[i], c='r', marker='s')
        else:
            plt.scatter(x[i], y[i], c='b', marker='x')

    # 画一条斜率分界线

    # max =int( x_max if x_max >y_max else y_max)
    line_x = np.linspace(0, x_max, 500)
    line_y30 = line_x*(pow(1/3, 0.5))
    line_y45 = line_x
    line_y60 = line_x*(pow(3, 0.5))
    plt.grid("true")
    plt.plot(line_x, line_y30, color='black', linewidth=1)
    plt.plot(line_x, line_y45, color='black', linewidth=1)
    plt.plot(line_x, line_y60, color='black', linewidth=1)
    # plt.scatter(z1x,z1y,c ="r",marker="s")
    # plt.scatter(z2x,z2y,c ="b",marker="s")
    plt.savefig("fig{0}.png".format(n))
    # plt.show()


for i in range(5):
    print("第{0}次作图".format(i+1))
    os.system("python create-random_couple.py")
    print("第{}组随机数已生成".format(i+1))
    main_draw(i+1)
    print("第{}副图已完成".format(i+1))

print("Work done!!!\n")
