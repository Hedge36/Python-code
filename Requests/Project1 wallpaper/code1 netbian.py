#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/2/21 20:23
# @File : code1 netbian.py
# @Software: PyCharm
# @Comment : standard frame

import requests
from bs4 import BeautifulSoup
import os
import re

def getHtmlurl(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        # 有效的判断网络连接的状态。如果网连接出现错误，那么它就会用try-except来获取一个异常。
        r.encoding = r.apparent_encoding
        # 设置编码格式为 从内容中分析出的相应内容编码方式
        return r.text
    except:
        return "出现异常"

def getimgurl(img):
    href = img['href']
    url = "http://www.netbian.com" + href
    htm = getHtmlurl(url)
    soup = BeautifulSoup(htm, 'html.parser')
    # htm 表示被解析的html格式的内容
    # html.parser表示解析用的解析器
    return soup

def getpic(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_img = soup.find('div', class_='list').find('ul').find_all("a", attrs={'href': re.compile('^((?!http).)*$'),
                                                                              'target': '_blank'})
    # find返回第一个符合条件的bs对象，find_all返回所有符合条件的bs列表对象，不可重复筛选
    for img in all_img:
        title = img['title']
        if title.find(u"女") != -1:
            # u"str"表示字符串为万国码，返回-1即无
            # 你可以自定义规则来筛选你想要的壁纸
            print("不符合要求，跳过")
            continue

        soup1 = getimgurl(img)
        im1 = soup1.find('div', id='main').find('div', class_='endpage').find('p').find('img')

        img_url = im1['src']
        print(img_url)

        root = 'Fetched_File/images/'
        # 这是你要保存图片的位置
        t = title.split()
        # 将图片title按空格分开，取第一个空格前的字符作为图片名，这个你可以自己调整
        path = root + t[0] + '.jpg'

        try:
            if not os.path.exists(root):
                # 检查路径是否存在
                os.mkdir(root)
                # 若不存在，则创建文件夹
            if not os.path.exists(path):
                r = requests.get(img_url)
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print('文件保存成功')
            else:
                print('文件已存在')
        except Exception as e:
            print(str(e))
            print('爬取失败')

def getNextpage(html):
    soup = BeautifulSoup(html, 'html.parser')
    nextpage = soup.find('div', class_='list').find('ul').find('li', class_='nextpage').find('a')
    href = nextpage['href']
    url = "http://www.netbian.com" + href
    return url

def main():
    url = 'http://www.netbian.com/weimei/index.htm'
    for i in range(1, 10):
        html = getHtmlurl(url)
        print(str(i) + " : ")
        getpic(html)
        url = getNextpage(html)
"""
此处操作方法：下一页它是通过找到当前页面内的下一页标签进行跳转，也可以直接通过url操作，如：
http://pic.netbian.com/4kdongman/index_i.html表示第i页，其中4k唯美为固定可选标题
"""
if __name__ == '__main__':
    main()


