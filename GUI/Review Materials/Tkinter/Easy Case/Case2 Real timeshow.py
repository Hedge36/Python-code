import tkinter as tk

window = tk.Tk()
window.title("test")
window.geometry("400x300")

st = tk.IntVar()    # 样式选择类型
mode = tk.IntVar()    # 模式选择类型
dt = tk.IntVar()    # 详情展示类型


def styletrace(*args):
    print("Track the variety of style.")
    if st.get() == 1:
        checkbox1.place(x=30, y=150)
        checkbox2.place_forget()
    elif st.get() == 2:
        checkbox1.place_forget()
        checkbox2.place(x=170, y=30)
    pass


def detail(*args):
    """根据选项，实时显示"""
    if mode.get() == 1:
        detailbox2.place_forget()
        detailbox1.place(x=0, y=0)
    elif mode.get() == 2:
        detailbox1.place_forget()
        detailbox2.place(x=0, y=0)


def click1(*args):
    mode.set(1)
    choice21["bg"] = "lightgray"
    choice21["bd"] = 1
    choice22["bg"] = "SystemButtonFace"
    choice22["bd"] = 0    

def click2(*args):
    mode.set(2)
    choice21["bg"] = "SystemButtonFace"
    choice21["bd"] = 0
    choice22["bg"] = "lightgray"
    choice22["bd"] = 1

    
# 样式选择框
stylebox = tk.LabelFrame(window, height=100, width=100, text="Style",
                         visual="best")
stylebox.place(x=30, y=30)
# 样式选择
style1 = tk.Radiobutton(stylebox, text="style1", value=1, variable=st)
style2 = tk.Radiobutton(stylebox, text="style2", value=2, variable=st)
style1.place(x=10, y=10)
style2.place(x=10, y=45)


# 样式1模式选择框
checkbox1 = tk.LabelFrame(window, height=100, width=100, text="Mode",
                         visual="best")
# 样式1模式选项
choice11 = tk.Radiobutton(checkbox1, text="mode1", value=1, variable=mode)
choice12 = tk.Radiobutton(checkbox1, text="mode2", value=2, variable=mode)
choice11.place(x=10, y=10)
choice12.place(x=10, y=45)

# 样式2模式选择框
checkbox2 = tk.LabelFrame(window, height=55, width=200, text="Mode",
                         visual="best")
# 样式2模式选项
choice21 = tk.Label(checkbox2, text="mode1",relief="groove",bd=0)
choice22 = tk.Label(checkbox2, text="mode2",relief="groove",bd=0)
choice21.place(x=5, relheight=1, relwidth=0.49)
choice22.place(x=100, relheight=1, relwidth=0.47)

choice21.bind("<Button-1>", click1)
choice22.bind("<Button-1>", click2)

# 详情展示框
Detail = tk.LabelFrame(window, width=200, height=160, text="Detail")
Detail.place(x=170, y=90)

detailbox1 = tk.Frame(Detail, width=180, height=120)
greet = tk.Label(detailbox1, text="Hey,")
hello = tk.Label(detailbox1, text="you have choose mode1.")
greet.place(x=20, y=20)
hello.place(x=20, y=40)

detailbox2 = tk.Frame(Detail, width=180, height=120)
Button1 = tk.Radiobutton(detailbox2, text="Yes", value=1, variable=dt)
Button2 = tk.Radiobutton(detailbox2, text="No", value=2, variable=dt)
Button1.place(x=40, y=30)
Button2.place(x=40, y=80)



# 追踪变量的变化并实时响应
st.trace("w", styletrace)
mode.trace("w", detail)
st.set(1)   # 样式选择默认为样式1


window.mainloop()
