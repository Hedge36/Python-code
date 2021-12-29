#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Spyder
from Interface import Application
from tkinter import messagebox as msg


class MainWindow(Application):
    def __init__(self):
        super().__init__()
        self.loadspyder()
        self.Confirm["command"] = lambda: self.update(self.fetch)
        self.Save["command"] = self.save

    def loadspyder(self):
        """加载所有爬虫类"""
        self.zhihusearch = Spyder.ZhihuSearch("知乎热搜")
        self.zhihubank = Spyder.ZhihuBank("知乎热榜")
        self.weibosearch = Spyder.WeiboSearch("微博热搜")
        self.baidunews = Spyder.BaiduNews("百度新闻")

    def gettarget(self):
        """获取当前需要调用的爬虫"""
        website = self.website.get()
        # 获取对应爬虫
        webmap = {"ZhihuSearch": self.zhihusearch,
                  "ZhihuBank": self.zhihubank,
                  "WeiboSearch": self.weibosearch,
                  "BaiduNews": self.baidunews}
        target = webmap[website]
        return target

    def fetch(self):
        """获取当前界面参数及爬虫数据刷新数据表"""
        # 获取界面参数
        key = self.key.get()
        target = self.gettarget()
        target.setkey(key)
        target.fetch()

        if not target.data.size:
            msg.showwarning(title="异常", message="查询结果为空，请重新设置关键词！")
        else:
            self.setdata(target.data)
            self.updatedata()
        self.thread = False

    def save(self):
        """保存到本地Excel"""
        target = self.gettarget()   #
        if len(target.data) == 0:
            msg.showwarning(title="警告", message="请先获取数据！")
        else:
            filename = self.savefile()
            if filename:
                target.savedata(filename)
                msg.showinfo(title="提示", message="文件已保存！")
            else:
                print("放弃操作")


if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()
