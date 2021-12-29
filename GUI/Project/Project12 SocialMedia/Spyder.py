#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import datetime
import pandas as pd
import requests
from lxml import etree
import os

# 第二次运行保存相同表名不能正确覆盖


class BasicSpyder:
    """Spyder basic class."""

    def __init__(self, name):
        self.name = name
        self._headers = {
            'user-agent': 'Mozilla/5.0 (X11 \
                             Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        }
        self._url = None
        self._key = None
        self.data = []

    def getdata(self) -> str:
        """Get Html source code."""
        response = requests.get(self._url, headers=self._headers)
        html = response
        return html

    def getcontent(self):
        """Get data in need from source code."""
        return data

    def savedata(self, filename='Data.xlsx') -> None:
        """Save Dataframe to excel at current path."""
        if self.data.size:
            if self.data.index[0] == 0:
                self.data.index += 1
            if self._key:
                self.data.index.name = f"key:{self._key}"

            if not os.path.exists(filename):
                self.data.to_excel(filename, sheet_name=(self.name + str(
                    datetime.datetime.now().strftime('%Y.%m.%d'))))
            else:
                with pd.ExcelWriter(filename, mode="a", engine="openpyxl",
                                    if_sheet_exists='replace') as writer:
                    self.data.to_excel(writer, sheet_name=(self.name + str(
                        datetime.datetime.now().strftime('%Y.%m.%d'))))
            return True
        else:
            print("Found no results.")
            return False

    def fetch(self):
        """Fetch data from website."""
        html = self.getdata()
        if html.status_code == 200:
            data = self.getcontent(html)
            print("成功获取数据!")
            self.data = data
            return True
        else:
            return False

    def setkey(self, key):
        """Set search key."""
        if isinstance(key, str):
            self._key = key

    def clrkey(self):
        """Clear key."""
        self._key = None


class BaiduNews(BasicSpyder):
    """Spyder towards BaiduNews(with a little messy)."""

    def __init__(self, name):
        super().__init__(name)
        self._url = 'http://news.baidu.com/'
        self._headers = {
            'user-agent': 'Mozilla/5.0 (X11 \
                             Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'Referer': 'https://www.zhihu.com/billboard'
        }

    def getcontent(self, html):
        """Get data in need, to specify only key to filter news."""
        tree = etree.HTML(html.text)
        ainfo = tree.xpath('//*[@id="body"]//li//a[@target="_blank"]')
        labels, links = [], []
        # 装饰器不太好处理
        for a in ainfo:
            label = "".join(a.xpath('.//text()'))
            if not self._key:
                labels.append(label)
                links.append(a.xpath('./@href')[0])
            elif self._key in label:
                labels.append(label)
                links.append(a.xpath('./@href')[0])
        df = pd.DataFrame({"词条": labels, "链接": links})
        return df


class ZhihuBank(BasicSpyder):
    """Spyder towards zhihu HotBank(50 records in total)."""

    def __init__(self, name):
        super().__init__(name)
        self._url = 'https://www.zhihu.com/billboard'
        self._headers = {
            'user-agent': 'Mozilla/5.0 (X11 \
                             Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'Referer': 'https://www.zhihu.com/billboard'
        }

    def getcontent(self, html):
        html = html.text
        content = re.findall(
            r'<div class="HotList-itemTitle">([\s\S]+?)</div>', html, re.M)  # 获取问题内容
        hot = re.findall(
            r'<div class="HotList-itemMetrics">([\s\S]+?)</div>', html, re.M)  # 获取问题热度
        abstract = re.findall(
            r'"excerptArea":{"text":"([\s\S]*?)"},"imageArea"', html, re.M)  # 获取问题摘要
        link = re.findall(
            r'"link":{"url":"([\s\S]+?)"}}?,"[at]', html, re.M)  # 获取问题超链接
        data = []
        for i in range(len(content)):
            label = content[i]
            if not self._key:
                line = []
                line.append(label)
                line.append(abstract[i])
                line.append(str(link[i]).replace('u002F', ''))
                line.append(hot[i])
                data.append(line)
            elif self._key in label:
                line = []
                line.append(label)
                line.append(abstract[i])
                line.append(str(link[i]).replace('u002F', ''))
                line.append(hot[i])
                data.append(line)
        df = pd.DataFrame(data, columns=['词条', '摘要', '链接', '热度'])
        return df


class ZhihuSearch(BasicSpyder):
    """Spyder towards zhihu HotBank(50 records in total)."""

    def __init__(self, name):
        super().__init__(name)
        # self._url = 'https://www.zhihu.com/topsearch'
        self._url = 'https://tenapi.cn/zhihuresou/'     # 采用API接口

    def getcontent(self, html):
        text = requests.get(self._url, headers=self._headers).json()
        # 为数据保存做准备
        data = []
        for e in text['list']:
            label = e['name']
            if not self._key:
                line = []
                line.append(label)
                line.append(e['query'])
                line.append(e['url'])
                data.append(line)
            elif self._key in label:
                line = []
                line.append(label)
                line.append(e['query'])
                line.append(e['url'])
                data.append(line)
        df = pd.DataFrame(data, columns=['词条', '摘要', '链接'])
        return df
    '''不采用API
    tree = etree.HTML(response.text)
    HotList = tree.xpath('//*[@id="root"]/div/main/div/div[2]/div')
    for e in HotList:
        print(e.xpath('.//text()'))
    '''


class WeiboSearch(BasicSpyder):
    """Spyder towards Weibo Topsearch."""

    def __init__(self, name):
        super().__init__(name)
        self._url = 'https://tophub.today/n/KqndgxeLl9'  # 微博热搜代替网址
        # self.api = 'https://tenapi.cn/resou/'   # 微博热搜API

    def getcontent(self, html):
        html = html.text
        path = '//*[@id="page"]/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr'
        # path = '//*[@id="page"]/div[2]/div[2]/div[2]/div[2]/div/div[1]/table/tbody/tr' # 近期历史
        tree = etree.HTML(html)
        HotList = tree.xpath(path)
        data = []
        for e in HotList:
            line = []
            label = e.xpath("./td[2]/a/text()")[0]
            if not self._key:
                line.append(label)
                line.append(
                    f'https://s.weibo.com/weibo?q=%23{label}%23&Refer=top')
                line.append(e.xpath("./td[3]/text()")[0])
                data.append(line)
            elif self._key in label:
                line.append(label)
                line.append(
                    f'https://s.weibo.com/weibo?q=%23{label}%23&Refer=top')
                line.append(e.xpath("./td[3]/text()")[0])
                data.append(line)
        df = pd.DataFrame(data, columns=['词条', '链接', '热度'])
        return df
