# Python网络爬虫与图形用户界面

# 网络爬虫

## 什么是爬虫

> 网络爬虫（又称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。

## 爬虫的应用

> 抢票软件、
>
> 爬取图片视频音乐等、
>
> 各种搜索引擎、
>
> 全自动人机区分图灵测试

## 爬虫的安全隐患

> 君子协议（Robots协议）

## 爬虫分类

### 一、通用网络爬虫

> 通用网络爬虫又称全网爬虫（ScalableWebCrawler），爬行对象从一些种子URL扩充到整个Web，主要为门户站点搜索引擎和大型Web服务提供商采集数据。

### 二、聚焦网络爬虫

> 聚焦网络爬虫（FocusedCrawler），又称主题网络爬虫（TopicalCrawler），是指选择性地爬行那些与预先定义好的主题相关页面的网络爬虫。

### 三、增量式网络爬虫

> 增量式网络爬虫（IncrementalWebCrawler）是指对已下载网页采取增量式更新和只爬行新产生的或者已经发生变化网页的爬虫，它能够在一定程度上保证所爬行的页面是尽可能新的页面。

### 四、DeepWeb爬虫

> Web页面按存在方式可以分为表层网页（SurfaceWeb和深层网页（DeepWeb，也称InvisibleWebPages或HiddenWeb）。

## 反爬虫与反反爬虫

> 1. User-Argent屏蔽；
> 2. IP封禁；
> 3. cookies封禁；
> 4. 图灵测试；
> 5. 数据加密；
> 6. 动态加载；

## Python爬虫实践

> Document : https://docs.python-requests.org/en/master/

### 工具

> requests
>
> selenium
>
> bs4
>
> lxml

### 网址抓包解析

> 1. 直接抓包-彼岸壁纸
> 2. 动态上传-百度壁纸
> 3. blob加密-bilibili视频
> 4. headers及ip地址封装-百度壁纸
> 5. 截图类-冰点文库
> 6. API-天气查询
> 7. backend request-酷狗音乐
> 8. anti-encryption-腾讯视频（暂时不会）

### 网页文本解析

> bs4
>
> xpath
>
> selenium
>
> re
>
> json
>
> pyquery

![image-20210616104623929](E:/工具/Typora/Temp/image-20210616104623929.png)

### 代码实现

> 多线程，线程池

### Matlab

| [`webread`](https://www.mathworks.com/help/matlab/ref/webread.html) | Read content from RESTful web service         |
| ------------------------------------------------------------ | --------------------------------------------- |
| [`webwrite`](https://www.mathworks.com/help/matlab/ref/webwrite.html) | Write data to RESTful web service             |
| [`websave`](https://www.mathworks.com/help/matlab/ref/websave.html) | Save content from RESTful web service to file |
| [`weboptions`](https://www.mathworks.com/help/matlab/ref/weboptions.html) | Specify parameters for RESTful web service    |
| [`web`](https://www.mathworks.com/help/matlab/ref/web.html)  | Open web page or file in browser              |

