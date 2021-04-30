# calculate of experiment 6
# 1.Melting heat of ice

cmc = __import__("common math calculate")
import math

__experience__ = "冰的熔化热的测量"
m0 = 102.15  # 量热器内筒中所取温水的质量g
m1 = 28.63  # 量热器内筒及搅拌器的质量g
m = 34.23   # 冰的质量g
c = 4.18  # 水的比热
C1 = 0.9  # 铝制量热器内筒及搅拌器的比热
t0 = 36.0   # 修正后投冰前系统的平衡温度。
t1 = 8.0    # 修正后投冰后系统的平衡温度。
L0 = 334  # 冰的熔化热标准值

__experience__ = "液体比热容的测量"
ms = 13.86  # 盐水的质量
mw = 12.94  # 水的质量
c2 = 0.389   # 铜制量热器内筒及搅拌器比热
m2 = 42.26  # 盐水比热实验中量热器内筒及搅拌棒的质量
Tw_t = [11.9, 11.1, 9.5, 8.1, 6.9, 5.9, 5.0, 4.3, 3.7, 3.1,
        2.7, 2.3, 1.9, 1.7, 1.4, 1.2, 1.0, 0.9, 0.7, 0.7,
        0.5, 0.5, 0.3, 0.3, 0.2, 0.3, 0.2, 0.2, 0.1, 0.2, 0.2]    # 纯水温度差随时间变化
Correct_Tw = [math.log(x) for x in Tw_t[1:18 + 1]]  # 修正后的纯水随时间温度变化
Ts_t = [12.6, 11.2, 8.2, 6.0, 4.5, 3.4, 2.6, 2.0, 1.5, 1.2,
        0.9, 0.7, 0.5, 0.4, 0.3, 0.2, 0.2, 0.1, 0.1, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # 饱和食盐水温度差随时间变化
Correct_Ts = [math.log(x) for x in Ts_t[1:17 + 1]]  # 修正后的盐水随时间温度变化
t = [x for x in range(30 + 1)]   # 时间注记
Sw = cmc.liner_fitting(t[1:len(Correct_Tw) + 1], Correct_Tw)[0]  # 水的拟合直线斜率
Ss = cmc.liner_fitting(t[1:len(Correct_Ts) + 1], Correct_Ts)[0]  # 盐水的拟合直线斜率
cs = 3.29   # 常温下饱和食盐水的比热(g/℃)


def c_L():
    L = (m0 * c + m1 * C1) * (t0 - t1) / m - c * t1
    return L


def c_Cx():
    Cx = ((mw * c + m2 * c2) * Sw / Ss - m2 * c2) / ms
    return Cx


def main():
    print("实验测得冰的熔化热为%.2fJ/g，标准值为%.2fJ/g" % (c_L(), L0))
    print("实验测得冰的熔化热相对误差为%s" % (cmc.relative_error(c_L(), L0)))
    print("实验测得盐水的比热为%.2fJ/g，常温下饱和食盐水比热的标准值为%.2fJ/g" % (c_Cx(), cs))
    print("实验测得盐水的比热相对误差为%s" % (cmc.relative_error(c_Cx(), cs)))


if __name__ == '__main__':
    main()
