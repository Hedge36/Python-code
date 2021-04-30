import tkinter as tk

window = tk.Tk()
window.title("test")
window.geometry("400x300")


checkbox = tk.LabelFrame(window, height=100, width=100, text="Mode",
                         visual="best")
checkbox.place(x=30, y=100)

# detailbox = tk.Frame(window, height=200, width=200,
#                      bg="white", bd=1, relief="solid")
# detailbox.place(x=170, y=50)

t = tk.IntVar()
s = tk.IntVar()


choice2 = tk.Radiobutton(checkbox, text="mode2", value=2, variable=t,
                         activeforeground="red")
choice1 = tk.Radiobutton(checkbox, text="mode1", value=1, variable=t,
                         highlightcolor="red", highlightbackground="blue")
choice1.place(x=10, y=10)
choice2.place(x=10, y=45)

# show1 = tk.Label(detailbox, text="hey, you have choose 1",
#                  bg="gray", width=25, height=2)
# show2 = tk.Label(detailbox, text="hey, you have choose 2",
#                  bg="gray", width=25, height=2)


# def detail(*args):
#     """根据选项，实时显示"""
#     if t.get() == 1:
#         show2.place_forget()
#         show1.place(x=10, y=20)
#     elif t.get() == 2:
#         show1.place_forget()
#         show2.place(x=10, y=60)

Detail = tk.LabelFrame(window, width=200, height=200, text="Detail")
Detail.place(x=170, y=50)

detailbox1 = tk.Frame(Detail, width=180, height=160)
greet = tk.Label(detailbox1, text="Hey,")
hello = tk.Label(detailbox1, text="you have choose mode1.")
greet.place(x=20, y=20)
hello.place(x=20, y=40)

detailbox2 = tk.Frame(Detail, width=180, height=160)
Button1 = tk.Radiobutton(detailbox2, text="Yes", value=1, variable=s)
Button2 = tk.Radiobutton(detailbox2, text="No", value=2, variable=s)
Button1.place(x=40, y=30)
Button2.place(x=40, y=80)


def detail(*args):
    """根据选项，实时显示"""
    if t.get() == 1:
        detailbox2.place_forget()
        detailbox1.place(x=0, y=0)
    elif t.get() == 2:
        detailbox1.place_forget()
        detailbox2.place(x=0, y=0)


# 追踪变量的变化并实时响应
t.trace("w", detail)


window.mainloop()
