# 猜数字游戏
from random import*
from time import perf_counter
start = perf_counter()
print("Tip:无校正程序，请勿输入其他形式数据,此外，八位数开始可能会造成电脑卡顿。")
c = int(input("输入答案位数(小于10):"))            # 答案位数确认
ls0 = ['0', '1', '2', '3']                            # 游戏难度序列
print("选择游戏难度:其中0，1，2，3分别为简单，普通，困难，赌博难度，可尝试次数分别为区间长度d/1，[d/3],[d/5]和1次。")
dif = input()
while dif not in ls0:
    print("输入格式有误，请重新输入。")
    dif = input()
dif = int(dif)
m = 10**(c-1)
n = 10**c
s = list(range(m, n))                               # 报错校正列表
b = randint(m, n)                                   # 答案设定
i = 0
Max1 = (n-m)//3                                    # 普通难度最大尝试次数
Max2 = (n-m)//5                                    # 困难难度最大尝试次数
大写数字 = '一两三四五六七八九'
难度 = ['简单', '普通', '困难', '赌博']
print('游戏说明：\n当前游戏难度为{}难度，您需要猜一个{}位数,答案将由系统随机生成，可尝试次数用尽后游戏将结束。'.format(
    难度[dif], 大写数字[c-1]))
print('温馨提示：输入格式错误时同样会计算次数。')
while b in s:
    if dif == 1 and i >= Max1:                       # 判定游戏是否可以继续
        print("您已经达到了当前难度最大尝试次数{}次，游戏结束。".format(i))
        break
    elif dif == 2 and i >= Max2:
        print("您已经达到了当前难度最大尝试次数{}次，游戏结束。".format(i))
        break
    elif dif == 3 and i == 1:
        print("您已经达到了当前难度最大尝试次数1次，不是欧皇劝您清醒一下。")
        break
    else:                                        # 游戏正常程序
        a = input('请输入您的答案:\n')
        i += 1
        try:
            if eval(a) == '':
                print('游戏结束，您失败了。')
                break
            if int(a) in s and m < int(a) < n:
                if int(a) == b:                  # 判定答案
                    print('恭喜你猜对了！\n本次猜数字您共猜了{}次。'.format(i))
                    print("本次用时：{:.2f}s".format(perf_counter()-start))
                    break
                elif int(a) < b:                 # 提示信息
                    print('很可惜您猜的数字偏小了，再加把劲吧！')
                elif int(a) > b:
                    print('很可惜您猜的数字偏大了，再加把劲吧！')
            else:
                print('输入格式有误，请重新输入!')
        except:
            print('输入格式有误，请重新输入!')
input("输入回车或者Ctrl+C以退出程序\n")
