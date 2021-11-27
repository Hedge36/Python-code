# 抛硬币实验
'''
# 集合计数法
import random
print("抛硬币实验")
n = eval(input("输入模拟次数:"))
Ω=[]                   #全体事件
ls=[0,1]                #正反面
for i in range(n):
    a=random.choice(ls)
    Ω.append(a)
print("{}次实验结果如下:".format(n))
print("正面出现{}次,频率为{}。".format(Ω.count(1),Ω.count(1)/n))
print("反面出现{}次,频率为{}。".format(Ω.count(0),Ω.count(0)/n))

'''

# 字典计数法
import random
import tkinter as tk
import tkinter.messagebox


def test(content):
    "输入文本验证，过滤非数字类型"
    return_variable = False  # 设置默认返回值为False
    list1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  # 设置默认检测数列

    L_content = list(content)
    if len(content) > 1:
        del L_content[-1]

    for i in list1:  # for循环来检测最新输入的字符是否满足要求
        # 这两个条件不可以调换顺序，否则当输入框内无内容时content[-1]索引无效报错
        if content == "" or content[-1] == i:
            return_variable = True
            break
    return return_variable  # 返回值


def show():
    """显示计算结果"""
    n = entry.get()
    if n != '':
        n = int(n)
        ls = [0, 1]  # 正反面
        for i in range(n):
            a = random.choice(ls)
            counts[a] = counts.get(a, 0)+1
        outcome_win = tk.Toplevel(window)
        outcome_win.title("投币结果")
        center_x, center_y = int(screen_width/2-150), int(screen_height/2-100)

        outcome_win.geometry("300x200+%d+%d" % (center_x, center_y))
        tk.Label(outcome_win, text="%d次实验结果如下:" %
                 n).grid(row=0, padx=90, pady=15)
        tk.Label(outcome_win, text="正面出现{}次,频率为{:.3f}".format(
            counts[1], counts[1] / n)).grid(row=1, pady=5)
        tk.Label(outcome_win, text="反面出现{}次,频率为{:.3f}".format(
            counts[0], counts[0] / n)).grid(row=2, pady=5)
        tk.Button(outcome_win, text="确认", width=9, command=outcome_win.destroy).grid(
            row=3, pady=15)
        counts.clear()
    else:
        tkinter.messagebox.showwarning("Alert", "您还没有输入任何内容。")


window = tk.Tk()
window.title("抛硬币实验")
width, height = 300, 120
window.update()
screen_width, screen_height = window.maxsize()
center_x, center_y = int(screen_width/2-width/2), int(screen_height/2-height/2)
window.geometry("%dx%d+%d+%d" % (width, height, center_x, center_y))
window.resizable(0, 0)  # 窗口大小不可改变

testCMD = window.register(test)  # 需要将函数包装一下
v1 = tk.StringVar()
tip = tk.Label(window, text="输入试验次数:")
tip.grid(row=0, column=0, pady=25, padx=20)
entry = tk.Entry(window, show=None, textvariable=v1, validate="key",
                 validatecommand=(testCMD, '%P'))
entry.grid(row=0, column=1)
tk.Button(window, text="确认", width=8, command=show).grid(
    row=1, columnspan=2)
counts = {}


window.mainloop()
