#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/11 10:33
# @Author : Hedge
# @File : Tkinter6 Checkbutton.py
# @Software: PyCharm
import tkinter as tk
window = tk.Tk()
window.title("my window")
window.geometry("200x200")


def print_selection():
    l.config(text="You have selected")



l = tk.Label(window, bg="yellow")
l.pack()
var1 = tk.IntVar()
var2 = tk.IntVar()
# from to起止，length长度/px，tickinterval标签间隔，solution精度，command有默认返回参数
c1 = tk.Checkbutton(window, text="Python",variable=var1, onvalue = 1, offvalue=0,
                    command = print_selection())
c2 = tk.Checkbutton(window, text="C",variable=var2, onvalue = 1, offvalue=0,
                    command = print_selection())
c1.pack()
c2.pack()

window.mainloop()