#TextProBarV3.py                     完整效果文本进度条
import random
s = '0123456789'
b = random.randint(0,10)                   #答案设定
i = 0                       #计数变量
print('游戏规则：\n猜一个小于10的数字')
while str(b) in s:
    a = input('请输入您的答案:\n')
    i=i+1
    if str(a) in s and int(a) < 10 :
        if int(a) == b:
            if i==1:
                print('恭喜你猜对了！\n本次猜数字您只猜了{}次，您看了剧本？？？'.format(i))
                break
            if 1<i<=3:
                print('恭喜你猜对了！\n本次猜数字您只猜了{}次，太厉害了吧！'.format(i))
                break
            if 9>=i>=4:
                print('恭喜你猜对了！\n本次猜数字您共猜了{}次，您太菜了吧！'.format(i))
                break
            if i==10:
                print('恭喜你猜对了！\n本次猜数字您共猜了{}次，您怕不是猪哦！'.format(i))
                break            
        elif int(a) < b:
            print('很可惜您猜的数字偏小了，再加把劲吧！')
        elif int(a) > b:
            print('很可惜您猜的数字偏大了，再加把劲吧！')
    else:
        print('输入格式有误，请重新输入!')
input()
