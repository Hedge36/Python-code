# 水力学实验报告
import math
g = 9.8
r = round

def experiment1():
    '伯努利和毕托管实验'
    Δh = [12.5e-2,1.8e-2,13.4e-2,15e-2] # 水头差
    Q = 2.35e-4 # 流量
    d = [14e-3,25e-3,14e-3,14e-3]  # 对应测点管道内径
    Vs = [r((2*g*h)**0.5,3) for h in Δh] # 点流速
    Va = [r(4*Q/3.14/d**2,3) for d in d] # 平均流速
    print("第一次测量各测点点流速：")
    print(Vs)
    print("第一次测量各测点平均流速：")
    print(Va)


def experiment2():
    '雷诺实验'
    pass


def experiment3():
    '文丘里实验'
    d1 = 1.4e-2
    d2 = 0.8e-2
    a = d2/d1
    Δh = [12.7e-2, 22.7e-2, 14.8e-2, 16.3e-2, 12.1e-2, 26.9e-2, 10e-2]  # 水头差
    t = [16.50, 12.86, 15.42, 14.49, 17.00, 11.26, 18.21]  # 时间注记
    V = 1200   # 体积/cm3
    A = 3.14*d2**2/4
    K = A/(1-a**4)**0.5*(2*g)**0.5
    Q0 =[r(V/t,3) for t in t]
    Q = [r(K*h**0.5*1e6,3) for h in Δh]
    μ = [r(Q0[i] / Q[i],3) for i in range(len(Q))]
    print("实际流量(cm3/s)：")
    print(Q0)
    print("理论流量(cm3/s)：")
    print(Q)
    print("流量比：")
    print(μ)
    print("流量系数(cm2/s)：")
    print(K*1e4)


def experiment4():
    "局部阻力系数测量系数"
    D1 = 1.02    # 管道1内径/cm
    D2 = 2.01    # 管道2内径/cm
    D3 = 1.06    # 管道3内径/cm
    h12 = [0.5, 2.9, 4.2, 0.9, 1.8]  # 1，2两点间的水头差/cm
    h23 = [0.1, -0.3, -0.4, -0.1, -0.2]  # 2，3两点间的水头差/cm
    h34 = [-0.2, -0.1, -0.1, -0.3, -0.1]  # 3，4两点间的水头差/cm
    h45 = [-2.2, -10.6, -15.3, -4.1, -6.8]  # 4，5两点间的水头差/cm
    h56 = [-0.4, -1.7, -2.4, -0.6, -1.1]  # 5，6两点间的水头差/cm
    Q = [46.8,103.6,125.2,61.6,83.5]    # 流量/(cm3/s)
    A1 = 3.14*D1**2/4   # 管道1截面面积
    A2 = 3.14*D2**2/4   # 管道2截面面积
    A3 = 3.14*D3**2/4   # 管道3截面面积
    hv1 = [(Q[i]/A1)**2/2/g for i in range(len(Q))] # 突扩前速度水头
    hv2 = [(Q[i]/A2)**2/2/g for i in range(len(Q))]  # 突扩后速度水头
    hv3 = [(Q[i]/A3)**2/2/g for i in range(len(Q))]  # 突缩后速度水头
    hw1 = [-r(h12[i]-hv1[i]+hv2[i],3) for i in range(len(Q))]  # 突扩水头损失
    hw2 = [-r(h56[i]-hv2[i]+hv3[i],3) for i in range(len(Q))]  # 突缩水头损失
    ζk = [r(hw1[i]/hv1[i],3) for i in range(len(Q))]  # 突扩阻力系数
    ζs = [r(hw2[i]/hv2[i],3) for i in range(len(Q))]  # 突缩阻力系数
    print(hw1)
    print(hw2)
    print(ζk)
    print(ζs)

def experiment5():
    "沿程水头损失实验"
    d = 0.72e-2 # 圆管直径/cm
    L = 85e-2   # 测量段长度/cm
    def v(t):
        "运动粘滞系数/(m2/s)"
        μ = 1.78e-3/(1+3.37e-2*t+2.21e-4*t**2)
        v = μ / 1000
        return v
    t = [25.4, 26.6, 27.8, 28.4, 28.6,
        28.6, 28.7, 28.7, 29.0, 28.7, 29.0] # 温度注记
    vs = [v(t) for t in t]
    d = 0.72e-2  # 圆管直径/m
    L = 85e-2   # 测量段长度/m
    A = 3.14/4*d**2
    v = [11.06, 22.80, 31.21, 482.62, 519.73, 286.77, 303.73,
        340.83, 445.52, 462.72, 470.33]    # 流速/(cm/s)
    hf = [0.5, 1.54, 2.20, 304, 328, 125, 141, 169, 265, 281, 441]
    x = [math.log10(v[i]) for i in range(len(v))]
    y = [math.log10(hf[i]) for i in range(len(hf))]
        

experiment4()
