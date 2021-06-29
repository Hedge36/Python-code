import tkinter as tk
from tkinter import messagebox as tkm


def happy():
    win = tk.Toplevel()
    win.title('郑重警告')
    win.geometry("%dx%d+%d+%d" % (width, height, x, y))
    message = "不准你开心"
    sperator = tk.Frame(win, width=width, height=70)
    sperator.place(x=0, y=0)
    tk.Label(sperator, text=message, fg="red", font="宋体 18 bold",
             ).place(x=40, y=25)
    tk.Button(win, text='偏不，我就是开心', command=lambda: (happy(), win.destroy(), win.bell()),
              width=15).place(x=45, y=80)
    tk.Button(win, text='好好好，我不开心', command=lambda: (unhappy(), win.destroy()),
              width=15).place(x=45, y=130)


def unhappy():
    tkm.showinfo(title="没事，我很开心。",
                 message="不开心？不开心就对了，以后会更不开心的。")


window = tk.Tk()
window.title("Soul ask")
window.update()
x, y = window.maxsize()  # 获取当前屏幕像素
width, height = 210, 180
x, y = int(x/2-width/2), int(y/2-height/2)  # 计算屏幕中心坐标
window.geometry("%dx%d+%d+%d" % (width, height, x, y))  # 居中显示
tk.Label(text="你开心吗？", font="楷体 16").place(x=50, y=50)
tk.Button(text="开心", width=8, height=1, command=happy).place(x=30, y=110)
tk.Button(text="不开心", width=8, height=1, command=unhappy).place(x=120, y=110)


window.mainloop()
