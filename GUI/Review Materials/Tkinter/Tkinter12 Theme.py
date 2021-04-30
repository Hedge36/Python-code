from tkinter import *
from tkinter.ttk import *
root = Tk()
root.title("style属性")
root.geometry("300x200")
style01 = Style()
style01.configure("TLabel", font=("华文黑体", 18),
                  background="green", foreground="blue")
# 把Label01控件绑定给style01对象
Label01 = Label(root, text="用户名", style="TLabel")
Label01.pack(padx=10, pady=10)
Label02 = Label(root, text="密码")
Label02.pack(padx=10, pady=10)
# 展示窗体
root.mainloop()
