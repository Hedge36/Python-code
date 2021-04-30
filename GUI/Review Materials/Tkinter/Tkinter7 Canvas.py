#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/11 10:40
# @Author : Hedge
# @File : Tkinter7 Canvas.py
# @Software: PyCharm
import tkinter as tk
window = tk.Tk()
window.title("my window")
window.geometry("200x200")


def move():
    canvas.move(oval, 0,2)


# 只支持gif
canvas = tk.Canvas(window, bg="blue", height = 100, width = 200)
image_file = tk.PhotoImage(file="1.gif")
# 锚点，图片对齐格式点
image = canvas.create_image(0,0,anchor="NW", image=image_file)
line = canvas.create_line(50,50,80,80)
oval = canvas.create_oval(50,50,80,80,fill="red")

canvas.pack()
b = tk.Button(window, text = "Move", command = move).pack()

window.mainloop()