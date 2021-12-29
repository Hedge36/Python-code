#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox as msg
from ttkthemes import ThemedTk
import threading
import pandas as pd


class Application:
    """窗口主类"""

    def __init__(self):
        self.data = None    # UI界面数据，可以将这部分完全转移至Main
        self.thread = False     # 表示当前是否有线程在运行
        self.setroot()
        self.setui(self.root)

    # ——————————————————————————————————————————————————————————
    # 初始化函数
    def setroot(self):
        """创建主窗口"""
        self.root = ThemedTk(theme="arc", toplevel=True, themebg=True)
        self.root.update()
        x_max, y_max = self.root.maxsize()
        x, y = int(x_max/2-300), int(y_max/2-200)
        self.root.geometry("600x400+%s+%s" % (x, y))    # 居中显示
        self.root.title("Spyder")
        self.root.resizable(0, 0)  # 锁定长宽大小

        # 创建变量
        self.key = tk.StringVar()
        self.website = tk.StringVar()

    def setui(self, master):
        """创建窗口组件"""
        # ViewBox
        self.ViewBox = tk.LabelFrame(
            master, text="Result", width=420, height=360)
        self.ViewBox.place(x=20, y=20)
        self.view = ttk.Treeview(self.ViewBox, show='headings',
                                 column=('num', 'ct', 'zy', 'lj', 'rd'))
        self.view.place(x=0, y=0, width=400, relheight=1)

        # InfoBox
        self.InfoBox = tk.LabelFrame(
            master, text=u"Option", width=120, height=360)
        self.InfoBox.place(x=460, y=20)
        tk.Label(self.InfoBox, text="Website").place(x=10, y=20)
        self.Web = ttk.Combobox(self.InfoBox, textvariable=self.website,
                                values=[
                                    "WeiboSearch", "ZhihuSearch", "ZhihuBank", "BaiduNews"],
                                width=11, state="readonly")
        self.Web.current(0)
        self.Web.place(x=10, y=50)
        tk.Label(self.InfoBox, text="Key").place(x=10, y=90)
        self.Key = tk.Entry(self.InfoBox, highlightcolor="sky blue",
                            highlightthickness=1, textvariable=self.key,
                            width=13)
        self.Key.place(x=10, y=120)
        self.Confirm = tk.Button(self.InfoBox, text="Update",
                                 width=9, height=1)
        self.Confirm.place(x=20, y=160)
        self.Clear = tk.Button(
            self.InfoBox, text="Clear", width=9,
            command=self.clrview)
        self.Clear.place(x=20, y=200)
        self.Save = tk.Button(
            self.InfoBox, text="Save", width=9)
        self.Save.place(x=20, y=240)

        # TreeView
        self.view.heading(column="num", text="Num")
        self.view.heading(column="ct", text="Entry")
        self.view.heading(column="zy", text="Excerpt")
        self.view.heading(column="lj", text="Link")
        self.view.heading(column="rd", text="Hot")
        self.view.column("num", width=30, anchor=tk.W)
        self.view.column("ct", width=100, anchor=tk.W)
        self.view.column("zy", width=110, anchor=tk.W)
        self.view.column("lj", width=80, anchor=tk.W)
        self.view.column("rd", width=80, anchor=tk.W)

        # 信号槽（暂无必要）

    # ——————————————————————————————————————————————————————————
    # 功能函数

    def setdata(self, data):
        """设置当前数据表数据"""
        std_data = self.standardlize(data)
        self.data = std_data

    def clrdata(self):
        """清除数据"""
        self.data = None

    def standardlize(self, data):
        """将不同格式的数据统一格式"""
        table = pd.DataFrame(
            {"序号": [], "词条": [], "摘要": [], "链接": [], "热度": []})
        table = table.merge(data, how="outer")
        table['序号'] = data.index.values+1
        table.fillna("", inplace=True)
        table = table[["序号", "词条", "摘要", "链接", "热度"]]
        return table.values.tolist()

    def viewsort(col, reverse):
        """表格排序，暂未绑定"""
        l = [(self.view.set(k, col), k) for k in self.view.get_children('')]
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            self.view.move(k, '', index)

        # reverse sort next time
        self.view.heading(col, text=col, command=lambda _col=col:
                          treeview_sort_column(_col, not reverse))

    def savefile(self):
        """选择保存文件的路径"""
        filename = filedialog.asksaveasfilename(initialdir=".", initialfile="Data.xlsx",
                                                defaultextension="xlsx",
                                                filetypes=[("数据表", ".xls"), ("数据表", ".xlsx")])
        return filename

    def clrview(self):
        """清除数据表数据"""
        items = self.view.get_children()
        for item in items:
            self.view.delete(item)

    def update(self, func):
        """通过线程运行命令"""
        if not self.thread:
            self.thread = True
            t = threading.Thread(target=func)
            t.start()
        else:
            t = threading.Thread(target=lambda: msg.showinfo(
                title="Info", message="程序正在运行中，请稍后再试！"))

    def updatedata(self):
        """刷新数据表数据"""
        if self.data == None:
            msg.showwarning(title="Warning",
                            message="None Data!Please fetch first!")
        else:
            self.clrview()
            for d in self.data:
                self.view.insert('', tk.END, values=d)  # 添加数据到末尾
            self.thread = False

    def themechose(self, theme="arc"):
        """更换主题，包括'arc','adapta','aqua','breeze'"""
        self.root.configure(theme=theme)

    def mainloop(self):
        """窗口挂起"""
        self.root.mainloop()
