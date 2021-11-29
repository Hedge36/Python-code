# 汉诺塔

def hanoi(n, src, dst, mid):  # (圆盘的个数，左塔标记，右塔标记，中塔标记)
    global count
    if n == 1:
        print('{}:{}->{}'.format(1, src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print('{}:{}->{}'.format(n, src, dst))
        count += 1
        hanoi(n-1, mid, dst, src)  # 函数递归


print('汉诺塔：\n汉诺塔（又称河内塔）问题是源于印度一个古老传说的益智玩具。大'
      '梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序'
      '摞着64片黄金圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在'
      '另一根柱子上。并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能'
      '移动一个圆盘。')
count = 0
n = eval(input("输入圆盘个数:【注：左塔\"A\"，中塔\"B\"，右塔\"C\"】\n"))

hanoi(n, "A", "C", "B")
print("共需要搬运{}次。".format(count))
input()
