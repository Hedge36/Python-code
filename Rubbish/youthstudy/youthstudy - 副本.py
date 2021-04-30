#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/5 23:16
# @Author : Hedge
# @File : selenium-Edge.py.py
# @Software: PyCharm
from selenium import webdriver
import time
import os
import openpyxl
import tkinter as tk
from tkinter import scrolledtext as st


def namecheck():
    """名单校对，核查未学习名单"""
    namelist = ['胡卓', '黄辰昊', '黄海俊', '黄乐雯', '黄世豪', '黄帅', '黄伟明', '黄文基', '黄炫超',
                '黄智桓', '简理龙', '江钰鑫', '李佳豪', '李家霖', '李杰尧', '李文杰', '李小兰', '李兴凌',
                '李永翔', '李宇亨', '李子强', '梁耀浩', '梁梓聪', '廖雨畅', '林本民', '林枫']
    book = openpyxl.load_workbook(r"C:\Users\Hedge\Downloads\组织名单【青年大学习】.xlsx")
    sheet = book.active
    namefinish = [cell.value for cell in list(sheet.columns)[0]][2:]
    return list(set(namelist).difference(set(namefinish)))


def indicate(namelist):
    """"""
    window = tk.Tk()
    window.title("捡漏")
    window.geometry("300x300")
    window.resizable(width=False, height=False)
    text_display = tk.Label(window, text="以下同学未完成青年大学习：")
    text_display.grid(row=0, pady=10)
    text_display = st.ScrolledText(window, bg="white", width=28,
                                   height=8, font="Arial 12")
    text_display.grid(row=1, columnspan=4, padx=20, pady=10)
    tk.Label(window, text="共计%d个" % len(namelist),
             font="Arial 12").grid(row=2, pady=10)

    def change(string):
        """向文本框输入数字"""
        text_display.insert("insert", string + '\n')

    for name in namelist:
        change(name)
    window.mainloop()


namelist = namecheck()
indicate(namelist)
