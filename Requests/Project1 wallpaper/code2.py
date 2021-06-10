#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/2/23 15:04
# @Author : Hedge
# @File : code2.py
# @Software: PyCharm
import  requests
from lxml import etree
import os

class Bizi(object):
    def __init__(self):
        #如果爬到一半就停止了，想从某页开始爬取就改一些下index_后面的数字改为你想爬的页码就可以了
        self.url = 'http://www.netbian.com/dongman/index_2.htm'
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    # 获取网页数据
    def Get_data(self,url):
        # print(url)
        req = requests.get(url=url, headers=self.headers)
        return req.content.decode('GBK')
    #获取图片名字、图片页面链接、文件夹页码、下一页链接
    def Link_name(self,data):
        html = etree.HTML(data)
        # 从网上获取一个etree对象
        list_name = html.xpath('//*[@id="main"]/div[2]/ul/li/a/b/text()')
        # tag[@arrtname =vaule]/[index]/@attr（index从1开始计数，表示第几个）
        # 文本属性内有多个属性标签(如加粗)时，每个属性标签对应一个“/”再接text()获取文本
        list_link = html.xpath('//*[@id="main"]/div[2]/ul/li/a/@href')
        wname = html.xpath('//*[@id="main"]/div[3]/b/text()')
        net_url1 = html.xpath('//*[@id="main"]/div[3]/a[10]/@href')
        return list_name,list_link,wname,net_url1
    #拿取图片的链接
    def Tu_link(self,t_link):
        req2 = requests.get(url=t_link)
        html2 = etree.HTML(req2.text)
        jpg_link = html2.xpath('//*[@id="main"]/div[2]/div/p/a/img/@src')
        return  jpg_link
    #获取图片
    def Tu_data(self,tu_bin):
        req3 = requests.get(url=tu_bin)
        return req3.content
    def run(self):
        net_url = self.url
        ab = '2'
        while True:
            try:
                index_data = self.Get_data(net_url)
                name,link,fname,net_url = self.Link_name(index_data)
                # print(net_url)
                net_url = 'http://www.netbian.com' + str(net_url[0])
                print(f"正在爬取第{ab}页")
                ab = int(fname[0]) + 1
                # print(name,link)
                #字典化
                dis = dict(zip(name,link))
                #循环拿到key，然后就是可以利用key拿到value
                for i in dis:
                    lb_link = self.Tu_link('http://www.netbian.com'+str(dis[i]))
                #     # print(str(lb_link[0]))
                    tu_bindata = self.Tu_data(str(lb_link[0]))
                    try:
                        os.mkdir('第'+str(fname[0])+'页')
                        f = open('./第' + str(fname[0]) + '页/' + str(i) + '.jpg', 'wb')
                        f.write(tu_bindata)
                        f.close()
                    except  Exception as e:
                        # print(e)
                        f = open('./第'+str(fname[0])+'页/'+str(i)+'.jpg', 'wb')
                        f.write(tu_bindata)
                        f.close()
            except Exception as l:
                # print(l)
                print('这页没了哦')
                # break
if __name__ == '__main__':
        bz = Bizi()
        bz.run()