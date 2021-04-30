#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/11 16:31
# @Author : Hedge
# @File : Tkinter10 Messagebox.py
# @Software: PyCharm

import tkinter as tk
import tkinter.messagebox
window = tk.Tk()
window.title("my window")
window.geometry("200x200")


def hit_me():
    # tk.messagebox.showinfo(title="Hi", message="hahahaha" )       # 消息框
    # tk.messagebox.showerror(title="Hi", message="No！Never！" )    # 错误框
    # tk.messagebox.showwarning(title="Hi", message="nononono" )    # 警告框
    # tk.messagebox.askquestion(title="Hi", message="what?")        # 对话框，返回yes,no
    # tk.messagebox.askyesno(title="Hi", message="what?")           # 对话框，返回布尔值
    tk.messagebox.askretrycancel(title="Hi", message="what?")       # 对话框，返回布尔值
    # tk.messagebox.askokcancel(title="Hi", message="what?")        # 对话框，返回布尔值
    #tk.messagebox.askyesnocancel(title="Hi", message="what?")      # 对话框，返回布尔值与None


tk.Label(window, text = "main frame").pack()
tk.Button(window, text="hit me", command=hit_me).pack()

window.mainloop( )