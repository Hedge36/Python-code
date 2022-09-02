# openpyxl notes

## 创建excel文件对象

```python
>>> from openpyxl import *

>>> wb = Workbook() #创建excel文件对象，写在内存里的，不保存的话在关闭后就没了

>>> ws = wb.active  #获取excel文件的一个sheet

>>> ws['A1']=12  #写入内容 单格写

>>> ws['A2']=12.333

>>> ws['A3']=u"小七"

>>> wb.save("e:\\test1.xlsx") #保存文件

>>> ws["B1"]=u"哥哥"

>>> ws["B2"]=u"我想我哥哥了"

>>> wb.save("e:\\test1.xlsx")

>>> import time  #写入时间

>>> ws["c1"]= time.strftime(u"%Y年%m月%d日 %H时%M分%S秒".encode("utf-8"),time.lo

caltime())

>>> wb.save("e:\\test1.xlsx")

import datetime
import time
ws['A2'] = datetime.datetime.now() 
```

 

## 打印有效行和列

\>>> ws.columns

<generator object _cells_by_col at 0x0000000002E117E0>

\>>> for col in ws.columns:

...   print col

...

(<Cell u'Sheet'.A1>, <Cell u'Sheet'.A2>, <Cell u'Sheet'.A3>)

(<Cell u'Sheet'.B1>, <Cell u'Sheet'.B2>, <Cell u'Sheet'.B3>)

(<Cell u'Sheet'.C1>, <Cell u'Sheet'.C2>, <Cell u'Sheet'.C3>)

\>>> for col in ws.rows:

...   print col

...

(<Cell u'Sheet'.A1>, <Cell u'Sheet'.B1>, <Cell u'Sheet'.C1>)

(<Cell u'Sheet'.A2>, <Cell u'Sheet'.B2>, <Cell u'Sheet'.C2>)

(<Cell u'Sheet'.A3>, <Cell u'Sheet'.B3>, <Cell u'Sheet'.C3>)

 

什么是有效行和列？

 

数据写入的可包含整体数据的最大范围，这个范围内的都是有效行和列

 

**6.创建sheet**

\>>> ws = wb.create_sheet("gloryroad")

\>>> ws = wb.create_sheet("I love")

\>>> ws = wb.create_sheet(u"哥哥")

\>>> wb.save("e:\\test.xlsx")

**7.获取sheet名称**

\>>> wb.get_sheet_names() #获取所有名称

[u'Sheet', u'gloryroad', u'I love', u'\u54e5\u54e5']

\>>> ws = wb.get_sheet_by_name(u"哥哥") #获取指定名称

\>>> ws

<Worksheet "\u54e5\u54e5">

\>>> print ws.encode("gbk")

\>>> ws = wb.get_sheet_by_name(wb.get_sheet_names()[-1]) #获取指定位置的sheet名称

\>>> ws

<Worksheet "\u54e5\u54e5">

 

**8.修改sheet名称**

\>>> ws = wb.get_sheet_by_name(wb.get_sheet_names()[-1]) #修改前需要先获取

\>>> ws

<Worksheet "\u54e5\u54e5">

\>>> ws.title = "lin"

\>>> wb.get_sheet_names()

[u'Sheet', u'gloryroad', u'I love', u'lin']

\>>> ws.title

u'lin'

 

**9.获取sheet名称**

\>>> ws = wb["I love"]

\>>> ws

<Worksheet "I love">

\>>> wb.sheetnames

[u'Sheet', u'gloryroad', u'I love', u'lin']

 

**10. 通过行和列修改表格内的内容**

\>>> ws.cell(row=1,column=2,value=123456)

<Cell u'I love'.B1>

\>>> ws["B1"].value

123456

\>>> ws.cell(row=1,column=2,value="I love")

<Cell u'I love'.B1>

\>>> ws["B1"].value

u'I love'

 

**小练习：**

**从A1到D4区域的所有单元格都要写内容，内容是行号是第一位，列号是第二位**

\>>> for row in range(1,5):

...   for col in range(1,5):

...     ws.cell(row=row,column=col,value=str(row)+str(col))

...

<Cell u'I love'.A1>

<Cell u'I love'.B1>

<Cell u'I love'.C1>

<Cell u'I love'.D1>

<Cell u'I love'.A2>

<Cell u'I love'.B2>

<Cell u'I love'.C2>

<Cell u'I love'.D2>

<Cell u'I love'.A3>

<Cell u'I love'.B3>

<Cell u'I love'.C3>

<Cell u'I love'.D3>

<Cell u'I love'.A4>

<Cell u'I love'.B4>

<Cell u'I love'.C4>

<Cell u'I love'.D4>

\>>> wb.save("e:\\test.xlsx")

\>>> 

 

 

**11. 操作某列中所有有效数据**

\>>> print ws["A"]

(<Cell u'I love'.A1>, <Cell u'I love'.A2>, <Cell u'I love'.A3>, <Cell u'I love'.

A4>)

**12. 操作某两列之间的所有有效值**

\>>> print ws["A:D"]

((<Cell u'I love'.A1>, <Cell u'I love'.A2>, <Cell u'I love'.A3>, <Cell u'I love'

.A4>), (<Cell u'I love'.B1>, <Cell u'I love'.B2>, <Cell u'I love'.B3>, <Cell u'I

 love'.B4>), (<Cell u'I love'.C1>, <Cell u'I love'.C2>, <Cell u'I love'.C3>, <Ce

ll u'I love'.C4>), (<Cell u'I love'.D1>, <Cell u'I love'.D2>, <Cell u'I love'.D3

\>, <Cell u'I love'.D4>))

 

**13. 打印出获取到的指定位置的值**

\>>> print ws["A:D"][0][0].value

11

\>>> ws["A:D"][0][0].value='22'  第一列的第一行：列在前，行在后

\14. 取出列的值；取出行和列的值

\>>> ws[1] 取出1行

(<Cell u'I love'.A1>, <Cell u'I love'.B1>, <Cell u'I love'.C1>, <Cell u'I love'.

D1>)

\>>> ws[1:2] 取出1行2列的值

((<Cell u'I love'.A1>, <Cell u'I love'.B1>, <Cell u'I love'.C1>, <Cell u'I love'

.D1>), (<Cell u'I love'.A2>, <Cell u'I love'.B2>, <Cell u'I love'.C2>, <Cell u'I

 love'.D2>))

**小练习：取出1到3行的内容**

自己的做法，取了3列

\>>> for i in range(1,3):

...   print ws[i:3]

...

((<Cell u'I love'.A1>, <Cell u'I love'.B1>, <Cell u'I love'.C1>, <Cell u'I love'

.D1>), (<Cell u'I love'.A2>, <Cell u'I love'.B2>, <Cell u'I love'.C2>, <Cell u'I

 love'.D2>), (<Cell u'I love'.A3>, <Cell u'I love'.B3>, <Cell u'I love'.C3>, <Ce

ll u'I love'.D3>))

((<Cell u'I love'.A2>, <Cell u'I love'.B2>, <Cell u'I love'.C2>, <Cell u'I love'

.D2>), (<Cell u'I love'.A3>, <Cell u'I love'.B3>, <Cell u'I love'.C3>, <Cell u'I

 love'.D3>))

老师的方法：

\>>> for row in ws[1:3]:
...   for j in range(len(row)): 利用每行元素的个数来确定有多少列
...     print row[j].value

 

同学的方法：

for rows in ws[1:3]:
  for row in rows:
    print row.value,
  print

 

**15. 指定一个范围，通过限制最大行号和列号，最小行号和列号来实现**

\>>> for row in ws.iter_rows(min_row=1,max_col=3,max_row=3):

...   for cell in row:

...     print cell.value

...

22

12

13

21

22

23

31

32

33

\>>> for row in ws.iter_rows(min_row=1,min_col=1,max_col=3,max_row=3):

...   for cell in row:

...     print cell.value

...

 

**16. 打印所有的行和列**

\>>> for row in ws.rows: 打印所有的行

...   print row

...

\>>> for col in ws.columns: 打印所有的列

...   print col

...

 

**17. 写入百分数**

\>>> ws["Z100"]="66%"

\>>> print ws["Z100"].value

66%

\>>> wb.guess_type = True  为True时excel里面就是常规类型，为False时是百分数？

\>>> ws["Z101"].value

\>>> wb.save("e:\\test.xlsx")

 

 

**18. 修改excel里面的值**

\>>> wb = load_workbook("e:\\test.xlsx") #读取一个现有的文件进行操作

\>>> ws = wb.active #获取当前sheet

\>>> ws['A1'].vlue

\>>> ws['A1'].value

12L

\>>> ws['A1'].value=12 #修改值

\>>> ws['A1'].value

12

\>>> ws['A2'].value

12.333

\>>> ws['A2'].value=u"gege" #修改值

\>>> ws['A2'].value

u'gege'

 

**19. 判断excel内存储的数值格式类型**

\>>> ws['A3'].value = "12%"

\>>> ws['A3'].number_format

'General'

\>>> ws['A20'].number_format

'General'

\>>> wb.guess_type = True

\>>> ws['A10']="12%"

\>>> ws['A10'].number_format

'General'

\>>> ws['A10']="12%"

\>>> wb.save("e:\\test.xslx")

\>>> ws['A10'].number_format

'General'

\>>> import datetime

\>>> ws["A11"]=datetime.datetime(1017,1,1)

\>>> ws['A11'].number_format

'yyyy-mm-dd h:mm:ss'

\>>> 

 

**20. 写入一个sum函数**

\>>> ws["A11"]="=sum(1,1)"
\>>> print ws["A11"]
<Cell u'Sheet'.A11>
\>>> print ws["A11"].value
=sum(1,1)
\>>> wb.save("e:\\sample.xlsx")

 

**21. 合并单元格和取消合并**

ws.merge_cells("A1:C3")

ws.umerge_cells("A1:C3")

 

ws.merge_cells(start_row=2,start_column=1,end_row=2,end_column=4)
ws.unmerge_cells(start_row=2,start_column=1,end_row=2,end_column=4)

 

**22. 插入图片**

from openpyxl import load_workbook

from openpyxl.drawing.image import Image

 

wb = load_workbook('e:\\test.xlsx')

ws1=wb.active

img = Image('e:\\1.png')

ws1.add_image(img, 'A1')

 

\# Save the file

wb.save("e:\\test.xlsx")

E:\>python a.py

Traceback (most recent call last):

 File "a.py", line 13, in <module>

  wb.save("e:\\test.xlsx")

 File "C:\Python27\lib\site-packages\openpyxl\workbook\workbook.py", line 349,

in save

  save_workbook(self, filename)

 File "C:\Python27\lib\site-packages\openpyxl\writer\excel.py", line 267, in sa

ve_workbook

  archive = ZipFile(filename, 'w', ZIP_DEFLATED, allowZip64=True)

 File "C:\Python27\lib\zipfile.py", line 756, in __init__

  self.fp = open(file, modeDict[mode])

IOError: [Errno 13] Permission denied: 'e:\\test.xlsx'

Excel没有关闭，所以报错！！！

E:\>python a.py

**23. 隐藏列**

ws1.column_dimensions.group('A', 'D', hidden=True)  隐藏列

**24. 生成柱形图**

from openpyxl import load_workbook

from openpyxl import Workbook

from openpyxl.chart import BarChart, Reference, Series

 

wb = load_workbook('e:\\test.xlsx')

ws1=wb.active

 

wb = Workbook()

ws = wb.active

for i in range(10): #生成数据

  ws.append([i])

values = Reference(ws, min_col=1, min_row=1, max_col=1, max_row=10)  #数据范围

chart = BarChart() #生成柱状图对象

chart.add_data(values) #柱状图对象用values存储数据

ws.add_chart(chart, "E15")

 

\# Save the file

wb.save("e:\\test.xlsx")

 

**25. 生成单元格，有样式**

\# -*- coding: utf-8 -*-

 

from openpyxl import load_workbook

from openpyxl import Workbook

from openpyxl.worksheet.table import Table, TableStyleInfo

 

wb = Workbook()

ws = wb.active

 

data = [

  ['Apples', 10000, 5000, 8000, 6000],

  ['Pears',  2000, 3000, 4000, 5000],

  ['Bananas', 6000, 6000, 6500, 6000],

  ['Oranges', 500, 300, 200, 700],

]

 

\# add column headings. NB. these must be strings

ws.append(["Fruit", "2011", "2012", "2013", "2014"])

for row in data:

  ws.append(row)

 

tab = Table(displayName="Table1", ref="A1:E5") #table指的是要使用样式的区域

 

\# Add a default style with striped rows and banded columns

style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=True,

​            showLastColumn=True, showRowStripes=True,

 

showColumnStripes=True)

tab.tableStyleInfo = style

ws.add_table(tab)

 

\# Save the file

wb.save("e:\\test.xlsx")

 

 

**26. 设置单元格中的字体**

\# -*- coding: utf-8 -*-

from openpyxl import Workbook

from openpyxl.styles import colors

from openpyxl.styles import Font

 

wb = Workbook()

ws = wb.active

 

a1 = ws['A1']

d4 = ws['D4']

ft = Font(color=colors.RED) # color="FFBB00"，颜色编码也可以设定颜色

a1.font = ft

d4.font = ft

 

\# If you want to change the color of a Font, you need to reassign it::

 

a1.font = Font(color=colors.RED, italic=True) # the change only affects A1

a1.value = "abc"

 

\# Save the file

wb.save("e:\\test.xlsx")

 

16进制的颜色：

可以在网上查

 

**27. 设置字体和大写**

\# -*- coding: utf-8 -*-

 

from openpyxl import Workbook

from openpyxl.styles import colors

from openpyxl.styles import Font

 

 

wb = Workbook()

ws = wb.active

 

a1 = ws['A1']

d4 = ws['D4']

ft = Font(color="FFBB00") # color="FFBB00"，颜色编码也可以设定颜色

a1.font = ft

d4.font = ft

 

\# If you want to change the color of a Font, you need to reassign it::

 

a1.font = Font(name=u'宋体',size=28,color=colors.RED, italic=True) # the change only

 

affects A1

a1.value = "abc"

 

 

\# Save the file

wb.save("e:\\test.xlsx")

 

**28. 设置为粗体**

\# -*- coding: utf-8 -*-

 

from openpyxl import Workbook

from openpyxl.styles import colors

from openpyxl.styles import Font

 

 

wb = Workbook()

ws = wb.active

 

a1 = ws['A1']

d4 = ws['D4']

ft = Font(color="FFBB00") # color="FFBB00"，颜色编码也可以设定颜色

a1.font = ft

d4.font = ft

 

\# If you want to change the color of a Font, you need to reassign it::

 

a1.font = Font(name=u'宋体',size=28,bold=True,color=colors.RED, italic=True) # the

 

change only affects A1

a1.value = "abc"

 

 

\# Save the file

wb.save("e:\\test.xlsx")

 

 

**29. 设置成样式模板再去给单元格应用，但是不支持多个同时设置，需要的话可以通过循环**

\# -*- coding: utf-8 -*-

 

from openpyxl import Workbook

from openpyxl.styles import Font

from openpyxl.styles import NamedStyle, Font, Border, Side,PatternFill

 

wb = Workbook()

ws = wb.active

 

highlight = NamedStyle(name="highlight")

highlight.font = Font(bold=True, size=20,color= "ff0100")

highlight.fill = PatternFill("solid", fgColor="DDDDDD")

bd = Side(style='thick', color="000000") #边框颜色及粗细

highlight.border = Border(left=bd, top=bd, right=bd, bottom=bd) #边框 上下左右

 

print dir(ws["A1"])

ws["A1"].style =highlight #设置单元格样式

 

\# Save the file

wb.save("e:\\test.xlsx")

 

 

**30. 常用的样式和属性设置**

\# -*- coding: utf-8 -*-

from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.styles import NamedStyle, Font, Border, Side,PatternFill
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font

wb = Workbook()
ws = wb.active

ft = Font(name=u'微软雅黑',
  size=11,
  bold=False,
  italic=False,
  vertAlign=None,
  underline='none',
  strike=False,
  color='FF000000')

fill = PatternFill(fill_type="solid",
  start_color='FFEEFFFF',
  end_color='FF001100')

\#边框可以选择的值为：'hair', 'medium', 'dashDot', 'dotted', 'mediumDashDot', 'dashed', 'mediumDashed', 'mediumDashDotDot', 'dashDotDot', 'slantDashDot', 'double', 'thick', 'thin']
\#diagonal 表示对角线
bd = Border(left=Side(border_style="thin",
       color='FF001000'),
  right=Side(border_style="thin",
        color='FF110000'),
  top=Side(border_style="thin",
       color='FF110000'),
  bottom=Side(border_style="thin",
        color='FF110000'),
  diagonal=Side(border_style=None,
         color='FF000000'),
  diagonal_direction=0,
  outline=Side(border_style=None,
         color='FF000000'),
  vertical=Side(border_style=None,
         color='FF000000'),
  horizontal=Side(border_style=None,
          color='FF110000')
        )

alignment=Alignment(horizontal='general',
    vertical='bottom',
    text_rotation=0,
    wrap_text=False,
    shrink_to_fit=False,
    indent=0)

number_format = 'General'

protection = Protection(locked=True,
      hidden=False)

ws["B5"].font = ft
ws["B5"].fill =fill
ws["B5"].border = bd
ws["B5"].alignment = alignment
ws["B5"].number_format = number_format

ws["B5"].value ="glory road"

\# Save the file
wb.save("e:\\sample.xlsx")

### openpyxl的使用

openpyxl（可读写excel表）专门处理Excel2007及以上版本产生的xlsx文件，xls和xlsx之间转换容易

注意：如果文字编码是“gb2312” 读取后就会显示乱码，请先转成Unicode

 

#### openpyxl定义多种数据格式

```
最重要的三种：
NULL空值：对应于python中的None，表示这个cell里面没有数据。
numberic： 数字型，统一按照浮点数来进行处理。对应于python中的float。
string： 字符串型，对应于python中的unicode。
```

#### Excel文件三个对象

```
workbook： 工作簿，一个excel文件包含多个sheet。
sheet：工作表，一个workbook有多个，表名识别，如“sheet1”,“sheet2”等。
cell： 单元格，存储数据对象
```

### 1创建一个workbook（工作簿）

wb = Workbook() # 一个工作簿(workbook)在创建的时候同时至少也新建了一张工作表(worksheet)。

 

##### 2 打开一个已有的workbook：

```
 wb = load_workbook('file_name.xlsx')
```

##### 3 打开sheet：

```
通过名字
    ws = wb["frequency"] 或ws2 = wb.get_sheet_by_name('frequency')
 
不知道名字用index
    sheet_names = wb.get_sheet_names()  #方法得到工作簿的所有工作表
    ws = wb.get_sheet_by_name(sheet_names[index])# index为0为第一张表 
```

`或者`（调用得到正在运行的工作表）``

```
    ws =wb.active或ws = wb.get_active_sheet() #通过_active_sheet_index设定读取的表，默认0读第一个表
    活动表表名wb.get_active_sheet().title
```

##### 4 新建sheet（工作表）

```
ws1 = wb.create_sheet() #默认插在最后
ws2 = wb.create_sheet(0) #插在开头 ，在创建工作表的时候系统自动命名，依次为Sheet, Sheet1, Sheet2 ...
 
ws.title = "New Title" #修改表名称
简化 ws2 = wb.create_sheet(title="Pi")
```

##### 5 读写单元格

当一个工作表被创建时，其中是不包含单元格。只有当单元格被获取时才被创建。这种方式下，我们不会创建我们使用不到的单元格，从而减少了内存消耗。

 

```
可以直接根据单元格的索引直接获得
c = ws['A4']     #读取单元格，如果不存在将在A4新建一个
 
可以通过cell()方法获取单元格(行号列号从1开始)
d = ws.cell(row = 4, column = 2) #通过行列读
d = ws.cell('A4')
 
写入单元格（cell）值
ws['A4'] = 4      #写单元格 
ws.cell(row = 4, column = 2).value = 'test'
ws.cell(row = 4, column = 2, value = 'test')
```

##### 6 访问多个单元格

```
cell_range = ws['A1':'C2']    #使用切片获取多个单元格
 
get_cell_collection()     #读所有单元格数据
```

##### 7 按行、按列操作

```
逐行读
 ws.iter_rows(range_string=None, row_offset=0, column_offset=0) #返回一个生成器, 获得多个单元格
 例如：
  for row in ws.iter_rows('A1:C2'):
      for cell in row:
          print cell
迭代文件中所有的行或者列:
ws.rows         #迭代读取行row 
ws.columns      #迭代读取列column
 
直接读取行列数据 
print rows[n]      #显示第n行数据 
print columns[n]   #显示第n列数据
 
逐行写，添加一行到当前sheet的最底部。 
1,如果是list,将list从头到尾顺序添加。 2，如果是dict,按照相应的键添加相应的键值。
 append([‘This is A1’, ‘This is B1’, ‘This is C1’])
 append({‘A’ : ‘This is A1’, ‘C’ : ‘This is C1’})
 append({1 : ‘This is A1’, 3 : ‘This is C1’})
 
通过公式计算产生写入的值
ws["A1"] = "=SUM(1, 1)"
ws["A1"] = "=SUM(B1:C1)"
 
```

##### 8 显示有多少张sheet表

```
wb.get_sheet_names()  
#显示表名，表行数，表列数   
print ws.title  
print ws.max_row
print ws.max_column
 
```

##### 9 获得列号的字母

```
from openpyxl.utils import get_column_letter
for  x  in  range( 1, len(record)+ 1 ):  
    col = get_column_letter(x)    # 默认x从1开始
    ws.cell( '%s%s' %(col, i)).value = x
 
通过列字母获取多个excel数据块
cell_range = "E3:{0}28".format(get_column_letter(bc_col))
ws["A1"] = "=SUM(%s)"%cell_range
```

##### 10 excel文件是gbk编码，读入时需要先编码为gbk，再解码为unicode，再编码为utf8

```
cell_value.encode('gbk').decode('gbk').encode('utf8')  
 
 
```

##### 11保存到文件

wb = Workbook()

wb.save('balances.xlsx')

save（）会在不提示的情况下用现在写的内容，覆盖掉原文件中的所有内容

```
 
```

## 写入例子一

```
from` `openpyxl import` `Workbook
```

 

```
wb =` `Workbook()
# ``激活 worksheet
ws =` `wb.active
# ``数据可以直接分配到单元格中
ws['A1'] =` `42
# ``可以附加行，从第一列开始附加
ws.append([1, 2, 3])
# Python ``类型会被自动转换
import` `datetime
```

 

```
ws['A3'] =` `datetime.datetime.now().strftime("%Y-%m-%d")
# ``保存文件
wb.save("sample.xlsx")
```

## 写入例子二

```
# workbook``相关
from` `openpyxl import` `Workbook
from` `openpyxl.compat import` `range
from` `openpyxl.utils import` `get_column_letter
```

 

```
wb =` `Workbook()
```

 

```
dest_filename =` `'empty_book.xlsx'
```

 

```
ws1 =` `wb.active
ws1.title =` `"range names"
```

 

```
for` `row in` `range(1, 40):
  ws1.append(range(600))
```

 

```
ws2 =` `wb.create_sheet(title="Pi")
```

 

```
ws2['F5'] =` `3.14
```

 

```
ws3 =` `wb.create_sheet(title="Data")
for` `row in` `range(10, 20):
  for` `col in` `range(27, 54):
    _ =` `ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
print(ws3['AA10'].value)
wb.save(filename=dest_filename)
```

## 读取例子一

![img](https://images2017.cnblogs.com/blog/846822/201709/846822-20170927192546137-1266184835.png)

from openpyxl.reader.excel import load_workbook
import json

\# 读取excel2007文件
wb = load_workbook(filename=r'test_book.xlsx')

\# 显示有多少张表
print "Worksheet range(s):", wb.get_named_ranges()
print "Worksheet name(s):", wb.get_sheet_names()

\# 取第一张表
sheetnames = wb.get_sheet_names()
ws = wb.get_sheet_by_name(sheetnames[0])

\# 显示表名，表行数，表列数
print "Work Sheet Titile:", ws.title
print "Work Sheet Rows:", ws.max_row
print "Work Sheet Cols:", ws.max_column


\# 建立存储数据的字典
data_dic = {}

\# 把数据存到字典中
for rx in range(1, ws.max_row + 1):
  temp_list = []
  pid = rx
  w1 = ws.cell(row=rx, column=1).value
  w2 = ws.cell(row=rx, column=2).value
  w3 = ws.cell(row=rx, column=3).value
  w4 = ws.cell(row=rx, column=4).value
  temp_list = [w1, w2, w3, w4]

  data_dic[pid] = temp_list

\# 打印字典数据个数
print 'Total:%d' % len(data_dic)
print json.dumps(data_dic, encoding="UTF-8", ensure_ascii=False)

 读取结果：

```
Worksheet range(s): []
Worksheet name(s): [u'\u6d3b\u52a8\u8868', u'\u7528\u6237\u4fe1\u606f', u'Sheet3']
Work Sheet Titile: ``活动表
Work Sheet Rows: 3
Work Sheet Cols: 5
Total:3
{"1": ["张三", 18, "男", "广州"], "2": ["李四", 20, "女", "湖北"], "3": ["王五", 25, "女", "北京"]}
```

### 实例

```
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.cell import get_column_letter
 
dest_filename = 'empty_book.xlsx'
 
wb = Workbook()
ws1 = wb.active
ws1.title = "range names"
for row in range(1, 40):
   ws1.append(range(600))
 
ws3 = wb.create_sheet(title="Data")
for row in range(10, 20):
   for col in range(27, 54):
       _ = ws3.cell(column=col, row=row, value="%s" % get_column_letter(col))
print(ws3['AA10'].value)
wb.save(filename = dest_filename)
 
sheet_ranges = wb['range names']
print(sheet_ranges['D18'].value)
 
ws['A1'] = datetime.datetime(2010, 7, 21)
ws['A1'].number_format #输出'yyyy-mm-dd h:mm:ss'
 
rows = [
    ['Number', 'Batch 1', 'Batch 2'],
    [2, 40, 30],
    [3, 40, 25],
    [4, 50, 30],
    [5, 30, 10],
    [6, 25, 5],
    [7, 50, 10],
]
 
rows = [
    ['Date', 'Batch 1', 'Batch 2', 'Batch 3'],
    [date(2015,9, 1), 40, 30, 25],
    [date(2015,9, 2), 40, 25, 30],
    [date(2015,9, 3), 50, 30, 45],
    [date(2015,9, 4), 30, 25, 40],
    [date(2015,9, 5), 25, 35, 30],
    [date(2015,9, 6), 20, 40, 35],
]
 
for row in rows:
    ws.append(row)
```

 

#### excel中图片的处理，PIL模块

```
    try:
        from openpyxl.drawing import image
        import PIL            
    except ImportError, e:
        print "[ERROR]",e
 
    report_file = self.excel_path + "/frquency_report_%d.xlsx" %id
    shutil.copyfile(configs.PATTEN_FILE, report_file)
    if not os.path.exists(report_file):
       print "generate file failed: ", report_file
       sys.exit(1)
 
    wb = load_workbook(report_file)
    ws = wb.get_sheet_by_name('frequency')
    img_f = configs.IMAGE_LOGO
    if os.path.exists(img_f):
        try:
            img = image.Image(img_f)
            ws.add_image(img, 'A1')
        except Exception, e:
            print "[ERROR]%s:%s" % (type(e), e)
            ws['A1'] = "程序化营销平台"
        else:
            ws['A1'] = "程序化营销平台"
 
        font1 = Font(size=22)
        ws['A1'].font = font1
        ws['B4'] = ad_plan #等同ws.cell('B4') = ad_plan
        ws['B5'] = ad_names
        ws['B6'] = str(start_d) + '  to  ' + str(end_d)
 
        wb.save(report_file)
 
 
    try:
        wb = load_workbook(report_file)
        ws = wb.get_sheet_by_name('frequency')            
        row = 9
        for it in query_result:
            one_row = it.split('\t')
            print one_row
            if '10' == one_row[0]:
                one_row[0] = '10+'
            col = 1
            for one_cell in one_row:
                ws.cell(row = row, column = col).value = one_cell
                col = col + 1
            row = row + 1      
    except Thrift.TException, tx:
        print '[ERROR] %s' % (tx.message)
    else:
        wb.save(report_file)
    finally:
        pass
```