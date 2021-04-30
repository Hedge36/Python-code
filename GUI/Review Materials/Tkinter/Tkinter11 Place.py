#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/11 16:53
# @Author : Hedge
# @File : Tkinter11 Place.py
# @Software: PyCharm

import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("200x200")
# pack 与 grid 不能同时使用
# tk.Label(window, text=1).pack(side="top")
# tk.Label(window, text=1).grid(row=3, column=4, ipadx=10, ipady=10)
# place 放置在指定坐标位置，左上角为(0,0),同时可带参数anchor
tk.Label(window, text=1).place(x=10, y=100)

if __name__ == '__main__':
    window.mainloop()
