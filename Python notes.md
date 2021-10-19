# 板块一 数据类型及操作

## 1. 简述

> 内置数据类包括数值，字符串，字典，集合，序列，布尔值六种类型，包括各自不同的操作方法，是python的基础。对一个元素的类型检查，可以通过 `type` 方法，该方法返回对象的类型，其本身则是 type 类，可以直接使用对象名进行校检，也可以通过 `isinstance` 方法来检查对象是否是某个类的实例。

## 2. 数值类型

### 2.1 整数型

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
> power(x,y)，用于计算X的y次方。
> 	
>**c.关于等于的判断符号：**
> 
>如输入0.1+0.2==0.3，输出False。

#### 关于进制转换

> 在python中10进制转2进制；10进制转8进制；10进制转16进制分别用内置函数`bin();` `oct();` `hex()`实现，也可以通过 int(object, base) 实现，其中base为转化后的目标进制，并且转化出来的其他进制，均为字符串类型。

### 2.2 浮点型

**除法默认返回浮点数**

> 浮点数之间的运算存在不确定尾数，一般发生在10的-16次方左右，常见的有0.1 + 0.2 == 0.3000000004；计算机中用的二进制并不完全等同十进制，通过 decimal 模块的 `Decimal` 方法，可以解决这个问题，如果想要表示分数，可以通过 fraction模块的 `Fraction` 方法。
>

### 2.3 科学计数法的使用

> 使用e或者E作为幂的符号，以10为基数，格式如下：

\<a>e\<b>表示a10的b次方**（b如果为负数不可以加括号）**。

### 2.4 复数型

> a. python中的复数与数学中的复数保持一致
>
> b. 通过指令“变量.real”获得变量的实部，“变量.imag”获得其虚部。

### 2.5 运算符

> 运算符在不同的对象间具有不同的效果，这种特性称为**多态**，我们可以根据自身需要重载这些操作符，具体使用方法参见第六章类。

> | 比较运算符 | 说明                           |
> | ---------- | ------------------------------ |
> | <, >       | 大于或小于比较，返回布尔值     |
> | <=, >=     | 不大于或不小于判断，返回布尔值 |
>
> | 算术与位运算符 | 说明                      |
> | -------------- | ------------------------- |
> | //             | 整数除，取商的整数部;     |
> | %              | 余数，模运算 如：10%3==1; |
> | **             | 幂运算，x的y次方;         |
> | <<,>>          | 移位(按二进制移动位数)    |
> | \|, ^, &       | 按位或，非，与            |
> | ~              | 按位翻转                  |

#### 扩展赋值运算符

> 在一般情况下，如：x op =y, 其中op为二元操作符，其中不能加空格，如 x\*=3 与 x=x*3 等价。**但对于不可变类型，不应该认为改语法改变现有对象的值，而是它将新构造的值重新分配标识符。**在以下例子中可以看出两者的微小差异：

```python
>>> a = [1,2]
>>> b = a
>>> b += [3,]
>>> b
[1, 2, 3]
>>> a
[1, 2, 3]
>>> b = b +[5]
>>> b
[1, 2, 3, 5]
>>> a
[1, 2, 3]
```

### 2.6 运算符计算优先顺序

> 指数运算>>算术运算>>位运算>>比较运算>>相等比较运算>>赋值运算>>恒等运算>>隶属运算>>逻辑运算

其中圆括号拥有最高优先级，指数运算**从右至左**进行运算，同优先级内从左到右。

```python
>>> 3 ** 4 ** 2
43046721	# 3^16
```

注：数据计算过程中默认输出最宽范围的数据，其中整数<浮点数<复数。

操作函数：

> abs(x)         			     取x的绝对值;
>
> divmod(x,y)       		 商余，输出元组类型（x//y,x%y);
>
> power(x,y[，z])     	  x的y次幂，z为幂余;
>
> max(x,y,..)       			取参数中的最大值;
>
> min(x,y,..)       			 取参数中的最小值；
>
> int(x, base=10)     	  将**浮点数**变成整数并舍弃其小数部分或将base进制的**字符串**转化为整数（表示为"xxxxx.."其中前两位表示字符串的进制，非必要）；
>
> float(x)        			    将x变成浮点数，增加小数部分;
>
> complex(x)       		  将x变成复数，增加虚数部分;
>
> hex(x)	    				  将数字x转换为十六进制
>
> **round(x,d)				  对x四舍五取偶，d是小数截取位数，默认为0，意为取整。**

## 3. 字符串

字符串的本质是字符序列，不同于列表，字符串**定义之后不能再对原字符串进行索引再赋值**。

### 3.1 字符串的创建

  使用 `""` 或者 `''` 创建字符串（换行需要用"`\n`"），也可以使用连**续三个”或者’创建多行字符串**（正常显示换行）或**注释**。

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

更多方法参考Python参考手册。

> str.lower()    	     返回字符串的副本并全部小写   
>
> str.upper()			 返回字符串的副本并全部大写，如：sadef.upper(),输出 SADEF；
>
> str.capitalize()		产生新字符串并将首字母大写其他字母小写
>
> str.title()				 产生新字符串并将所有单词首字母大写
>
> str.swapcase()		产生新字符串并将所有大小写转换
>
> str.index(substr[, start])				如果找到字串str则返回最低索引，如果找不到则返回ValueError。
>
> str.partition(sep)	根据给定的sep，将字符串分为3个部分
>
> str.split(sep=)  	  **返回**一个**列表**，由str根据sep被分割的部分组成,如：'啊,哦,呃'.split(',')，输出['啊','哦','呃']；
>
> str.count(sub)  	  返回字符串sub在str中出现的次数**（非重叠式）**；
>
> str.replace(old,new)
>
> ​           	**返回**字符串str的**副本**，副本中所有的old字符串被替换成new字符串；
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
> str.strip(chars)
>
> ​           	**返回**一个从str中去掉在其左右两侧的char中列出的字符后的字符串；
>
> str.Istrip(chars)
>
> ​           	**返回**一个从str中去掉在其左侧的char中列出的字符的字符串；
>
> str.rstrip(chars)
>
> ​           	**返回**一个从str中去掉在其右侧的char中列出的字符的字符串；
>
> **str.join(iter)**
>
> ​           	**在iter(全部由字符串组成的可迭代对象)对象除最后一个元素外每个元素后都加一个str,主要用于字符串的分隔等；**
>
> str[m:n:k]				表示从m索引到n-1，以k为步长(亦即间距)(不输入默认为1)的字符串进行切片（输出为字符串，而非整数，浮点数）[::-1]表示字符串倒过来切片得结果;
>
> str.startswith(s)   	判断字符串str是否以指定字符串s开头
>
> str.endswith(s)   	 判断字符串str是否以指定字符串s结尾
>
> str.find(s)   			字符串str第一次出现字符串s的位置，如果找不到返回-1
>
> str.rfind(s)   		   字符串str最后一次出现字符串s的位置
>
> str.isalnum()      	判断字符串str中所有字符是否都为字母或者数字
>
> str.isalpha()      	 判断字符串str中所有字符是否都为字母(包括汉字)
>
> str.isdigit()      	  判断字符串str中所有字符是否都为整数
>
> str.isspace()      	判断字符串str是否为空字符串
>
> str.isupper()     	 判断字符串str中所有字符是否都为大写字母
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

### 3.8 字符串格式化

#### 字符串前加 u

> 后面字符串以 Unicode 格式进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。

如：u"我是含有中文字符组成的字符串。"

#### 字符串前加 r

> raw原生字符串，表示只读，去掉反斜杠的转义机制。（特殊字符：即反斜杠加上对应字母，表示对应的特殊含义的，比如最常见的”\n”表示换行，”\t”表示Tab等。 ）常用于正则表达式，对应着re模块。

如：r"\n\n\n\n”　　# 表示一个普通生字符串 \n\n\n\n，而不表示换行了。

#### 字符串前加 b

> 前缀表示后面字符串是bytes 类型。网络编程中，服务器和浏览器只认bytes 类型数据。

如: response = b'Hello World!'   # b' ' 表示这是一个 bytes 对象

> **附：**
>
> 在 Python3 中，bytes 和 str 的互相转换方式是
>
> ```python
> str.encode('utf-8')
> 
> bytes.decode('utf-8')
> ```

#### 字符串前加 f

> 表示在字符串内支持大括号内的python 表达式。

如：

```python
import time
t0 = time.time()
time.sleep(1)
name = 'processing'

*# 以 **f**开头表示在字符串内支持大括号内的python 表达式*
print(f'{name} done in {time.time() - t0:.2f} s') 
```

> **输出：**
>
> processing done in 1.00 s

### 3.9* 字符串的修改

> 字符串是不可修改的，但是严格来说，可以在任何位置修改字符串，只要通过 `bytearray()` 方法，但仅支持字符编码之多8位宽的文本，其他的字符依然是不可变的。bytearray 融合了不可变的字节字符串类型和可变别表的特性。

```python
b = bytearray(b"hedge")
b.extend(b"36")
b.decode()
```



## 4. 字典

### 4.1 映射

> 从键(key)到值(value)的一种映射。

### 4.2 定义

字典是键值对的集合，键值对之间无序，采用大括号{}或者dict()创建字典，可以通过索引获得索引对应的值，键值为不可变数据类型。

注:{}为空字典而不是空集合，空集合需要用set()建立。

创建字典:

> ==dict(zip(k,v)) 					   k,v分别为键与值对应列表，并以其对应元素创建字典==
>
> Fromkeys(list)			  	  将list中每个元素作为键，创建值为空(None)的字典

### 4.3 字典操作方法

> d[k]									键k存在则返回相应值，不在则返回异常；
>
> d[key]=x        			  	  修改或者添加键值key对应值x;
>
> d.get(k,\<default>)    	    键k存在则返回相应值，不在则返回\<defalut>；
>
> d.pop(k,\<default>)           键k存在则取出相应值，不在则返回\<defalut>值；
>
> d.popitem()       			   随机从字典d中取出一个键值对，并以元组形式返回被删除键值对；
>
> d.pop(a)       	 			   删除字典d中的键值对a，并返回被删除键对应的值；
>
> d.clear()        					清除字典中的所有键值对；
>
> **d.items()						  以元组类型返回所有键值对；**
>
> **d.keys()							返回所有键组成的列表**
>
> **d.vaules()						 返回所有值组成的列表**
>
> len(d)								返回键值对数量
>
> d.update(c)					   将新字典c中所有键值对添加到旧字典d对象上，且有重复自动覆盖

### 4.4 字典的特点

字典十分占内存，但其键查询速度很快，典型的空间换时间，其次，不要在遍历字典的同时修改字典(原因较复杂，暂时不做解析)

## 5. 集合 

### 5.1 定义

> 多个元素的无序组合，其底层是字典实现，所有元素都是字典的“键对象”，故不能重复，且python要求**集合中的元素是不可变数据类型**，如：整数，浮点数，元组类型，不包括列表。(注意空集也是集合)

**Tip：集合不支持索引操作，只能遍历打印！**

### 5.2 表示

> 集合用“{}”表示，元素用逗号分隔，用{}或者set()建立，如果建立空集合必须用set()，且集合顺序是无序的，不一定是最初的定义的顺序。
>

### 5.3 集合类方法

> frozenset(s)		  返回一个冻结的集合，冻结后的集合为不可变类型。
>
> set(ls)          	   使ls中的每一个字符单独拆分变成集合中的元素，且去掉重复元素；
>
> s.add(x)         	 如果x不在集合S中，将s增加到x；
>
> s.update(x)		  原地更新集合s与集合x的并集；
>
> s.discard(x)         若x在集合s中，则移除s中的元素x，否则无效但不报错；
>
> s.remove(x)        移除s中的元素x，如果x不在，则会返回keyerror异常；
>
> s.clear()         	 移除s中的所有元素；
>
> s.pop()          	 随机返回s的一个元素，并且会更新s，若本身s为空，返回keyerror异常；
>
> s.copy()        	 返回集合s的一个副本；
>
> len(s)          	   返回集合s的元素个数；
>
> x in /not in s     判断元素x是否在集合s中；

### 5.4 集合间的运算

>   s|t            	 	返回集合s和集合t的并集；
>
>   s-t            		返回集合s和集合t的差集；
>
>   s&t               	返回集合s和集合t的交集；
>
>   s^t               	返回集合s和集合t中的非相同元素；
>
>   s<=t,s<t....     判断集合s和集合t的包含关系；

### 5.5 常见应用

去除列表中的重复数据：

```python
ls = [] ;s = set(ls);ls = list(s)
```

 

## 6. 序列

### 6.1 定义

> 序列是有先后顺序的一组元素，元素可以相同，类型可以不同。

### 6.2 类型

> 字符串类型，元组类型，列表类型。

### 6.3 操作符语法

>   in/not in        		 判断函数变量是否包含于序列；
>
>   s+t      					连接两个序列s,t；
>
>   s*n           			   将序列s复制n次；
>
>   s[i]         				 索引，返回s中的第i个元素，i为序列的序号，包括正向，反向，										 不更新序列；
>
>   s[l:i:j:k]         		    切片
>
>   len,min,max(obj)     同上, obj可以为字符串，且可自定义最小值计算函数；
>
>   s.index(x[,i,j])     	  返回序列s从i开始到j位置中第一次出现元素x的位置
>
>   s.count(x)        		返回x的出现次数

#### 关于大小比较：

> 所有序列规定的比较操作都是基于字典顺序，即一个元素一个元素地比较，直至找出一个不同的元素进行大小判断为止。

#### 关于切片：

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

> 元组是一种**不可变的**list类型，一旦创建就不能更改，使用小括号()或者tuple()创建，元素用逗号分离，可省略括号，常用于数据保护，若元组中仅含一个元素，则必须后面加逗号。

zip(list1,list2,...)将多个列表对应位置元素组合成元组并返回这个zip对象；

大小排序只可使用sorted(tuple)返回列表再转化为元组，其他相关操作与序列一致，无特殊操作。

元组类型的访问和处理速度比列表快，且元组可作为字典的键值，而列表不可以。

### 6.5 列表类型

> 列表类型是一种序列类型，但是可以随意修改，使用方括号[]或者list()创建，元素间用逗号分离，类型可不同，无长度限制且无需在字面表达出来，列表相互嵌套以表示多维列表，多维列表可多次索引。

操作函数：

> list()			   		  将可转化类型（字符串、元组、迭代器）转换为列表
>
> ls[i]=x         		     替换列表ls第i个元素为x
>
> ls[i:j:k]         		     切片
>
> del ls[i[:j:k]]      	    删除切片对于ls
>
> ls.append(x)            在列表最后加入元素x
>
> **ls.insert(index,x)	在列表list指定位置list处插入元素x**
>
> ls.extend(alist)		 将列表alist所有元素加到列表ls尾部
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
> ls.sort([reverse=True])     将列表ls升(降)序排序（依据数字大小或首字母排序）且**无返回值**
>
> sorted(ls)      					将列表ls排序并**返回值**，亦可单独使用；
>
> s.replace(x,y)     				用y替换列表s中x元素

实例：

```python
b=[i for i in range(10) if i%2==0]
```

### **6.6 序列类型的打包与解包**

> (自动)**打包**是将多个变量打包成一个序列类型输出，序列**解包**则是将一个解析序列元素用于对多个变量同时赋值。自动打包与自动解包结合起来就是**同时分配**技术，即显示地将一系列的值赋给一系列标识符。在进行同时分配式，都是先计算右侧表达式，在赋值给左边。

#### a. 用于列表,元组：

```python
x, y, z = 1, 2, 3

[x, y, z] = [1, 2, 3]
```

#### b. 用于字典时，则是默认对键进行操作赋值，如：

```python
x, y = {1:a, 2:b}

x = 1, y = 2
```

如需对键值对操作，则需要使用函数dict.items()

如需对值操作，则需使用函数dict.values() 

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

> 注：0、空列表等空的容器或者None，也可以采用bool（foo）语法创造一个布尔类型(False)。



# 板块二 print输出格式化

## 输出格式美化

Python两种输出值的方式: 表达式语句和 print() 函数。

第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。

如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。

如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。

> - **str()：** 函数返回一个用户易读的表达形式。
>
> - **repr()：** 产生一个解释器易读的表达形式。
>
>   Click  [here](https://www.runoob.com/python3/python3-inputoutput.html)  to learn more.

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
>    %e 		指数 (基底写为e)·
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

| Operation symbol | Fuction                                                      |
| ---------------- | ------------------------------------------------------------ |
| name             | 填充对象或参数的标识符                                       |
| flag             | 格式符，用于设置对齐格式，其后可跟填充符，如："+0"<br />"+"表示右对齐。"-"表示左对齐，" "为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐，"0"表示使用0填充，不设置填充符时默认使用空格填充。 |
| width            | 显示宽度，不足时使用填充符填充，值得注意的是，小数点算一个字符 |
| precision        | 小数显示精度                                                 |

```python
>>>"%+10x" % 10
>>>'        +a'
>>>"%04d" % 5
>>>'0005'
>>>"Name:%10s Age:%8d Height:%8.2f" % ("Aviad", 25, 1.83)
>>>'Name:     Aviad Age:      25 Height:    1.83'
>>>"I'm %(c)s. I have %(l)d yuan."% {'c':'hungry','l':22}
>>>" I'm hungry. I have 22 yuan."
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

> **显示方式:** 0（默认值）、1（高亮，即加粗）、4（下划线）、7（反显）、  
>
> **前景色:** 30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（梅色）、36（青色）、37（白色）  
>
> **背景色:** 40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（梅色）、46（青色）、47（白色）

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

   

# 板块三 程序结构与异常处理

## 1. 基本原理

> 根据判断条件结果而选择不同向前路径的运动方式。

Python支持条件表达式的语法，可以取代一个简单的控制结构。一般的语法表达式语法形式如下：

> expr1 if condition else expr2

## 2. 基本条件组合

### 2.1 逻辑运算符

> **逻辑非not、逻辑与and、逻辑或or**（条件判断存在先后顺序）
>
> 其中and和or运算符是短路保护，即指如果结果可以通过第一个操作符的值来确定，便不会对第二个操作数进行运算。

### 2.2 相等运算符

> **is、==、!=**
>
> is 用于判断两个变量引用对象是否为同一个，即比较对象的标识；
>
> ==用于判断两个变量的值是否相同。

见下：

a=1000,b=1000

a==b但是a is not b(id不同)

但是对于整数[-5,256]**（小整数池）**，python控制台会进行缓存，此时a，b的地址是相同的，而对于[-5,ꝏ]在文件中打开都会进行缓存。此外，is 比 == 的运行效率要高。

**附：**

> 赋值符不可以出现在条件句中。

## 3. 异常处理

```python
try:

	block to run

except [error_type] [as e]:（可使用多个except定向处理不同的异常类型）

 	block to run if error

[else:

	block to run if without error

   如果不发生异常，执行语句三；]

[finally:

	block to run no matter if error occur]
```

Tip：一般情况下，不要将return语句放在try, except, else, finally块中，而是在板块的最后，否则会发生意想不到的错误。

### 1.常见异常错误

| Error type          | Error reason                               |
| ------------------- | ------------------------------------------ |
| AssertionError      | assert语句失败                             |
| AttributeError      | 属性赋值或引用失败                         |
| EOFError            | 用户输入文件到达末尾                       |
| FloatingPointError  | 浮点计算错误                               |
| GeneratorExit       | generator.close()方法被调用                |
| ImportError         | 导入模块失败                               |
| IndexError          | 索引超出序列的范围                         |
| MemoryError         | 内存溢出                                   |
| NotImplementedError | 尚未实现的方法                             |
| OSError             | 操作系统产生的异常                         |
| ReferenceError      | 试图访问一个已经被垃圾回收机制回收了的对象 |
| RuntimeError        | 一般的运行时错误                           |
| StopIteration       | 迭代器没有更多的值                         |
| SyntaxError         | 语法错误                                   |
| IndentationError    | 缩进错误                                   |
| TabError            | Tab和空格混合使用                          |
| TypeError           | 不同类型间的无效操作                       |
| ValueError          | 传入无效的参数                             |

### 2.with上下文管理

基本语法结构：

```python
with context_expr[as var]:

	block
```

with上下文管理可以自动管理资源，在with代码块执行完毕后自动还原进入该代码之前的现场或者上下文。无论何种原因跳出with块，无论是否有异常，总能保证资源正常释放，极大的简化了工作，在文本操作，网络同学向该年度场合非常常用。

### 3.traceback异常模块

```python
import traceback

traceback.print_exc([file=''])
```

打印详细异常现象

### 4.自定义异常类

> 可通过class定义一异常类，并通过raise抛出异常。
>



## 4. 程序的循环结构

### 4.1 遍历循环

基本语法：

```python
for item in items:

block              
```

遍历结构有：

> for i in range(m,n,k):     	计数遍历循环，k可以取负值
>
> for c in s:          				 字符串s遍历循环(取出每一个字符串循环)
>
> for item in ls:       			  列表ls遍历循环（ls=[]）
>
> for line in file:        			遍历文件file的每一行，file为文件标识符

特别地，字典的遍历：

> for i in d(d.keys()):				遍历字典d中的所有key
>
> for i in d.vaules():				 遍历字典d中的所有value
>
> for i in d.items():				   遍历字典d中的所有键值对

可迭代对象包括：序列，字典，迭代器对象(range)，生成器对象。

### 4.2 无限循环

> while condition:
>
> ​	block

反复执行语句块，直至条件不满足为止；(ctrl+c可以强制结束程序)

### 4.3 循环控制保留字

> break           	   跳出并结束当前整个(最内层)循环，执行循环后的语句；
>
> continue         	只结束当次循环，继续执行后续次数的循环

### 4.4 循环的高级用法

  循环与else，else语句作为正常完成循环(即未被break中断)的奖励

### 4.5 循环代码优化

优化代码遵循下列三个原则：

> (1)尽量减少循环内部不必要的计算
>
> (2)嵌套循环中，尽量减少内部循环的计算，尽可能向外提
>
> (3)局部变量查询较快，尽量使用局部变量。

其他方法：

> (1)连接多个字符串用join而不是+；
>
> (2)列表进行元素插入和删除时，尽量在列表尾部操作；

原因参考板块七数据结构中数组表示原理。



# 板块四 函数的定义及调用

## 1. 函数的结构

> **def** tag (arguments : type) -> type hint:	# flag of fuction
>
> ​	*"""Annotion of Fuction, can inquire and print by `help`, according to PEP8"""*
>
> ​     Expressions
>
> ​     **return** values

**函数**是就是将一个函数名变量(栈)绑定到一个函数**对象**(function)(形如字符串)，有特定的id，因而这个函数对象(堆)可以多次赋值到别的函数名变量中。参数类型包括两种，可有可无，可以通过*":"type*对参数类型进行说明(任意字符串)，但对参数无实际限制，函数外亦可使用，*-> type hint*则表示为对输入输出的类型提示，*必须是准确的现存的数据类型*，作用同type，没有实际限制力。

return可以返回需要的数据作为函数输出值，不设置返回值时默认返回None，当返回多个数值时，将自动打包返回元组类型。

**通过help(函数名)，可以查询函数或者模块的批注。**

## 2. 函数参数

函数定义往往需要用到参数，参数列表包括可变参数，可以没有(保留括号)，也可以是多个。

### 2.1 参数形式

> 参数形式包括**形式参数**与**实际参数**，形式参数即定义函数时用于描述预期参数的标识符，形参命名只要符合"标识符"命名规则即可，而在调用过程中传递的参数为实际参数，简称"实参"。

### 2.2 参数传递

参数传递即从实参到形参的赋值，包括两种方式：位置传递，名称传递。传递不可变对象(int,float,元组等)使用的是浅拷贝。

附：参数传递copy栈堆的内存分析

(copy模块需额外引入)

> **浅拷贝copy():**
>
> > 不拷贝子对象的内容，只拷贝对象的引用，即直接引用源对象的引用，对此引用改变时会改变源对象。
> 
>**深拷贝deepcopy():**
> 
>> 拷贝子对象的全部内容，包括子对象的引用，此时修改子对象不改变源对象。 

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

`*params`意为将多个参数收集到一个"元组"对象当中。

`**params`意为将多个参数收集到一个"字典"对象当中。

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

> 变量分为两类，局部变量和全局变量，局部变量为组合数据类型且未创建时，等同于全局变量，函数内部变量未经声明则为局部变量，若使用global声明则为全局变量；
>
> 全局变量降低了函数的通用性和可读性，应避免全局变量的使用。局部变量只作用在定义与结束之间的模块，调用比全局变量快*(提高效率应考虑将全局变量更换为局部变量)*，应优先考虑使用。如果局部变量与全局变量同名，则在函数内隐藏全局变量，只使用同名的局部变量。
>

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

>  如：x=y=2
>

#### 3.2.2 系列解包赋值：

 如：a,b,c=4,5,6相当于各自赋值，非元组类型

>  可用于变量值的互换，如：a, b = b, a
>

*Tip：变量名称不可与函数名相同，否则<u>**多次调用**</u>时会出现歧义报错。*

### 3.3 变量的删除

>  使用del函数删除不再使用的变量，此时如果对象没有被引用，则会被垃圾回收器回收，清理内存空间。
>

### 3.4 常量

>  python不支持常量，即没有语法规则限制改变一个常量的值，只能通过逻辑上不做修改。
>

## 附注： 私有属性函数

### 附注1 概况

> 下划线对解释器有特殊的意义，而且是内建标识符所使用的符号，因此我们对于普通的变量，需要避免用下划线作为变量名的开始。一般来讲，变量名\_xx被看作是“私有的”，在模块或类外不可以使用。当变量是私有的时候，用_xxx 来表示变量是很好的习惯。

**“单下划线” 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；**

**“双下划线” 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。**

### 附注2 保留属性：

| Attributes | Description |
|---|---|
|Class.\__doc__ | 类型帮助信息  |
|Class.\__name__ | 类型名称 |
|Class.\_\_module\__ | 类型所在模块 '\__main__' |
|Class.\__bases__ |类型所继承的基类 |
|Class.\__dict__| 类型字典，存储所有类型成员信息 |
|Class().\_\_class__| 类型 <class '\__main__.Class'> |
|Class().\_\_module__ |实例类型所在模块 '\_\_main__'|
|Class().\__dict__ |对象字典，存储所有实例成员信息|

### 附注3 保留方法:

可以把保留方法分类：

对\__init\_\_() 方法的调用发生在实例被创建之后 。如果要控制实际创建进程，请使用 \_\_new__() 方法。

按照约定， \_\_repr\_\_() 方法所返回的字符串为合法的 Python 表达式。

在调用 print(x) 的同时也调用了 \_\_str__() 方法。

### 附注4 行为方式与迭代器类似的类 

无论何时创建迭代器都将调用 \_\_iter\_\_() 方法。这是用初始值对迭代器进行初始化的绝佳之处。无论何时从迭代器中获取下一个值都将调用 \__next__() 方法。\_\_reversed\_\_() 方法并不常用。它以一个现有序列为参数，并将该序列中所有元素从尾到头以逆序排列生成一个新的迭代器。

### 附注5 计算属性 

如果某个类定义了 __getattribute__() 方法，在 每次引用属性或方法名称时 Python 都调用它（特殊方法名称除外，因为那样将会导致讨厌的无限循环）。

如果某个类定义了 __getattr__() 方法，Python 将只在正常的位置查询属性时才会调用它。如果实例 x 定义了属性color， x.color 将 不会 调用x.__getattr__('color')；而只会返回x.color 已定义好的值。

无论何时给属性赋值，都会调用 __setattr__() 方法。

无论何时删除一个属性，都将调用 __delattr__() 方法。

如果定义了 __getattr__() 或 __getattribute__() 方法， __dir__() 方法将非常有用。通常，调用 dir(x) 将只显示正常的属性和方法。如果__getattr()__方法动态处理color 属性， dir(x) 将不会将 color 列为可用属性。可通过覆盖 __dir__() 方法允许将 color 列为可用属性，对于想使用你的类但却不想深入其内部的人来说，该方法非常有益。 

### 附注6 可比较的类

我将此内容从前一节中拿出来使其单独成节，是因为“比较”操作并不局限于数字。许多数据类型都可以进行比较——字符串、列表，甚至字典。如果要创建自己的类，且对象之间的比较有意义，可以使用下面的特殊方法来实现比较。 

### 附注7 可序列化的类

Python 支持 任意对象的序列化和反序列化。（多数 Python 参考资料称该过程为 “pickling” 和 “unpickling”）。该技术对与将状态保存为文件并在稍后恢复它非常有意义。所有的 内置数据类型 均已支持 pickling 。如果创建了自定义类，且希望它能够 pickle，阅读 pickle 协议 了解下列特殊方法何时以及如何被调用 

要重建序列化对象，Python 需要创建一个和被序列化的对象看起来一样的新对象，然后设置新对象的所有属性。__getnewargs__() 方法控制新对象的创建过程，而 __setstate__() 方法控制属性值的还原方式。

### 附注8 可在 with 语块中使用的类

with 语块定义了 运行时刻上下文环境；在执行 with 语句时将“进入”该上下文环境，而执行该语块中的最后一条语句将“退出”该上下文环境。 

该文件对象同时定义了一个 __enter__() 和一个 __exit__() 方法。该 __enter__() 方法检查文件是否处于打开状态；如果没有， _checkClosed()方法引发一个例外。

__enter__() 方法将始终返回 self —— 这是 with 语块将用于调用属性和方法的对象

在 with 语块结束后，文件对象将自动关闭。怎么做到的？在 __exit__() 方法中调用了 self.close() .

### 附注9 真正神奇的东西

 如果知道自己在干什么，你几乎可以完全控制类是如何比较的、属性如何定义，以及类的子类是何种类型。 

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

x.\__dictoffset__ attribute tells you the offset to where you find the pointer to the __dict__ object in any instance object that has one. It is in bytes.

x.\__flags__, 返回一串数字，用来判断该类型能否被序列化（if it's a heap type), __flags__ & 512

S.__format__, 有些类有用

x.__getitem__(y) == x[y], 相应还有__setitem__, 某些不可修改类型如set，str没有__setitem__

x.__getslice__(i, j) == x[i:j], 有个疑问，x='123456789', x[::2],是咋实现得

x.\__subclasscheck__(), check if a class is subclass

x.\__instancecheck__(), check if an object is an instance

x.\__itemsize__, These fields allow calculating the size in bytes of instances of the type. 0是可变长度， 非0则是固定长度

x.__mod__(y) == x%y, x.__rmod__(y) == y%x

x.__module__ , x所属模块

x.__mul__(y) == xy,  x.__rmul__(y) == yx

x.\__reduce__, __reduce_ex__ , for pickle

x.\__slots__ 使用之后类变成静态一样，没有了__dict__, 实例也不可新添加属性

x.\__getattr__ 在一般的查找属性查找不到之后会调用此函数

x.\__setattr__ 取代一般的赋值操作，如果有此函数会调用此函数， 如想调用正常赋值途径用 object.__setattr__(self, name, value)

x.\__delattr__ 同__setattr__, 在del obj.name有意义时会调用

## 4. lambda函数

  lambda函数是一种匿名函数，没有名称，使用lambda保留字定义，只允许有一个表达式并且该表达式计算所得结果即为函数返回值。常用于定义**简单的能在一行内表示的**函数；

>    lambda *Params* : *expression*
>

比如：

```python
f = [lambda x,y: x+y, lambda x,y: x*y]
print(f[1](1,2))
```

注：函数定义后需调用



## 5. 嵌套函数与组合函数

嵌套函数，在函数内部定义的函数，嵌套函数的定义及调用都只能在函数内部使用。常用于数据的封装(即数据隐藏，使得外部无法访问)，贯彻DRY(Don't repeat yourself)原则以及闭包。

```python
def f1():
	print("hello,world")
	def f2():
		print("byebye ,world")
```

> 组合函数与嵌套函数相似，但是区别在于嵌套的函数全局定义，这种情况下无法实现函数的封装，通过相互调用实现嵌套，实际应用比较广泛，同时较简单，不展开叙述。



## 6. 函数装饰器

### 概述

> **装饰器**(Decorators)是 Python 的一个重要部分，其**本质是**，在函数调用的同时，动态地修改目标函数的功能的**函数**。他们有助于让我们的代码更简短，也更Pythonic（Python范儿），其基本语法如下:

```python
def func1():
  block

@func1
def func2():
  block
```

以下是其基本的使用场景：

### 授权(Authorization)

> 装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。它们被大量使用于Flask和Django web框架中。
>

```python
from functools import wraps  

def requires_auth(f):    
	@wraps(f)    
	def decorated(*args, **kwargs):        
    auth = request.authorization        
    if not auth or not check_auth(auth.username, auth.password):            authenticate()        
    return f(*args, **kwargs)    
  return decorated
```



### 日志(Logging)

> 日志是装饰器运用的另一个亮点。
>

```python
from functools import wraps  

def logit(func):    
  @wraps(func)    
  def with_logging(*args, **kwargs):        
    print(func.__name__ + " was called")        
    return func(*args, **kwargs)    
  return with_logging  

@logit 
def addition_func(x):   
  """Do some math."""   
  return x + x   


result = addition_func(4) 
# Output: addition_func was called
```

------

### 带参数的装饰器

我们回到日志的例子，并创建一个包裹函数，能让我们指定一个用于输出的日志文件。

```python
from functools import wraps  

def logit(logfile='out.log'):    
  def logging_decorator(func):        
    @wraps(func)        
    def wrapped_function(*args, **kwargs):            
      log_string = func.__name__ + " was called"            
      print(log_string)            
      # 打开logfile，并写入内容
      with open(logfile, 'a') as opened_file:                
        # 现在将日志打到指定的logfile                
        opened_file.write(log_string + '\n')            
      return func(*args, **kwargs)        
    return wrapped_function    
  return logging_decorator  

@logit() 
def myfunc1():    
  pass  

myfunc1() 
# Output: myfunc1 was called 
# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串  

@logit(logfile='func2.log') 
def myfunc2():    
  pass  

myfunc2() 
# Output: myfunc2 was called 
# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串
```



------

### 装饰器类

现在我们有了能用于正式环境的logit装饰器，但当我们的应用的某些部分还比较脆弱时，异常也许是需要更紧急关注的事情。比方说有时你只想打日志到一个文件。而有时你想把引起你注意的问题发送到一个email，同时也保留日志，留个记录。这是一个使用继承的场景，但目前为止我们只看到过用来构建装饰器的函数。

幸运的是，类也可以用来构建装饰器。那我们现在以一个类而不是一个函数的方式，来重新构建logit。

```python
from functools import wraps 

class logit(object): 
  def __init__(self, logfile='out.log'):        
    self.logfile = logfile 
  def __call__(self, func):        
    @ wraps(func) 
    def wrapped_function(*args, **kwargs):            
      log_string = func.__name__ + " was called" 					
      print(log_string)
			# 打开logfile并写入
      with open(self.logfile, 'a') as opened_file:
      # 现在将日志打到指定的文件
      	opened_file.write(log_string + '\n')
       	# 现在，发送一个通知
      	self.notify()
        return func(*args, **kwargs)
      return wrapped_function
    
    def notify(self):
        # logit只打日志，不做别的
        pass
```

这个实现有一个附加优势，在于比嵌套函数的方式更加整洁，而且包裹一个函数还是使用跟以前一样的语法：

```python
@logit()
def myfunc1():
    pass
```

现在，我们给 logit 创建子类，来添加 email 的功能(虽然 email 这个话题不会在这里展开)。

```python
class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

		def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass
```



## 7. 偏函数

Python的`functools`模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。

在介绍函数参数的时候，我们讲到，**通过设定参数的默认值，可以降低函数调用的难度。**而偏函数也可以做到这一点，这里其实有点像函数重定义，具体用法见下：

```python
import functools
func1 = functools.partial(func2, params=params)
```

当然，也可以通过以下方式实现：

```python
def func2(params=params):
  func1(params=params)
```



## 8. 常用内置函数

### eval函数

将字符串str当作有效的表达式来求值并**返回结果**，一般语法表达式如下：

```python
eval(source[,globals[,locals]]) -->value
```

参数：

> source			 一个python表达式或者函数compile()返回的代码对象
>
> globals			可选，必选是dictionary
>
> locals			   可选，任意的映射对象

```python
dict = {a = 100, b = 10}
eval("a+b",dict)
```

---

### exec函数

```python
exec(object [,  globals [,  locals]])
```

这个函数支持动态执行 Python 代码。 *object* 必须是字符串或者代码对象。 如果是字符串，那么该字符串将被解析为一系列 Python 语句并执行（除非发生语法错误）。如果是代码对象，它将被直接执行。 在任何情况下，被执行的代码都应当是有效的文件输入（见参考手册中的“文件输入”一节）。 请注意即使在传递给 `exec()` 函数的代码的上下文中，`nonlocal`, `yield` 和 `return` 语句也不能在函数定义以外使用。 该函数的返回值是 `None`。

无论哪种情况，如果省略了可选项，代码将在**当前作用域**内执行。 如果只提供了 *globals*，则它必须是一个字典（不能是字典的子类），该字典将同时被用于全局和局部变量。 如果同时提供了 *globals* 和 *locals*，它们会分别被用于全局和局部变量。 如果提供了 *locals*，则它可以是任何映射对象。 请记住在模块层级上，globals 和 locals 是同一个字典。 如果 exec 得到两个单独对象作为 *globals* 和 *locals*，则代码将如同嵌入类定义的情况一样执行。

如果 *globals* 字典不包含 `__builtins__` 键值，则将为该键插入对内建 `builtins` 模块字典的引用。因此，在将执行的代码传递给`exec()` 之前，可以通过将自己的 `__builtins__` 字典插入到 *globals* 中来控制可以使用哪些内置代码。

引发一个 审计事件 `exec` 附带参数 `code_object`。

**注解**

内置 `globals()` 和 `locals()` 函数各自返回当前的全局和本地字典，因此可以将它们传递给 `exec()` 的第二个和第三个实参。

默认情况下，*locals* 的行为如下面 `locals()` 函数描述的一样：不要试图改变默认的 *locals* 字典。如果您想在 `exec()` 函数返回时知道代码对 *locals* 的变动，请明确地传递 *locals* 字典。

```python
def name():
	record = [1, 2]
    for i in range(2):
		exec('A{} = record[{}]'.format(i + 1, i))
name()
print(A1)  
```

[ OUTPUT]: NameError: name 'A1' is not defined

```python
def name():
	record = [1, 2]
    for i in range(2):
		exec('A{} = record[{}]'.format(i + 1, i)， globals())
name()
print(A1)  
```

[ OUTPUT ]: 1

```python
record = [1, 2]
for i in range(2):
	exec('A{} = record[{}]'.format(i + 1, i))
print(A1) 
```

[ OUTPUT ]:  1

---

### compile函数

> compile() 函数将一个字符串编译为字节代码，以下是 compile方法的一般表达语法:

```python
compile(source, filename, mode[, flags[, dont_inherit]])
```

#### Params

> - source -- 字符串或者AST（Abstract Syntax Trees）对象。。
> - filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
> - mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
> - flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
> - flags和dont_inherit是用来控制编译源码时的标志

#### Return

> 返回表达式执行结果。

#### Instance

以下展示了使用 compile 函数的实例：

```python
>>>str = "for i in range(0,10): print(i)"  

c = compile(str,'','exec')   # 编译为字节代码对象  

c <code object <module> at 0x10141e0b0, file "", line 1> 

exec(c) 0 1 2 3 4 5 6 7 8 9 

str = "3 * 4 + 5" 

a = compile(str,'','eval') 

eval(a) 17
```

---

### assert函数

assert声明函数，对条件进行检查声明，若声明为True则无返回值，若声明为False，返回AssertionError，其一般语法表达式为：

```python
assert(expression, [arguments ])
```

> 注：该函数必须顶行单独使用

---

### map函数

#### Description

> **map函数**会根据提供的函数对指定序列做映射。
>
> 第一个参数 function 以参数序列中的每一个元素调用 function 函数，**返回**包含每次 function 函数返回值的**迭代器**，其一般表达语法为：

```python
map(function, iterable, ...)
```

#### Params

> - function -- 函数
> - iterable -- 一个或多个序列

---

### enumerate函数

#### Description

> enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。其一般语法表达式为:

```python
enumerate(sequence, [start=0])
```

#### Params

> - sequence -- 可迭代对象。
> - start -- 下标起始位置。

#### Return

返回 enumerate(枚举) 对象。



# 板块五 文件的读取与操作

## 1. 文件类型

本质上，所有文件都是二进制文件，但展示形式包括二进制文件及文本文件。

## 2. 文件的打开与关闭

### 2.1 概述

文件需要从存储状态转变为占用状态才可唯一地排他地进行操作，其基本语法：

文件句柄.<函数名>

```python
open(filename, open_mode, encoding='UTF-8')
```

**注意：对于带有BOM的txt文本，解码方式应该选择UTF-8-sig**

文件路径表示：

> 绝对路径(反斜杠换位斜杠/或只读表示)
>
> 相对路径（源文件同目录可省略，使用"."，单一目录无需"."，上级目录使用".."）

Tip：在powershell中带有空格的路径，路径需要用英文双引号括起来。

### 2.2 打开模式  

读写模式：

> "r"，只读模式，默认值，如果文件不存在，返回FileNoFoundError;
>
> "w"，覆盖写模式，文件不存在则创建，存在则完全覆盖；
>
> "x"，创建写模式，文件不存在则创建，存在则返回FileExistsError(文本的创建另存为);
>
>  "a"，追加写模式，文件不存在则创建，存在则在文件最后追加内容；

展示模式：

> "b"，二进制文本类型；
>
> "t"，文本文件模式，默认值；
>
> "+"，与w/x/a同时使用，在原基础上增加读功能。

close()   	关闭文件，且python关闭后自动关闭(最好自己打上，减少运行内存占用)

**Note：**

> 在windows平台下使用python内置函数 open() 时发现，当不传递encoding参数时，会自动采用gbk(cp936)编码打开文件，而当下**很大部分**文件的编码都是**UTF-8**，部分加密为**UTF-8-sig**（带有BOM加密文件）。
>
> 我们当然可以通过每次手动传参encoding='utf-8'，但是略显冗余，而且有很多外国的第三方包，里面调用的内置open()函数并没有提供接口让我们指定encoding，这就会导致这些包在windows平台上使用时，常会出现如 "UnicodeDecodeError:'gbk' codec can't decode byte 0x91 in position 209: illegal multibyte sequence" 的报错。

遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

```python
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
```

读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。python文件读写,以后就用with open语句。

读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。

最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的。

由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现。

但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

```python
with open('/path/to/file', 'r') as f:

	print(f.read())
```

这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

## 3. 文件内容的读取

格式：<变量名称>.<函数名称>

> read([size])      		读入全部内容，如果给出参数，则读入前size个字节；     
>
> readline([size])    	读入一行内容，如果给出参数，则读入前size个字节；  
>
> readlines([hint])   	读入所有行内容，以每行为元素形成列表，如果给出参数，则读入前hint行。
>

## 4. 全文本操作

> a. 一次读入一次处理；
>
> b. 分次读入一次处理，每次读取n行，读取完毕后关闭再次读取n行，节省内存。
>
> c. 一次读入逐行处理；
>
> d. 分行读入逐行处理；

 

## 5. 文件对象方法总览        						

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

**注：文件的操作无任何输出值**，关于字节计算，一个字母1个字节，一个汉字3个字节。

### **附注：关于\_\_name__**

> 首先需要了解 \_\_name__ 是属于 python内置类属性，在一个 python 程序中，代表对应程序名称。当一段程序作为主线运行程序时其内置名称就是 \_\_main__，使用if条件判断对该属性进行检查可以防止在被其他文件调用时语句块被调用。
>



## 6. 文件的操作

### 6.1 文件调用

#### (1)工作目录下

> 工作目录下可以直接使用import导入，随后直接调用对应的属性和方法。

#### (2)非工作目录下

> 在非工作目录下，需要先调用sys库，将目标文件路径添加到解释器路径中，方可正常使用import调用。

```python
import sys

sys.path.append('path')

import file
```

*Tip:文件路径及名称中尽量不要出现空格，否则无法直接引用，但是可以引用如下：*

```python
symbol= __import__("filepath")
```

### 6.2 文本复制

> copyFile(source_path, target_path)
>

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

类可以通过`__init__(self, 参数)`来给初始化创建好的实例对象设置实例属性。

类是实例的蓝图，每个实例通过属性（又称为域）来确定其状态信息。，且在Python中，不同于其他语言，Python没有方法的重载，即不能通过参数的不同辨别同名方法，后定义的方法和覆盖先定义的方法，只有最后一个方法有效，且不会报错。方法也是对象，在python中方法具有动态性，可以再定义及修改。

在类中调用实例属性及方法的语法如下：

> object.attribute
>
> object.methods(params)

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

如果需要在类外修改`类属性`，必须通过`类对象`去引用然后进行修改。如果通过实例对象去引用，会产生一个同名的`实例属性`，这种方式修改的是`实例属性`，不会影响到`类属性`，并且之后如果通过实例对象去引用该名称的属性，实例属性会强制屏蔽掉类属性，即引用的是`实例属性`，除非删除了该`实例属性`。

###  3.3 实例方法

实例方法或者叫对象方法，又称为成员函数，指的是我们在类中定义的普通方法。
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

和函数一样，代码遇到return下面就不在执行，会将值返回给调用处。

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

### (1)给对象绑定方法

实例

```python
from types import MethodType

def func(self):
    
	print('func')
    
from types import MethodType

a = A()

#a.func = MethodType(方法名,对象名)

a.func = MethodType(func,a)
```

### (2) 给类绑定方法

实例

```python
def func(self):

	print('func')#类名.属性名 = 函数名

A.func = func
```

注意:

> 1.构造方法第一个参数必须为self
>
> 2.给对象绑定属性或者方法只有当前对象有给类绑定属性或者方法所有当前类的实例化的对象都会拥有。

## 7. slots限制对象

动态添加属性

只能创建\__slots__允许的属性，否则会报 AttributeError: ‘A’ object has no attribute ‘xxx’

实例:

class A:

\__slots__ = ('属性1'，'属性2'...)

 

## 8. 私有属性和私有方法

### 8.1 类的私有属性:

> 以下划线开头的变量不能在类的外部进行直接使用和访问，单下划线表示变量是受保护的，而双下划线表示变量是私有的。

#### 私有属性的访问

在类的外部：*对象._类名__(前1个后2个，这也是私有属性的存储方式，可查询)*属性名查找

在类的内部：方法里面的变量self.__属性名调用

注意：在类的内部只要使用self.\_\_属性名那么就会去找私有属性_类名___属性名

### 8.2 类的私有方法

以\_\_作为开头，不能在类的外部进行使用和访问，在类的里面使用self.__方法名。在公有方法里面通过self去调用，方法本质上也是属性。



## 9. 继承

面向对象编程带来最大的好处就代码的重用，实现代码重用的操作就是类的继承，被继承的类称之为**父类或者基类**，超类继承的类称之为**子类**。

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

> 类的单一继承子类会继承父类的全部属性及方法，但是只能直接调用**私有以外**的属性和方法；
>
> 如果在子类里存在和父类同名的属性或者方法叫做方法或属性的**重写**（也就是会覆盖掉）再次调用的时候调用的是子类的方法和属性；

**在子类里调用父类的方法：**

> 父类名.方法名(self[,参数…])，self代表当前类的实例化的对象；或者使用super()（获得父类的定义）.方法名
>
> super(当前类名,self).方法名（如果是单一继承super方法不建议加参数）
>
> **super().方法名(建议)**

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

### **1. 组合的定义**

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

## 10. 运算重载

### 10.1 构造函数

类可以通过构造函数来实现实例化

```python
	class Number:
    	# 构造函数
    	def __init__(self, value):
        	self.data = value
          
    a = Number(5)
```

### 10.2 常见运算符重载方法

| method                                                       | overload           | call                                                         |
| ------------------------------------------------------------ | ------------------ | ------------------------------------------------------------ |
| \__del__                                                     | 析构函数           | X对象收回                                                    |
| \__add__                                                     | 云算法+            | 如果没有_iadd_， X+Y， X+=Y                                  |
| \__or__                                                      | 运算符\|           | 如果没有_ior_，X\|Y, X\|=Y                                   |
| \_repr\_\_, \__str__                                         | 打印，转换         | print(X)，repr(X)，str(X)                                    |
| \__call__                                                    | 函数调用           | X(*args, **kwargs)                                           |
| \__getattr__                                                 | 点号运算           | X.undefined                                                  |
| \__setattr__                                                 | 属性赋值语句       | X.any=value                                                  |
| \__delattr__                                                 | 属性删除           | del X.any                                                    |
| \__getattribute__                                            | 属性获取           | X.any                                                        |
| \__getitem__                                                 | 索引运算           | X[key]，X[i:j]                                               |
| \__setitem__                                                 | 索引赋值语句       | X[key]，X[i:j]=sequence                                      |
| \__delitem__                                                 | 索引和分片删除     | del X[key]，del X[i:j]                                       |
| \__len__                                                     | 长度               | len(X)，如果没有\__bool__，真值测试                          |
| \__bool__                                                    | 布尔测试           | bool(X)                                                      |
| \__lt\_\_, _\_gt\_\_, _\_le\_\_, \_\_ge\_\_, \_\_eq\_\_, \_\_ne__ | 特定的比较         | X<Y，X>Y，X<=Y，X>=Y， X==Y，X!=Y 注释：（lt: less than, gt: greater than,  le: less equal, ge: greater equal,  eq: equal, ne: not equal ） |
| \__radd__                                                    | 右侧加法           | other+X                                                      |
| \__iadd__                                                    | 实地（增强的）加法 | X+=Y(or else \__add__)                                       |
| \_\_iter_\_, _\_next__                                       | 迭代环境           | I=iter(X), next()                                            |
| _\_contains__                                                | 成员关系测试       | item in X(任何可迭代)                                        |
| \__index__                                                   | 整数值             | hex(X), bin(X), oct(X)                                       |
| \_\_enter_\_, _\_exit__                                      | 环境管理器         | with obj as var:                                             |
| \_\_get\__, \__set\__, \_\_delete__                          | 描述符属性         | X.attr, X.attr=value, del X.attr                             |
| _\_new__                                                     | 创建               | 在\__init__之前创建对象                                      |

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

> __doc__ 									类的说明
>
> __name__								 返回类名
>
> __base__ 								 返回类的一个父类
>
> __bases__ 								返回类的多个父类
>
> __dict__ 								   返回对象或者类的字典属性
>
> __mor__或者mro()				   查看类的继承层次结构
>
> __str__									  用于重写obj对象描述信息，输出返回值(必须为str类型)，默认为													obj的对象信息
>
> __repr__								   转换成解释器查看的形式
>
> __add__ 								  运算符重载
>
> __getattr__ 							 调用不存在的属性的时候触发
>
> __len__									 即函数len()
>
> __getitem__
>
> __setitem__
>
> dir(obj)								获取对象所有的属性
>
> pass									 空语句
>
> isinstance(对象，类)			判断对象是否是指定类的实例对象
>
> __call__									 定义后使得对象可以像函数一样使用类名()来调用

 

## 12. 设计模式

### 12.1 工厂方法模式

#### 前言

>
> 但是在实际过程中还有一种工厂模式经常被使用，那就是 **简单工厂模式（Simple Factory）**。有一种常见的分类的方法：根据产品是由具体产品还是具体工厂可以分为 **工厂方法模式** 和 **简单工厂模式**；根据工厂的抽象程度可以分为 **工厂方法模式** 和 **抽象工厂模式**。接下来会通过例子对比简单工厂模式和工厂方法模式。

#### 工厂意图

>
> 定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method 使一个类的实例化延迟到其子类。

#### 别名


虚构造器（Virtual Constructor）

#### 案例

#### 第一阶段

> 小李开了一个代工厂，专门帮各大厂商生产手机，一开始只有小米找他生产小米手机(MiPhone)，后来质量过硬，声名远播，苹果公司也找上门了，准备让他生产苹果手机，生意来了，小李小手一挥，停工几个月，加了一个生产线专门生成苹果手机(Iphone)。于是乎，现在一个工厂有两个生产线。

#### 第一阶段 UML 图

让我们借助 UML 图直观了解一下工厂现在的样子。
<img src="https://cdn.nlark.com/yuque/__puml/83ce437ce8df7956994e7bb6a64f4a30.svg#lake_card_v2=eyJjb2RlIjoiQHN0YXJ0dW1sXG5jbGFzcyDlt6XljoIge1xuXHQr55Sf5Lqn5bCP57Gz5omL5py6KCk65omL5py6IC4uPiDlsI_nsbPmiYvmnLpcblx0K-eUn-S6p-iLueaenOaJi-acuigpOuaJi-acuiAuLj4g6Iu55p6c5omL5py6XG59XG5DbGllbnQgLS0g5bel5Y6CXG7miYvmnLogLS0gIENsaWVudFxu5bCP57Gz5omL5py6IC0tPiDmiYvmnLpcbuiLueaenOaJi-acuiAtLT4g5omL5py6XG5AZW5kdW1sIiwidHlwZSI6InB1bWwiLCJtYXJnaW4iOnRydWUsImlkIjoiWU9xUXYiLCJ1cmwiOiJodHRwczovL2Nkbi5ubGFyay5jb20veXVxdWUvX19wdW1sLzgzY2U0MzdjZThkZjc5NTY5OTRlN2JiNmE2NGY0YTMwLnN2ZyIsImNhcmQiOiJkaWFncmFtIn0=" alt="img" style="zoom:25%;" />

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

# 板块七 Somethingelse

> **数据结构**是组织和访问数据的一种系统化方式，**算法**是在有限的时间内一步步执行某些任务的过程。为了分辨好的算法和数据结构，我们通过对其**运行时间**和**空间内存的占用**来分析。
>
> 运行时间更准的测度方法是算法所使用的CPU周期的数量，即使用相同的输入重复相同的算法可能没有保持一致性。通常我们任务运行时间依赖于输入的大小和结构，所以应在各种大小的不同测试输入上执行独立试验。

## 1. 推导式

### 1.1 分类：

> 列表推导式，字典推导式，集合推导式

### 1.2 列表推导式：

通过列表生成列表对象，又称列表解析式，一般语法如下：

> **[ expression for value in iterable if condition ]**

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

> **{ expression for value in iterable if condition }**

### 1.5 生成器推导式(生成元组)：

同列表：(表达式 for item in 可迭代对象)(可使用多个循环,括号此时**不可省略**)

> **( expression for value in iterable if condition ) **

**但是生成器推导式返回一个生成器，而不是一个数组。**

如:

```python
>>>(x for x in range(5) if x != 0 )
>>><generator object <genexpr> at 0x00000189566F2F90>
```

### 附：迭代器与生成器

迭代器是一个对象，通过一系列的值来管理迭代。一般情况下，同一个可迭代对象可以产生多个迭代器，同时每个迭代器维护自身进度的条件。迭代器不存储自己的元素副本，但它保存原始列表的当前索引，该索引指向下一个元素。**因此，如果原始列表的内容在迭代器构造后但在迭代完成前被修改，迭代器将抱告原始列表的更新内容。**

生成器对象generator object，一个生成器只能调用一次，调用完毕后即清除数据，但可多次访问，生成器是生成迭代器最方便的技术。生成器的技术有点像函数，但是不返回值。为了显示序列中的每一个值，要使用**yield**语句(函数内使用，生成并返回一个生成器，此时函数返回值无效)。生成器不会立刻产生数据占用内存，称为懒惰计算方式，能够节省内存。

> 通过iter(iterable)来生成迭代器，通过iter.\__next__()或者next(generator)移动指标并返回下一个指标索引值。

## 2. python对象

### 2.1对象的基本组成

在python中，一切皆对象，其本质是一个内存块，拥有特定的值，支持特定类型的操作，每个对象由**标识**(identity)，**类型**(type)，**值**(value)三个要素组成。

> 标识，对应于对象在计算机内存中的地址，使用内置函数id(object)可返回对象的标识；
>
> 类型，对应于对象储存的数据所属类型，类型可以限制对象的数据范围以及可执行的操作，可以使用内置函数type(object)查看对象所属类型；
>
> 值，表示对象残存的数据信息，可以使用print(object)打印对象的值。

### 2.2 对象的引用

标识通过地址引用了“对象”，容器本身并不存储任何数据，相应地，每一个元素都有一个64位（即8个字节）的存储地址（主存的存储位置则由计算机生成，往往不相关），当访问对应的元素时，实则访问该存储地址对应的值，这种情况下，访问任意一种元素所花费的时间及空间，都是一样的，这种存储结构称为引用结构。（直接存储元素本身的称为紧凑结构，往往效率更高，由array模块支持）

变量位于栈内存，对象(不变量)位于堆内存，赋值将变量绑定到对象，且为动态赋值。Python是动态类型语言，因此变量不需要显式声明类型。Python是强类型语言，每个对象都有数据类型，只支持该类型格式的操作。

### 2.3 标识符

标识符用于变量，函数，类，模块等的名称。标识符有以下规则：

> ⑴区分大小写；
>
> ⑵第一个字符必须是字母或者”_”，其后是字母，数字，下划线；
>
> ⑶不能使用保留字；
>
> ⑷双下划线开头结尾往往有特殊的用法，尽量避免这种写法。

###  2.4 作用域与命名空间

确定与标识符相关联的值的过程称为**名称解析**。每当标识符分配了一个值，这个定义都有特定的作用范围，称为**作用域**。最高级赋值通常是全局范围，对于在函数体内的赋值，其作用范围通常是函数内部局部范围。

Python中的每一个定义域使用了抽象空间，称为**命名空间**。命名空间管理当前在给定作用域内定义的所有标识符。Python实现命名空间是用自己的字典将每个标识符字符串映射到其相关的值。Python还提供了几种方法来检查一个给定的命名空间。函数dir()报告给定命名空间中的标识符的名词，而函数var()返回完整的字典。



## 3. 数据持久化--pickle

### 1. Synposis

> pickle模块用于实现序列化和反序列化，提供了一种简单的持久化功能，可以将对象以文件的形式加密存放在磁盘上。pickle是python语言的标准模块。
>
> pickle模块是以二进制的形式序列化后保存到文件中（保存文件的后缀为”.pkl”），不能直接打开进行预览。pickle模块的接口主要有两类，即序列化和反序列化。

### 2. Method

#### (1) pickle.load(file)

作用：将文件的内容反序列化读出

参数：	

> file:文件名

```python
import pickle	

with open("data.pickle", "wb") as f:
	
    pickle.load(f)
```

#### (2) pickle.dump(obj, file, [,protocol])

作用：将数据序列化后存入文件

参数:

> obj:序列化对象
>
> fle:文件
>
> protocol : 序列化使用的协议。如果该项省略，则默认为0。如果为负值或HIGHEST_PROTOCOL，则使用最高的协议版本。

它们可以如下图这样使用：

```python
import pickle	

with open("data.pickle", "wb") as f:
	
    pickle.dump(data, f, prorocol=pickle.HIGHEST_PROTOCOL)
```

#### (3) pickle.dumps(obj,[protocol])

作用：将obj序列化为string形式，而不是存入文件。

#### (4) pickle.loads(str)

作用：从str中读取序列化前的对象。

### 3. Data type supported to pickle![img](https://img2018.cnblogs.com/blog/1378116/201904/1378116-20190411175538121-1771757134.png)



## 4. 常见编码形式

![image-20210324165352696](C:\Users\Hedge\AppData\Roaming\Typora\typora-user-images\image-20210324165352696.png)

window系统默认解码方式为GBK，linux默认解码方式为UTF，python解释器默认解码方式为Unicode，文本文件打开默认解码方式为UTF-8。

## 5. 赋值表达式

海象运算符是在 PEP 572 被提出的，直到 3.8 版本合入发布。

它的英文原名叫 `Assignment Expressions`，翻译过来也就是 `赋值表达式`，不过现在大家更普遍地称之为海象运算符，其一般语法表达式如下。

```python
identity : = value
```

结合函数等使用可以简化代码。



# 板块八 面向对象

## 基础

> **面向对象(OOP)**编程中的主体被称为**对象**。每个对象都是类的实例。类呈现给外部世界的是该类实例中个对象的一种简洁、一致的概括，没有太多不必要的细节，也没有提供访问类内部工作过程的接口。

### 设计目标

> 软件的实现应该达到健壮性、适应性和可重用性目标。

+ **健壮性**是指应用程序中事先考虑到所有输入都会产生一个正确的输出，也可以说是没有明确定义的异常输出。

+ **适用性**是指软件能随时间不断优化，以应对外部环境条件的变化。

+ **可重用性**是指代码是可以重用的，尤其是指在不同的操作系统上的软件运行。

### 设计原则

> **模块化、抽象化、封装**

在Python中，模块是一个源代码中定义的密切相关的函数和类的集合。

**抽象化**是指从一个复杂的系统中提炼出最基本的部分。通常，描述系统的各个部分涉及给这些部分命名和解释它们的功能。将抽象模式应用于数据结构的设计便产生了抽象数据类型(Abstract Data Types, ADT)。ADT是数据结构的数学模型，它规定了数据存储的类型、支持的操作和操作参数的类型。Python采用一种抽象基类(Abstract Base Class, ABC)的机制支持抽象数据类型。

**封装**指软件系统的不同组件不应显示其各自实现的内部细节。封装的主要优点之一就是它给程序员实现组件细节的自由，而不用关心其他程序员写的其他依赖于这些内部代码的程序。

### 设计模式

> 设计模式是一种可以应用于不同情况的解决方案提供了通用模板的模式。模式包括一个名称（标识）、一个语境（输入）、一个模板（环境）以及一个结果（输出）。接下来所涉及的设计模式分为解决**算法设计**和**软件工程**问题的模式，鉴于实际需求，此处着重介绍算法设计类。
>

|          | 算法设计类                                                   | 软件工程类                                                   |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 实例模式 | 递归<br />摊销<br />分治法<br />暴力算法<br />动态规划法<br />贪心法 | 迭代器<br />适配器<br />位置<br />合成<br />模板方法<br />定位器<br />工厂模式 |

## 软件开发

传统的软件开发包括三个阶段：**设计**、实现与测试和调试

### 设计

> 面向对象编程，设计也许是软件开发过程中最重要的阶段。在这一阶段，我们要决定程序的交互方式，存储的数据和功能。以下一些经验原则可以为设计类提供方便。

+ 责任：将工作分为不同的角色，用不同的类，通过不同的动作实现；
+ 独立：在尽可能独立的情况下规定每个人类的工作，细分各个类的责任，使得他们在各自的领域具有自主权。
+ 行为：仔细且精确地定义每个类的行为，这样与它交互的其他类可以更好地理解这公关由类执行的动作结果。

**面向对象设计程序的关键在于定义类和f它们的实例变量和方法。**

### 测试与调试

> **测试是指模拟用户输入测试程序是否存在错误的过程，而调试是指对程序bug的定位及修正的过程。**在程序开发中，测试和调试通过是最耗时间的一项活动。

详细的测试计划是编写程序最重要的部分。用所有可能的输入检验程序的正确性通常是不可能的，所以我们应该用有代表性的输入子集来运行程序。在特殊情况的输入下，程序往往会失败。需要仔细确认和测试这些情况。

最简单的调试技术包括使用打印语句来跟踪程序执行过程中的变量的值，一种更好的办法是是调试器(debugger)运行程序。



## 不同级导入

```python
from ..name import func	# 从包的上上级导入
from .name import func	# 从包的上级导入
```



# 板块九 PythonShell

## 基本Shell指令

Run library module as a script in terminal via `-m`.

### 1. webbrowser

> Webbrowser is a standard module in python in fact, it provides a high-level interface to allow displaying web-based documents to users. The script **webbrowser** can be used as a command-line interface for the module. It accepts a URL as the argument.

#### Usage

> Open a web in default browser. You can also achieve via script through import method.

```shell
python -m webbrowser -t url
```

#### Params

> + `-n` opens the URL in a new browser window, if possible; 
>
> + `-t` opens the URL in a new browser page (“tab”). The options are, naturally, mutually exclusive.

#### Return

> None.

