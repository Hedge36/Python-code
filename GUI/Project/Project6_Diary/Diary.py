import tkinter as tk
from time import asctime
from tkinter import messagebox as tkm
from tkinter import scrolledtext as st
from tkinter import filedialog
from PIL import Image, ImageTk


def gettime():
    """获取当前时间并实时显示"""
    pretime = asctime().split(" ")
    year = pretime[4]
    month = pretime[1]
    date = pretime[2]
    detailtime = pretime[3]
    week = pretime[0]   # 可以逐项具体打印的
    timeshow["text"] = pretime  # 动态修改标签
    window.after(100, gettime)


def read():
    """阅读模式"""
    pass


def write():
    """撰写模式"""
    pass


def savefile():
    """保存文本模式"""
    if mode.get() == 1:
        content = diarywrite.get(1.0, tk.END)
        savepath = filedialog.asksaveasfilename(title="选择文件保存路径",
                                                initialdir=".", filetypes=[("文本文件", ".txt"), ("Markdown文件", ".md")])
        tkm.showinfo(title="Tip", message="功能尚在开发中，只是做个样子！")
    else:
        tkm.showwarning("Alert", message="请先更换至写入模式!")


def indicate(*agrs):
    """已选模式着色处理"""
    if mode.get() == 1:
        mode1["fg"] = "red"
        mode2["fg"] = "black"
        diarywrite.place(x=10, y=12)
        diaryshow.place_forget()
    else:
        mode2["fg"] = "red"
        mode1["fg"] = "black"
        diaryshow.place(x=10, y=12)
        diarywrite.place_forget()


window = tk.Tk()
window.title("随笔日记")
window.geometry("450x550")
window.resizable(0, 0)  # 锁定屏幕大小
# 背景图片
background_image = ImageTk.PhotoImage(Image.open("1.png"))
background_label = tk.Label(window, image=background_image, anchor='nw')
background_label.place(relwidth=1, relheight=1)


# 标题展示框
Screentitle = tk.Label(text="随笔心记", width=10, height=2, font="楷体 14",
                       bd=1, relief="groove")
Screentitle.place(x=175, y=10)

# 程序描述框
Description = tk.Label(text="程序描述", width=40, height=5, font="楷体 14",
                       bd=1, relief="groove")
Description.place(x=24, y=60)

# 模式选择框
window.update()  # 刷新框宽度并同步
width = Description.winfo_width()
modebox = tk.LabelFrame(text="Mode", height=50, width=width, bd=1,
                        relief="groove")
modebox.place(x=24, y=165)

mode = tk.IntVar()
mode1 = tk.Radiobutton(modebox, text="Write", variable=mode, value=1,
                       highlightcolor="red", activeforeground='red',
                       font="宋体 12")
mode2 = tk.Radiobutton(modebox, text="Read", variable=mode, value=2,
                       font="宋体 12")

mode1.place(x=60, y=0)  # box内的坐标采用相对坐标(其实都是，父容器不同而已)
mode2.place(x=240, y=0)

# 时间展示框
timeshow = tk.Label(width=40, height=2, bg="yellow", font="楷体 14")
timeshow.place(x=24, y=230)
window.after(100, gettime)  # 实时显示时间

# 写入展示框
Detail = tk.LabelFrame(text="Detail", width=width,
                       height=200)
window.update()  # 刷新框宽度并同步
Detail.place(x=24, y=timeshow.winfo_height()+240)
diarywrite = st.ScrolledText(Detail, width=50, height=11, highlightcolor="sky blue",
                             highlightthickness=1)   # 改字体有点麻烦，又要引库，懒得改了

diaryshow = tk.Label(Detail, text="文本展示框", width=50, height=8)


# 保存文件
window.update()  # 刷新框宽度并同步
save = tk.Button(text="Save", width=6, height=1, font="Arial 13",
                 command=savefile)
save.place(x=130, y=Detail.winfo_height()+timeshow.winfo_height()+250)

close = tk.Button(text="Quit", width=6, height=1, font="Arial 13",
                  command=window.quit)
close.place(x=250, y=Detail.winfo_height() + timeshow.winfo_height() + 250)

mode.trace("w", indicate)
window.mainloop()
