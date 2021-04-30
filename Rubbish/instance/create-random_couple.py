import random


def creatranint(a, b):
    n = random.randint(a, b)
    return n

# print("————————————————————————————随机整数对产生器————————————————————————————----\n")
# n = int(input("请输入你要产生的随机数对个数\n"))
# a1,b1 = input("请输入你要产生的随机数对x的大小范围,用逗号隔开\n").split(",")
# a1=int(a1)
# b1=int(b1)
# a2,b2 = input("请输入你要产生的随机数对y的大小范围,用逗号隔开\n").split(",")
# a2=int(a2)
# b2=int(b2)
# print("---------------生成完毕，已生成一个random_couple.txt的文件在根目录-------------\n")


list = []
x = []
y = []

with open("random_couple.txt", 'w') as fp:
    # for i in range(n):
    #     x = creatranint(a1,b1)
    #     y = creatranint(a2,b2)
    #     x ="{0}".format(x)
    #     y ="{0}".format(y)
    #     fp.write(x+","+y+"\n")
    # 固定生成
    for i in range(5000):
        x = creatranint(100, 2000)
        y = creatranint(200, 3000)
        x = "{0}".format(x)
        y = "{0}".format(y)
        fp.write(x+","+y+"\n")
fp.close()

series = ['(%f, %f)' % (creatranint(100, 2000),
                        creatranint(200, 3000)) for _ in range(5000)]
x = creatranint(100, 2000)
y = creatranint(200, 3000)
