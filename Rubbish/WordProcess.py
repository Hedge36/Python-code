import tkinter as tk
import pyperclip
import os
from tkinter import scrolledtext as st
from tkinter import ttk
"""
自动挂起暂时不可用
"""

window = tk.Tk()
window.title("快捷文本处理")
window.resizable(width=False, height=False)  # 窗口大小不可改变
window.geometry("400x280")


def run():
    """"""
    texts = text_display.get(0.1, "end")
    final = texts.replace("\r", "").replace(
        "\n", "").replace(" ", "").rstrip()
    pyperclip.copy(final)
    text_display.delete(0.1, tk.END)


def paste():
    """向文本框中粘贴剪切板中的内容"""
    text_display.delete(0.1, tk.END)
    text_display.insert(0.1, pyperclip.paste())


def clear():
    """"""
    text_display.delete(0.1, tk.END)


def autopro():
    """"""
    # 如何实现自动挂起？
    # while modechose.get() == "Auto":
    #     print("Test")
    if text != pyperclip.paste():
        print("1")
        texts = pyperclip.paste()
        final = texts.replace("\r", "").replace(
            "\n", "").replace(" ", "").rstrip()
        pyperclip.copy(final)


description = tk.Label(text="copyright: SYSU-Hedge")
tk.Label(text="模式选择：").place(x=230, y=10)
modechose = ttk.Combobox(values=["Manual", "Auto", ], width=8)
modechose.current(0)
modechose.place(x=300, y=10)
description.place(x=25, y=10)
description = tk.Label(text="用于pdf等汉字复制文本处理，自动去除空格换行，"
                       "但划分不准，请自行调整，进一步功能，敬请期待。", wraplength=350)
description.place(x=25, y=40)
tip = tk.Label(text="将文本复制到下框中，点击复制即可自动复制到剪切板")
tip.place(x=25, y=80)
text_display = st.ScrolledText(window, bg="white", width=42,
                               height=5, font="宋体 12")
text_display.place(x=25, y=120)
confirm = tk.Button(text="复制", command=run, width=10, height=1)
confirm.place(x=40, y=230)
confirm = tk.Button(text="粘贴", command=paste, width=10, height=1)
confirm.place(x=150, y=230)
confirm = tk.Button(text="清空", command=clear, width=10, height=1)
confirm.place(x=260, y=230)
text = ""


window.mainloop()
'''更新预告：
1. 识别断行，自动分行
2. 识别英文，理性去空格！Hard
3. 上线文献模式，删改形如文献引用部分
4. 自动模式上线后，下架手动模式

计划：
1. 通过正则匹配出所有的序号，在去掉‘\n’后的文本中再给它加上；
2. 英文处理暂时没有思路;
3. 升级为监听剪切板，后台全自动处理；借助after函数
'''
