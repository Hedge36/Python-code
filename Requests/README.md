# According requests

##  Phase I 

### Phase Arrangement

> **State : Completed**
>
> Start at 2021.2.16, end in 2021.3.6, about **20 days** in total. 



### Main description

> Learning how to basic **Crawler** information, main including severals method including <u>**xpath, bs4, re**</u> with **<u>automate tool selenium</u>** to grab and its safety measurement, and some method to improve speed including **<u>pool</u>** and know **<u>asynch</u>**. Additionally, learn some information of **composition of page elements and how the web operation**. At last, learn to program some orginal projects like wallpaper grabbing, simple music grabbing and so on, maybe I can grap a large amount of information and **combine with data visualization** to take on, there are still some ideas to be implemented in one day like shangxueba and paokka's cracking. That's all.
>
> <p align="right">Hedge</p>
>
> <p align="right">2021.3.6</p>



### Main contents

> 1. **爬虫风险与Robots协议(url/robots.txt)**
> 2. 爬虫与反爬虫
> 3. **Requests请求与header属性封装，动态IP加载与Cookie**
> 4. **网页解析——检查功能的使用**
> 5. **网页解析——文本解析的三种方法**
> 6. 自动化测试与反屏蔽
> 7. Pool多线程
> 8. 异步携程





### Total stduy progress

> > - [x] 百度搜图破解
> >
> >
> > 1. 获取网页全部信息
> > 2. 截取筛选
> > 3. 下载
> >
> > All in:
> >
> > 1. 数据分析**解析json**，获取url路径，操作较麻烦，但抓取效率高
> > 2. 利用selenium自动化测试获取动态数据，易操作，但抓取效率较低
> > 3. tip: 访问需加上<u>完整的</u>**headers**属性
>
> > - [x] 上学吧破解
> >
> > 涉及网站**cookie**参数附加，能够便利查询，但做不到破解，破解需要循着加密机理等等，无法做到，暂时搁置。
>
> > - [x] 音乐视频下载方法
> >
> > 音乐：详情见酷狗音乐爬虫，涉及多种网页数据解析方法；
> >
> > **php**带参数**解析**以及hash获取，但是vip封装音乐仍然无法获取；
> >
> > 视频：同，采用线程池抓取，多为动态上传且采取blob加密，需对网页json文件进行解析。
>
> > - [x] Xpath方法
> >
> > 即为tree方法，根据目录标签关系进行追踪定位。
>
> > - [x] 线程池
> >
> > 多线程的另外开发Pool类，能够限制线程的创建与销毁，提高处理阻塞进程的效率，同时也能防止过多占用内存。
>
> > - [x] 异步携程方法(粗略了解即可)
> >
> > 类似于多线程，task与future对象加入一个事件循环，反复执行，感觉没啥用处。
>
> > - [x] selenium方法
> >
> > 浏览器的自动化测试，懒得下载谷歌，现使用edge浏览器作为驱动，可解决模拟人为浏览器操作，获取动态加载数据，自带标签定位功能，可不使用上述解析定位方法，同时可以无界面化(无头浏览器)及规避无头检测，用于爬取动态数据及登陆十分便捷。



### Orginal Project

> 1. netbian.py——彼岸壁纸爬虫
> 2. selenium-Edge.py——自动化edge百度图片爬虫

------



##  Phase Ⅱ

### Phase Arrangement

> **State : Wait**
>
> ？
>
> **Target:** 
>
> 1. Scrapy
>
> 2. JS逆向
>
> 3. 巩固爬虫应用，尤其是有关主流媒体的数据抓包破解
>
> 4. 百度文库
>
> **Suggestion：**
>
> 在图书馆淘点书回来辅助学习

