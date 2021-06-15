#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/5 23:16
# @Author : Hedge
# @File : selenium-Edge.py.py
# @Software: PyCharm
from selenium import webdriver
from lxml import etree
import requests
import time
import os

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
# 浏览器驱动路径
drive_url = r".\edgedriver_win64\msedgedriver.exe"
browser = webdriver.Edge(executable_path=drive_url)
# browser = webdriver.Edge(executable_path=drive_url, capabilities=EDGE)
url = "https://max.book118.com/html/2016/0808/50824696.shtm"
buttonxpath = '//*[@id="btn_preview_remain"]'


def download(word, page):
    """下载图片 ，word为关键字，page为面数，大致为每面20个图片"""
    browser.get(
        "https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%s&fr=ala&ala=1"
        "&alatpl=adress&pos=0&hs=2&xthttps=000000" % word)
    for i in range(page):
        # 滚动至页面底部
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
    html = browser.page_source
    tree = etree.HTML(html)
    lists = tree.xpath("//*[@id='imgid']/div/ul/li/div/a/img/@data-imgurl")
    counter = 0
    size = len(lists)
    root = "./%s" % word
    if not os.path.exists(root):
        os.mkdir(root)
    for url in lists:
        time.sleep(0.2)
        counter += 1
        response = requests.get(url)
        name = str(counter) + ".jpg"
        with open("%s/%s" % (root, name), "wb") as f:
            f.write(response.content)
        print("Saved(%d/%d):" % (counter, size))
    print("All pictuers have been downloaded!")
    browser.quit()


if __name__ == "__main__":
    download("插画", 3)
