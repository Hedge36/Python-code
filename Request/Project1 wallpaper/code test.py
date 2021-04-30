#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/2/23 15:08
# @Author : Hedge
# @File : code3-origrinal.py
# @Software: PyCharm
import requests
import requests.sessions
from bs4 import BeautifulSoup
import time
import re
import webbrowser


session = requests.Session()
imgs = []
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) / "
                         "Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.1071 SLBChan/8",
           }




def gethtmlurl(url):
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except:
        return "发生未知错误"

url = "https://pcw-data.video.iqiyi.com/videos/vts/20200220/a6/fd/e808634c8990adbdcf49165e5726205f.ts?start=0&end=561932&contentlength=561932&sd=0&qdv=1&qd_uid=0&qd_tvid=321234500&qd_vip=0&qd_src=01010031010000000000&qd_tm=1614760364406&qd_ip=0&qd_p=0&qd_k=a86a4cde22b2a1e2c4d61757bc167272&ve=&sgti=14_30e2496f3fdd7d8fc47a77de65e3bf13_1614760363075&dfp=&qd_sc=f5aa34953de04d674e555727e932746a&pv=0.1&cross-domain=1&mss=1&stauto=1"
html = gethtmlurl(url).text
soup = BeautifulSoup(html, "lxml")
urllist = soup.find("div", id="artworks-list").find_all("img")
count = 0
for imgurl in urllist:
    count += 1
    time.sleep(0.5)
    link = imgurl["src"]
    image_name = str(count)+".jpg"
    with open("test/"+image_name, 'wb') as f:
        f.write(gethtmlurl(link).content)
        print(image_name, "Saved")

