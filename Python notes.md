# **Python基础语法**

# 目录



[TOC]

 

# 板块一 数据类型及操作

## 1. 简述

> 数据类型包括数值，字符串，字典，集合，序列，布尔值六种类型，包括各自不同的操作方法，是python的基础。（maybe包括函数对象）

## 2. 数值

### 2.1 整型

> **a.进制：**
> 	
>
> 二进制：以0b或者0B开头，如：0b010
> 	
>
> 八进制：以0o或者0O开头, 如：0o456
> 	
>
> 十六进制：以0x或者0X开头, 如：-0x9a
>
> **b.相关函数：**
> 	
>
> power(x,y)，用于计算X的y次方
> 	
>**c.关于等于的判断符号：**
> 
>如输入0.1+0.2==0.3，输出False。

附：Python3中整数可任意大，且[-5, 256] 为小整数池，其间整数对象全局共享且唯一。

#### 关于进制转换

> 在python中10进制转2进制；10进制转8进制；10进制转16进制分别用内置函数`bin();` `oct();` `hex()`实现，也可以通过 int(object, base) 实现，其中base为转化后的目标进制，并且转化出来的其他进制，均为字符串类型。

### 2.2 浮点型

浮点数之间的运算存在不确定尾数，一般发生在10的-16次方左右，常见的有0.1+0.2==0.3000000004,

计算机中用的二进制并不完全等同十进制。

### 2.3 科学计数法的使用

使用e或者E作为幂的符号，以10为基数，格式如下：

\<a>e\<b>表示a10的b次方（b如果为负数不可以加括号）。

### 2.4 复数数据

> a.python中的复数与数学中的复数保持一致
>
> b.通过指令“变量.real”获得变量的实部，“变量.imag”获得其虚部。

### 2.5 数字操作

操作符：

> //       			    整数除，取商的整数部;
>
> x%y          	     余数，模运算 如：10%3==1;
>
> x**y          		 幂运算，x的y次方;
>
> <<,>>			    移位(按二进制移动位数)
>
> |, ^, &				  按位或，非，与
>
> ~					  	按位翻转

辅助二元操作符：x op =y, 其中op为二元操作符，其中不能加空格，如 x\*=3 与 x=x*3 等价。

### 2.6 运算符计算优先顺序

位运算和算术运算>>比较运算>>赋值运算>>逻辑运算

>```python
>type(3.1//3)
>```

<class 'float'>

注：数据计算过程中默认输出最宽范围的数据，其中整数<浮点数<复数。

操作函数：

> abs(x)         			   取x的绝对值;
>
> divmod(x,y)       		 商余，输出元组类型（x//y,x%y);
>
> power(x,y[，z])     	 [,z]表示参数可省略，表示幂余;
>
> max(x,y,..)       			取参数中的最大值;
>
> min(x,y,..)       			 取参数中的最小值；
>
> int(x, base=10)     	  将x变成base进制整数并舍弃其小数部分;
>
> float(x)        			   将x变成浮点数，增加小数部分;
>
> complex(x)       		  将x变成复数，增加虚数部分;
>
> hex(x)	    				 将数字x转换为十六进制
>
> round(x,d)				   对x四舍五入，d是小数截取位数，默认为0，取整。

## 3. 字符串

字符串的本质是字符序列，不同于列表，字符串**定义之后不能再对原字符串进行改变**。

### 3.1 字符串的创建

  使用 "" 或者 '' 创建字符串，也可以使用连续三个”或者’创建多行字符串注释。

### 3.2 转义符

  表达特定的字符的本意，形成一些组合，表达一些不可打印的含意，在python控制台中是不显示换行的效果的。如：

> "\b回退"(光标向前回退一个位置)
>
> "\n"换行(光标移动到下一行首)
>
> "\r"回车(光标回到本行首)
>
> "\t”横向制表符

除此之外，”\”还用做行连接符又称续行符，虽然python单行长度无限制，但是为了美观往往需要换行，此外，换行后无限定格式，无需上下对齐。

### 3.3 操作符

>   x + y      	     连接两个字符串，生成一个新字符串，多次加和内存占用多;
>
>   nx或者xn   		复制n次字符串x;
>
>   x in s     		   如果x是s的子串，则返回True,否则返回False;

### 3.4 字符串处理函数

>   len(x):     	      返回字符串x的长度
>
>   str(x)：    	 	 使任何类型x增加一对引号使其转化为字符串类型
>
>   chr(x)：    	     输出十进制数字x对应Unicode值的对应字符
>
>   ord(x):    		    输出字符x对应的Unicode值

### 3.5 字符串处理方法

方法特指\<a>.\<b>()风格中的函数\<b>()

> str.lower()    	     返回字符串的副本并全部小写   
>
> str.upper()			 返回字符串的副本并全部大写，如：sadef.upper(),输出 SADEF；
>
> str.capitalize()		产生新字符串并将首字母大写
>
> str.title()				 产生新字符串并将所有单词首字母大写
>
> str.swapcase()		产生新字符串并将所有大小写转换
>
> ==str.split(sep=)  	  **返回**一个列表，由str根据sep被分割的部分组成,如：'啊,哦,呃'.split(',')，输出['啊','哦','呃']；==
>
> str.count(sub)  	  返回字符串sub在str中出现的次数；
>
> ==str.replace(old,new)==
>
> ​           	==**返回**字符串str的副本，副本中所有的old字符串被替换成new字符串；==
>
> str.center(width[,fillar])
>
> ​           	字符串str根据宽度width居中，fillchar填充字符可选且默认为空白；
>
> str.ljust(width[,fillar])
>
> ​           	字符串str根据宽度width向左对齐，fillchar填充字符可选且默认为空白；
>
> str.rjust(width[,fillar])
>
> ​           	字符串str根据宽度width向右对齐，fillchar填充字符可选且默认为空白；
>
> ==str.strip(chars)==
>
> ​           	==**返回**一个从str中去掉在其左右两侧的char中列出的字符后的字符串；==
>
> str.Istrip(chars)
>
> ​           	**返回**一个从str中去掉在其左侧的char中列出的字符的字符串；
>
> str.rstrip(chars)
>
> ​           	**返回**一个从str中去掉在其右侧的char中列出的字符的字符串；
>
>  
>
> ==**str.join(iter)**==
>
> ​           	==**在iter(字符串)变量除最后一个元素外每个元素后都加一个str,主要用于字符串的分隔等；**==
>
> ==str[m:n:k]				表示从m索引到n-1，以k为步长(亦即间距)(不输入默认为1)的字符串进行切片（输出为字符串，而非整数，浮点数）[::-1]:表示字符串倒过来切片得结果;==
>
> 注意，不同于range(m,n),range(m,n)表示m为开头，n为结尾(不包括n)生成数字序列；
>
> str.startswith(s)   	判断字符串str是否以指定字符串s开头
>
> str.endswith(s)   	 判断字符串str是否以指定字符串s结尾
>
> str.find(s)   			字符串str第一次出现字符串s的位置，如果找不到返回-1
>
> str.rfind(s)   		 字符串str最后一次出现字符串s的位置
>
> str.isalnum()      	判断字符串str中所有字符是否都为字母或者数字
>
> str.isalpha()      	判断字符串str中所有字符是否都为字母(包括汉字)
>
> str.isdigit()      	 判断字符串str中所有字符是否都为整数
>
> str.isspace()      	判断字符串str是否为空字符串
>
> str.isupper()     	判断字符串str中所有字符是否都为大写字母
>
> str.islower()      	判断字符串str中所有字符是否都为小写字母

 

### 3.6 槽格式化

> a.{}.format()  		槽
>
> 只在字符串中有用，表示占位信息符，将format()中的参数按顺序填入槽中，也可以在槽中填数字自定义顺序;

>   b.槽内部对格式化的配置格式：
>
>   <参数序号>:<控制符>（注意，计算机中顺序是以0开始的！）
>
>   :          			引导符号，后接填充内容与控制符，以下是顺序；
>
>   <填充>       	用于填充的单个字符；
>
>   <对齐>       	<左对齐，>右对齐，^居中对齐，默认左对齐；
>
>   <宽度>       	槽设定的输出宽度；
>
>   <,>         		数字的千位分隔符；
>
>   <.精度>       	浮点数小数精度Nf;
>
>   <精度>			字符串最大输出长度Nd(仅限整数)；
>
>   <类型>       	输出形式：b二进制形式，c Unicode值，d十进制形式，e，                      									E科学计数法e表示；

### 3.7 字符串驻留机制

  仅保存一份相同且不可变字符串的方法，不同的值被存放在字符串驻留池中。

  对于符合标识符规则的字符串(仅包括下划线，字母和数字)会启用字符串驻留机制。

 

## 4. 字典

### 4.1 映射

键(索引)和值(数据)的一种对应。

### 4.2 定义

字典是键值对的集合，键值对之间无序，采用大括号{}或者dict()创建字典，可以通过

[]索引获得索引对应的值，键值为不可变数据类型。

注:{}为空字典而不是空集合，空集合需要用set()建立。

创建字典:

> ==dict(zip(k,v)) 				k,v分别为键与值对应列表，并以其对应元素创建字典==
>
> Fromkeys(list)			  将list中每个元素作为键，创建值为空(None)的字典

### 4.3 字典操作方法

> d[k]									键k存在则返回相应值，不在则返回异常；
>
> d.get(k,\<default>)    	   键k存在则返回相应值，不在则返回\<defalut>；
>
> d.pop(k,\<default>)         键k存在则取出相应值，不在则返回\<defalut>；
>
> d.popitem()       			  随机从字典d中取出一个键值对，并以元组形式返回被删除												键值对；
>
> d.pop(a)       	 			  删除字典d中的键值对a，并返回被删除键对应的值；
>
> d.clear()        					清除字典中的所有键值对；
>
> d.items()							以元组类型返回所有键值对；
>
> d.keys()							 返回所有键组成的列表
>
> d.vaules()						  返回所有值组成的列表
>
> len(d)								返回键值对数量
>
> d.update(c)					  将新字典c中所有键值对添加到旧字典d对象上，且有重复												自动覆盖

### 4.4 字典功能

   d[key]=x        			  修改或者添加键值key对应值x;

###    附:一键多值使用方法 

```python
from collections import defaultdict
d = defaultdict(li)
d['1'].append("a")
```

简易方法：

```python
{"name":["1","2"]}
key1 : {key2: vaule}
```



### 4.5 字典的特点

字典十分占内存，但其键查询速度很快，典型的空间换时间，其次，不要在遍历字典的同时修改字典(原因较复杂，暂时不做解析)

## 5. 集合 

### 5.1 定义

多个元素的无序组合，其底层是字典实现，所有元素都是字典的“键对象”，故不能重复，且python要求集合中的元素是不可变数据类型，如：整数，浮	点数，元组类型，不包括列表。(注意空集也是集合)

### 5.2 表示

集合用“{}”表示，元素用逗号分隔，用{}或者set()建立，如果建立空集合必须用set()

且集合顺序是无序的，不一定是最初的定义的顺序。

### 5.3 集合操作方法

  <集合>.函数

> set(ls)          	 使ls中的每一个字符单独拆分变成集合中的元素，且去掉重复元素；
>
> s.add(x)         	如果x不在集合S中，将s增加到x；
>
> s.discard(x)        若x在集合s中，则移除s中的元素x，否则无效但不报错；
>
> s.remove(x)        移除s中的元素x，如果x不在，则会返回keyerror异常；
>
> s.clear()         	移除s中的所有元素；
>
> s.pop()          	 随机返回s的一个元素，并且会更新s，若本身s为空，返回keyerror									异常；
>
> s.copy()        	 返回集合s的一个副本；
>
> len(s)          	  返回集合s的元素个数；
>
> x in s          	  判断元素x是否在集合s中；
>
> x not in s          类似上一个；

​              

### 5.4 集合间的运算

>   s|t            	  返回集合s和集合t的并集；
>
>   s-t            	 返回集合s和集合t的差集；
>
>   s&t               返回集合s和集合t的交集；
>
>   s^t               返回集合s和集合t中的非相同元素；
>
>   s<=t,s<t....     判断集合s和集合t的包含关系；

### 5.5 常见应用

  去除列表中的重复数据：

```python
ls = [] ;s = set(ls);ls = list(s)
```

 

## 6. 序列

### 6.1 定义

  序列是有先后顺序的一组元素，元素可以相同，类型可以不同。

### 6.2 类型

  字符串类型，元组类型，列表类型。

### 6.3 函数

>   in/not in        		 判断函数；
>
>   s+t      					连接两个序列s,t；
>
>   s*n           			   将序列s复制n次；
>
>   s[i]         				 索引，返回s中的第i个元素，i为序列的序号，包括正向，反向，										 不更新序列；
>
>   s[l:i:j:k]         		    切片
>
>   len,min,max       	 同上
>
>   s.index(x[,i,j])     	  返回序列s从i开始到j位置中第一次出现元素x的位置
>
>   s.count(x)        		返回x的出现次数
>
>   

关于切片：

```python
a =[ 0.64061262  0.8451399   0.965673    0.89256687  0.48518743]

print(a[-1]) ###取最后一个元素
[0.48518743]

print(a[:-1])  ### 除了最后一个取全部
[ 0.64061262  0.8451399   0.965673    0.89256687]

print(a[::-1]) ### 取从后向前（相反）的元素
[ 0.48518743  0.89256687  0.965673    0.8451399   0.64061262]

print(a[2::-1]) ### 取从下标为2的元素翻转读取
[ 0.965673  0.8451399   0.64061262]
```





### 6.4 元组类型

元组是一种序列类型，一旦创建就不能更改，使用小括号()或者tuple()创建，元素用逗号分离，可省略括号,常用于数据保护，若元组中仅含一个元素，则必须后面加逗号。

zip(list1,list2,...)将多个列表对应位置元素组合成元组并返回这个zip对象；

大小排序只可使用sorted(tuple)返回列表再转化为元组，其他相关操作与序列一致，无特殊操作。

元组类型的访问和处理速度比列表快，且元组可作为字典的键值，而列表不可以。

 注：

#### 变量加","的含义

逗号`,`用于生成一个长度为1的元组

```python
>>> (1)
1
>>> (1,)
(1,)
>>> 1,
(1,)
```

因此需要将长度为1的元组或列表中元素提取出来可以用`,`简化赋值操作。

```python
>>> a = ['this']
>>> b, = a
>>> b
'this'
```

### 6.5 列表类型

列表类型是一种序列类型，但是可以随意修改，使用方括号[]或者list()创建，元素间用逗号分离，类型可不同，无长度限制，列表相互嵌套以表示多维列表，多维列表可多次索引。

  操作函数：

> ls[i]=x         		   替换列表ls第i个元素为x
>
> ls[i:j:k]         		   切片
>
> del ls[i[:j:k]]      	   删除切片对于ls
>
> ls.append(x)           在列表最后加入元素x
>
> **ls.insert(index,x)	在列表list指定位置list处插入元素x**
>
> ls.extend(alist)		  将列表alist所有元素加到列表ls尾部
>
> ls.clear()        		  清空列表
>
> ls.copy()        	      生成列表ls的副本
>
> ls.pop(i)         	     取出并返回列表ls中的第i个元素并更新列表，默认最后一个元素
>
> ls.remove(x)             将列表ls中出现的第一个元素x删除，若元素x不存在则报错
>
> ==ls.reverse()    	      将列表ls中的元素顺序反转，**没有返回值**==
>
> ==reversed(ls)		     **返回**ls的逆序排列的**迭代器**，可通过列表打印，且只能使用一次，二次打印为空==
>
> ls.sort([reverse=True])     将列表ls升(降)序排序且**无返回值**
>
> sorted(ls)      					将列表ls排序并**返回值**，亦可单独使用；
>
> s.replace(x,y)     				用y替换列表s中x元素

  实例：

```python
b=[i for i in range(10) if i%2==0]
```



### **6.6 序列解包**

> 序列解包用于对多个变量同时赋值；
>
> a.用于列表,元组：x, y, z = 1, 2, 3
>
> ​         [x, y, z] = [1, 2, 3]
>
> b.用于字典时，则是默认对键进行操作赋值，如：x, y = {1:a, 2:b}
>
>    x = 1, y = 2
>
> 如需对键值对操作，则需要使用函数dict.items()
>
> 如需对值操作，则需使用函数dict.values() 

### **6.7 使用zip()进行迭代**

zip()函数可对多个序列进行并行迭代，在最短序列”用完”时就会停止。

代码实例：

```python
names =['hedge', 'heaven', 'headdy']
ages = [19, 23, 27, 31]
for name, age in zip(names, ages):
	print("{}:{}".format(name, age)) 
```

打印结果：	

hedge :19

heaven :23

heddy :27

## 7. 布尔值

表示真假，仅包括True与False，其本质为1，0，甚至可以与数字相加，常作为判断返回值。

注：空的列表,0,空字符串，空range对象,空迭代对象等或者None直接作为布尔条件则输出False，反之输出True.

# 板块二 print输出格式化

## 输出格式美化

Python两种输出值的方式: 表达式语句和 print() 函数。

第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。

如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。

如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。

- **str()：** 函数返回一个用户易读的表达形式。

- **repr()：** 产生一个解释器易读的表达形式。

  Click  [here](https://www.runoob.com/python3/python3-inputoutput.html)  to learn more.

## print

```python
print(value, ..., sep=' ', end='\n', 
      file=sys.stdout, flush=False)
```

Prints the values to a stream, or to sys.stdout by default.

**Optional keyword arguments:**

> file:  a file-like object (stream); defaults to the current sys.stdout.
>
> sep:   string inserted between values, default a space.
>
> end:   string appended after the last value, default a newline.
>
> flush: whether to forcibly flush the stream.

除了槽填充格式化外，还有%格式化输出。



## %格式化输出

### Format character

格式符为真实值预留位置，并控制显示的格式。格式符可以包含有一个类型码，用以控制显示的类型，具体类型如下:

>    %s		字符串 (采用str()的显示)
>
>    %r		字符串 (采用repr()的显示)
>
>    %c 		单个字符
>
>    %b 		二进制整数
>
>    %d 		十进制整数
>
>    %i 		十进制整数
>
>    %e 		指数 (基底写为e)
>
>    %E 		指数 (基底写为E)
>
>    %f 		浮点数
>
>    %F 		浮点数，与上相同
>
>    %g 		指数(e)或浮点数 (根据显示长度)
>
>    %G 		指数(E)或浮点数 (根据显示长度)
>
>    %% 		字符"%"

可以用如下的方式，对格式进行进一步的控制：

```
%[(name)][flags][width].[precision]typecode
```

**Operation symbol**

> (name)为命名，用于参数的名称传递(字典的键值)
>
> flags可以有`+`，`-`，`’‘`或`0`。+表示右对齐。-表示左对齐。’ '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。
>
> width		表示显示宽度
>
> precision	表示小数点后精度

比如：

```python
print("%+10x" % 10)
```

```python
print("%04d" % 5)
```

```python
print("%6.3f" % 2.3)
```

```python
print (“Name:%10s Age:%8d Height:%8.2f”%(“Aviad”,25,1.83))
```

```python
print (“Name:%-10s”%(“Aviad”))
```

```python
print (Height:%8.2f”%(1.83))
```

### 字典传递

我们还可以用词典来传递真实值。如下：

```python
print (‘I’m %©s. I have %(l)d yuan.’% {‘c’:’hungry’,’l’:22})
```



## 附：彩色终端

### 1. 实现过程

终端的字符颜色是用转义序列控制的，是文本模式下的系统显示功能，和具体的语言无关。

转义序列是以ESC开头,即用\\033来完成（ESC的ASCII码用十进制表示是27，用八进制表示就是033）。

### 2. 书写格式

**开头部分**：**\\033**\[**显示方式;前景色;背景色m** 

**结尾部分：\\033\[0m** 

 **完整格式： **\\033**\[**显示方式;前景色;背景色m要打印的文字**\\033\[0m** 　　 

如果有空格，空格也会打印出来

注意：开头部分的三个参数：显示方式，前景色，背景色是可选参数，可以只写其中的某一个；另外由于表示三个参数不同含义的数值都是唯一的没有重复的，所以三个参数的书写先后顺序没有固定要求，系统都能识别；但是，建议按照默认的格式规范书写。

**对于结尾部分，其实也可以省略，但是省略后，如果打印了背景色，则整行都会有背景色（包括没有字体的部分），故为了书写规范，建议\\033\[\*\*\*开头，\\033\[0m结尾。**

### 3. 数值表示的参数含义：

**显示方式:** 0（默认值）、1（高亮，即加粗）、4（下划线）、7（反显）、  

**前景色:** 30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（梅色）、36（青色）、37（白色）  

**背景色:** 40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（梅色）、46（青色）、47（白色）

### 4. 常见开头格式：

> \\033\[0m      默认字体正常显示，不高亮
>
> \\033\[32;0m 红色字体正常显示 
>
> \\033\[1;32;40m  显示方式: 高亮    字体前景色：绿色  背景色：黑色
>
> \\033\[0;31;46m  显示方式: 正常    字体前景色：红色  背景色：青色 

### 5. 实例：

(1)

print("\\033\[1;31;40m您输入的帐号或密码错误！\\033\[0m")   **标准写法** 

print("\\033\[1;31;40m您输入的帐号或密码错误！") 

上方代码的输出格式为：字体高亮，红色前景，黄色背景      

PS：前景色也就是字体的颜色


上面两行代码的结果如下：

[![](E:\工具\Typora\Temp\1195739-20170913194547360-1833284876.png)](https://images2017.cnblogs.com/blog/1195739/201709/1195739-20170913194547360-1833284876.png)

 **对于结尾部分，其实也可以省略，但是省略后，如果打印了背景色，则整行都会有背景色（包括没有字体的部分）**

(2)

print("\\033\[0;31m%s\\033\[0m" % "输出红色字符")　　  **标准写法**  

print("\\033\[31m%s\\033\[0m" % "输出红色字符")   　　 **显示方式为0时，可以省略**

print("\\033\[31m%s" % "输出红色字符")

#上方代码的输出格式为：字体默认，红色前景，无背景色

结果如下：

[![](E:\工具\Typora\Temp\1195739-20170913194726453-1419623639.png)](https://images2017.cnblogs.com/blog/1195739/201709/1195739-20170913194726453-1419623639.png)

**没有背景色时，上面3种方式都能得到想要的效果**

   

# 板块三 程序结构

## 1. 基本原理

根据判断条件结果而选择不同向前路径的运动方式。

## 2. 基本条件组合

逻辑非与逻辑与与逻辑或（条件判断存在先后顺序）

关于is与“==”：

is 用于判断两个变量引用对象是否为同一个，即比较对象的地址；

==用于判断两个变量的值是否相同。

见下：

a=1000,b=1000

a==b但是a is not b(id不同)

但是对于整数[-5,256]，python控制台会进行缓存，此时a，b的地址是相同的，而对于[-5,ꝏ]在文件中打开都会进行缓存。此外，is 比 == 的运行效率要高。

*其他细节：*
*赋值符不可以出现在条件句中。*

## 3. 异常处理

**try:**

​     <语句一>

**except** [<异常类型>] [as e]:（可使用多个except定向处理不同的异常类型）

​     <语句二>

保留字try表示运行语句一，若出现(指定类型异常)异常则运行语句二；

[**else:**

​     <语句三>

   如果不发生异常，执行语句三；

**finally：**

​     <语句四>

   无论是否异常，都最后执行语句四，因而通常用来放置释放资源的代码。]

Tip：一般情况下，不要将return语句放在try,except,else,finally块中，而是在板块的最后，否则会发生意想不到的错误。

### 1.常见异常错误

#### SyntaxError

语法错误

#### NameError

尝试访问一下未定义的变量

#### ZeroDivisionError

#### ValueError

值错误

#### TypeError

类型错误

#### AttributeError

访问对象不存在的属性

#### IndexError

索引越界

#### KeyError

字典关键字不存在

### 2.with 上下文管理

基本语法结构：

with context_expr[as var]:

​	语句块

with上下文管理可以自动管理资源，在with代码块执行完毕后自动还原进入该代码之前的现场或者上下文。无论何种原因跳出with块，无论是否有异常，总能保证资源正常释放，极大的简化了工作，在文本操作，网络同学向该年度场合非常常用。

### 3.traceback异常模块

```python
import traceback
traceback.print_exc([file=''])
```

打印详细异常现象

### 4.自定义异常类

可通过class定义一异常类，并通过raise 抛出异常。

## 4. 程序的循环结构

### 4.1 遍历循环

   for <循环变量> in <可迭代对象>:

​     <循环体>                  

   遍历结构有：

   for i in range(m,n,k):     计数遍历循环

   for c in s:          	字符串s遍历循环(取出每一个字符串循环)

   for item in ls:        列表ls遍历循环（ls=[]）

   for line in file:        	遍历文件file的每一行，file为文件标识符

特别地，字典的遍历：

for i in d(d.keys()):				遍历字典d中的所有key

for i in d.vaules():				遍历字典d中的所有value

for i in d.items():				遍历字典d中的所有键值对

可迭代对象包括：序列，字典，迭代器对象(range)，生成器对象。

### 4.2 无限循环

   while <条件>:

​     <语句块>

   反复执行语句块，直至条件不满足为止；(ctrl+c可以强制结束程序)

### 4.3 循环控制保留字

   break           跳出并结束当前整个(最内层)循环，执行循环后的语句；

   continue         	只结束当次循环，继续执行后续次数的循环

### 4.4 循环的高级用法

  循环与else，else语句作为正常完成循环(即未被break中断)的奖励

### 4.5 循环代码优化

优化代码遵循下列三个原则：

(1)尽量减少循环内部不必要的计算

(2)嵌套循环中，尽量减少内部循环的计算，尽可能向外提

(3)局部变量查询较快，尽量使用局部变量。

其他方法：
	

(1)连接多个字符串用join而不是+；

(2)列表进行元素插入和删除时，尽量在列表尾部操作；

# 板块四 函数的定义及调用

## 1. 函数的结构

def <函数名> (参数列表):

​	*"函数注释，可通过help()查询，不会打印"*

​     <函数体>

​     return <返回值>

**函数**是就是将一个函数名变量(栈)绑定到一个函数**对象**(function)(形如字符串)，有特定的id，因而这个函数对象(堆)可以多次赋值到别的函数名变量中。

return可以返回需要的数据作为函数输出值，不设置返回值时默认返回None，当返回多个数值时，返回元组类型。



## 2. 函数参数

函数定义往往需要用到参数，参数列表包括可变参数，可以没有(保留括号)，也可以是多个。

### 2.1 参数形式

参数形式包括形式参数与实际参数，形式参数即定义函数时使用的参数，形参命名只要符合"标识符"命名规则即可，而在调用过程中传递的参数为实际参数，简称"实参"。

### 2.2 参数传递

参数传递即从实参到形参的赋值，包括两种方式：位置传递，名称传递。传递不可变对象(int,float,元组等)使用的是浅拷贝。

附：参数传递copy栈堆的内存分析

(copy模块需额外引入)

浅拷贝copy():

不拷贝子对象的内容，只拷贝对象的引用，即直接引用源对象的引用，对此引用改变时会改变源对象。

深拷贝deepcopy():

拷贝子对象的全部内容，包括子对象的引用，此时修改子对象不改变源对象。 

### 2.3 参数类型

#### 2.3.1 位置参数

函数调用时，实参默认按照位置顺序传递，需要个数与形参匹配，按照位置传递，称为位置参数。若不匹配则返回报错TypeError:missing arguments。

形如：

```python
def test(a, b)：
	c = a + b
test(1,2)
```



#### 2.3.2 默认值参数

我们可以为某些函数设置默认值，这样这些函数在传递时就是可选的，称为"默认值参数"，默认值参数必须放到位置参数后边。

```python
def test(a, b, c = 10):
    d = a + b + c
test(10, 20)
```



#### 2.3.3. 命名参数

我们也可以按照形参的名称传递参数，称为"命名参数"，也称"关键字参数"。

```python
def test(a, b):
	c = a + b
test(b = 10, a = 10)
```



### 2.3.4 可变参数

可变参数指"数量可变的参数"。包括两种情况：

"*param”意为将多个参数收集到一个"元组"对象当中。

"**param"意为将多个参数收集到一个"字典"对象当中。

```python
def test(a, *b, **c):
    print(a, b, c)
test(3, 2, 1, name = 'hedge', age = '19')
```



### 2.3.5 强制命名参数

在可变参数后边的参数为"强制命名参数"，必须按照"命名参数"传递。

```python
def test(*a , b):
	print(a, b)
test(1, 2, 3, b = 3)
```





## 3. 变量的初始化

### 3.1 变量的类型与声明

变量分为两类，局部变量和全局变量，局部变量为组合数据类型且未创建时，等同于全局变量，函数内部变量未经声明则为局部变量，若使用global声明则为全局变量；

全局变量降低了函数的通用性和可读性，应避免全局变量的使用。局部变量只作用在定义与结束之间的模块，调用比全局变量快*(提高效率应考虑将全局变量更换为局部变量)*，应优先考虑使用。如果局部变量与全局变量同名，则在函数内隐藏全局变量，只使用同名的局部变量。

比如：

```python
import math
def text01():
	for i in range(10000):
		s = math.sqrt(i)
```

可以修改为如下代码:

```python
import math
def test02():
    b = math.sqrt
	for i in range(10000):
    	s = b(i)
```

*Tip:如果在一个范围内，对一个变量进行赋值，那么这个变量就会被认为是局部变量。总的来说，引用全局变量，不需要golbal声明，**修改全局变量，需要使用global声明**，特别地，列表、字典等如果只是修改其中元素的值，可以直接使用全局变量，不需要global声明。*

此外，调用函数locals()及globals()可以查看局部变量与全局变量。

值得注意的是，在嵌套函数中，用nonlocal宣称外层局部变量。

### 3.2 变量的赋值

 变量名=表达式，包括以下两种赋值方法：

#### 3.2.1 链式赋值：

 如：x=y=2

#### 3.2.2 系列解包赋值：

 如：a,b,c=4,5,6相当于各自赋值，非元组类型

 可用于变量值的互换，如：a, b = b, a

*Tip：变量名称不可与函数名相同，否则<u>**多次调用**</u>时会出现歧义报错。*



### 3.3 变量的删除

 使用del函数删除不再使用的变量，此时如果对象没有被引用，则会被垃圾回收器回收，清理内存空间。

### 3.4 常量

 python不支持常量，即没有语法规则限制改变一个常量的值，只能通过逻辑上不做修改。

 

## 附注： __xxx__ 函数

### 附注1 概况

python用下划线作为变量前缀和后缀指定特殊变量

_xxx 不能用’from module import ’导入

__xxx__ 系统定义名字

__xxx 类中的私有变量名

核心风格：避免用下划线作为变量名的开始。

因为下划线对解释器有特殊的意义，而且是内建标识符所使用的符号，我们建议程序员避免用下划线作为变量名的开始。一般来讲，变量名_xxx被看作是“私有的”，在模块或类外不可以使用。当变量是私有的时候，用_xxx 来表示变量是很好的习惯。因为变量名__xxx__对Python 来说有特殊含义，对于普通的变量应当避免这种命名风格。

“单下划线” 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；
“双下划线” 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。

以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用“from xxx import ”而导入；以双下划线开头的（__foo）代表类的私有成员；以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如 __init__（）代表类的构造函数。

### 附注2 保留属性：

 先来看下保留属性：

>>> Class1.__doc__ # 类型帮助信息 'Class1 Doc.' 
>>> Class1.__name__ # 类型名称 'Class1' 
>>> Class1.__module__ # 类型所在模块 '__main__' 
>>> Class1.__bases__ # 类型所继承的基类 (<type 'object'>,) 
>>> Class1.__dict__ # 类型字典，存储所有类型成员信息。 <dictproxy object at 0x00D3AD70> 
>>> Class1().__class__ # 类型 <class '__main__.Class1'> 
>>> Class1().__module__ # 实例类型所在模块 '__main__' 
>>> Class1().__dict__ # 对象字典，存储所有实例成员信息。 {'i': 1234}

### 附注3 保留方法:

可以把保留方法分类：

![img](file:///C:UsersHedgeAppDataLocalTempksohtml22996wps1.jpg) 

对 __init__() 方法的调用发生在实例被创建 之后 。如果要控制实际创建进程，请使用 [__new__() 方法](#esoterica)。

按照约定， __repr__() 方法所返回的字符串为合法的 Python 表达式。

在调用 print(x) 的同时也调用了 __str__() 方法。

由于 bytes 类型的引入而从 Python 3 开始出现。

### 附注4 行为方式与迭代器类似的类

![img](file:///C:UsersHedgeAppDataLocalTempksohtml22996wps2.jpg) 

无论何时创建迭代器都将调用 __iter__() 方法。这是用初始值对迭代器进行初始化的绝佳之处。

无论何时从迭代器中获取下一个值都将调用 __next__() 方法。

__reversed__() 方法并不常用。它以一个现有序列为参数，并将该序列中所有元素从尾到头以逆序排列生成一个新的迭代器。

 

### 附注5 计算属性

![img](file:///C:UsersHedgeAppDataLocalTempksohtml22996wps3.jpg) 

如果某个类定义了 __getattribute__() 方法，在 每次引用属性或方法名称时 Python 都调用它（特殊方法名称除外，因为那样将会导致讨厌的无限循环）。

如果某个类定义了 __getattr__() 方法，Python 将只在正常的位置查询属性时才会调用它。如果实例 x 定义了属性color， x.color 将 不会 调用x.__getattr__('color')；而只会返回x.color 已定义好的值。

无论何时给属性赋值，都会调用 __setattr__() 方法。

无论何时删除一个属性，都将调用 __delattr__() 方法。

如果定义了 __getattr__() 或 __getattribute__() 方法， __dir__() 方法将非常有用。通常，调用 dir(x) 将只显示正常的属性和方法。如果__getattr()__方法动态处理color 属性， dir(x) 将不会将 color 列为可用属性。可通过覆盖 __dir__() 方法允许将 color 列为可用属性，对于想使用你的类但却不想深入其内部的人来说，该方法非常有益。

![img](file:///C:UsersHedgeAppDataLocalTempksohtml22996wps4.jpg) 

### 附注6 可比较的类

我将此内容从前一节中拿出来使其单独成节，是因为“比较”操作并不局限于数字。许多数据类型都可以进行比较——字符串、列表，甚至字典。如果要创建自己的类，且对象之间的比较有意义，可以使用下面的特殊方法来实现比较。

![img](file:///C:UsersHedgeAppDataLocalTempksohtml22996wps5.jpg) 

### 附注7 可序列化的类

Python 支持 [任意对象的序列化和反序列化](http://blog.163.com/jackylau_v/blog/serializing.html)。（多数 Python 参考资料称该过程为 “pickling” 和 “unpickling”）。该技术对与将状态保存为文件并在稍后恢复它非常有意义。所有的 [内置数据类型](http://blog.163.com/jackylau_v/blog/native-datatypes.html) 均已支持 pickling 。如果创建了自定义类，且希望它能够 pickle，阅读 [pickle 协议](http://docs.python.org/3.1/library/pickle.html) 了解下列特殊方法何时以及如何被调用

![img](file:///C:UsersHedgeAppDataLocalTempksohtml22996wps6.jpg) 

要重建序列化对象，Python 需要创建一个和被序列化的对象看起来一样的新对象，然后设置新对象的所有属性。__getnewargs__() 方法控制新对象的创建过程，而 __setstate__() 方法控制属性值的还原方式。

 

### 附注8 可在 with 语块中使用的类

with 语块定义了 [运行时刻上下文环境](#typecontextmanager)；在执行 with 语句时将“进入”该上下文环境，而执行该语块中的最后一条语句将“退出”该上下文环境。

![img](file:///C:UsersHedgeAppDataLocalTempksohtml22996wps7.jpg) 

该文件对象同时定义了一个 __enter__() 和一个 __exit__() 方法。该 __enter__() 方法检查文件是否处于打开状态；如果没有， _checkClosed()方法引发一个例外。

__enter__() 方法将始终返回 self —— 这是 with 语块将用于调用属性和方法的对象

在 with 语块结束后，文件对象将自动关闭。怎么做到的？在 __exit__() 方法中调用了 self.close() .

 

### 附注9 真正神奇的东西

 如果知道自己在干什么，你几乎可以完全控制类是如何比较的、属性如何定义，以及类的子类是何种类型。

![img](file:///C:UsersHedgeAppDataLocalTempksohtml22996wps8.jpg) 

python中以双下划线的是一些系统定义得名称，让python以更优雅得语法实行一些操作，本质上还是一些函数和变量，与其他函数和变量无二，比如:x.__add__(y) 等价于 x+y
有一些很常见，有一些可能比较偏，在这里罗列一下，做个笔记，备忘。


x.__contains__(y) 等价于 y in x, 在list,str, dict,set等容器中有这个函数
__base__, __bases__, __mro__, 关于类继承和函数查找路径的。
class.__subclasses__(), 返回子类列表
x.__call__(...) == x(...)
x.__cmp__(y) == cmp(x,y)
x.__getattribute__('name') == x.name == getattr(x, 'name'),  比__getattr__更早调用
x.__hash__() == hash(x)
x.__sizeof__(), x在内存中的字节数, x为class得话， 就应该是x.__basicsize__
x.__delattr__('name') == del x.name
__dictoffset__ attribute tells you the offset to where you find the pointer to the __dict__ object in any instance object that has one. It is in bytes.
__flags__, 返回一串数字，用来判断该类型能否被序列化（if it's a heap type), __flags__ & 512
S.__format__, 有些类有用
x.__getitem__(y) == x[y], 相应还有__setitem__, 某些不可修改类型如set，str没有__setitem__
x.__getslice__(i, j) == x[i:j], 有个疑问，x='123456789', x[::2],是咋实现得
__subclasscheck__(), check if a class is subclass
__instancecheck__(), check if an object is an instance
__itemsize__, These fields allow calculating the size in bytes of instances of the type. 0是可变长度， 非0则是固定长度
x.__mod__(y) == x%y, x.__rmod__(y) == y%x
x.__module__ , x所属模块
x.__mul__(y) == xy,  x.__rmul__(y) == yx

__reduce__, __reduce_ex__ , for pickle

__slots__ 使用之后类变成静态一样，没有了__dict__, 实例也不可新添加属性

__getattr__ 在一般的查找属性查找不到之后会调用此函数

__setattr__ 取代一般的赋值操作，如果有此函数会调用此函数， 如想调用正常赋值途径用 object.__setattr__(self, name, value)

__delattr__ 同__setattr__, 在del obj.name有意义时会调用

 

## 4.lambda函数

  lambda函数是一种匿名函数，没有名称，使用lambda保留字定义，只允许有一个表达式并且该表达式计算所得结果即为函数返回值。常用于定义**简单的能在一行内表示的**函数；

   lambda<参数>:<表达式>

  比如：

```python
f = [lambda x,y: x+y,lambda x,y: x*y]
print(f[1](1,2))
```

注：函数定义后需调用

 

## 5.函数的查询

通过help(函数名),注意，不要加()，查询函数或者模块的批注。



## 6. 常用函数应用

### 6.1 递归函数

递归函数是指自己调用的函数，在函数体内部直接或者间接地调用本身，类似于数学归纳法。每个递归函数必修包括两个部分：中止条件与递归条件。

常见数学应用如：斐波那契数列，阶乘及汉诺塔



### 6.2 嵌套函数

嵌套函数，在函数内部定义的函数，嵌套函数的定义及调用都只能在函数内部使用。常用于数据的封装(即数据隐藏，使得外部无法访问)，贯彻DRY(Don't repeat yourself)原则以及闭包。

```python
def f1():
	print("hello,world")
	def f2():
		print("byebye ,world")
```



# 板块五 文件的读取与操作

## 1. 文件类型

本质上，所有文件都是二进制文件，但展示形式包括二进制文件及文本文件。

 

## 2. 文件的打开与关闭

文件需要从存储状态转变为占用状态才可唯一地排他地进行操作，其中常用函数有：

文件句柄.<函数名>

open(<文件名>,<打开模式>,encoding='UTF-8')

**注意：对于带有BOM的txt文本，解码方式应该选择UTF-8-sig**

文件名表示：绝对路径(反斜杠换位斜杠/)

​        相对路径（源文件同目录可省略，使用"."，单一目录无需"."）

Tip：在powershell中带有空格的路径，路径需要用英文双引号括起来。

打开模式：  

​		读写模式：

​        "r"只读模式，默认值，如果文件不存在，返回FileNoFoundError;

​        "w"覆盖写模式，文件不存在则创建，存在则完全覆盖；

​        "x"创建写模式，文件不存在则创建，存在则返回FileExistsError(文本的创建另存为);

​        "a"追加写模式，文件不存在则创建，存在则在文件最后追加内容；

​       文件类型：

​       "b"二进制文本类型；

​        "t"文本文件模式，默认值；

​        "+"与w/x/a同时使用，在原基础上增加读功能。

​	close()   	关闭文件，且python关闭后自动关闭(最好自己打上，减少运行内存占用)

​	注：在windows平台下使用python内置函数 open() 时发现,当不传递encoding参数时，会自动采用gbk(cp936)编码打开文件，而当下**很大部分**文件的编码都是**UTF-8**，部分加密为**UTF-8-sig**（带有BOM加密文件）。

​    我们当然可以通过每次手动传参encoding='utf-8'，但是略显冗余，而且有很多外国的第三方包，里面调用的内置open()函数并没有提供接口让我们指定encoding，这就会导致这些包在windows平台上使用时，常会出现如 "UnicodeDecodeError:'gbk' codec can't decode byte 0x91 in position 209: illegal multibyte sequence" 的报错。

[python文件读写,以后就用with open语句](https://www.cnblogs.com/ymjyqsx/p/6554817.html)

读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。

读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。

读文件

要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：

```python
f = open('/Users/michael/test.txt', 'r')
```

标示符'r'表示读，这样，我们就成功地打开了一个文件。

如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：

```python
f=open('/Users/michael/notfound.txt', 'r')
```

```python
Traceback (most recent call last):

File "<stdin>", line 1, in <module>

FileNotFoundError: [Errno 2] No such file or directory: '/Users/michael/notfound.txt'
```

如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：

```python
f.read()
'Hello, world!'
```

最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：

```python
f.close()
```

由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

```python
try:

	f = open('/path/to/file', 'r')

	print(f.read())

finally:

	if f:

	f.close()
```

但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

```python
with open('/path/to/file', 'r') as f:

	print(f.read())
```

这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

```python
for line in f.readlines():

	print(line.strip()) # 把末尾的'\n'删掉
```

写文件

写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

```python
f = open('/Users/michael/test.txt', 'w')>>> f.write('Hello, world!')>>> f.close()
```

你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：

with open('/Users/michael/test.txt', 'w') as f:

  f.write('Hello, world!')

要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码

字符编码

要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：

```python
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')>>> f.read()'测试'
```

遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

```python
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
```

二进制文件

前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

```python
f = open('/Users/michael/test.jpg', 'rb')>>> f.read()
```

b'xffxd8xffxe1x00x18Exifx00x00...' # 十六进制表示的字节

 

 

总结：以后读写文件都使用with open语句，不要再像以前那样用f = open()这种语句了

 

　　　对于多个文件的读写，可以写成以下两种方式：

![img](file:///C:UsersHedgeAppDataLocalTempksohtml22996wps9.png) 

with open('/home/xbwang/Desktop/output_measures.txt','r') as f:

  with open('/home/xbwang/Desktop/output_measures2.txt','r') as f1:

​    with open('/home/xbwang/Desktop/output_output_bk.txt','r') as f2:
　　　　　　　........
　　　　　　　........
　　　　　　　........



![img](file:///C:UsersHedgeAppDataLocalTempksohtml22996wps11.png) 

with open('/home/xbwang/Desktop/output_measures.txt','r') as f:

........

with open('/home/xbwang/Desktop/output_measures2.txt','r') as f1:

........

with open('/home/xbwang/Desktop/output_output_bk.txt','r') as f2:

........

![img](file:///C:UsersHedgeAppDataLocalTempksohtml22996wps12.png) 

 

## 3. 文件内容的读取

格式：<变量名称>.<函数名称>

​	read([size])      读入全部内容，如果给出参数，则读入前size个字节；     

​	readline([size])    读入一行内容，如果给出参数，则读入前size个字节；  

​	readlines([hint])   	读入所有行内容，以每行为元素形成列表，如果给出参数，则

​           	读入前hint行。

## 4. 全文本操作

​	a.一次读入一次处理；

​	b.分次读入一次处理，每次读取n行，读取完毕后关闭再次读取n行，节省内存。

​	c.一次读入逐行处理；

​	d.分行读入逐行处理；

 

## 5. 文件属性与方法

### 方法：

write(s)       				向文件中写入一个字符串或者字节流；

writelines(lines)   		将一个元素全为字符串的列表写入文件，不换行无空格无返回值；

seek(offset)    		 	改变当前文件操作指针的位置，offset含义如下：

​           						

| 序号 | 方法                         | 描述                                                         |
| :--- | :--------------------------- | ------------------------------------------------------------ |
| 1    | file.close()                 | 关闭文件。关闭后文件不能再进行读写操作。                     |
| 2    | file.flush()                 | 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。 |
| 3    | file.fileno()                | 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。 |
| 4    | file.isatty()                | 如果文件连接到一个终端设备返回 True，否则返回 False。        |
| 5    | file.next()                  | 返回文件下一行。                                             |
| 6    | file.read([size])            | 从文件读取指定的字节数，如果未给定或为负则读取所有。         |
| 7    | file.readline([size])        | 读取整行，包括 "\n" 字符。                                   |
| 8    | file.readlines([sizeint\])   | 读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力。 |
| 9    | file.seek(offset[, whence\]) | 设置文件当前位置，0-文件开头；1-当前位置；2-文件结尾         |
| 10   | file.tell()                  | 返回文件当前指针位置。                                       |
| 11   | file.truncate([size\])       | 截取指标当前size个字节的内容，默认为当前文件位置。           |
| 12   | file.write(str)              | 将字符串写入文件，返回的是写入的字符长度。                   |
| 13   | file.writelines(sequence)    | 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。 |

### 注：文件的操作无任何输出值

字节计算：一个字母1个字节，一个汉字3个字节

关于name__

首先需要了解 __name__ 是属于 python 中的内置类属性，就是它会天生就存在于一个 python 程序中，代表对应程序名称。

比如所示的一段代码里面（这个脚本命名为 pcRequests.py），我只设了一个函数，但是并没有地方运行它，所以当 run 了这一段代码之后我们有会发现这个函数并没有被调用。但是当我们在运行这个代码时这个代码的 __name__ 的值为 __main__ （一段程序作为主线运行程序时其内置名称就是 __main__）。

```python
import requestsclass requests(object):
	def __init__(self,url):
	self.url=url
	self.result=self.getHTMLText(self.url)
def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return "This is a error."
  print(__name__)
```

结果：

__main__Process finished with exit code 0

当这个 pcRequests.py 作为模块被调用时，则它的 __name__ 就是它自己的名字：

import pcRequestspcRequestsc=pcRequestsc.__name__

结果：

'pcRequests'

看到这里应该能明白，自己的 __name__ 在自己用时就是 main，当自己作为模块被调用时就是自己的名字，就相当于：我管自己叫我自己，但是在朋友眼里我就是小仙女一样。

 

## 6. 文件的操作

### 6.1 文件调用

(1)相同文件夹

```python
import a

a.test()
```

(2)不同文件夹

```python
import sys

sys.path.append('path( of a)')

import a

a.test()
```

 *Tip:文件路径及名称中尽量不要出现空格，否则无法直接引用，但是可以引用如下：*

```python
umc = __import__("usual math calculate")
```

引用模块usual math calculate并命名为umc



### 6.2 文本复制

copyFile(source_path, target_path)

```python
# copyfile .py

from shutil import copyfile

from sys import exit

source = 'D:\\testData\\123.png'  # 源路径

target = 'D:\\123.png'                   # 目标路径 

# adding exception handling

try:
    
    copyfile(source, target)            # copyfile 函数调用

except:
    
	print('copy file faild')
```



# 板块六 类

## 1. 类的定义

类也是一种对象，不同于数组列表等的是，类包含数据及方法(即函数)两种不同对象，类似于对象的*"模具"*，用于输出打印实例对象，即实例对象是通过类打印出来的对象。此外，结构包括：类属性，实例属性，实例方法(代码对象)，实例对象。

对象命名通常首字母大写，多个单词采取驼峰原则。

实例分析:

```python
class Women:

	sex = '女'

	faceValue = "高"

	height = "168"

	weight = "85斤"

	color = "yellow"		# 类属性
    def __init__(self,name):	# 实例属性
        self.name = name

	def makeChild(self):
        
        print("可以生宝宝")		# 实例方法

	def cookie(self):

		print("做饭")

	def memeda(self):
		
        print("白天么么哒")
```

#打印Women 类

```python
print(Women)
#输出结果：<class '__main__.Women'>
```

或动态创建一个类

```python
def init(self, name):
    self.name = name

attrs = dict(name=None, age=None, __init__=init )
# type创建一个类, base object, 设置属性和__init__等
klass = type("MyClass", (object, ), attrs)

my = klass(name="Hello")

print(my)       # <__main__.MyClass object at 0x10b882290>
print(my.name)  # Hello
```

 

## 2. 实例对象

通过object = 类名([参数…])构造实例对象，实例对象具有全部的类属性及实例属性，实例方法，且调用实例对象时，自动调用实例属性。

实例分析：

```python
lisi = Women() # 将Women类实例化成对象

print(lisi)  # <__main__.Women object at 0x000001B6873C8CC0>
```

 

## 3. 属性和方法

构造函数: __init__(self, 参数)方法:

​	初始化创建好的对象，给实例赋值

实例属性从属于实例对象，相当于实例变量，实例方法从属于实例对象，相当于函数，且在Python中，不同于其他语言，Python没有方法的重载，即不能通过参数的不同辨别同名方法，后定义的方法和覆盖先定义的方法，只有最后一个方法有效，且不会报错。

方法也是对象，在python中方法具有动态性，可以再定义及修改。

在本类中调用实例属性及方法的语法如下：

object.属性名

object.方法名(实参列表)

附：方法调用的本质

```python
a = Person()

a.study() = Person.study(a)
```



### 3.1 实例属性

A.使用对象创建的属性称之为对象属性，只有当前对象里才存在，如果使用对象属性创建了一个和类里面同名的属性，那么调用的时候会优先查找对象里面的属性

B.使用类里面的方法的参数self创建的属性也为对象属性

```python
class People(object):

    address = '山东' #类属性

    def __init__(self):

        self.name = 'xiaowang' #实例属性

        self.age = 20 #实例属性

p = People()

p.age =12 #实例属性

print(p.address) #正确

print(p.name)    #正确

print(p.age)     #正确

print(People.address) #正确

print(People.name)    #错误

print(People.age)     #错误
```



### 3.2 类属性

A.当使用对象.属性名来改类里面的属性的时候，其实是在对象里面创建了一个同名的属性

B.当将对象里面同名的属性删除掉以后还是会调用类的属性

C.不能再对象里删除类里面的属性，只有使用的权利使用类操作过的属性所有对象在调用类属性的时候都是修改后的属性创建对象属性的方法

```python
class People(object):

    name = 'Tom'  #公有的类属性

    __age = 12     #私有的类属性

p = People()

print(p.name)           #正确

print(People.name)      #正确

print(p.__age)            #错误，不能在类外通过实例对象访问私有的类属性

print(People.__age)        #错误，不能在类外通过类对象访问私有的类属性
```



### 附：实例属性与类属性的区别

类属性就相当与全局变量，实例对象共有的属性，实例对象的属性为实例对象自己私有。

类属性就是`类对象`（Tool）所拥有的属性，它被所有`类对象`的`实例对象(实例方法)`所共有，在内存中只存在一个副本，这个和C++中类的静态成员变量有点类似。对于公有的类属性，在类外可以通过`类对象`和`实例对象`访问。

```python
class People(object):

    country = 'china' #类属性

print(People.country)

p = People()

print(p.country)

p.country = 'japan' 

print(p.country)      #实例属性会屏蔽掉同名的类属性

print(People.country)

del p.country    #删除实例属性

print(p.country)
```

- 如果需要在类外修改`类属性`，必须通过`类对象`去引用然后进行修改。如果通过实例对象去引用，会产生一个同名的`实例属性`，这种方式修改的是`实例属性`，不会影响到`类属性`，并且之后如果通过实例对象去引用该名称的属性，实例属性会强制屏蔽掉类属性，即引用的是`实例属性`，除非删除了该`实例属性`。

###  3.3 实例方法

实例方法或者叫对象方法，指的是我们在类中定义的普通方法。
只有实例化对象之后才可以使用的方法，该方法的第一个形参接收的一定是对象本身。

Python 的实例方法用得最多，也最常见。我们先来看 Python 的实例方法。

```python
class Kls(object):
    def __init__(self, data):
        self.data = data

    def printd(self):
        print(self.data)


ik1 = Kls('leo')
ik2 = Kls('lee')

ik1.printd()
ik2.printd()
```

输出：

> leo
>
> lee

上述例子中，`printd`为一个实例方法。实例方法第一个参数为`self`，当使用`ik1.printd()`调用实例方法时，实例`ik1`会传递给`self`参数，这样`self`参数就可以引用当前正在调用实例方法的实例。利用实例方法的这个特性，上述代码正确输出了两个实例的成员数据。

### 3.4 类方法

#### 3.4.1 概述

类方法用来操作类属性，可以通过装饰器@classmethod来定义，classmethod修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。

#### 3.4.2 定义方法

@classmethod

def 类方法(cls,[形参])：

​	函数体

```python
class A(object):  
    
bar = 1    

def func1(self):    
    
    print ('foo')   
    
    @classmethod  
    
    def func2(cls):  
        
        print ('func2')  
        
        print (cls.bar) 
        
        cls().func1()   # 调用 foo 方法 
        
A.func2()               # 不需要实例化
```

注意：

1. @classmethod必须位于方法上面一行；

2. 第一个cls必须有；cls指的是类对象本身(class缩写)；
3. 无需给cls传参；
4. 类方法中访问实例变量和实例方法会导致错误；
5. 子类继承父类方法时，传入的cls是子类对象，而非父类对象。



### 3.5 静态方法

#### 3.5.1 概述

python允许定义与类对象无关的方法，称为“静态方法”，“静态方法”和在普通模块中的的函数没有区别，只不过“静态方法”放到了“类的名字空间里”，调用需要通过类调用。

#### 3.5.2 定义方法

“静态方法”可以通过装饰器@staticmethod来定义，格式如下：

@staticmethod

def 静态方法名([参数])：

​	函数体

注意：

1. @staticmethod必须位于方法上面一行；
2. 调用方法：“类名.静态方法名(参数列表)”
3. 静态方法中访问实例变量和实例方法会导致错误；

实例

```python
class A:

	@staticmethod

	def demo():
	
		print('类来调用')

a = A()

a.demo()

A.demo()
```

 

### 3.6 析构方法

__del__（self）方法又称析构方法，用于实现对象被销毁时所需的操作(释放空间等)，也可以直接使用del语句。

Python实现自动的垃圾回收，当对象没有被引用时(即引用次数为0)，由垃圾回收器调用析构方法进行删除。因此，系统会自动使用析构方法，一般无需自定义(重新定义后系统会按照自定义的**del**语法删除对象)，自定义可在当前文件执行完毕之前去执行或者是使用del对象名去触发。



### 附：@property装饰器

@property装饰器可以使得有个方法的*调用方式*变成“属性调用”，但是不能改变其值。

实例分析见下：

在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：

```python
s = Student()
s.score = 9999
```

上面的赋值显然不符合实际情况，为了限制score的范围，可以通过一个`set_score()`方法来设置成绩，再通过一个`get_score()`来获取成绩，这样，在`set_score()`方法里，就可以检查参数：

```python
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```

现在，对任意的Student实例进行操作，就不能随心所欲地设置score了：

```python
>>>s = Student()
>>>s.set_score(60)
>>>s.get_score()
60
>>>s.set_score(9999)
Traceback (most recent call last):

ValueError: score must between 0 ~ 100!
```

但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必要要做到的！

还记得装饰器(secorator)可以给函数添加上功能吗？对于类的方法，装饰器一样其作用。Python内置的`@property`装饰器就是负责把一个方法变成属性调用的：

```python
class Student(object):
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!!!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!!!')
        self.__score = score
```

`@property`的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上`@property`就可以了，此时，`@property`本身又创建了另一个装饰器`@score.setter`，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：

```python
>>> s = Student()
>>> s.score = 60 # OK，实际转化为s.set_score(60)
>>> s.score # OK，实际转化为s.get_score()
60
>>> s.score = 9999
Traceback (most recent call last):

ValueError: score must between 0 ~ 100! 
```

注意到这个神奇的`@property`，我们都在对实例操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

```python
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
```

上面的`birth`是可读写属性，而`age`就是一个只读属性，因为`age`可以根据`birth`和当前时间计算出来。

`@property`广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性

## 4. self的说明

方法里面的self代表的是当前类对应的实例对象；

self不是只能叫self别的也可以，但是规范来说都使用self，且调用实例方法时不能给self传参，self由解释器自动传参。

实例：

```python
class A:

	name = ''

	def demo(self):

		print(self) # 代表当前实例化类的对象

		print(id(self))

a = A()

a.demo()

print(a)

print(id(a))
```

 

## 5. return 方法的返回值

和函数一样，代码遇到return下面就不在执行，会将值返回给调用处

没有return的方法打印调用处的值为None

实例

```python
class Demo:

	name = ''

	def speak(self):

		print("我是{}号楼".format(self.name))

	def myRetuen(self):

		return self.name

		print(self.name) # 不在执行

d2 = Demo()

d2.name = 'd2'
# 输出结果：给当前对象添加对象属性
print(d2.name)	
# 输出结果：'d2'
print(d2.speak()) 
# 输出结果：我是d2楼
d2Name = d2.myRetuen()	

print(d2Name) 
# 输出结果：None
```

 



 

## 6. 给对象和类绑定方法

(1)给对象绑定方法

from types import MethodType

实例

```python
def func(self):
    
	print('func')
    
from types import MethodType

a = A()

#a.func = MethodType(方法名,对象名)

a.func = MethodType(func,a)
```

 

(2) 给类绑定方法

实例

```python
def func(self):

	print('func')#类名.属性名 = 函数名

A.func = func
```

注意:

1.构造方法第一个参数必须为self

2.给对象绑定属性或者方法只有当前对象有给类绑定属性或者方法所有当前类的实例化的对象都会拥有

 

## 7. __slots__ 限制对象

动态添加属性

只能创建__slots__允许的属性 否则会报 AttributeError: ‘A’ object has no attribute ‘xxx’

实例:

class A:

  __slots__ = ('属性1'，'属性2'...)

 

## 8. 私有属性和私有方法

#### 8.1类的私有属性:

以'__'作为开头不能在类的外部进行使用和访问在类的里面使用self.__属性名

私有属性的访问

在类的外部：*对象._类名__(前1个后2个，这也是私有属性的存储方式，可查询)*属性名查找

在类的内部：方法里面的变量self.__属性名调用

注意：在类的内部只要使用self.__属性名那么就会去找私有属性_类名___属性名

#### 8.2类的私有方法

以__作为开头，不能再类的外部进行使用和访问，在类的里面使用self.__方法名

在公有方法里面通过self去调用，方法本质上也是属性。

 

## 9. 继承

概念：面向对象编程带来最大的好处就代码的重用，实现代码重用的操作就是类的继承，被继承的类称之为父类或者基类，超类继承的类称之为子类。

所有的类都会继承一个超类object，即定义新类时()为空，默认继承object类。

### 9.1 单一继承

继承方法：

*class 类名(继承的父类，可以是多个):*

 pass

实例：

```python
class A:
#不管是本类还是子类,只要实例化,就会调用(前提是没有被子类的__init__覆盖）
	def __init__(self,n,a,s):
		self.name = n
		self.age = a
		self.sex = s
	def speak(self):
		print("我现在{}岁了，我叫{}，我的性别是{}".format(self.age,self.name,self.sex))# a = A('张三',18,'男')
print(a.name)
a.speak()
```

```python
class B(A):

	grade = ''

	def __init__(self,name,age,sex,grade):

		print('我是子类的__init__')

		self.grade = grade
	
		A.__init__(self,name,age,sex)	#必须显式调用父类的初始化方法，不然解释器
        
        								#不会调用

	def speak(self):
        
		A.speak(self)
    
print("我今年{} 我叫{} 我的成绩是{}".format(self.age,self.name,self.grade))

b = B('张三',18,'男',60)# print(b.name)# print(b.__dict__)

b.speak()
```

 

注意：

类的单一继承子类会继承父类的全部属性及方法，但是只能直接调用**私有以外**的属性和方法；

如果在子类里存在和父类同名的属性或者方法叫做方法或属性的**重写**（也就是会覆盖掉）再次调用的时候调用的是子类的方法和属性；

在子类里调用父类的方法：

父类名.方法名(self[,参数…])，self代表当前类的实例化的对象；或者使用super()（获得父类的定义）.方法名

super(当前类名,self).方法名（如果是单一继承super方法不建议加参数）

super().方法名(建议)

### 9.2 多继承

class类名(继承的父类1,继承的父类2[,父类3..]):

 pass

注意：

*当类进行多继承的时候注意父类的顺序当父类存在**同名的属性或者方法**的时候会从继承时父类的顺序**从左->右**依次查找第一个出现的，同时，多继承会使得类的整体层次异常复杂，尽量避免使用。*

调用父类的方法

```python
class A:

	def speak(self):

		print('我是A类的speak方法')

	def a(self):

		print('a')
```

```python
class B:

	def speak(self):

    	print('我是B类的speak方法')

    def b(self):

    	print('b')
```

```python
class C(A,B):

	def speak(self):
	
		super().speak() #还是从左往右找..

	#super(C,self).speak()

	# super(A,self).speak()

	# super(B,self).speak()
```

## 附：类的组合使用

### **1.组合的定义**

软件重用的重要方式除了继承之外还有另外一种方式，即：组合

组合指的是，在一个类中以另外一个类的对象作为数据属性，称为类的组合。

![img](https://upload-images.jianshu.io/upload_images/13717038-cfb5acf395bf97be.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 2.组合的应用例子-圆环计算

圆环是由两个圆组成的，圆环的面积是外面圆的面积减去内部圆的面积。圆环的周长是内部圆的周长加上外部圆的周长。

这个时候，我们就首先实现一个圆形类，计算一个圆的周长和面积。然后在"环形类"中组合圆形的实例作为自己的属性来用。

![img](https://upload-images.jianshu.io/upload_images/13717038-c585850a1f5c519f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 3.组合的应用例子-实例化组合调用

用组合的方式建立了类与组合的类之间的关系，它是一种‘有’的关系,比如教授有生日，教授教python课程。

当类之间有显著不同，并且较小的类是较大的类所需要的组件时，用组合比较好。

## 10. 运算重载符

### 10.1 构造函数与表达式： **init, sub**

![img](https://images2015.cnblogs.com/blog/817474/201510/817474-20151027101046372-173543059.png)

### 10.2 常见运算符重载方法

| method                                         | overload           | call                                                         |
| ---------------------------------------------- | ------------------ | ------------------------------------------------------------ |
| __init__                                       | 构造函数           | 对象创建: X = Class(args)                                    |
| __del__                                        | 析构函数           | X对象收回                                                    |
| __add__                                        | 云算法+            | 如果没有_iadd_， X+Y， X+=Y                                  |
| __or__                                         | 运算符\|           | 如果没有_ior_，X\|Y, X\|=Y                                   |
| _repr__, __str__                               | 打印，转换         | print(X)，repr(X)，str(X)                                    |
| __call__                                       | 函数调用           | X(*args, **kwargs)                                           |
| __getattr__                                    | 点号运算           | X.undefined                                                  |
| __setattr__                                    | 属性赋值语句       | X.any=value                                                  |
| __delattr__                                    | 属性删除           | del X.any                                                    |
| __getattribute__                               | 属性获取           | X.any                                                        |
| __getitem__                                    | 索引运算           | X[key]，X[i:j]                                               |
| __setitem__                                    | 索引赋值语句       | X[key]，X[i:j]=sequence                                      |
| __delitem__                                    | 索引和分片删除     | del X[key]，del X[i:j]                                       |
| __len__                                        | 长度               | len(X)，如果没有__bool__，真值测试                           |
| __bool__                                       | 布尔测试           | bool(X)                                                      |
| __lt__, __gt__, __le__, __ge__, __eq__, __ne__ | 特定的比较         | X<Y，X>Y，X<=Y，X>=Y， X==Y，X!=Y 注释：（lt: less than, gt: greater than,  le: less equal, ge: greater equal,  eq: equal, ne: not equal ） |
| __radd__                                       | 右侧加法           | other+X                                                      |
| __iadd__                                       | 实地（增强的）加法 | X+=Y(or else __add__)                                        |
| __iter__, __next__                             | 迭代环境           | I=iter(X), next()                                            |
| __contains__                                   | 成员关系测试       | item in X(任何可迭代)                                        |
| __index__                                      | 整数值             | hex(X), bin(X), oct(X)                                       |
| __enter__, __exit__                            | 环境管理器         | with obj as var:                                             |
| __get__, __set__, __delete__                   | 描述符属性         | X.attr, X.attr=value, del X.attr                             |
| __new__                                        | 创建               | 在__init__之前创建对象                                       |

重新定义运算符可以自定义运算规则

### 10.3 索引和分片： __getitem__, __setitem__

如果在类中定义的话，则对于实例的索引运算，会自动调用__getitem__。当实例X出现X[i]这样的索引运算时，Python会自动调用__getitem__方法

![img](https://images2015.cnblogs.com/blog/817474/201510/817474-20151027150259950-645044481.png)

### 10.4 拦截分片

![img](https://images2015.cnblogs.com/blog/817474/201510/817474-20151027150305138-1676343554.png)

### 10.5 索引迭代： __getitem__

![img](https://images2015.cnblogs.com/blog/817474/201510/817474-20151027150309716-303335578.png)

### 10.6 迭代器对象: __iter__, __next__

尽管上一节__getitem__是有效的，但它是迭代退而求其次的方法。Python所有的迭代环境会有优先尝试__iter__的方法，再尝试__getitem__。

从技术角度上讲，迭代环境是通过iter去尝试寻找__iter__方法来实现，而这种方法返回一个迭代器对象。如果已经提供了，python会重复调用迭代器对象的next()方法，直到发生StopIteration异常。如果没有找到__iter__，python会使用__getitem__机制。

![img](https://images2015.cnblogs.com/blog/817474/201510/817474-20151027150320529-1936668870.png)

### 10.7 __getattr__和__setattr__捕捉属性的的引用

__getattr__拦截属性.运算符

![img](https://images2015.cnblogs.com/blog/817474/201510/817474-20151027150324216-2106190284.png)

### 10.8 __repr__和__str__会返回字符串表达形式

![img](https://images2015.cnblogs.com/blog/817474/201510/817474-20151027150330169-840200039.png)

### 10.9 __radd__处理右侧加法

![img](https://images2015.cnblogs.com/blog/817474/201510/817474-20151027154157982-441718945.png)

### 10.10 __call__拦截调用

当实例调用时，使用__call__方法，该方法的功能类似于在类中重载 () 运算符，使得类实例对象可以像调用普通函数那样，以“对象名()”的形式使用。

![img](https://images2015.cnblogs.com/blog/817474/201510/817474-20151027154159044-2002606217.png)



## 11. 常用属性及方法说明

__doc__ 									类的说明

__name__								 返回类名

__base__ 								 返回类的一个父类

__bases__ 								返回类的多个父类

__dict__ 								   返回对象或者类的字典属性

__mor__或者mro()				   查看类的继承层次结构

__str__									  用于重写obj对象描述信息，输出返回值(必须为str类型)，默认为													obj的对象信息

__repr__								   转换成解释器查看的形式

__add__ 								  运算符重载

__getattr__ 							 调用不存在的属性的时候触发

__len__									 即函数len()

__getitem__

__setitem__

dir(obj)								获取对象所有的属性

pass									 空语句

isinstance(对象，类)			判断对象是否是指定类的实例对象

__call__									 定义后使得对象可以像函数一样使用类名()来调用

 

## 12. 设计模式

### 12.1 工厂方法模式



#### 前言


在《设计模式》一书中工厂模式提到了：

- 工厂方法模式（Factory Method）
- 抽象工厂模式 （Abstract Factory）


但是在实际过程中还有一种工厂模式经常被使用，那就是 **简单工厂模式（Simple Factory）**。有一种常见的分类的方法：根据产品是由具体产品还是具体工厂可以分为 **工厂方法模式** 和 **简单工厂模式**；根据工厂的抽象程度可以分为 **工厂方法模式** 和 **抽象工厂模式**。接下来会通过例子对比简单工厂模式和工厂方法模式。



#### 工厂意图


定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method 使一个类的实例化延迟到其子类。

#### 别名


虚构造器（Virtual Constructor）



#### 案例



#### 第一阶段

小李开了一个代工厂，专门帮各大厂商生产手机，一开始只有小米找他生产小米手机(MiPhone)，后来质量过硬，声名远播，苹果公司也找上门了，准备让他生产苹果手机，生意来了，小李小手一挥，停工几个月，加了一个生产线专门生成苹果手机(Iphone)。于是乎，现在一个工厂有两个生产线。

#### 第一阶段 UML 图

让我们借助 UML 图直观了解一下工厂现在的样子。
![img](https://cdn.nlark.com/yuque/__puml/83ce437ce8df7956994e7bb6a64f4a30.svg#lake_card_v2=eyJjb2RlIjoiQHN0YXJ0dW1sXG5jbGFzcyDlt6XljoIge1xuXHQr55Sf5Lqn5bCP57Gz5omL5py6KCk65omL5py6IC4uPiDlsI_nsbPmiYvmnLpcblx0K-eUn-S6p-iLueaenOaJi-acuigpOuaJi-acuiAuLj4g6Iu55p6c5omL5py6XG59XG5DbGllbnQgLS0g5bel5Y6CXG7miYvmnLogLS0gIENsaWVudFxu5bCP57Gz5omL5py6IC0tPiDmiYvmnLpcbuiLueaenOaJi-acuiAtLT4g5omL5py6XG5AZW5kdW1sIiwidHlwZSI6InB1bWwiLCJtYXJnaW4iOnRydWUsImlkIjoiWU9xUXYiLCJ1cmwiOiJodHRwczovL2Nkbi5ubGFyay5jb20veXVxdWUvX19wdW1sLzgzY2U0MzdjZThkZjc5NTY5OTRlN2JiNmE2NGY0YTMwLnN2ZyIsImNhcmQiOiJkaWFncmFtIn0=)

#### 第一阶段代码

通过代码去实现这个逻辑

```python
Copyfrom abc import ABC, abstractmethod

# 手机
class Phone(ABC):
    
    @abstractmethod
    def make(self):
        pass

# 苹果手机
class Apple(Phone):
    
    def make(self):
        print("make apple")

# 小米手机
class XiaoMi(Phone):
    
    def make(self):
        print("make xiaomi")


class Factory:

    def product_phone(self, mobile_type):
        if mobile_type == 'apple':
            return Apple()
        else:
            return XiaoMi()


if __name__ == '__main__':
    factory = Factory()
    factory.product_phone('apple').make()
    factory.product_phone('xiaomi').make()
```

看一下运行结果：

```
Copymake apple
make xiaomi
```



#### 第二阶段

随着第一阶段的订单完成，现在越来越多的手机厂商来找小李来生产手机，问题来了，生产线改造需要导致整个工厂停工一段时间，每次停工对工厂来说都是巨大的损失。那么该怎么解决问题呢？一个工厂似乎不够用了，那么该怎么解决呢？ 把所有的生产线独立出来到单独的工厂，这样子需要生产新的手机只需要新增新的工厂就好了，不会影响其他的手机的生产。



#### 第二阶段代码

同样让我们借助代码去实现这一阶段的逻辑

```python
Copyfrom abc import ABC, abstractmethod

# 抽象工厂
class AbastractFactory(ABC):
    
    @abstractmethod
    def product_phone(self):
        pass

# 苹果工厂
class AppleFactory(AbastractFactory):
    
    def product_phone(self):
        return Apple().make()

# 小米工厂
class XiaomiFactory(AbastractFactory):
    
    def product_phone(self):
        return XiaoMi().make()

# 生产线
class Phone(ABC):
   	
    @abstractmethod
    def make(self):
        pass

# 苹果生产线
class Apple(Phone):
    
    def make(self):
        print("make apple")

# 小米生产线
class XiaoMi(Phone):
    
    def make(self):
        print("make xiaomi")

def client_product(factory:AbastractFactory):
    return factory

if __name__ == '__main__':
    xiaomi = client_product(XiaomiFactory())
    xiaomi.product_phone()
    apple = client_product(AppleFactory())
    apple.product_phone()
```

看一下运行结果：

```python
Copymake xiaomi
make apple
```





#### 简单工厂模式优缺点

- 优点：客户端与产品的创建分离，客户端不需要知道产品创建的逻辑，只需要消费该产品即可。
- 缺点：工厂类集成了所有产品的创建逻辑，当工厂类出现问题，所有产品都会出现问题；还有当新增加产品都会修改工厂类，违背开闭原则

#### 工厂方法模式优缺点

- 优点：更符合开闭原则，增加一个产品类，则只需要实现其他具体的产品类和具体的工厂类即可；符合单一职责原则，每个工厂只负责生产对应的产品
- 缺点：增加一个产品，就需要实现对应的具体工厂类和具体产品类；每个产品需要有对应的具体工厂和具体产品类



### 12.2 单例模式以及Python实现

单例模式

单例模式就是确保一个类只有一个实例.当你希望整个系统中,某个类只有一个实例时,单例模式就派上了用场.
比如,某个服务器的配置信息存在在一个文件中,客户端通过AppConfig类来读取配置文件的信息.如果程序的运行的过程中,很多地方都会用到配置文件信息,则就需要创建很多的AppConfig实例,这样就导致内存中有很多AppConfig对象的实例,造成资源的浪费.其实这个时候AppConfig我们希望它只有一份,就可以使用单例模式.

实现单例模式的几种方法

**1. 使用模块**
其实,python的模块就是天然的单例模式,因为模块在第一次导入的时候,会生成.pyc文件,当第二次导入的时候,就会直接加载.pyc文件,而不是再次执行模块代码.如果我们把相关的函数和数据定义在一个模块中,就可以获得一个单例对象了.
新建一个python模块叫singleton,然后常见以下python文件
`mysingleton.py`



```python
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()
使用:
```



```jsx
from singleton.mysingleton import singleton
```

**2. 使用装饰器**
装饰器里面的外层变量定义一个字典,里面存放这个类的实例.当第一次创建的收,就将这个实例保存到这个字典中.
然后以后每次创建对象的时候,都去这个字典中判断一下,如果已经被实例化,就直接取这个实例对象.如果不存在就保存到字典中.



```python
# encoding:utf-8
__author__ = 'Fioman'
__time__ = '2019/3/6 10:22'


def singleton(cls):
    # 单下划线的作用是这个变量只能在当前模块里访问,仅仅是一种提示作用
    # 创建一个字典用来保存类的实例对象
    _instance = {}

    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        # 将实例对象返回
        return _instance[cls]

    return _singleton


@singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x
        print('这是A的类的初始化方法')


a1 = A(2)
a2 = A(3)
print(id(a1), id(a2))
```

**3.使用类**
思路就是,调用类的instance方法,这样有一个弊端就是在使用类创建的时候,并不是单例了.也就是说在创建类的时候一定要用类里面规定的方法创建



```python
# encoding:utf-8
__author__ = 'Fioman'
__time__ = '2019/3/6 11:06'


class Singleton(object):
    def __init__(self,*args,**kwargs):
        pass

    @classmethod
    def get_instance(cls, *args, **kwargs):
        # 利用反射,看看这个类有没有_instance属性
        if not hasattr(Singleton, '_instance'):
            Singleton._instance = Singleton(*args, **kwargs)

        return Singleton._instance


s1 = Singleton()  # 使用这种方式创建实例的时候,并不能保证单例
s2 = Singleton.get_instance()  # 只有使用这种方式创建的时候才可以实现单例
s3 = Singleton()
s4 = Singleton.get_instance()

print(id(s1), id(s2), id(s3), id(s4))
```

**注意,这样的单例模式在单线程下是安全的,但是如果遇到多线程,就会出现问题.如果遇到多个线程同时创建这个类的实例的时候就会出现问题.**



```python
# encoding:utf-8
__author__ = 'Fioman'
__time__ = '2019/3/6 11:26'
import threading


class Singleton(object):
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            Singleton._instance = Singleton(*args, **kwargs)

        return Singleton._instance


def task(arg):
    obj = Singleton.get_instance(arg)
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
```

![img](https://upload-images.jianshu.io/upload_images/2905385-7df9a07c0ee3a15e.png?imageMogr2/auto-orient/strip|imageView2/2/w/730/format/webp)

*执行结果好像也没有问题,那是因为执行的速度足够的快,如果在**init**()方法中有阻塞,就看到非常的明显.*



```python
# encoding:utf-8
__author__ = 'Fioman'
__time__ = '2019/3/6 11:26'
import threading
import time

class Singleton(object):
    def __init__(self, *args, **kwargs):
        time.sleep(1)
        pass

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            Singleton._instance = Singleton(*args, **kwargs)

        return Singleton._instance


def task(arg):
    obj = Singleton.get_instance(arg)
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
```

![img](https://upload-images.jianshu.io/upload_images/2905385-435f4dede67656d9.png?imageMogr2/auto-orient/strip|imageView2/2/w/689/format/webp)

*可以看到是创建了10个不同的实例对象,这是什么原因呢.因为在一个对象创建的过程中,另外一个对象也创建了.当它判断的时候,会先去获取_instance属性,因为这个时候还没有,它就会调用**init**()方法.结果就是调用了10次,然后就创建了10个对象.*

**如何解决呢?**
`加锁:`
在哪里加锁呢?在获取对象属性_instance的时候加锁,如果已经有人在获取对象了,其他的人如果要获取这个对象,就要等一哈.因为前面的那个人,可能在第一次创建对象.

**创建对象的时候加锁即可**



```python
# encoding:utf-8
__author__ = 'Fioman'
__time__ = '2019/3/6 11:38'

import time
import threading

class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self,*args,**kwargs):
        time.sleep(1)

    @classmethod
    def get_instance(cls,*args,**kwargs):
        if not hasattr(Singleton,'_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton,'_instance'):
                    Singleton._instance = Singleton(*args,**kwargs)

        return Singleton._instance

def task(arg):
    obj = Singleton.get_instance(arg)
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()

obj = Singleton.get_instance()
print(obj)
这种方式创建的单例,必须使用Singleton_get_instance()方法,如果使用Singleton()的话,得到的并不是单例.所以我们推荐使用__new__()方法来创建单例,这样创建的单例可以使用类名()的方法进行实例化对象
```

**4.基于`__new__`方法实现的单例模式(推荐使用,方便)**
知识点:
1> 一个对象的实例化过程是先执行类的`__new__方法`,如果我们没有写,默认会调用object的`__new__`方法,返回一个实例化对象,然后再调用`__init__方法`,对这个对象进行初始化,我们可以根据这个实现单例.
2> 在一个类的`__new__方法中`先判断是不是存在实例,如果存在实例,就直接返回,如果不存在实例就创建.



```python
# encoding:utf-8
__author__ = 'Fioman'
__time__ = '2019/3/6 13:36'
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(cls, '_instance'):
                    Singleton._instance = super().__new__(cls)

            return Singleton._instance


obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)


def task(arg):
    obj = Singleton()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
```

# 板块七 其他

## 1. 推导式

### 1.1 类别：

列表推导式，字典推导式，集合推导式

### 1.2 列表推导式：

通过列表生成列表对象，语法如下：

[表达式 for item in 可迭代对象 ]

```python
>>>[x for x in range(5) if x != 0 ]
>>>[1, 2, 3, 4]
```



### 1.3 字典推导式：

类似于字典推导式，字典推导式也可以增加if条件判断，多个for循环，语法格式如下：

{ key_expression : value_expression for 表达式 in 可迭代对象}

如:

```python
char_	count = { c: (1, 2, 3).count(c) for c in (1, 2, 3)}
```



### 1.4 集合推导式：

通过集合生成集合对象，语法如下：

{ 表达式 for item in 可迭代对象 }(可使用多个循环)

### 1.5 生成器推导式(生成元组)：

同列表：(表达式 for item in 可迭代对象)(可使用多个循环,括号此时**不可省略**)

**但是生成器推导式返回一个生成器，而不是一个数组。**

如:

```python
>>>(x for x in range(5) if x != 0 )
>>><generator object <genexpr> at 0x00000189566F2F90>
```



### 附：生成器迭代器

生成器对象generator object，一个生成器只能调用一次，调用完毕后即清除数据，但可多次访问

遍历函数s(生成器).__next__()移动指标



## 2. python对象

### 2.1对象的基本组成

在python中，一切皆对象，其本质是一个内存块，拥有特定的值，支持特定类型的操作，每个对象由标识(identity)，类型(type)，值(value)三个要素组成。

标识，对应于对象在计算机内存中的地址，使用内置函数id(object)可返回对象的标识；

类型，对应于对象储存的数据所属类型，类型可以限制对象的数据范围以及可执行的操作，可以使用内置函数type(object)查看对象所属类型；

值，表示对象残存的数据信息，可以使用print(object)打印对象的值。

 

### 2.2 对象的引用

变量通过地址引用了“对象”

变量位于栈内存，对象位于堆内存。

赋值将变量绑定到对象，且为动态赋值

Python是动态类型语言，因此变量不需要显式声明类型。

Python是强类型语言，每个对象都有数据类型，只支持该类型格式的操作。

 

### 2.3 标识符

标识符用于变量，函数，类，模块等的名称。标识符有以下规则：

⑴区分大小写；

⑵第一个字符必须是字母或者”_”，其后是字母，数字，下划线；

⑶不能使用保留字；

⑷双下划线开头结尾往往有特殊的用法，尽量避免这种写法。

 

## 3. eval与exec函数

### eval函数

功能：将字符串str当作有效的表达式来求值并**返回结果**

语法：eval(source[,globals[,locals]]) -->value

参数：

source			 一个python表达式或者函数compile()返回的代码对象

globals			可选，必选是dictionary

locals			  可选，任意的映射对象

```python
dict = {a = 100, b = 10}
eval("a+b",dict)
```



### exec()函数

仅执行语句，返回**None**

注：关于exec函数的作用域：**主函数**

```python
def name():
	record = [1, 2]
    for i in range(2):
		exec('A{} = record[{}]'.format(i + 1, i))
name()
print(A1)  
```

[OUTPUT]: NameError: name 'A1' is not defined

```python
def name():
	record = [1, 2]
    for i in range(2):
		exec('A{} = record[{}]'.format(i + 1, i)， globals())
name()
print(A1)  
```

[OUTPUT]: 1



```python
record = [1, 2]
for i in range(2):
	exec('A{} = record[{}]'.format(i + 1, i))
print(A1) 
```

[OUTPUT]:  1

## 4. compile函数

### 描述

compile() 函数将一个字符串编译为字节代码。

### 语法

以下是 compile() 方法的语法:

```
compile(source, filename, mode[, flags[, dont_inherit]])
```

### 参数

- source -- 字符串或者AST（Abstract Syntax Trees）对象。。
- filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
- mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
- flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
- flags和dont_inherit是用来控制编译源码时的标志

### 返回值

返回表达式执行结果。

### 实例

以下展示了使用 compile 函数的实例：

\>>>str = "for i in range(0,10): print(i)"  

c = compile(str,'','exec')   # 编译为字节代码对象  

c <code object <module> at 0x10141e0b0, file "", line 1> 

exec(c) 0 1 2 3 4 5 6 7 8 9 

str = "3 * 4 + 5" 

a = compile(str,'','eval') 

eval(a) 17





#### python实现复制粘贴

\#pyperclip模块中的copy()/paste()可以向计算机的剪贴板发送文本，或从它接受文本。

将程序的输出发送到剪贴板，使它容易粘贴到邮件，文字处理程序或者其他软件中

```python
import pyperclip

pyperclip.copy('hello world')	# 把hello world 复制到计算机的剪切板

print(pyperclip.paste())	# 把计算机剪切板的内容粘贴下来
```



## 5. map函数

------

### 描述

**map()** 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

### 语法

map() 函数语法：

```
map(function, iterable, ...)
```

### 参数

- function -- 函数
- iterable -- 一个或多个序列



## 6. 数据储存--pickle

### 1. 概念

pickle是python语言的**标准模块**，安装python后以包含pickle库，不需要再单独安装。

pickle提供了一种简单的持久化功能，可以将对象以文件的形式存放在磁盘上。

pickle模块用于实现序列化和反序列化。

pickle模块是以二进制的形式序列化后保存到文件中（保存文件的后缀为”.pkl”），不能直接打开进行预览。

pickle模块的接口主要有两类，即序列化和反序列化。

### 2. 常用方法

#### (1) pickle.load(file)

作用：将文件的内容反序列化读出

参数：	

> file:文件名

#### (2) pickle.dump(obj, file, [,protocol])

作用：将数据序列化后存入文件

参数:

> obj:序列化对象
>
> fle:文件
>
> protocol : 序列化使用的协议。如果该项省略，则默认为0。如果为负值或HIGHEST_PROTOCOL，则使用最高的协议版本。

它们可以如下图这样使用：

![img](https://img2018.cnblogs.com/blog/1378116/201904/1378116-20190411175657036-878722408.png)

#### (3) pickle.dumps(obj,[protocol])

作用：将obj序列化为string形式，而不是存入文件。

#### (4) pickle.loads(str)

作用：从str中读取序列化前的对象。

### 3. 可以序列化和反序列化的数据

![img](https://img2018.cnblogs.com/blog/1378116/201904/1378116-20190411175538121-1771757134.png)

## 7. enumerate

### 描述

enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

Python 2.3. 以上版本可用，2.6 添加 start 参数。

### 语法

以下是 enumerate() 方法的语法:

```
enumerate(sequence, [start=0])
```

### 参数

- sequence -- 一个**序列**、**迭代器**或**其他支持迭代对象**。
- start -- 下标起始位置。

### 返回值

返回 enumerate(枚举) 对象。

## 8. 常见编码形式

![image-20210324165352696](C:\Users\Hedge\AppData\Roaming\Typora\typora-user-images\image-20210324165352696.png)

window系统默认解码方式为GBK，linux默认解码方式为UTF，python解释器默认解码方式为Unicode，文本文件打开默认解码方式为UTF-8。



# 板块八 模块化编程

## 1. 编程流程

1. 设计API与描述说明
2. 代码实现
3. 变量局部处理
4. 函数封装



## 2. 不同级导入

```python
from ..name import func	# 从包的上上级导入
from .name import func	# 从包的上级导入
```



## 3. sys.path

### 介绍

指定模块的搜索路径的字符串列表。

sys模块包含了与python解释器和它的环境有关的函数, 里面有个 sys.path属性。它是一个list.默然情况下python导入文件或者模块的话，他会先在sys.path里找模块的路径。如果没有的话,程序就会报错。

#### path[0]

此列表的第一项，path[0],在程序启动时初始化，是包含用来调用Python解释器的脚本的目录。如果脚本目录不可用（例如，如果解释器被交互式地调用，或者脚本是从标准输入读取的），path[0]是空字符串，它引导Python首先在当前目录中搜索模块。

path[0]是C:\Users\chenxi3\Desktop\Simplify，调用python解释器的脚本所在的目录。

#### 标准库

lib目录下(home目录\pythonXX\lib)

#### 第三方库

在lib目录下的site-package目录下(home目录\pythonXX\lib\site-packages)

### 修改path

一个程序可以根据它自己的目的自由地修改path列表。

场景：在实际开发中，默认包含了当前目录为搜索路径，所以，当前目录下的模块和子模块均可以正常访问。

但是若一个模块需要import平级的不同目录的模块，或者上级目录里面的模块，就可以通过修改path来实现。

修改path常用两种方法：

#### 函数添加

这是即时生效的方法，就是在模块里面修改sys.path值，这种方法修改的sys.path作用域只是当前进程，进程结束后就失效了。

个人比较推荐这种方法，比较干净， 避免一些冲突问题。

假如Database.py期望导入config. py，则可以增加上级目录到sys.path列表里面：

```python
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
import configs.config
```

最好加个判断，避免重复加入。

#### 修改环境变量

添加系统环境变量PYTHONPATH，在这个环境变量中输入相关的路径，不同的路径之间用逗号（英文的！)分开。路径会自动加入到sys.path中。

sys.path与init.py
_ init_ .py文件将一个文件夹转化为一个package，这对于创建一个模块的层次结构是很有用的，这样就可以使用这样的导入语句：

```python
import mymodule.cool.stuff
```


如果没有package，这样就不行了。

假如有文件夹mymodule,mymodule下有文件夹cool,cool目录下有stuff.py脚本
将环境变量C:\mymodule加到sys.path中，在mymodule目录下简历_ init_ .py里面写上import cool(文件夹),在cool目录下新建_ init_ .py内容为空
运行时，就只需import mymodule.cool.stuff即可。

注：不需要增加子目录，因为在目录中我们有_ init_ .py