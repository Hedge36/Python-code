#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/11 12:21
# @Author : Hedge
# @File : Tkinter8 Menubar.py
# @Software: PyCharm
import tkinter as tk


def do_job():
    l.config(text = "do"+"?")
window = tk.Tk()
window.title("my window")
window.geometry("200x200")

l = tk.Label(window, text="", bg="yellow")
l.pack()
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=do_job)
# 分割线
filemenu.add_separator()
filemenu.add_command(label="Exit",command=window.quit)
# 同理设置子菜单栏

window.config(menu = menubar)
window.mainloop()