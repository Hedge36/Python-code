# hesitating and casting
# 犹豫不决？投一投。
# 表决机器人
'''
模拟人格表决：
自我 4；6         20
zj   8：2         15    
lj   7：3         15        
模拟性格表决：
积极：4；6        20
消极：3；7        30
保守；4;6         20
创新；7;3         20
天命 5；5         50 
'''
import random
import os
import time

'''copyright
__author__ = 'hedge'
__date__ = 2020.10.7
__version__ = 1.1
'''

record = 0  # 单次通过票数
total_score = 0  # 单次净得分
records = 0  # 统计通过票数
result_myself = 1  # 单次模拟表决结果
result_Lijia = 1
result_Zoujie = 1
result_moni = 0     # 每次的模拟结果
circle = 100   # 预设循环次数
control_line = 50   # 通过分数控制线


def init_():
    print("《————————————————————遇事不决，可问上帝—————————————————————》")
    print("本程序模拟分为三个人格向，根据预设参数随机给出评判，此外上帝仅供参考。")
    # os.system('cls')    # 清屏
    thing = input("请输入你想要占一卦的事情:\n")
    try:
        print("关于\"%s\"这件事情模拟表决结果如下：" % (thing))
    except:
        print("模拟表决结果如下")


def myself():
    "模拟自我人格进行表决，其中保守占6成，进取占4成，比重20分，最终根据随机取数表达态度"
    global total_score, record, result_myself
    record = 0  # 重置单次赞成票数
    total_score = 0  # 重置单次净得分
    score = random.randint(1, 11)
    if score >= 4:
        print("本我：反正你一无所有，失败又何妨？试一试又何妨？")
        record += 1
        result_myself = 1
    else:
        print("本我：何苦为难自己呢，做好本分就行，既然不适合，就不去了吧。")
        result_myself = 0
    total_score += score*2


def Zoujie():
    "邹洁表决，其中保守占2成，进取占8成，比重40分，最终根据随机取数表达态度"
    global total_score, record, result_Zoujie
    score = random.randint(1, 10)
    if score >= 2:
        print("邹洁：试一试咯，相信你可以的")
        record += 1
        result_Zoujie = 1
    else:
        print("邹洁：不想去就算了吧，也没必要去")
        result_Zoujie = 0
    total_score += score*4


def Lijia():
    "李佳表决，其中保守占3成，进取占7成，比重40分，最终根据随机取数表达态度"
    global total_score, record, result_Lijia
    score = random.randint(1, 10)
    if score >= 3:
        print("李佳：可以试一试")
        record += 1
        result_Lijia = 1
    else:
        print("李佳：不用为难自己")
        result_Lijia = 0
    total_score += score*4


def print_score():
    "统计综合得分并对最后的结果进行综合分析得出最终结果"
    global total_score, result_moni
    # print("最终随机得分为%d"%(total_score))
    #print("共计%d票赞成票，%d票反对票"%(record, 3-record))
    if total_score >= control_line:
        print("模拟投票综合结果：可以一试")
        result_moni = 1
        # print("我：嗯？还不想去？那你点进来干嘛？搬砖去好吧？时间很宝贵的行吧。")
    else:
        print("模拟测试综合结果：不必勉强")
        result_moni = 0
    print("———————————————————————————————————————")


def god():
    "遇事不决，可问上帝，上帝来也"
    result_god = ["可以一试", "不必勉强"]
    print("姗姗来迟的上帝：我觉得%s，但是我不知道当今时代我说话还算不算数(・∀・）" %
          (random.choice(result_god)))


def main():
    "主程序函数"
    init_()
    myself()
    Zoujie()
    Lijia()
    print_score()
    god()


def check():
    "校检函数，运用统计学办法多次运行计算赞成的概率，计算其中的欺诈性"
    start = time.perf_counter()
    print("测试模式进行中，循环估计用时%.2fs\n" % (circle * 0.02))
    for i in range(1, circle+1):
        global records, result_moni
        main()
        records += result_moni
    print("%d次循环计算得到试一试的概率是%.2f%%" % (circle, records / circle * 100))
    print("计算实际用时：%.5fs" % (time.perf_counter() - start))


'''
当综合通过分数控制线为40时，通过概率约为81%；
当综合通过分数控制线为50时，通过概率约为64%；
当综合通过分数控制线为60时，通过概率约为43%；
当综合通过分数控制线为70时，通过概率约为24%；
'''


def check_part():
    "局部调试函数"
    for i in range(1, circle+1):
        myself()
    print("此部分运行正常")


if __name__ == '__main__':
    main()
    # check()
    # check_part()

input()  # 命令行驻留

'''
关于后续的改进办法：
1.关联data文档，保存每一次占卦的事情，留作纪念；
2.设计check部分，算出赞成与反对分别的概率，了解程序本身的欺骗性，不推荐，下面是目前暂定方案：
(1)按照算法逐步计算，改动篇幅较大
(2)在main函数上面设计循环，最后统计概率，这里涉及每次都会输出的问题，屏幕很乱。
   此外出现的问题，为什么不能重复跑myself()。-----已解决
(3)多线程运行加快计算速度
'''
