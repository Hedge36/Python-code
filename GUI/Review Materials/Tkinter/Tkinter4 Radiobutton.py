#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/9 22:31
# @Author : Hedge
# @File : Tkinter3 Listbox.py
# @Software: PyCharm
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("200x200")


def print_selection():
    l.config(text="You have selected " + var.get())


var = tk.StringVar()
l = tk.Label(window, bg="yellow", width=18, text="empty")
l.pack()

r1 = tk.Radiobutton(window, text="Option A", variable=var,
                    value="A", command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text="Option B", variable=var,
                    value="B", command=print_selection)
r2.pack()

window.mainloop()
