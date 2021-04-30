#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/9 23:26
# @Author : Hedge
# @File : Tkinter5 Scale.py.py
# @Software: PyCharm


import tkinter as tk
window = tk.Tk()
window.title("my window")
window.geometry("200x200")


def print_selection(v):
    l.config(text="You have selected " + v)



l = tk.Label(window, bg="yellow")
l.pack()
# from to起止，length长度/px，tickinterval标签间隔，solution精度，command有默认返回参数
tk.Scale(window, label="try me",from_=5,to_=11,orient=tk.HORIZONTAL,
           length=200,showvalue=0, tickinterval=3, resolution=0.01,
           command = print_selection).pack()


window.mainloop()
