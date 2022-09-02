"""
程序相关说明：
英文复制暂不支持
如何根据序号自动换行
"""

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
import pyperclip
import os
import time


window = tk.Tk()
window.title("快捷文本处理")
window.resizable(width=False, height=False)  # 窗口大小不可改变
window.geometry("400x280")


def copy():
    """复制当前文本框的内容至剪切板并清除文本框。"""
    texts = text_display.get(0.1, "end")
    final = texts.replace("\n", '').replace(" ", '').rstrip()
    pyperclip.copy(final)
    text_display.delete(0.1, tk.END)


def paste(continual=False):
    """删除原文本内容并粘贴剪切板中的内容。"""
    if not continual:
        text_display.delete(0.1, tk.END)
    text_display.insert(0.1, pyperclip.paste())


def clear():
    """清除文本框当前内容。"""
    text_display.delete(0.1, tk.END)


def process(text):
    """文本处理函数。"""
    result = text.get().replace("\n", '').replace(" ", '').rstrip()
    return result


def convert(*agrs):
    """"""
    if mode.get() == "Auto":
        autoprocess()


def autoprocess(interval=1000):
    """以固定的频率(1ps)监测剪切板自动相应粘贴修改。"""
    if text.get() != pyperclip.paste():
        print("检测到剪切板内容变化")
        text.set(pyperclip.paste())
        result = process(text)
        pyperclip.copy(result)
        paste()
    if mode.get() == "Auto":
        window.after(interval, autoprocess)
    # 该工作应该单独开一个线程完成


# 变量工作区
mode = tk.StringVar()   # 当前工作模式
text = tk.StringVar()   # 剪切板当前内容


# 界面工作区
description = tk.Label(text="copyright: SYSU-Hedge")
tk.Label(text="模式选择：").place(x=220, y=10)
modechose = ttk.Combobox(
    values=["Manual", "Auto", ], textvariable=mode, width=8)
modechose.current(0)
modechose.place(x=290, y=10)
description.place(x=25, y=10)
description = tk.Label(text="pdf等汉字复制文本处理，自动去除空格换行，但划分不准，请自行\n调整。")
description.place(x=25, y=40)
tip = tk.Label(text="将文本复制到下框中，点击复制即可自动复制到剪切板")
tip.place(x=25, y=80)
text_display = st.ScrolledText(window, bg="white", width=42,
                               height=5, font="宋体 12")
text_display.place(x=25, y=120)
confirm = tk.Button(text="复制", command=copy, width=10, height=1)
confirm.place(x=40, y=230)
confirm = tk.Button(text="粘贴", command=paste, width=10, height=1)
confirm.place(x=150, y=230)
confirm = tk.Button(text="清空", command=clear, width=10, height=1)
confirm.place(x=260, y=230)

# 变量监测区
mode.trace("w", convert)    # 模式更换响应

# 窗口操作区
window.mainloop()
'''
作者：Hedge
版本号：V1.1
更新时间：2020.07.04
更新说明：
    完善了剪切板监听功能，当前监听功能已经正常工作并上线。
更新预告：
1. 识别断行，自动分行
2. 识别英文，理性去空格！Hard

计划：
1. 通过正则匹配出所有的序号，在去掉‘\n’后的文本中再给它加上；
2. 英文处理暂时没有思路;
3. 监听剪切板界面的重新定制；
'''
