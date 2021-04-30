import tkinter as tk
import pyperclip
import os
from tkinter import scrolledtext as st

"""
程序相关说明：
英文复制暂不支持
如何根据序号自动换行
"""

window = tk.Tk()
window.title("快捷文本处理")
window.resizable(width=False, height=False)  # 窗口大小不可改变
window.geometry("400x300")


def run():
    """"""
    texts = text_display.get(0.1, "end")
    final = texts.replace("\n", '').replace(" ", '')
    pyperclip.copy(final)
    text_display.delete(0.1, tk.END)


def clear():
    """"""
    text_display.delete(0.1, tk.END)


description = tk.Label(text="copyright: SYSU-Hedge")
description.place(x=25, y=10)
description = tk.Label(text="pdf等汉字复制文本处理，自动去除空格换行，但划分不准，\n请自行调整。")
description.place(x=25, y=40)
tip = tk.Label(text="将文本复制到下框中，点击复制即可自动复制到剪切板")
tip.place(x=25, y=80)
text_display = st.ScrolledText(window, bg="white", width=42,
                               height=5, font="宋体 12")
text_display.place(x=25, y=120)
confirm = tk.Button(text="复制", command=run, width=10, height=1)
confirm.place(x=80, y=230)
confirm = tk.Button(text="清空", command=clear, width=10, height=1)
confirm.place(x=220, y=230)


window.mainloop()

'''更新预告：
1. 识别断行，自动分行
2. 识别英文，理性去空格！Hard

计划：
1. 通过正则匹配出所有的序号，在去掉‘\n’后的文本中再给它加上；
2. 英文处理暂时没有思路。
'''
