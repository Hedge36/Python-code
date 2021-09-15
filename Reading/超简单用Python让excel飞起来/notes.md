# 超简单：用Python让Excel飞起来

> 出版发行：机械工业出版社
>
> 版次：2021年5月第一版

## 目录

> 第一章 Python快速上手
>
> 第二章 Python的基础语法知识
>
> 第三章 Python模块
>
> 第四章 使用Python批处理工作薄和工作表
>
> 第五章 使用Python批处理行、列和单元格
>
> 第六章 使用Python批量进行数据分析
>
> 第七章 使用Python制作简单的图标并设置图表元素
>
> 第八章 使用Python制作常用图表
>
> 第九章 在Excel中调用Python代码





# xlwings

## 特色

> - xlwings能够非常方便的读写Excel文件中的数据，并且能够进行单元格格式的修改
> - 可以和matplotlib以及pandas无缝连接
> - 可以调用Excel文件中VBA写好的程序，也可以让VBA调用用Python写的程序。
> - 开源免费，一直在更新

![图片](E:/工具/Typora/Temp/640.webp)

excel已经成为必不可少的数据处理软件，几乎天天在用。python有很多支持操作excel的第三方库，`xlwings`是其中一个。

![img](E:/工具/Typora/Temp/v2-6b754a8b51ca58fd45af303cc2783190_b.jpg)

## xlwings实操

- 建立excel表连接

```python3
wb = xw.Book("e:\example.xlsx")
```

- 实例化工作表对象

```text
sht = wb.sheets["sheet1"]
```

- 返回工作表绝对路径

```text
wb.fullname
```

- 返回工作簿的名字

```text
sht.name
```

- 在单元格中写入数据

```text
sht.range('A1').value = "xlwings"
```

- 读取单元格内容

```text
sht.range('A1').value
```

- 清除单元格内容和格式

```text
sht.range('A1').clear()
```

- 获取单元格的列标

```text
sht.range('A1').column
```

- 获取单元格的行标

```text
sht.range('A1').row
```

- 获取单元格的行高

```text
sht.range('A1').row_height
```

- 获取单元格的列宽

```text
sht.range('A1').column_width
```

- 列宽自适应

```text
sht.range('A1').columns.autofit()
```

- 行高自适应

```text
sht.range('A1').rows.autofit()
```

- 给单元格上背景色，传入RGB值

```python3
sht.range('A1').color = (34,139,34)
```

- 获取单元格颜色，RGB值

```python3
sht.range('A1').color
```

- 清除单元格颜色

```text
sht.range('A1').color = None
```

- 输入公式，相应单元格会出现计算结果

```python3
sht.range('A1').formula='=SUM(B6:B7)'
```

- 获取单元格公式

```python3
sht.range('A1').formula_array
```

- 在单元格中写入批量数据，只需要指定其实单元格位置即可

```python3
sht.range('A2').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
```

- 读取表中批量数据，使用expand()方法

```python3
sht.range('A2').expand().value
```

- 其实你也可以不指定工作表的地址，直接与电脑里的活动表格进行交互

```python3
# 写入
xw.Range("E1").value = "xlwings"# 读取
xw.Range("E1").value
```

## xlwings与numpy、pandas、matplotlib互动

- 支持写入numpy array数据类型

```python3
import numpy as np
np_data = np.array((1,2,3))
sht.range('F1').value = np_data
```

- 支持将pandas DataFrame数据类型写入excel

```python3
import pandas as pd
df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
sht.range('A5').value = df
```

- 将数据读取，输出类型为DataFrame

```python3
sht.range('A5').options(pd.DataFrame,expand='table').value
```

- 将matplotlib图表写入到excel表格里

```python3
import matplotlib.pyplot as plt
%matplotlib inline
fig = plt.figure()
plt.plot([1, 2, 3, 4, 5])
sht.pictures.add(fig, name='MyPlot', update=True)
```

## xlwings与VBA互相调用

xlwings与VBA的配合非常完美，你可以在python中调用VBA，也可以在VBA中使用python编程，这些通过xlwings都可以巧妙实现。这里不对该内容做详细讲解，感兴趣的童鞋可以去xlwings官网学习。

### 1. 创建带宏表格

在当前目录下创建一个带有宏的表格可以通过cmd命令来实现：

```
xlwings quickstart filename
```

初始化代码如下：

```python
import xlwings as xw


def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    if sheet["A1"].value == "Hello xlwings!":
        sheet["A1"].value = "Bye xlwings!"
    else:
        sheet["A1"].value = "Hello xlwings!"


@xw.func
def hello(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    xw.Book("table.xlsm").set_mock_caller()
    main()
```









# 附：xlwings-API

## 顶层函数

`xlwings.view`(*obj*, *sheet=None*)
默认情况下，打开新工作簿并在其第一个工作表上显示对象。 如果提供工作表对象，它将在现有工作表上显示对象之前清除工作表。

参数：obj（具有内置转换器的任何类型） - 要显示的对象，例如 数字，字符串，列表，numpy数组，pandas dataframessheet（工作表，默认无） - 工作表对象。 如果未提供，则使用新工作簿的第一张表。

Examples

```
>>> import xlwings as xw
>>> import pandas as pd
>>> import numpy as np
>>> df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
>>> xw.view(df)
```

版本0.7.1中的新功能。

## 对象模型

### Apps

*class*`xlwings.main.``Apps`(*impl*)

所有`app`对象的集合：

```
>>> import xlwings as xw
>>> xw.apps
Apps([<Excel App 1668>, <Excel App 1644>])
active
```

返回活动的应用程序。

0.9.0版中的新功能。

`add`()

创建一个新的应用程序。 新的应用程序成为活动的应用程序。 返回一个App对象。
`count`
返回应用数量。

0.9.0版中的新功能。

`keys`()
提供用作应用程序集合中的键的Excel实例的PID。

0.13.0版中的新功能。

### App

*class*`xlwings.``App`(*visible=None*, *spec=None*, *add_book=True*, *impl=None*)

应用程序对应于Excel实例。 可以像这样启动新的Excel实例：

```
>>> import xlwings as xw
>>> app1 = xw.App()
>>> app2 = xw.App()
```

app对象是[`apps`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474)集合的成员：

```
>>> xw.apps
Apps([<Excel App 1668>, <Excel App 1644>])
>>> xw.apps[1668]  # get the available PIDs via xw.apps.keys()
<Excel App 1668>
>>> xw.apps.active
<Excel App 1668>
```

参数：visible（bool，default None） - 返回或设置一个布尔值，用于确定应用程序是否可见。 默认情况下保持状态不变或如果对象不存在则设置visible = True.spec（str，默认为None）-Mac-only，使用Excel应用程序的完整路径，例如， / Applications / Microsoft Office 2011 / Microsoft Excel或/ Applications / Microsoft ExcelOn Windows，如果要更改xlwings与之对话的Excel版本，请转到“控制面板”>“程序和功能”并修复默认情况下所需的Office版本。

> 注意
> 在Mac上，虽然xlwings允许您运行多个Excel实例，但它是Excel for Mac不正式支持的功能：与Windows不同，Excel不会要求您打开文件的只读版本（如果已经存在） 在另一个实例中打开。 这意味着您需要注意自己，以便不会从不同的实例覆盖相同的文件。

`activate`(*steal_focus=False*)

激活Excel应用。

参数：steal_focus（bool，默认为False） - 如果为True，请创建最前面的应用程序并将焦点从Python移交给Excel。

0.9.0版中的新功能。

```
api
```

返回正在使用的引擎的本机对象（`pywin32`或`appscript` 对象）。

0.9.0版中的新功能。

```
books
```

当前打开的所有Book对象的集合。

0.9.0版中的新功能。

`calculate`()

计算所有打开的工作簿。

0.3.6版中的新功能。

```
calculation
```

返回或设置表示计算模式的计算值。 模式：`'manual'`, `'automatic'`, `'semiautomatic'`
('手动'，'自动'，'半自动')
Examples

```
>>> import xlwings as xw
>>> wb = xw.Book()
>>> wb.app.calculation = 'manual'
```

0.9.0版中的新功能。

```
display_alerts
```

默认值为true。将此属性设置为false可在代码运行时抑制提示和警报消息；当消息需要响应时，Excel将选择默认响应。

0.9.0版中的新功能。

```
hwnd
```

返回Window句柄（仅限Windows）。

New in version 0.9.0.

`kill`()
强制Excel应用程序通过终止其进程退出。
New in version 0.9.0.

`macro`(*name*)

在Excel VBA中运行不属于特定工作簿但属于外接程序的子或函数。
参数：name（带或不带模块名称的Sub或Function的名称，例如'Module1.MyMacro'或'MyMacro'） -
Examples

This VBA function:

```
Function MySum(x, y)
    MySum = x + y
End Function
```

可以像这样访问：

```
>>> import xlwings as xw
>>> app = xw.App()
>>> my_sum = app.macro('MySum')
>>> my_sum(1, 2)
3
```

另请参见： [`Book.macro()`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.Book.macro)

New in version 0.9.0.

```
pid
```

返回应用程序的PID。
New in version 0.9.0.

`quit`()

退出应用程序而不保存任何工作簿。

New in version 0.3.3.

`range`(*cell1*, *cell2=None*)

活动工作簿的活动工作表中的范围对象，请参见[`Range()`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.Range).

New in version 0.9.0.

```
screen_updating
```

关闭屏幕更新以加快脚本速度。 您将无法看到脚本正在执行的操作，但它将运行得更快。 记住在脚本结束时将screen \ _updating属性设置回True。

New in version 0.3.3.

```
selection
```

将所选单元格作为Range返回。

New in version 0.9.0.

```
version
```

返回Excel版本号对象。

Examples

```
>>> import xlwings as xw
>>> xw.App().version
VersionNumber('15.24')
>>> xw.apps[10559].version.major
15
```

Changed in version 0.9.0.

```
visible
```

获取或设置Excel的可见性为“True”或“False”。

New in version 0.3.3.

### Books

*class*`xlwings.main.``Books`(*impl*)

所有`book`对象的集合：

```
>>> import xlwings as xw
>>> xw.books  # active app
Books([<Book [Book1]>, <Book [Book2]>])
>>> xw.apps[10559].books  # specific app, get the PIDs via xw.apps.keys()
Books([<Book [Book1]>, <Book [Book2]>])
```

New in version 0.9.0.

```
active
```

Returns the active Book.

`add`()

创建一本新工作簿。 新工作簿成为活动工作簿，返回工作簿对象。

`open`(*fullname*)

如果工作簿尚未打开则打开并返回。 如果它已经打开，它不会引发异常，只是返回工作簿对象。

参数：fullname(str) - 文件名或完全限定的文件名，例如 `C:\path\to\file.xlsx`或`file.xlsm`。 如果没有完整路径，它将在当前工作目录中查找该文件。返回：BookReturn类型：已打开的工作簿。

### Book

*class*`xlwings.``Book`(*fullname=None*, *impl=None*)

book对象是[`books`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474)集合的成员：

```
>>> import xlwings as xw
>>> xw.books[0]
<Book [Book1]>
```

提供：它在所有应用程序实例中查找该工作簿并返回错误，如果同一工作簿在多个实例中打开。 要连接到活动应用程序实例中的g，请使用“xw.books”并引用特定应用程序工作簿，使用：

```
>>> app = xw.App()  # 或类似现有应用程序的xw.apps[10559]，通过xw.apps.keys()获取PID
>>> app.books['Book1']
```

|                    | xw.Book                            | xw.books                                 |
| :----------------- | :--------------------------------- | :--------------------------------------- |
| New book           | `xw.Book()`                        | `xw.books.add()`                         |
| Unsaved book       | `xw.Book('Book1')`                 | `xw.books['Book1']`                      |
| Book by (full)name | `xw.Book(r'C:/path/to/file.xlsx')` | `xw.books.open(r'C:/path/to/file.xlsx')` |

参数：fullname（str，default None） - 现有工作簿的完整路径或名称（包括xlsx，xlsm等）或未保存工作簿的名称。 如果没有完整路径，它将在当前工作目录中查找该文件。

`activate`(*steal_focus=False*)

激活工作簿。

参数：获取焦点（bool，默认为false）–如果为true，则创建最前面的窗口，并将焦点从python移交给excel。
`api`

返回正在使用的引擎的本机对象（`pywin32`或`appscript` obj）。

New in version 0.9.0.

```
app
```

返回表示工作簿创建者的app对象。

New in version 0.9.0.

*类方法*`caller`()

当通过`RunPython`从Excel调用Python函数时引用调用工作簿。 将它打包到从Excel调用的函数中，例如：
为了能够从Python轻松调用此类代码进行调试，请使用

`xw.Book.set_mock_caller()`.

New in version 0.3.0.

`close`()

关闭工作簿而不保存它。

New in version 0.1.1.

```
fullname
```

以字符串形式返回对象的名称，包括其在磁盘上的路径。 只读字符串。

`macro`(*name*)

在Excel VBA中运行Sub或Function。

参数：name（带或不带模块名称的Sub或Function的名称，例如'Module1.MyMacro'或'MyMacro'） -

Examples

This VBA function:

```
Function MySum(x, y)
    MySum = x + y
End Function
```

可以像这样访问：

```
>>> import xlwings as xw
>>> wb = xw.books.active
>>> my_sum = wb.macro('MySum')
>>> my_sum(1, 2)
3
```

See also: [`App.macro()`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.App.macro)

New in version 0.7.1.

```
name
```

以文本形式返回工作簿的名称。

```
names
```

返回一个名称集合，该集合表示指定工作簿中的所有名称（包括所有特定于工作表的名称）。

Changed in version 0.9.0.

*静态*`open_template`()

使用已包含的xlwings VBA模块创建新的Excel文件。 必须从交互式Python shell调用此方法：

```
>>> xw.Book.open_template()
```

See also: [Command Line Client](https://www.kancloud.cn/gnefnuy/xlwings-docs/command_line.html#command-line)

New in version 0.3.3.

`save`(*path=None*)

保存工作簿。 如果提供了路径，则其工作方式类似于Excel中的另存为。 如果未指定路径，并且先前未保存文件，则使用当前文件名将其保存在当前工作目录中。 在没有提示的情况下覆盖现有文件。

参数:path (str, default None) – 工作簿的完整路径

Example

```
>>> import xlwings as xw
>>> wb = xw.Book()
>>> wb.save()
>>> wb.save(r'C:\path\to\new_file_name.xlsx')
```

New in version 0.3.1.

```
selection
```

将所选单元格作为Range返回。

New in version 0.9.0.

`set_mock_caller`()

设置Excel文件，用于在从Python调用代码时模拟`xw.Book.caller()`，而不是通过`RunPython`从Excel调用。

Examples

```
# 此代码在Excel中通过RunPython和Python直接运行
import os
import xlwings as xw

def my_macro():
    sht = xw.Book.caller().sheets[0]
    sht.range('A1').value = 'Hello xlwings!'

if __name__ == '__main__':
    xw.Book('file.xlsm').set_mock_caller()
    my_macro()
```

New in version 0.3.1.

```
sheets
```

返回表示工作簿中所有工作表的工作表集合。

New in version 0.9.0.

### Sheets

*class*`xlwings.main.``Sheets`(*impl*)

A collection of all `sheet` objects:

```
>>> import xlwings as xw
>>> xw.sheets  # active book
Sheets([<Sheet [Book1]Sheet1>, <Sheet [Book1]Sheet2>])
>>> xw.Book('Book1').sheets  # specific book
Sheets([<Sheet [Book1]Sheet1>, <Sheet [Book1]Sheet2>])
```

New in version 0.9.0.

```
active
```

Returns the active Sheet.

`add`(*name=None*, *before=None*, *after=None*)

创建一个新的Sheet并使其成为活动工作表。

参数：name(str,default None) - 新工作表的名称。 如果为None，则默认为Excel的name.before (Sheet, default None) - 一个对象，指定在新工作表添加之前的added.after (Sheet, default None) - 指定工作表之后的工作表的对象 表格已添加。

### Sheet

*class*`xlwings.``Sheet`(*sheet=None*, *impl=None*)

A sheet object is a member of the [`sheets`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.main.Sheets) collection:

```
>>> import xlwings as xw
>>> wb = xw.Book()
>>> wb.sheets[0]
<Sheet [Book1]Sheet1>
>>> wb.sheets['Sheet1']
<Sheet [Book1]Sheet1>
>>> wb.sheets.add()
<Sheet [Book1]Sheet2>
```

Changed in version 0.9.0.

`activate`()

Activates the Sheet and returns it.

```
api
```

Returns the native object (`pywin32` or `appscript` obj) of the engine being used.

New in version 0.9.0.

`autofit`(*axis=None*)

在整个工作表上自动调整列，行或两者的宽度。

参数:axis (string, default None) –要自动调整行, 使用以下之一: rows 或 r，要自动调整列, 使用以下之一: columns h c，要自动调整行和列, 不提供参数

Examples

```
>>> import xlwings as xw
>>> wb = xw.Book()
>>> wb.sheets['Sheet1'].autofit('c')
>>> wb.sheets['Sheet1'].autofit('r')
>>> wb.sheets['Sheet1'].autofit()
```

New in version 0.2.3.

```
book
```

返回指定Sheet的Book。 只读。

```
cells
```

返回一个Range对象，该对象表示Sheet上的所有单元格（而不仅仅是当前正在使用的单元格）。

New in version 0.9.0.

```
charts
```

See [`Charts`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.main.Charts)

New in version 0.9.0.

`clear`()

清除整个工作表的内容和格式。

`clear_contents`()

清除整个工作表的内容但保留格式。

`delete`()

删除工作表。

```
index
```

返回工作表的索引（以1为基准，与Excel相同）。

```
name
```

获取或设置Sheet的名称。

```
names
```

返回表示所有工作表特定名称（使用“SheetName！”前缀定义的名称）的名称集合。

New in version 0.9.0.

```
pictures
```

See [`Pictures`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.main.Pictures)

New in version 0.9.0.

`range`(*cell1*, *cell2=None*)

从活动工作簿的活动工作表中返回Range对象，请参阅[`Range()`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.Range).

New in version 0.9.0.

`select`()

选择工作表。 选择仅适用于活动工作簿。

New in version 0.9.0.

```
shapes
```

See [`Shapes`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.main.Shapes)

New in version 0.9.0.

```
used_range
```

工作表已使用的Range

返回:返回类别:xw.Range

New in version 0.13.0.

### Range

*class*`xlwings.``Range`(*cell1=None*, *cell2=None*, ***可选*)

返回表示单元格或单元格范围的Range对象。

参数:cell1 (str or tuple or Range) – A1表示法左上角或作为索引元组或名称或xw的范围名称.Range对象. 它还可以使用范围运算符（冒号）指定范围, 例如 ‘A1:B2’，cell2 (str or tuple or Range, 默认 None) – 下方范围的名称

Examples

活动工作表:

```
import xlwings as xw
xw.Range('A1')
xw.Range('A1:C3')
xw.Range((1,1))
xw.Range((1,1), (3,3))
xw.Range('NamedRange')
xw.Range(xw.Range('A1'), xw.Range('B2'))
```

特定工作表:

```
xw.books['MyBook.xlsx'].sheets[0].range('A1')
```

`add_hyperlink`(*address*, *text_to_display=None*, *screen_tip=None*)

添加指定范围的超链接（单个单元格）

参数:address (str) – 超链接的地址；text_to_display (str, default None) – 要为超链接显示的文本. 默认为超链接地址；screen_tip (str, default None) – 鼠标指针暂停在超链接上时显示的屏幕提示. Default is set to ‘<address> - Click once to follow. Click and hold to select this cell.’

New in version 0.3.0.

```
address
```

Returns a string value that represents the range reference. Use `get_address()` to be able to provide paramaters.

New in version 0.9.0.

```
api
```

Returns the native object (`pywin32` or `appscript` obj) of the engine being used.

New in version 0.9.0.

`autofit`()

Autofits the width and height of all cells in the range.

- To autofit only the width of the columns use `xw.Range('A1:B2').columns.autofit()`
- To autofit only the height of the rows use `xw.Range('A1:B2').rows.autofit()`

Changed in version 0.9.0.

`clear`()

Clears the content and the formatting of a Range.

`clear_contents`()

Clears the content of a Range but leaves the formatting.

```
color
```

Gets and sets the background color of the specified Range.

To set the color, either use an RGB tuple `(0, 0, 0)` or a color constant. To remove the background, set the color to `None`, see Examples.

Returns:RGBReturn type:tuple

Examples

```
>>> import xlwings as xw
>>> wb = xw.Book()
>>> xw.Range('A1').color = (255,255,255)
>>> xw.Range('A2').color
(255, 255, 255)
>>> xw.Range('A2').color = None
>>> xw.Range('A2').color is None
True
```

New in version 0.3.0.

```
column
```

Returns the number of the first column in the in the specified range. Read-only.

Returns:Return type:Integer

New in version 0.3.5.

```
column_width
```

Gets or sets the width, in characters, of a Range. One unit of column width is equal to the width of one character in the Normal style. For proportional fonts, the width of the character 0 (zero) is used.

If all columns in the Range have the same width, returns the width. If columns in the Range have different widths, returns None.

column_width must be in the range: 0 <= column_width <= 255

Note: If the Range is outside the used range of the Worksheet, and columns in the Range have different widths, returns the width of the first column.

Returns:Return type:float

New in version 0.4.0.

```
columns
```

Returns a [`RangeColumns`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.RangeColumns) object that represents the columns in the specified range.

New in version 0.9.0.

```
count
```

Returns the number of cells.

```
current_region
```

This property returns a Range object representing a range bounded by (but not including) any combination of blank rows and blank columns or the edges of the worksheet. It corresponds to `Ctrl-*` on Windows and `Shift-Ctrl-Space` on Mac.

Returns:Return type:Range object

`end`(*direction*)

Returns a Range object that represents the cell at the end of the region that contains the source range. Equivalent to pressing Ctrl+Up, Ctrl+down, Ctrl+left, or Ctrl+right.

Parameters:direction (One of 'up', 'down', 'right', 'left') –

Examples

```
>>> import xlwings as xw
>>> wb = xw.Book()
>>> xw.Range('A1:B2').value = 1
>>> xw.Range('A1').end('down')
<Range [Book1]Sheet1!$A$2>
>>> xw.Range('B2').end('right')
<Range [Book1]Sheet1!$B$2>
```

New in version 0.9.0.

`expand`(*mode='table'*)

Expands the range according to the mode provided. Ignores empty top-left cells (unlike `Range.end()`).

Parameters:mode (str, default 'table') – One of 'table' (=down and right), 'down', 'right'.Returns:Return type:Range

Examples

```
>>> import xlwings as xw
>>> wb = xw.Book()
>>> xw.Range('A1').value = [[None, 1], [2, 3]]
>>> xw.Range('A1').expand().address
$A$1:$B$2
>>> xw.Range('A1').expand('right').address
$A$1:$B$1
```

New in version 0.9.0.

`formula`
Gets or sets the formula for the given Range.

`formula_array`
Gets or sets an array formula for the given Range.

New in version 0.7.1.

`get_address`(*row_absolute=True*, *column_absolute=True*, *include_sheetname=False*, *external=False*)
Returns the address of the range in the specified format. `address` can be used instead if none of the defaults need to be changed.

Parameters:row_absolute (bool, default True) – Set to True to return the row part of the reference as an absolute reference.column_absolute (bool, default True) – Set to True to return the column part of the reference as an absolute reference.include_sheetname (bool, default False) – Set to True to include the Sheet name in the address. Ignored if external=True.external (bool, default False) – Set to True to return an external reference with workbook and worksheet name.Returns:Return type:str

Examples

```
>>> import xlwings as xw
>>> wb = xw.Book()
>>> xw.Range((1,1)).get_address()
'$A$1'
>>> xw.Range((1,1)).get_address(False, False)
'A1'
>>> xw.Range((1,1), (3,3)).get_address(True, False, True)
'Sheet1!A$1:C$3'
>>> xw.Range((1,1), (3,3)).get_address(True, False, external=True)
'[Book1]Sheet1!A$1:C$3'
```

New in version 0.2.3.

`height`
Returns the height, in points, of a Range. Read-only.

Returns:Return type:float

New in version 0.4.0.

```
hyperlink
```

Returns the hyperlink address of the specified Range (single Cell only)

Examples

```
>>> import xlwings as xw
>>> wb = xw.Book()
>>> xw.Range('A1').value
'www.xlwings.org'
>>> xw.Range('A1').hyperlink
'http://www.xlwings.org'
```

New in version 0.3.0.

```
last_cell
```

Returns the bottom right cell of the specified range. Read-only.

Returns:Return type:Range

Example

```
>>> import xlwings as xw
>>> wb = xw.Book()
>>> rng = xw.Range('A1:E4')
>>> rng.last_cell.row, rng.last_cell.column
(4, 5)
```

New in version 0.3.5.

```
left
```

Returns the distance, in points, from the left edge of column A to the left edge of the range. Read-only.

Returns:Return type:float

New in version 0.6.0.

```
name
```

Sets or gets the name of a Range.

New in version 0.4.0.

```
number_format
```

Gets and sets the number_format of a Range.

Examples

```
>>> import xlwings as xw
>>> wb = xw.Book()
>>> xw.Range('A1').number_format
'General'
>>> xw.Range('A1:C3').number_format = '0.00%'
>>> xw.Range('A1:C3').number_format
'0.00%'
```

New in version 0.2.3.

`offset`(*row_offset=0*, *column_offset=0*)

Returns a Range object that represents a Range that’s offset from the specified range.

Returns:Range objectReturn type:Range

New in version 0.3.0.

`options`(*convert=None*, ***options*)

Allows you to set a converter and their options. Converters define how Excel Ranges and their values are being converted both during reading and writing operations. If no explicit converter is specified, the base converter is being applied, see [Converters and Options](https://www.kancloud.cn/gnefnuy/xlwings-docs/converters.html#converters).

Parameters:convert (object, default None) – A converter, e.g. dict, np.array, pd.DataFrame, pd.Series, defaults to default converterKeyword Arguments: ndim (int, default None) – number of dimensionsnumbers (type, default None) – type of numbers, e.g. intdates (type, default None) – e.g. datetime.date defaults to datetime.datetimeempty (object, default None) – transformation of empty cellstranspose (Boolean, default False) – transpose valuesexpand (str, default None) –One of 'table', 'down', 'right'=> For converter-specific options, see Converters and Options.Returns:Return type:Range object

New in version 0.7.0.

```
raw_value
```

Gets and sets the values directly as delivered from/accepted by the engine that is being used (`pywin32` or `appscript`) without going through any of xlwings’ data cleaning/converting. This can be helpful if speed is an issue but naturally will be engine specific, i.e. might remove the cross-platform compatibility.

`resize`(*row_size=None*, *column_size=None*)
Resizes the specified Range

Parameters:row_size (int > 0) – The number of rows in the new range (if None, the number of rows in the range is unchanged).column_size (int > 0) – The number of columns in the new range (if None, the number of columns in the range is unchanged).Returns:Range objectReturn type:Range

New in version 0.3.0.

```
row
```

Returns the number of the first row in the specified range. Read-only.

Returns:Return type:Integer

New in version 0.3.5.

`row_height`
Gets or sets the height, in points, of a Range. If all rows in the Range have the same height, returns the height. If rows in the Range have different heights, returns None.

row_height must be in the range: 0 <= row_height <= 409.5

Note: If the Range is outside the used range of the Worksheet, and rows in the Range have different heights, returns the height of the first row.

Returns:Return type:float

New in version 0.4.0.

```
rows
```

Returns a [`RangeRows`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.RangeRows) object that represents the rows in the specified range.

New in version 0.9.0.

`select`()

Selects the range. Select only works on the active book.

New in version 0.9.0.

```
shape
```

Tuple of Range dimensions.

New in version 0.3.0.

```
sheet
```

Returns the Sheet object to which the Range belongs.

New in version 0.9.0.

```
size
```

Number of elements in the Range.

New in version 0.3.0.

```
top
```

Returns the distance, in points, from the top edge of row 1 to the top edge of the range. Read-only.

Returns:Return type:float

New in version 0.6.0.

```
value
```

Gets and sets the values for the given Range.

Returns:objectReturn type:returned object depends on the converter being used, see xlwings.Range.options()

```
width
```

Returns the width, in points, of a Range. Read-only.

Returns:Return type:float

New in version 0.4.0.

### RangeRows

*class*`xlwings.``RangeRows`(*rng*)

Represents the rows of a range. Do not construct this class directly, use [`Range.rows`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.Range.rows) instead.

Example

```
import xlwings as xw

rng = xw.Range('A1:C4')

assert len(rng.rows) == 4  # or rng.rows.count

rng.rows[0].value = 'a'

assert rng.rows[2] == xw.Range('A3:C3')
assert rng.rows(2) == xw.Range('A2:C2')

for r in rng.rows:
    print(r.address)
```

`autofit`()

Autofits the height of the rows.

`count`[

Returns the number of rows.

New in version 0.9.0.

### RangeColumns

*class*`xlwings.``RangeColumns`(*rng*)

Represents the columns of a range. Do not construct this class directly, use [`Range.columns`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.Range.columns) instead.

Example

```
import xlwings as xw

rng = xw.Range('A1:C4')

assert len(rng.columns) == 3  # or rng.columns.count

rng.columns[0].value = 'a'

assert rng.columns[2] == xw.Range('C1:C4')
assert rng.columns(2) == xw.Range('B1:B4')

for c in rng.columns:
    print(c.address)
```

`autofit`()

Autofits the width of the columns.

```
count
```

Returns the number of columns.

New in version 0.9.0.

### Shapes

*class*`xlwings.main.``Shapes`(*impl*)

A collection of all `shape` objects on the specified sheet:

```
>>> import xlwings as xw
>>> xw.books['Book1'].sheets[0].shapes
Shapes([<Shape 'Oval 1' in <Sheet [Book1]Sheet1>>, <Shape 'Rectangle 1' in <Sheet [Book1]Sheet1>>])
```

New in version 0.9.0.

```
api
```

Returns the native object (`pywin32` or `appscript` obj) of the engine being used.

```
count
```

Returns the number of objects in the collection.

### Shape

*class*`xlwings.``Shape`(**args*, ***options*)

The shape object is a member of the [`shapes`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.main.Shapes) collection:

```
>>> import xlwings as xw
>>> sht = xw.books['Book1'].sheets[0]
>>> sht.shapes[0]  # or sht.shapes['ShapeName']
<Shape 'Rectangle 1' in <Sheet [Book1]Sheet1>>
```

Changed in version 0.9.0.

`activate`()

Activates the shape.

New in version 0.5.0.

`delete`()

Deletes the shape.

New in version 0.5.0.

```
height
```

Returns or sets the number of points that represent the height of the shape.

New in version 0.5.0.

```
left
```

Returns or sets the number of points that represent the horizontal position of the shape.

New in version 0.5.0.

```
name
```

Returns or sets the name of the shape.

New in version 0.5.0.

```
parent
```

Returns the parent of the shape.

New in version 0.9.0.

```
top
```

Returns or sets the number of points that represent the vertical position of the shape.

New in version 0.5.0.

```
type
```

Returns the type of the shape.

New in version 0.9.0.

```
width
```

Returns or sets the number of points that represent the width of the shape.

New in version 0.5.0.

### Charts

*class*`xlwings.main.``Charts`(*impl*)

A collection of all `chart` objects on the specified sheet:

```
>>> import xlwings as xw
>>> xw.books['Book1'].sheets[0].charts
Charts([<Chart 'Chart 1' in <Sheet [Book1]Sheet1>>, <Chart 'Chart 1' in <Sheet [Book1]Sheet1>>])
```

New in version 0.9.0.

`add`(*left=0*, *top=0*, *width=355*, *height=211*)

Creates a new chart on the specified sheet.

Parameters:left (float, default 0) – left position in pointstop (float, default 0) – top position in pointswidth (float, default 355) – width in pointsheight (float, default 211) – height in pointsReturns:Return type:Chart

Examples

```
>>> import xlwings as xw
>>> sht = xw.Book().sheets[0]
>>> sht.range('A1').value = [['Foo1', 'Foo2'], [1, 2]]
>>> chart = sht.charts.add()
>>> chart.set_source_data(sht.range('A1').expand())
>>> chart.chart_type = 'line'
>>> chart.name
'Chart1'
api
```

Returns the native object (`pywin32` or `appscript` obj) of the engine being used.

```
count
```

Returns the number of objects in the collection.

### Chart

*class*`xlwings.``Chart`(*name_or_index=None*, *impl=None*)

The chart object is a member of the [`charts`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.main.Charts) collection:

```
>>> import xlwings as xw
>>> sht = xw.books['Book1'].sheets[0]
>>> sht.charts[0]  # or sht.charts['ChartName']
<Chart 'Chart 1' in <Sheet [Book1]Sheet1>>
api
```

Returns the native object (`pywin32` or `appscript` obj) of the engine being used.

New in version 0.9.0.

```
chart_type
```

Returns and sets the chart type of the chart.

New in version 0.1.1.

`delete`()

Deletes the chart.

```
height
```

Returns or sets the number of points that represent the height of the chart.

```
left
```

Returns or sets the number of points that represent the horizontal position of the chart.

```
name
```

Returns or sets the name of the chart.

```
parent
```

Returns the parent of the chart.

New in version 0.9.0.

`set_source_data`(*source*)

Sets the source data range for the chart.

Parameters:source (Range) – Range object, e.g. xw.books['Book1'].sheets[0].range('A1')

```
top
```

Returns or sets the number of points that represent the vertical position of the chart.

```
width
```

Returns or sets the number of points that represent the width of the chart.

### Pictures

*class*`xlwings.main.``Pictures`(*impl*)

A collection of all `picture` objects on the specified sheet:

```
>>> import xlwings as xw
>>> xw.books['Book1'].sheets[0].pictures
Pictures([<Picture 'Picture 1' in <Sheet [Book1]Sheet1>>, <Picture 'Picture 2' in <Sheet [Book1]Sheet1>>])
```

New in version 0.9.0.

`add`(*image*, *link_to_file=False*, *save_with_document=True*, *left=0*, *top=0*, *width=None*, *height=None*, *name=None*, *update=False*)

Adds a picture to the specified sheet.

Parameters:image (str or matplotlib.figure.Figure) – Either a filepath or a Matplotlib figure object.left (float, default 0) – Left position in points.top (float, default 0) – Top position in points.width (float, default None) – Width in points. If PIL/Pillow is installed, it defaults to the width of the picture. Otherwise it defaults to 100 points.height (float, default None) – Height in points. If PIL/Pillow is installed, it defaults to the height of the picture. Otherwise it defaults to 100 [points.name](http://points.name/) (str, default None) – Excel picture name. Defaults to Excel standard name if not provided, e.g. ‘Picture 1’.update (bool, default False) – Replace an existing picture with the same name. Requires name to be set.Returns:Return type:Picture

Examples

1. Picture

```
>>> import xlwings as xw
>>> sht = xw.Book().sheets[0]
>>> sht.pictures.add(r'C:\path\to\file.jpg')
<Picture 'Picture 1' in <Sheet [Book1]Sheet1>>
```

1. Matplotlib

```
>>> import matplotlib.pyplot as plt
>>> fig = plt.figure()
>>> plt.plot([1, 2, 3, 4, 5])
>>> sht.pictures.add(fig, name='MyPlot', update=True)
<Picture 'MyPlot' in <Sheet [Book1]Sheet1>>
api
```

Returns the native object (`pywin32` or `appscript` obj) of the engine being used.

```
count
```

Returns the number of objects in the collection.

### Picture

*class*`xlwings.``Picture`(*impl=None*)

The picture object is a member of the [`pictures`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.main.Pictures) collection:

```
>>> import xlwings as xw
>>> sht = xw.books['Book1'].sheets[0]
>>> sht.pictures[0]  # or sht.charts['PictureName']
<Picture 'Picture 1' in <Sheet [Book1]Sheet1>>
```

Changed in version 0.9.0.

```
api
```

Returns the native object (`pywin32` or `appscript` obj) of the engine being used.

New in version 0.9.0.

`delete`()

Deletes the picture.

New in version 0.5.0.

```
height
```

Returns or sets the number of points that represent the height of the picture.

New in version 0.5.0.

```
left
```

Returns or sets the number of points that represent the horizontal position of the picture.

New in version 0.5.0.

```
name
```

Returns or sets the name of the picture.

New in version 0.5.0.

```
parent
```

Returns the parent of the picture.

New in version 0.9.0.

```
top
```

Returns or sets the number of points that represent the vertical position of the picture.

New in version 0.5.0.

`update`(*image*)

Replaces an existing picture with a new one, taking over the attributes of the existing picture.

Parameters:image (str or matplotlib.figure.Figure) – Either a filepath or a Matplotlib figure object.

New in version 0.5.0.

```
width
```

Returns or sets the number of points that represent the width of the picture.

New in version 0.5.0.

### Names

*class*`xlwings.main.``Names`(*impl*)

A collection of all `name` objects in the workbook:

```
>>> import xlwings as xw
>>> sht = xw.books['Book1'].sheets[0]
>>> sht.names
[<Name 'MyName': =Sheet1!$A$3>]
```

New in version 0.9.0.

`add`(*name*, *refers_to*)

Defines a new name for a range of cells.

Parameters:name (str) – Specifies the text to use as the name. Names cannot include spaces and cannot be formatted as cell references.refers_to (str) – Describes what the name refers to, in English, using A1-style notation.Returns:Return type:Name

New in version 0.9.0.

```
api
```

Returns the native object (`pywin32` or `appscript` obj) of the engine being used.

New in version 0.9.0.

```
count
```

Returns the number of objects in the collection.

### Name

*class*`xlwings.``Name`(*impl*)

The name object is a member of the [`names`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.main.Names) collection:

```
>>> import xlwings as xw
>>> sht = xw.books['Book1'].sheets[0]
>>> sht.names[0]  # or sht.names['MyName']
<Name 'MyName': =Sheet1!$A$3>
```

New in version 0.9.0.

```
api
```

Returns the native object (`pywin32` or `appscript` obj) of the engine being used.

New in version 0.9.0.

`delete`()

Deletes the name.

New in version 0.9.0.

```
name
```

Returns or sets the name of the name object.

New in version 0.9.0.

```
refers_to
```

Returns or sets the formula that the name is defined to refer to, in A1-style notation, beginning with an equal sign.

New in version 0.9.0.

```
refers_to_range
```

Returns the Range object referred to by a Name object.

New in version 0.9.0.

## UDF decorators

`xlwings.``func`(*category="xlwings"*, *volatile=False*, *call_in_wizard=True*)

Functions decorated with `xlwings.func` will be imported as `Function` to Excel when running “Import Python UDFs”.

category : int or str, default “xlwings”

1-14 represent built-in categories, for user-defined categories use strings

New in version 0.10.3.

volatile : bool, default False

Marks a user-defined function as volatile. A volatile function must be recalculated whenever calculation occurs in any cells on the worksheet. A nonvolatile function is recalculated only when the input variables change. This method has no effect if it’s not inside a user-defined function used to calculate a worksheet cell.

New in version 0.10.3.

call_in_wizard : bool, default True

Set to False to suppress the function call in the function wizard.

New in version 0.10.3.

`xlwings.``sub`()

Functions decorated with `xlwings.sub` will be imported as `Sub` (i.e. macro) to Excel when running “Import Python UDFs”.

`xlwings.``arg`(*arg*, *convert=None*, ***options*)

Apply converters and options to arguments, see also [`Range.options()`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.Range.options).

**Examples:**

Convert `x` into a 2-dimensional numpy array:

```
import xlwings as xw
import numpy as np

@xw.func
@xw.arg('x', np.array, ndim=2)
def add_one(x):
    return x + 1
```

`xlwings.``ret`(*convert=None*, ***options*)

Apply converters and options to return values, see also [`Range.options()`](https://www.kancloud.cn/gnefnuy/xlwings-docs/1127474#xlwings.Range.options).

**Examples**

1. Suppress the index and header of a returned DataFrame:

```
import pandas as pd

@xw.func
@xw.ret(index=False, header=False)
def get_dataframe(n, m):
    return pd.DataFrame(np.arange(n * m).reshape((n, m)))
```

1. Dynamic array:

`expand='table'` turns the UDF into a dynamic array. Currently you must not use volatile functions as arguments of a dynamic array, e.g. you cannot use `=TODAY()` as part of a dynamic array. Also note that a dynamic array needs an empty row and column at the bottom and to the right and will overwrite existing data without warning.

Unlike standard Excel arrays, dynamic arrays are being used from a single cell like a standard function and auto-expand depending on the dimensions of the returned array:

```
import xlwings as xw
import numpy as np

@xw.func
@xw.ret(expand='table')
def dynamic_array(n, m):
    return np.arange(n * m).reshape((n, m))
```

New in version 0.10.0.