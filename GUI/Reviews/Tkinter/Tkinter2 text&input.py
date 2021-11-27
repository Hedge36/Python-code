#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/9 15:34
# @Author : Hedge
# @File : Tkinter2 text&input.py.py
# @Software: PyCharm
import tkinter as tk
window = tk.Tk()
window.title("my window")
# geometry() 窗口大小，长乘宽。
window.geometry("300x200")
# show是否隐藏输入值，若不为none ，则隐藏为值，如"*"
e = tk.Entry(window, show=None)
e.pack()

def insert_point():
    var = e.get()
    t.insert("insert", var)


def insert_end():
    var = e.get()
    t.insert("end", var)
    # 1行1列则为t.insert(1.1, var)


b1 = tk.Button(window, text="insert point",width = 18, height = 2,
              command= insert_point)
b1.pack()

b2 = tk.Button(window, text="insert end",width = 18, height = 2,
              command= insert_end)
b2.pack()

t = tk.Text(window, height =3)
t.pack()
window.mainloop()