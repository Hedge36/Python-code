#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/9 22:31
# @Author : Hedge
# @File : Tkinter3 Listbox.py
# @Software: PyCharm
import tkinter as tk
window = tk.Tk()
window.title("my window")
window.geometry("300x200")


def print_selection():
    # 关于lb属性，可上网查询，此处为鼠标所选择的值
    value = lb.get(lb.curselection())
    var1.set(value)


var1 = tk.StringVar()
l = tk.Label(window, bg="yellow", width=4, textvariable=var1)
l.pack()
b = tk.Button(window, text="print selection",width = 18, height = 2,
              command= print_selection)
b.pack()


var2 = tk.StringVar()
var2.set((11,22,33,44))
# Listbox选项框
lb= tk.Listbox(window, listvariable = var2)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert("end", item)
# lb.insert(1,“first”)
# lb.delete(2, "second")
lb.pack()


t = tk.Text(window, height =3)
t.pack()
window.mainloop()