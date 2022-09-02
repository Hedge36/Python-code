import matplotlib.pyplot as plt
from math import pi


def init(file_path):
    with open(file_path, "r", encoding='UTF-8-sig') as file:
        texts = []
        for l in file:
            lc = l.replace('\t', ' ').strip().split(' ')
            i = 0
            for s in lc:
                if type(eval(s)) is float:
                    i += 1
            if i == len(lc):
                texts.append(lc)
    return texts


def get_data(file_lists, n=1, start=0):
    size = len(file_lists)
    F = []  # 应力大小
    x = []  # 位移
    t = []  # 时间注记
    for data in file_lists:
        F.append(float(data[0]))    # 将字符串数字转化为浮点数类型
        x.append(float(data[1]))

    def track():
        nonlocal start
        stage = 0   # 阶段标注
        for i in range(start, size):
            if stage == 0:  # 弹性阶段
                if F[i + 1] > F[i] and start == 0:
                    pass
                else:
                    N1, Mmax = i + 1, F[i]
                    Mmin = Mmax
                    stage = 1
                    # 选项：屈服阶段起点
                    # print(i+1)
            else:   # 屈服阶段
                if min(F[i:int(size / 4) + 1]) == F[i]:
                    Mmin = F[i]
                    start = i + 2
                    break
        return Mmin
    Mmin = track()
    # 屈服荷载
    print("Yield load:", Mmin, 'kN')
    Ps = Mmin * 1e3    # 屈服阶段最小轴力
    d = 12,
    A = pi * d[n - 1]**2 / 4
    yield_limit = round(Ps / A, 3)
    print('Yield_limit:', yield_limit, 'N/mm²')
    return F, x, start


def draw(x, F):
    "图形绘制"
    def order_check(x):
        "检查x坐标是否满足绘图顺序要求"
        size = len(x)
        ordered = True
        for i in range(size - 1):
            i += 1
            if x[i] > x[i - 1]:
                pass
            else:
                print(i, x[i], x[i - 1])
                ordered = False
            return ordered
    if order_check(x):
        print("Loading......")
        plt.plot(x, F)
        plt.title("Stress-Strain")
        plt.xlabel("Strain x/mm")
        plt.ylabel("Stress σ/(N/mm²)")
        plt.show()
        print("Doned.")
    else:
        print("Abscissa is not a 1-D ordered array!")


def run(file, start, n=1, times=1):
    "file为目标文件路径；n为低碳钢序号"
    print("Experiment number：", n)
    print("Number of runs:", times)
    file_lists = init(file)
    F, x, start = get_data(file_lists, n, start)
    # draw(F,x)
    return start, times


def main():
    start, times = run('DAQ：力, … - (实时值) - 副本.txt', 0, 1, 1)
    check = True
    while check:
        check_again = input(
            "Do you want to skip this result for another data?Yes/No.\n")
        print()
        if check_again == 'Yes' or check_again == 'yes':
            times += 1
            start = run('DAQ：力, … - (实时值).txt', start, 1, times)[0]
        else:
            check = False
    print("Doned.")


if __name__ == "__main__":
    main()
