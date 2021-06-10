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
from PIL import Image

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
drive_url = r"msedgedriver.exe"
browser = webdriver.Edge(executable_path=drive_url, capabilities=EDGE)

url = "https://max.book118.com/html/2016/0808/50824696.shtm"
browser.get(url)
time.sleep(1)
for i in range(34):
    time.sleep(1)
    browser.find_element_by_xpath(
        '//*[@id="main"]/div[1]/div[3]/div[4]/div/div/ul[1]/li[3]/a').click()
r = browser.page_source
tree = etree.HTML(r)
picurl = tree.xpath('//*[@id="main"]/div[1]/div[3]/div[2]//img/@src')
picurl = [url for url in picurl if len(
    requests.get("https:" + url).content) > 1024]
counter = 0
size = len(picurl)
root = "./asd"
if not os.path.exists(root):
    os.mkdir(root)
for url in picurl:
    time.sleep(0.5)
    response = requests.get("https:" + url)
    counter += 1
    name = str(counter) + ".png"
    with open("%s/%s" % (root, name), "wb") as f:
        f.write(response.content)
    print("Saved %d / %d" % (counter, size))
print("Success!")
browser.quit()

im1 = Image.open("1.png")
im = [Image.open("%s.png" % i) for i in range(2, 36)]
im1.save("河流动力学概论(清华版)习题.pdf", "PDF", resolution=100.0,
         save_all=True, append_images=im)
print("All down into file 河流动力学概论(清华版)习题.pdf!")
