#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/11 12:37
# @Author : Hedge
# @File : Tkinter9 Frame.py
# @Software: PyCharm
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("200x200")
tk.Label(window, text = "main frame").pack()
frm = tk.Frame(window)
frm.pack()
frm_left =tk.Frame(frm)
frm_right =tk.Frame(frm)
frm_left.pack(side="left")
frm_right.pack(side="right")

tk.Label(frm_left, text ="left 1").pack()
tk.Label(frm_left, text ="left 2").pack()
tk.Label(frm_right, text ="right 1").pack()

window.mainloop()