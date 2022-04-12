## BeautifulSoup简介

Beautiful Soup是python的一个库，最主要的功能是从网页抓取数据。官方解释如下：

> Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。
>
> Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。
>
> Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度。

BeautifulSoup支持Python标准库中的HTML解析器,还支持一些第三方的解析器，如果我们不安装它，则 Python 会使用 Python默认的解析器，lxml 解析器更加强大，速度更快，推荐使用lxml 解析器。

**我们先看一个完整实例，BeautifulSoup 解析58同城网，里面主要用到BeautifulSoup 的select()方法：**

```python
#encoding:UTF-8
from bs4 import BeautifulSoup
import requests
import time
import json


url = 'http://bj.58.com/pingbandiannao/24604629984324x.shtml'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
#获取每件商品的URL


def get_links_from(who_sells):
    urls = []
    list_view = 'http://bj.58.com/pbdn/pn{}/'.format(str(who_sells))
    print ('list_view:{}'.format(list_view) )
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #for link in soup.select('td.t > a.t'):
    for link in soup.select('td.t  a.t'):  #跟上面的方法等价
        print link
        urls.append(link.get('href').split('?')[0])
    return urls


#获取58同城每一类商品的url  比如平板电脑、手机等
def get_classify_url():
    url58 = 'http://bj.58.com'
    wb_data = requests.get(url58)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for link in soup.select('span.jumpBusiness a'):
        classify_href = link.get('href')
        print classify_href
        classify_url = url58 + classify_href
        print classify_url

        
#获取每件商品的具体信息
def get_item_info(who_sells=0):
    urls = get_links_from(who_sells)
    for url in urls:
        print url
        wb_data = requests.get(url)
        #print wb_data.text
        soup = BeautifulSoup(wb_data.text,'lxml')
        #print soup.select('infolist > div > table > tbody > tr.article-info > td.t > span.pricebiao > span')   ##infolist > div > table > tbody > tr.article-info > td.t > span.pricebiao > span
        print soup.select('span[class="price_now"]')[0].text
        print soup.select('div[class="palce_li"]')[0].text
        #print list(soup.select('.palce_li')[0].stripped_strings) if soup.find_all('div','palce_li') else None,  #body > div > div > div > div > div.info_massege.left > div.palce_li > span > i
        data = {
            'title':soup.title.text,
            'price': soup.select('span[class="price_now"]')[0].text,
            'area': soup.select('div[class="palce_li"]')[0].text if soup.find_all('div', 'palce_li') else None,
           	'date' :soup.select('.look_time')[0].text,
            'cate' :'个人' if who_sells == 0 else '商家',
        }
        print(data)
        result = json.dumps(data, encoding='UTF-8', ensure_ascii=False) #中文内容仍然无法正常显示。 使用json进行格式转换，然后打印输出。
        print result
        
# get_item_info(url)
# get_links_from(1)
get_item_info(2)
#get_classify_url()
```

 

## 1.  创建 BeautifulSoup 对象

首先导入库 bs4  lxml  requests

```python
#encoding:UTF-8
from bs4 import BeautifulSoup
import lxml
import requests
```

使用官方字符串来演示：

```python
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
```

创建 beautifulsoup 对象：

```python
soup = BeautifulSoup(html,'lxml')  #创建 beautifulsoup 对象
```

还可以用本地 HTML 文件来创建对象：

```python
soup1 = BeautifulSoup(open('index.html'))  #用本地 HTML 文件来创建对象
```

打印一下 soup 对象的内容，格式化输出：

```python
print soup.prettify()  #打印 soup 对象的内容，格式化输出
```

输出结果，格式化打印出了它的内容，这个函数经常用到。

## 2.  四种对象

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:

- Tag
- NavigableString
- BeautifulSoup
- Comment

**（1）Tag**

Tag就是 HTML 中的一个个标签，例如：

```python
<title>The Dormouse's story</title>
```

用 BeautifulSoup 可以很方便地获取 Tags：

```python
print soup.title
print soup.head
print soup.a
print soup.p
print type(soup.a)
```

这种方式查找的是在所有内容中的第一个符合要求的标签。

对于 Tag，它有两个重要的属性，name 和 attrs ：

```python
print soup.name
print soup.a.name
print soup.attrs
print soup.p.attrs #在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。
print soup.p['class'] #单独获取某个属性
print soup.p.get('class') ##单独获取某个属性 跟上面一样的
```

可以对这些属性和内容等等进行修改：

```python
soup.p['class']="newClass"
```

可以对这个属性进行删除：

```python
del soup.p['class']
```

**（2）NavigableString**

得到了标签的内容用 .string 即可获取标签内部的文字，例如：

```python
print soup.p.string
```

来检查一下它的类型：

```python
print type(soup.p.string)
#<class 'bs4.element.NavigableString'>
```

可以看到它的类型是一个 NavigableString，翻译过来叫 可以遍历的字符串。

**（3）BeautifulSoup**

BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称：

```python
print type(soup.name)
#<type 'unicode'>
print soup.name 
# [document]
print soup.attrs 
#{} 空字典
```

**（4）Comment**

Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号。我们找一个带注释的标签：

```python
print soup.a
print soup.a.string
print type(soup.a.string)
```

运行结果如下：

```
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
 Elsie 
<class 'bs4.element.Comment'>
```

a 标签里的内容实际上是注释，但是如果我们利用 .string 来输出它的内容，我们发现它已经把注释符号去掉了，所以这可能会给我们带来不必要的麻烦。

我们打印输出下它的类型，发现它是一个 Comment 类型，所以，我们在使用前最好做一下判断，判断代码如下：

```python
if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string
```

上面的代码中，我们判断了它的类型，是否为 Comment 类型。

## 3.  遍历文档树

**（1）直接子节点**

tag 的 .content 属性可以将tag的子节点以列表的方式输出：

```python
print soup.head.contents 
```

运行结果：

```
[<title>The Dormouse's story</title>]
```

输出方式为列表，我们可以用列表索引来获取它的某一个元素：

```python
print soup.head.contents[0]
```

**.children**

它返回的不是一个 list，不过我们可以通过遍历获取所有子节点。我们打印输出 .children 看一下，可以发现它是一个 list 生成器对象：

```python
print soup.head.children
```

运行结果：

```
<listiterator object at 0x7f71457f5710>
```

遍历一下获得里面的内容：

```python
for item in  soup.body.children:
    print item
```

**（2）所有子孙节点**

.contents 和 .children 属性仅包含tag的直接子节点，.descendants 属性可以对所有tag的子孙节点进行递归循环，和 children类似，要获取其中的内容，我们需要对其进行遍历：

```python
for item in soup.descendants:
    print item
```

查看运行结果，可以发现，所有的节点都被打印出来了：

```
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
```

**（3）节点内容**

如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容：

```python
print soup.head.string
```

运行结果：

```
The Dormouse's story
```

第二种情况：

```python
print soup.title.string
```

运行结果：

```
The Dormouse's story
```

如果tag包含了多个子节点,tag就无法确定，string 方法应该调用哪个子节点的内容, .string 的输出结果是 None：

```python
print soup.html.string
```

运行结果：

```
None
```

**（4）多个内容**

.strings 获取多个内容，不过需要遍历获取，比如下面的例子：

```python
for string in soup.strings:
    print(repr(string))
```

输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容：

```python
for string in soup.stripped_strings:
    print(repr(string))
```

**（5）父节点**

```python
p = soup.p
print p.parent.name
```

运行结果:

```
body
content = soup.head.title.string
print content.parent.name
```

运行结果：

```
title
```

**（6）全部父节点**

通过元素的 .parents 属性可以递归得到元素的所有父辈节点：

```python
content = soup.head.title.string
for parent in  content.parents:
    print parent.name
```

**（7）兄弟节点**

兄弟节点可以理解为和本节点处在统一级的节点，.next_sibling 属性获取了该节点的下一个兄弟节点，.previous_sibling 属性获取了该节点的上一个兄弟节点，如果节点不存在，则返回 None

注意：实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行。

```python
print soup.p.next_sibling
#       实际该处为空白
print soup.p.prev_sibling
#None   没有前一个兄弟节点，返回 None
print soup.p.next_sibling.next_sibling
```

**（8）全部兄弟节点**

通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出：

```python
for sibling in soup.a.next_siblings:
    print(repr(sibling))
```

**（9）前后节点**

与 .next_sibling  .previous_sibling 不同，它并不是针对于兄弟节点，而是在所有节点，不分层次

比如 head 节点为：

```html
<head><title>The Dormouse's story</title></head>
```

那么它的下一个节点便是 title，它是不分层次关系的。

```python
print soup.head.next_element
#<title>The Dormouse's story</title>
```

**（10）所有前后节点**

通过 .next_elements 和 .previous_elements 的迭代器就可以向前或向后访问文档的解析内容：

```python
for element in last_a_tag.next_elements:
    print(repr(element))
```

## 4.  搜索文档树

**（1）find_all( name , attrs , recursive , text , \**kwargs )**

find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件

- **name 参数**

   **A.传字符串**

name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉

最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的<b>标签：

```python
soup.find_all('b')
# [<b>The Dormouse's story</b>]
```

​    **B.传正则表达式**

如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.下面例子中找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到

```python
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# body
# b
```

​    **C.传列表**

如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有<a>标签和<b>标签：

```python
soup.find_all(["a", "b"])
# [<b>The Dormouse's story</b>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

​    **D.传 True**

True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点：

```python
for tag in soup.find_all(True):
    print(tag.name)
# html
# head
# title
# body
# p
# b
# p
# a
# a
```

​    **E.传方法**

如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数 ,如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False。下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True:

```python
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
```

将这个方法作为参数传入 find_all() 方法,将得到所有<p>标签：

```python
soup.find_all(has_class_but_no_id)
# [<p class="title"><b>The Dormouse's story</b></p>,
#  <p class="story">Once upon a time there were...</p>,
#  <p class="story">...</p>]
```

**2）keyword 参数**

如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性：

```python
2
soup.find_all(id='link2')
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```

如果传入 href 参数,Beautiful Soup会搜索每个tag的”href”属性：

```python
soup.find_all(href=re.compile("elsie"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
```

使用多个指定名字的参数可以同时过滤tag的多个属性：

```python
soup.find_all(href=re.compile("elsie"), id='link1')
# [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]
```

在这里我们想用 class 过滤，不过 class 是 python 的关键词，这怎么办？加个下划线就可以：

```python
soup.find_all("a", class_="sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性：

```python
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(data-foo="value")
# SyntaxError: keyword can't be an expression
```

可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag：

```python
data_soup.find_all(attrs={"data-foo": "value"})
# [<div data-foo="value">foo!</div>]
```

**3）text 参数**

通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True：

```python
soup.find_all(text="Elsie")
# [u'Elsie']
soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# [u'Elsie', u'Lacie', u'Tillie']
soup.find_all(text=re.compile("Dormouse"))
[u"The Dormouse's story", u"The Dormouse's story"]
```

**4）limit 参数**

find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.

文档树中有3个tag符合搜索条件,但结果只返回了2个,因为我们限制了返回数量：

```python
soup.find_all("a", limit=2)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```

**5）recursive 参数**

调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False：

```python
soup.html.find_all("title")
# [<title>The Dormouse's story</title>]
soup.html.find_all("title", recursive=False)
```

**（2）find( name , attrs , recursive , text , \**kwargs )**

它与 find_all() 方法唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果

**（3）find_parents()  find_parent()**

find_all() 和 find() 只搜索当前节点的所有子节点,孙子节点等. find_parents() 和 find_parent() 用来搜索当前节点的父辈节点,搜索方法与普通tag的搜索方法相同,搜索文档搜索文档包含的内容

**（4）find_next_siblings()  find_next_sibling()**

这2个方法通过 .next_siblings 属性对当 tag 的所有后面解析的兄弟 tag 节点进行迭代, find_next_siblings() 方法返回所有符合条件的后面的兄弟节点,find_next_sibling() 只返回符合条件的后面的第一个tag节点

**（5）find_previous_siblings()  find_previous_sibling()**

这2个方法通过 .previous_siblings 属性对当前 tag 的前面解析的兄弟 tag 节点进行迭代, find_previous_siblings()方法返回所有符合条件的前面的兄弟节点, find_previous_sibling() 方法返回第一个符合条件的前面的兄弟节点

**（6）find_all_next()  find_next()**

这2个方法通过 .next_elements 属性对当前 tag 的之后的 tag 和字符串进行迭代, find_all_next() 方法返回所有符合条件的节点, find_next() 方法返回第一个符合条件的节点

**（7）find_all_previous() 和 find_previous()**

这2个方法通过 .previous_elements 属性对当前节点前面的 tag 和字符串进行迭代, find_all_previous() 方法返回所有符合条件的节点, find_previous()方法返回第一个符合条件的节点

**注：以上（2）（3）（4）（5）（6）（7）方法参数用法与 find_all() 完全相同，原理均类似。**

## 5.  CSS选择器

我们在写 CSS 时，标签名不加任何修饰，类名前加点，id名前加 #，在这里我们也可以利用类似的方法来筛选元素，用到的方法是 **soup.select()，**返回类型是 **list**

**（1）通过标签名查找**

```python
print soup.select('title') 
#[<title>The Dormouse's story</title>]
print soup.select('a')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

**（2）通过类名查找**

```python
print soup.select('.sister')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

**（3）通过 id 名查找**

```python
print soup.select('#link1')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```

**（4）组合查找**

组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开：

```python
print soup.select('p #link1')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```

直接子标签查找：

```python
print soup.select("head > title")
#[<title>The Dormouse's story</title>]
```

**（5）属性查找**

查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到：

```python
print soup.select('a[class="sister"]')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print soup.select('a[href="http://example.com/elsie"]')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```

属性也可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格：

```python
print soup.select('p a[href="http://example.com/elsie"]')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```

以上的 select 方法返回的结果都是列表形式，可以遍历形式输出，然后用 get_text() 方法来获取它的内容：

```python
soup = BeautifulSoup(html, 'lxml')
print type(soup.select('title'))
print soup.select('title')[0].get_text()
for title in soup.select('title'):
    print title.get_text()
```