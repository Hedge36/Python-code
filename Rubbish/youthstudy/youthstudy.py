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


def nameget():
    """获取已完成学习的名单"""
    EDGE = {
        "browserName": "MicrosoftEdge",
        # 无头浏览器设置
        "ms:edgeOptions": {
            'args': [
                '--headless',
                '--disable-gpu',
                '--remote-debugging-port=9222',
            ]},
        # 无头检测规避
        "experimental_option": {
            'excludeSwitches': 'enable-automation',
        }

    }
    username = "zdtm192b"
    password = "ce1902..."

    # 浏览器驱动路径
    drive_url = r"D:\Study\2019-2020\Python\code\Request\Review Materials\msedgedriver.exe"
    # browser = webdriver.Edge(executable_path=drive_url, capabilities=EDGE)
    browser = webdriver.Edge(executable_path=drive_url)
    url = "https://tuan.12355.net/bg/index.html"

    browser.get(url)
    browser.find_element_by_id("userName").send_keys(username)
    browser.find_element_by_id("password").send_keys(password)
    browser.find_element_by_id("login").click()
    time.sleep(2)
    browser.find_element_by_xpath(
        '//*[@id="nav"]/div[9]/div[1]/div[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="nav"]/div[9]/div[1]/div[1]').click()
    # 转到新窗口
    time.sleep(4)
    browser.switch_to_window(browser.window_handles[-1])
    # 点击数据查询
    browser.find_element_by_xpath(
        '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/a/li/span').click()
    time.sleep(8)
    # 点击进入青年大学习详情页
    browser.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div[4]/div[3]/table/tbody/tr/td[5]/div').click()
    # 导出具体数据
    time.sleep(8)
    browser.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div[3]/form/div[4]/div/button/span').click()
    # 等待下载
    time.sleep(20)
    # 任务完成
    browser.quit()


def namecheck():
    """名单校对，核查未学习名单"""
    namelist = ['胡卓', '黄辰昊', '黄海俊', '黄乐雯', '黄世豪', '黄帅', '黄伟明', '黄文基', '黄炫超',
                '黄智桓', '简理龙', '江钰鑫', '李佳豪', '李家霖', '李杰尧', '李文杰', '李小兰', '李兴凌',
                '李永翔', '李宇亨', '李子强', '梁耀浩', '梁梓聪', '廖雨畅', '林本民', '林枫']
    book = openpyxl.load_workbook(r"C:\Users\Hedge\Downloads\组织名单【青年大学习】.xlsx")
    sheet = book.active
    namefinish = [cell.value for cell in list(sheet.columns)[0]][2:]
    os.remove(r"C:\Users\Hedge\Downloads\组织名单【青年大学习】.xlsx")
    return list(set(namelist).difference(set(namefinish)))


def indicate(namelist):
    """"""
    window = tk.Tk()
    window.withdraw()
    window.title("捡漏")
    window.geometry("300x300")
    window.resizable(width=False, height=False)
    text_display = tk.Label(window, text="以下同学未完成青年大学习：")
    text_display.grid(row=0, pady=15)
    text_display = st.ScrolledText(window, bg="white", width=28,
                                   height=8, font="Arial 12")
    text_display.grid(row=1, columnspan=4, padx=20, pady=10)
    tk.Label(window, text="共计%d个" % len(namelist),
             font="Arial 10").grid(row=2, column=0, pady=8)

    def change(string):
        """向文本框输入数字"""
        text_display.insert("insert", string + '\n')

    for name in namelist:
        change(name)
    window.mainloop()


# nameget()
namelist = namecheck()
indicate(namelist)
