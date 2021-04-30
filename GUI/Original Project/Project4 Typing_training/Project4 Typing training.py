import tkinter as tk
import tkinter.messagebox as tkm
import time
import random
import string
from tkinter import ttk

window = tk.Tk()
window.title("Typing Training")
window.geometry("300x300+600+220")
window.resizable(width=False, height=False)

mode = tk.IntVar()
mode.set(1)


def diffculty():
    """规定游戏难度"""
    diff = mode.get()
    if diff == 1:
        simple()
    elif diff == 2:
        normal()
    elif diff == 3:
        difficult()
    else:
        tkm.showwarning(title="Alter", message="暂未开放，敬请期待。")


def simple():
    """简单模式，记忆数字键盘"""
    allnumber = list(string.digits)  # 所有数字
    train(allnumber)


def normal():
    """常用模式，记忆所有大小写字母"""
    allletter = list(string.ascii_letters)  # 所有大小写字母
    train(allletter)


def difficult():
    """困难模式，记忆键盘所有单个输入"""
    allprint = list(string.printable)[:-6]  # 所有字符
    train(allprint)


def Type():
    """打字模式，模拟平时打字，直接键入字词"""
    allword = list(string.printable)  # 常见词组
    # 上网爬取保存成数据库?
    pass


def diff_init():
    """难度选择框初始化"""
    y0 = 5  # 第一个标签高度
    ydis = 30  # 标签间的高度
    # 框架定义
    diffframe = tk.Frame(window, bd=1, relief="groove",
                         height=2*y0+4*ydis, width=220)
    diffframe.place(x=50, y=90)
    # 难度1
    tk.Radiobutton(diffframe, text="Simple", variable=mode,
                   value=1).place(x=10, y=y0)
    tk.Label(diffframe, text="纯数字").place(x=110, y=y0)
    # 分隔线
    s1 = ttk.Separator(diffframe, orient='horizontal')
    s1.place(x=20, y=y0+ydis-2, width=180, height=2)
    # 难度2
    tk.Radiobutton(diffframe, text="Normal", variable=mode,
                   value=2).place(x=10, y=y0+ydis)
    tk.Label(diffframe, text="所有大小写字母").place(x=110, y=y0+ydis)
    s2 = ttk.Separator(diffframe, orient='horizontal')
    s2.place(x=20, y=y0+2*ydis-2, width=180, height=2)
    # 难度3
    tk.Radiobutton(diffframe, text="Difficult", variable=mode,
                   value=3).place(x=10, y=y0+2*ydis)
    tk.Label(diffframe, text="所有字符").place(x=110, y=y0+2*ydis)
    s3 = ttk.Separator(diffframe, orient='horizontal')
    s3.place(x=20, y=y0 + 3*ydis - 2, width=180, height=2)
    # 难度4
    tk.Radiobutton(diffframe, text="Type", variable=mode,
                   value=4).place(x=10, y=y0+3*ydis)
    tk.Label(diffframe, text="词组").place(x=110, y=y0+3*ydis)


def train(allletters):
    """练习窗口"""

    trainwindow = tk.Tk()
    trainwindow.title("Type training")
    trainwindow.geometry("240x200+640+270")
    trainwindow.resizable(width=False, height=False)
    start, count, right, typetime, answer = 0, 0, 0, 0, "0"

    def checkkey(event):
        """验证输入是否有效并对有效输入计数（不同于validate）"""
        nonlocal count, right, ask, answer, start
        if event.char in allletters:
            if event.char == answer and count != 0:
                right += 1
            if count == 1:
                start = time.time()
            typeinfo["text"] = "当前练习情况: %d/%d" % (right, count)
            answer = random.choice(allletters)
            ask["text"] = answer
            count += 1
        if len(entry.get()) > 8:
            entry.delete(0, 1)  # 删除第一个字符，防止过长

    def outcome():
        """结果展示"""
        nonlocal count, right, start, typetime
        if start:
            typetime = time.time() - start      # 总用时
            acculate_rate = right / (count-1) * 100          # 准确率
            average_acculate = right * 60 / typetime  # 每分钟有效码字率
        else:
            acculate_rate = average_acculate = 0

        ocwindow = tk.Tk()
        ocwindow.title("Type training")
        ocwindow.geometry("260x200+650+250")
        ocwindow.resizable(width=False, height=False)
        tk.Label(ocwindow, text="共计用时 %.2fs, 共键入字符 %d个" %
                 (typetime, count-1)).place(x=40, y=30)
        tk.Label(ocwindow, text="练习正确率 : %.2f%%" %
                 acculate_rate).place(x=40, y=60)
        tk.Label(ocwindow, text="分钟有效码字 : %.1f 词/分钟" %
                 average_acculate).place(x=40, y=90)
        tk.Button(ocwindow, text="退出", command=window.quit,
                  width=10).place(x=90, y=130)

    tk.Label(trainwindow, text="请按照以下要求键入对应的按键:").place(x=40, y=20)
    ask = tk.Label(trainwindow, text="Ready?", font=("Arial", "12"),
                   width=10, height=1)
    ask.place(x=70, y=48)

    entry = tk.Entry(trainwindow)
    # entry.focus_set()
    entry.place(x=50, y=80)
    entry.bind('<Key>', checkkey)
    typeinfo = tk.Label(trainwindow, text="当前练习情况: 0/0")
    typeinfo.place(x=50, y=110)
    tk.Button(trainwindow, text="查看结果", width=10,
              command=outcome).place(x=80, y=145)


if __name__ == "__main__":
    diff_init()
    tk.Label(window, text="难度选择：").place(x=50, y=20)
    tk.Label(window, text="根据说明，在以下选择中选择一个难度\n进行练习").place(x=50, y=40)
    tk.Button(window, text="确认", width=10,
              command=diffculty).place(x=110, y=230)
    window.mainloop()
