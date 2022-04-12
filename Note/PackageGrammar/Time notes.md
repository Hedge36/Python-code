# time库基础语法

## A.基础介绍

计算机时间的表达，能获取系统时间并格式化输出功能，提供系统级精确计时功能，用于程序性能分析;

## B.函数说明：

### 1.时间获取：

> #### time   				
>
> 获取当前系统的时间戳(从1970.1.1记起)即计算机内部时间值，以**浮点数**表示,单位为秒，辅以微秒的精确值。
>
> #### ctime     				
>
> 获取当前时间并以易读的方式表示，返回字符串(含占一个的空位)；
>
> #### gmtime
>
> 获取当前时间，表示为计算机可处理的时间格式；

### 2.时间格式化：

#### strftime(tpl,ts)			 

tpl是格式化模板字符串，用来定义输出效果，ts是计算机内部时间类型变量，比如：strftime("%Y-%m-%d %H:%M:%S"（控制符）,time(变量名称))，此处需要计算机可以操作的时间；

控制符：

> %B月份名称(英文全称)
>
> %b月份名称（英文缩写）
>
> %A星期（英文全称）
>
> %H小时（24小时制）
>
> %I小时（12小时制）
>
> %p上下午（AM,PM）
>

#### strptime(str,tpl)		

str是字符串形式的时间值，tpl是格式化模板字符串，用来定义输入					效果，与上一个函数相对。

### 3.程序计时：

#### sleep(s)     		

s为拟休眠时间，单位是秒，指程序会在该处暂停s秒再进行下一步; 

#### perf_counter()  		

返回一个CPU级别的精确时间计数值，单位为秒，但是计数值起点					不确定，需连续调用获取差值。

 

# time库整理

***\*1.Time库的作用\****
***\*2. Time库的使用\****
***\*3.实例\****

***\*1.Time库的作用\****

· time库是Python中处理时间的***\*标准库\****

· 提供***\*获取系统时间\****并***\*格式化\****输出功能

· 提供系统级精确计时功能，用于***\*程序性能分析\****

***\*2. Time库的使用\****

先明确几个概念：

**·** ***\*时间戳：\****格林威治时间1970年01月01日00分00秒（北京时间1970年01月01日08时00分00秒）起至现在的***\*总秒数，是个数字\****。

· Python中获取时间的常用方法是，先得到时间戳，再将其转换成想要的时间格式。

**·** ***\*元组struct_time：\****日期、时间是包含许多变量的，所以在Python中定义了一个元组struct_time将所有这些变量组合在一起，包括：年、月、日、小时、分钟、秒等。

***\*1）时间获取函数\****

![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps2.png)![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps3.jpg)![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps4.jpg) 

***\*2）时间格式化：\****将时间以合理的方式展示出来

![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps5.png)![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps6.png)![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps7.png) 

***\*3）问题：\****我们是否可以以字符串的形式构造一个时间，如”2018-01-26 12:55:20”,然后将其变成一个时间变量呢？

答案是可以的，通过展示模板定义的参数逐一解析字符串中对应的每一个值，它可能会形成一个时间变量。转化成一个计算机内部可以操作的一个时间。

![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps8.png) 

***\*4）程序计时应用：\****测量起止动作所经历时间的过程

![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps9.png)![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps10.jpg) 

**·** ***\*疑问：\****perf_counter()函数是用来做程序计时，但是time()函数不是也可以吗？

解答：
time()精度上相对没有那么高，而且受系统的影响，适合表示日期时间或者大程序程序的计时。
perf_counter()适合小一点的程序测试，会计算sleep()时间。

***\*3.实例：文本进度条\****

***\*1）实例1：\****每次进度换行:

print()函数默认输出一个字符后换到下一行，所以不用进行其他操作

![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps11.jpg) 

输出结果>>

![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps12.jpg) 

***\*2）实例2：\****每次进度不换行，只是不断地进行刷新：用后打印的字符覆盖之前的字符

· 为了实现***\*单行动态刷新\****，就需要要求我们的程序在输出某一个字符的字符串的时候，***\*不能够换行到下一行\****。因为换到下一行后，之前的信息不能够被修改

· 转义符 ***\*\r（光标移动到本行首）\****

· 有关转义符的使用当时困扰了我很久，比如应该放在哪个位置，所以单独放在了一个文档里专门介绍啦~~

![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps13.png) 

输出结果>>

![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps14.jpg) 

3）拓展：文本进度条的不同设计函数：

![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps15.jpg)![img](file:///C:\Users\Hedge\AppData\Local\Temp\ksohtml6192\wps16.jpg) 

 