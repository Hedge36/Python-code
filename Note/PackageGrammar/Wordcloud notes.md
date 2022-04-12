wordcloud库基础语法

1.基本介绍：

wordcloud是优秀的词云展示第三方库词云以词语为基本单位，更加直观和艺术的展示	文本。   

2.函数说明

w.wordcloud.WordCloud(参数)   	设定词云对象并可进行配置对象参数

  w.generate(txt)          向WordCloud对象w中加载文本txt

  w.to_file(filename.)        将词云输出为图像文件，选定png或者jpg格式

备注:中文需要先使用jieba库分词组成空格分隔字符串

如:w.generate(" ".join(jieba.lcut(txt))) 

  WordCloud参数(无序)：

  width             	图片宽度，默认400像素

  height              图片高度，默认200像素

  min_font_size          	指定词云中字体的最小字号，默认4号

  max_font_size          	指定词云中字体的最大字号，根据高度自动调节

  font_step            	指定词云中字体字号的步进间隔，默认为1

font_path            	指定字体文件的路径，默认none。

 

如：w=wordcloud.WordCloud(font_path="C:/Users/Hedge/Documents/Fonts/msyh.ttf")

 

​	max_words             指定词云显示的最大单词数量           

​	stop_words            指定词云的排除词列表

​	mask               指定词云形状，默认为长方形，需引入imread()

​                   函数，如下：

​                   from scipy.misc import imread

​                   mk=imread("pic.png")

​                   w=wordcloud.WordCloud(mask=mk)

​                

​	background_color         指定词云背景颜色

注：若想要生成图片样式的词云图，找到的图片背景必须为白色，或者使用Photoshop

​	抠图替换成白色背景，否则生成的词云为矩形。