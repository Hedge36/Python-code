import tkinter as tk
window = tk.Tk()
window.title("my window")
# geometry() 窗口大小，长乘宽。
window.geometry("300x200")
# 字符串变量
var = tk.StringVar()
var.set("你想干嘛?")
# width与height都是倍数单位，单位为字符大小，文本变量
l = tk.Label(window, textvariable=var , bg="red", font=("Arial", 12),
             width=15,height = 2)
# pack自动放在一个合适的位置，place放在指定位置
l.pack()

on_hit = 0
def hit_me():
    global on_hit
    if on_hit == 1:
        on_hit = 0
        var.set("打我呀")
    else:
        on_hit = 1
        var.set("别打了别打了")


b = tk.Button(window, text="打他",width = 15, height = 2,
              command=hit_me)
b.pack()

window.mainloop()