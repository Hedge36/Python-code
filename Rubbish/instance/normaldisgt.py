import numpy as np
import matplotlib.pyplot as plt
import time


def main_draw():
    x = np.random.randint(100, high=2000, size=10000)
    y = np.random.randint(200, high=3000, size=10000)

    # z1x,z1y = [],[]
    # z2x,z2y = [],[]
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
    plt.yticks(range(0, int(y_max * 1.2), 250))
    # np.where(condition)返回满足condition的数组索引号
    columns = np.where(x > y)
    # 数组切片
    x_r = x[columns]
    x_b = np.delete(x, columns)
    y_r = y[columns]
    y_b = np.delete(y, columns)
    plt.scatter(x_r, y_r, c="r", marker='s')
    plt.scatter(x_b, y_b, c="b", marker='s')

    # 画一条斜率分界线
    # max =int( x_max if x_max >y_max else y_max)

    line_y30 = x_max * (pow(1 / 3, 0.5))
    # 或者直接line_30 = x_max * np.tan(np.pi/6)
    line_y45 = x_max
    line_y60 = x_max*(pow(3, 0.5))
    plt.grid("true")
    # 画直线不用这么麻烦，参数[x1,x2],[y1,y2]，表示各自的范围，自动连线，但效率是差不多的
    plt.plot([0, x_max], [0, line_y30], color='black', linewidth=1)
    plt.plot([0, x_max], [0, line_y45], color='black', linewidth=1)
    plt.plot([0, x_max], [0, line_y60], color='black', linewidth=1)

    # plt.scatter(z1x,z1y,c ="r",marker="s")
    # plt.scatter(z2x,z2y,c ="b",marker="s")


start = time.time()
main_draw()
total = time.time() - start
print(total)
plt.show()


# for i in range(5):
#     print("第{}次作图".format(i+1))
#     print("第{}组随机数已生成".format(i+1))
#     main_draw(i+1)
#     print("第{}副图已完成".format(i+1))

# print("Work done!!!\n")
