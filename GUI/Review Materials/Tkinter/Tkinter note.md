# GUI-tkinter/tcl

## Before all

If you have any question, please seek the  [Docs](https://www.tcl.tk/doc/)  for answer. Learn more by refering to the  [tutorial](https://www.tcl.tk/man/tcl8.5/tutorial/tcltutorial.html) .

Tip : there something different with normal.

⬜⚪▭□△○◯

## Synopsis

> **Tcl**：工具命令语言，英文全称为Tool Command Language，它是一个非常强大，易学习动态编程语言，应用广泛。包括网页和桌面应用，网络，管理，测试，除此之外，还有很多其他应用。开源和商业友好，Tcl是一个成熟但不断发展的语言，是真正的跨平台，易于部署，高度可扩展的语言。
>
> **Tk**：图形用户界面工具包，英文为graphical user interface toolkit，它将开发桌面应用程序带到比传统方法更高水平。 Tk是Tcl和许多其他动态语言的标准图形用户界面，能产生丰富的本地应用程序，并且无需改变，就可在Windows，Mac OS X、Linux和更多平台上运行。

**略过cmd窗口只需将后缀名 .py 改为 .pyw 即可**



## Standard Attribute

> Standard properties are the common properties of all controls, such as size, font, color, and so on.

**And you can index them by `widget.cget("Attribute")` .**

| 属性       | 描述                |
| ---------- | ------------------- |
| Dimension  | 控件大小            |
| Color      | 控件颜色            |
| Font       | 控件字体            |
| Anchor     | 锚点                |
| Relief     | 控件样式            |
| Bitmap     | 位图                |
| Cursor     | 光标                |
| Image      | **图片；只支持GIF** |
| justify    | 对齐方式            |
| destroy    | 销毁组件            |
| highlight- | 具有焦点特性        |
| active-    | 具有焦点效果        |
| select-    | 选中效果            |

#### About config

> 1. 传参
>
>    label(text = ''who ")
>
> 2. 字典索引赋值
>
>    label['text'] = 'who'
>
> 3. config方法
>
>    label.config(text = 'who')

#### About Image

`tk.PhotoImage` only support .gif file, but **it doesn't raise an error** with other format, can't indicate image either, if you post a image of `.jpg` or formats else, you can use method below.

```python
from PIL import Image, ImageTk
background_image = ImageTk.PhotoImage(Image.open(filepath))
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)
```

> It's worth mentioning that if you define image as a **local** variable, it will be distroy after call, and can't be show normally. To solve this problem, you need to define it **global** variable to maintain it.

#### About color

backgroundcolor of window is `"SystemButtonFace"`, you can index it by `Tk().cget('bg')` .

**And ld/thinkness is need when you refer to the highlightcolor and else.**

Here is the common color of tkinter.

![Tk颜色库，from笑待人生原创库](E:\工具\Typora\Temp\20200226214558104.png)

## Base Widget

### Before Tk

#### 1. 窗口创建与标题

```python
tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
```

`Tk` 类被初始化时无参数。此时会创建一个 Tk 顶级控件，通常是应用程序的主窗口。每个实例都有自己关联的 Tcl 解释器。

```python
root.title('name')  　　 
```

修改框体的名字,也可在创建时使用className参数来命名；



#### 2. 取消主窗口

```python
tk.withdraw()
```

撤销主窗口。



#### 3. 窗口大小

```python
tk.geometry(width,height,x,y)
```

窗口显示绝对位置以及大小。

```python
tk.resizable(width=False, height=False)
# tk.resizable(0, 0)
```

固定窗口大小，不允许改变。

**屏幕居中显示**

```python
window.update()
x, y = window.maxsize() # 获取当前屏幕像素
width, height = 200, 200
x, y = int(x/2-width/2), int(y/2-height/2)  # 计算屏幕中心坐标
window.geometry("%dx%d+%d+%d"%(width, height,x,y))  # 居中显示
```



#### 4. 退出窗口

```python
window.quit() 
```



#### 5. 刷新窗口

```python
root.update_idletasks()
root.update() 
```



#### 6. 窗口图标

```python
window.iconbitmap(path)
```

**Tip:关于icon图标制作**

```python
import PythonMagick
img = PythonMagick.Image('robin.jpg')
img.sample('128x128')
img.write('robin.ico')
```

---

### 1. Label

> Label的textvariable暂时未发现可以直接使用的方法（其他控件可直接调用），若直接调用label标签会始终无法读取变量值，可通过Label["text"] = string 实现动态改变文本。



### 2. Button

**简单说明：**

Button（按钮）部件是一个标准的Tkinter窗口部件，用来实现各种按钮。按钮能够包含文本或图象，并且你能够将按钮与一个Python函数或方法相关联。当这个按钮被按下时，Tkinter自动调用相关联的函数或方法。

按钮仅能显示一种字体，但是这个文本可以跨行。另外，这个文本中的一个字母可以有下划线，例如标明一个快捷键。默认情况，Tab键用于将焦点移动到一个按钮部件。

**参数**

| Params       | Optional | Discription                     |
| ------------ | -------- | ------------------------------- |
| command      | True     | 指定按钮消息的回调函数；        |
| state        | True     | 指定按钮的状态（disabled）；    |
| text         | False    | 指定按钮上显示的文本；          |
| textvariable | True     | 可变文本，与StringVar等配合着用 |



### 3. Entry

**简单说明：**　　

Entry是tkinter类中提供的的一个单行文本输入域，用来输入显示一行文本，收集键盘输入(类似 HTML 中的 text)。

**什么时候用：**

需要用户输入用户信息时，比如我们平时使用软件、登录网页时，用户交互界面让我们登录账户信息等时候可以用到。



### 4. Text

#### Params

> Command-Line Name: **-autoseparators**
>
> Database Name: **autoSeparators**
>
> Database Class: **AutoSeparators**
>
> Specifies a boolean that says whether separators are automatically inserted in the undo stack. Only meaningful when the **-undo** option is true.
>
> Command-Line Name: **-blockcursor**
>
> Database Name: **blockCursor**
>
> Database Class: **BlockCursor**
>
> Specifies a boolean that says whether the blinking insertion cursor should be drawn as a character-sized rectangular block. If false (the default) a thin vertical line is used for the insertion cursor.
>
> Command-Line Name: **-endline**
>
> Database Name: **endLine**
>
> Database Class: **EndLine**
>
> Specifies an integer line index representing the line of the underlying textual data store that should be just after the last line contained in the widget. This allows a text widget to reflect only a portion of a larger piece of text. Instead of an integer, the empty string can be provided to this configuration option, which will configure the widget to end at the very last line in the textual data store.
>
> Command-Line Name: **-height**
>
> Database Name: **height**
>
> Database Class: **Height**
>
> Specifies the desired height for the window, in units of characters in the font given by the **-font** option. Must be at least one.
>
> Command-Line Name: **-inactiveselectbackground**
>
> Database Name: **inactiveSelectBackground**
>
> Database Class: **Foreground**
>
> Specifies the colour to use for the selection (the **sel** tag) when the window does not have the input focus. If empty, **{}**, then no selection is shown when the window does not have the focus.
>
> Command-Line Name: **-insertunfocussed**
>
> Database Name: **insertUnfocussed**
>
> Database Class: **InsertUnfocussed**
>
> Specifies how to display the insertion cursor when the widget does not have the focus. Must be **none** (the default) which means to not display the cursor, **hollow** which means to display a hollow box, or **solid** which means to display a solid box. Note that **hollow** and **solid** will appear very similar when the **-blockcursor** option is false.
>
> Command-Line Name: **-maxundo**
>
> Database Name: **maxUndo**
>
> Database Class: **MaxUndo**
>
> Specifies the maximum number of compound undo actions on the undo stack. A zero or a negative value imply an unlimited undo stack.
>
> Command-Line Name: **-spacing1**
>
> Database Name: **spacing1**
>
> Database Class: **Spacing1**
>
> Requests additional space above each text line in the widget, using any of the standard forms for screen distances. If a line wraps, this option only applies to the first line on the display. This option may be overridden with **-spacing1** options in tags.
>
> Command-Line Name: **-spacing2**
>
> Database Name: **spacing2**
>
> Database Class: **Spacing2**
>
> For lines that wrap (so that they cover more than one line on the display) this option specifies additional space to provide between the display lines that represent a single line of text. The value may have any of the standard forms for screen distances. This option may be overridden with **-spacing2** options in tags.
>
> Command-Line Name: **-spacing3**
>
> Database Name: **spacing3**
>
> Database Class: **Spacing3**
>
> Requests additional space below each text line in the widget, using any of the standard forms for screen distances. If a line wraps, this option only applies to the last line on the display. This option may be overridden with **-spacing3** options in tags.
>
> Command-Line Name: **-startline**
>
> Database Name: **startLine**
>
> Database Class: **StartLine**
>
> Specifies an integer line index representing the first line of the underlying textual data store that should be contained in the widget. This allows a text widget to reflect only a portion of a larger piece of text. Instead of an integer, the empty string can be provided to this configuration option, which will configure the widget to start at the very first line in the textual data store.
>
> Command-Line Name: **-state**
>
> Database Name: **state**
>
> Database Class: **State**
>
> Specifies one of two states for the text: **normal** or **disabled**. If the text is disabled then characters may not be inserted or deleted and no insertion cursor will be displayed, even if the input focus is in the widget.
>
> Command-Line Name: **-tabs**
>
> Database Name: **tabs**
>
> Database Class: **Tabs**
>
> Specifies a set of tab stops for the window. The option's value consists of a list of screen distances giving the positions of the tab stops, each of which is a distance relative to the left edge of the widget (excluding borders, padding, etc). Each position may optionally be followed in the next list element by one of the keywords **left**, **right**, **center**, or **numeric**, which specifies how to justify text relative to the tab stop. **Left** is the default; it causes the text following the tab character to be positioned with its left edge at the tab position. **Right** means that the right edge of the text following the tab character is positioned at the tab position, and **center** means that the text is centered at the tab position. **Numeric** means that the decimal point in the text is positioned at the tab position; if there is no decimal point then the least significant digit of the number is positioned just to the left of the tab position; if there is no number in the text then the text is right-justified at the tab position. For example, “**-tabs {2c left 4c 6c center}**” creates three tab stops at two-centimeter intervals; the first two use left justification and the third uses center justification.If the list of tab stops does not have enough elements to cover all of the tabs in a text line, then Tk extrapolates new tab stops using the spacing and alignment from the last tab stop in the list. Tab distances must be strictly positive, and must always increase from one tab stop to the next (if not, an error is thrown). The value of the **-tabs** option may be overridden by **-tabs** options in tags.If no **-tabs** option is specified, or if it is specified as an empty list, then Tk uses default tabs spaced every eight (average size) characters. To achieve a different standard spacing, for example every 4 characters, simply configure the widget with “**-tabs "[expr {4 \* [font measure $font 0]}] left" -tabstyle wordprocessor**”.
>
> Command-Line Name: **-tabstyle**
>
> Database Name: **tabStyle**
>
> Database Class: **TabStyle**
>
> Specifies how to interpret the relationship between tab stops on a line and tabs in the text of that line. The value must be **tabular** (the default) or **wordprocessor**. Note that tabs are interpreted as they are encountered in the text. If the tab style is **tabular** then the *n*'th tab character in the line's text will be associated with the *n*'th tab stop defined for that line. If the tab character's x coordinate falls to the right of the *n*'th tab stop, then a gap of a single space will be inserted as a fallback. If the tab style is **wordprocessor** then any tab character being laid out will use (and be defined by) the first tab stop to the right of the preceding characters already laid out on that line. The value of the **-tabstyle** option may be overridden by **-tabstyle** options in tags.
>
> Command-Line Name: **-undo**
>
> Database Name: **undo**
>
> Database Class: **Undo**
>
> Specifies a boolean that says whether the undo mechanism is active or not.
>
> Command-Line Name: **-width**
>
> Database Name: **width**
>
> Database Class: **Width**
>
> Specifies the desired width for the window in units of characters in the font given by the **-font** option. If the font does not have a uniform width then the width of the character “0” is used in translating from character units to screen units.
>
> Command-Line Name: **-wrap**
>
> Database Name: **wrap**
>
> Database Class: **Wrap**
>
> Specifies how to handle lines in the text that are too long to be displayed in a single line of the text's window. The value must be **none** or **char** or **word**. A wrap mode of **none** means that each line of text appears as exactly one line on the screen; extra characters that do not fit on the screen are not displayed. In the other modes each line of text will be broken up into several screen lines if necessary to keep all the characters visible. In **char** mode a screen line break may occur after any character; in **word** mode a line break will only be made at word boundaries.

#### Function

##### get

```python
text.get(index, index)
```

> Different from `Entry`, the index params of the get function of `Text` isn't optional indeed, it must be line.column format. For example, to get all content of text, you should use `get(1.0, tk.END)`(instead of `0.0`)

##### delete

```python
text.delete(index, index)
```

> the same as `get`.

### 5. Listbox

**简单说明：**　　

Text是tkinter类中提供的的列表框部件，显示供选方案的一个列表。listbox能够被配置来得到radiobutton或checklist的行为。

**什么时候用：**

在有一个很多内容选项组成的列表提供用户选择时会用到。



### 6. Radiobutton

#### Description

> In fact, radiobutton is a label, it's just achieved by changing text of label. Showing a choose circle and text first, and then change to a fonticon with two circle and text. Simultaneously, binded with event <Button-1>, so that can make choose true.
>
> Additionally, you can set a variable to make a just one choose from mulitiple radiobutton, and set a initial value to make one selected as default.

#### Format

```python
choice = tk.Radiobutton(master, *args)
```

#### Params

| Params              | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| command             | 此选项设置为每当更改单选按钮的状态时必须调用的过程。         |
| selectcolor         | 选中时单选按钮的颜色。                                       |
| selectimage         | 选择时在radiobutton上显示的图像。                            |
| state               | 它表示单选按钮的状态。 Radiobutton的默认状态为NORMAL。但是，我们可以将其设置为DISABLED以使radiobutton无响应。 |
| text                | 要在radiobutton上显示的文本。                               |
| textvariable        | 它是String类型，表示小部件显示的文本。                       |
| underline           | 此选项的默认值为-1，但是，我们可以将此选项设置为要加下划线的字符数。 |
| value               | 每个radiobutton的值在用户打开时分配给控制变量。              |
| variable            | 它是控制变量，用于跟踪用户的选择。它在所有radiobutton之间共享。 |
| wraplength          | 我们可以通过将此选项设置为所需的数字来将文本换行到行数，以便每行只包含该数量的字符。 |

#### Function

| Function   | Description                                     |
| ---------- | ----------------------------------------------- |
| deselect() | 用于转动单选按钮。                              |
| flash()    | 用于在有效和正常颜色之间闪烁几次无线电按钮。    |
| invoke()   | 它用于调用Radiobutton状态更改时关联的任何过程。 |
| select()   | 用于选择radiobutton。                           |



### 7. Checkbutton

**简单说明：**　　

**Checkbutton：**代表一个变量，它有两个不同的值。点击这个按钮将会在这两个值间切换，选择和取消选择。

**什么时候用：**

在有一个很多内容选项组成的选项列表提供用户选择时会用到，用户一次可以选择多个。



### 8. Scale

**简单说明**　　

**Scale： 尺度（拉动条），**允许你通过滑块来设置一数字值。

**使用环境**

在需要用户给出评价等级，或者给出一个评价分数，或者拉动滑动条提供一个具体的数值等等。



### 9. Canvas

**简单说明：**　　

**Canvas：画布，**提供绘图功能(直线、椭圆、多边形、矩形) 可以包含图形或位图，用来绘制图表和图，创建图形编辑器，实现定制窗口部件。

**什么时候用：**

在比如像用户交互界面等，需要提供设计的图标、图形、logo等信息是可以用到画布。

**示例代码：**

```python
# 第4步，在图形界面上创建 500 * 200 大小的画布并放置各种元素
canvas = tk.Canvas(window, bg='green', height=200, width=500)
# 说明图片位置，并导入图片到画布上
image_file = tk.PhotoImage(file='pic.gif')  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
image = canvas.create_image(250, 0, anchor='n',image=image_file)        # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
# 定义多边形参数，然后在画布上画出指定图形
x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)                   # 画直线
oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')  # 画圆 用黄色填充
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)      # 画扇形 从0度打开收到180度结束
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)                  # 画矩形正方形
canvas.pack()
# 第6步，触发函数，用来一定指定图形
def moveit():
    canvas.move(rect, 2, 2) # 移动正方形rect（也可以改成其他图形名字用以移动一起图形、元素），按每次（x=2, y=2）步长进行移动
# 第5步，定义一个按钮用来移动指定图形的在画布上的位置
b = tk.Button(window, text='move item',command=moveit).pack()
# 第7步，主窗口循环显示
window.mainloop()
```

　　**图片锚定点位置参数图：**

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808214423234-2053303150.png)

　　**测试效果：**

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808214010611-964561892.png)![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808214052169-1659760377.png)

#### Create

##### 1. Line

Items of type **line** appear on the display as one or more connected line segments or curves. Line items support coordinate indexing operations using the **dchars**, **index** and **insert** widget commands. Lines are created with widget commands of the following form:

```
pathName create line x1 y1... xn yn ?option value ...?
pathName create line coordList ?option value ...?
```

The arguments *x1* through *yn* or *coordList* give the coordinates for a series of two or more points that describe a series of connected line segments. After the coordinates there may be any number of *option*-*value* pairs, each of which sets one of the configuration options for the item. These same *option*-*value* pairs may be used in **itemconfigure** widget commands to change the item's configuration. A line item is the current item whenever the mouse pointer is over any segment of the line, whether drawn or not and whether or not the line is smoothed.

The following standard options are supported by lines:

| **-dash**          | **-activedash**      |
| ------------------ | -------------------- |
| **-disableddash**  | **-dashoffset**      |
| **-fill**          | **-activefill**      |
| **-disabledfill**  | **-stipple**         |
| **-activestipple** | **-disabledstipple** |
| **-state**         | **-tags**            |
| **-width**         | **-activewidth**     |
| **-disabledwidth** |                      |

The following extra options are supported for lines:

- **-arrow** *where*

  Indicates whether or not arrowheads are to be drawn at one or both ends of the line. *Where* must have one of the values **none** (for no arrowheads), **first** (for an arrowhead at the first point of the line), **last** (for an arrowhead at the last point of the line), or **both** (for arrowheads at both ends). This option defaults to **none**. When requested to draw an arrowhead, Tk internally adjusts the corresponding line end point so that the rendered line ends at the neck of the arrowhead rather than at its tip so that the line doesn't extend past the edge of the arrowhead. This may trigger a **Leave** event if the mouse is hovering this line end. Conversely, when removing an arrowhead Tk adjusts the corresponding line point the other way round, which may trigger an **Enter** event.

- **-arrowshape** *shape*

  This option indicates how to draw arrowheads. The *shape* argument must be a list with three elements, each specifying a distance in any of the forms described in the **COORDINATES** section above. The first element of the list gives the distance along the line from the neck of the arrowhead to its tip. The second element gives the distance along the line from the trailing points of the arrowhead to the tip, and the third element gives the distance from the outside edge of the line to the trailing points. If this option is not specified then Tk picks a “reasonable” shape.

- **-capstyle** *style*

  Specifies the ways in which caps are to be drawn at the endpoints of the line. *Style* may have any of the forms accepted by **[Tk_GetCapStyle](https://www.tcl.tk/man/tcl8.6/TkLib/GetCapStyl.htm)** (**butt**, **projecting**, or **round**). If this option is not specified then it defaults to **butt**. Where arrowheads are drawn the cap style is ignored.

- **-joinstyle** *style*

  Specifies the ways in which joints are to be drawn at the vertices of the line. *Style* may have any of the forms accepted by **[Tk_GetJoinStyle](https://www.tcl.tk/man/tcl8.6/TkLib/GetJoinStl.htm)** (**bevel**, **miter**, or **round**). If this option is not specified then it defaults to **round**. If the line only contains two points then this option is irrelevant.

- **-smooth** *smoothMethod*

  *smoothMethod* must have one of the forms accepted by **[Tcl_GetBoolean](https://www.tcl.tk/man/tcl8.6/TclLib/GetInt.htm)** or a line smoothing method. Only **true** and **raw** are supported in the core (with **bezier** being an alias for **true**), but more can be added at runtime. If a boolean false value or empty string is given, no smoothing is applied. A boolean truth value assumes **true** smoothing. If the smoothing method is **true**, this indicates that the line should be drawn as a curve, rendered as a set of quadratic splines: one spline is drawn for the first and second line segments, one for the second and third, and so on. Straight-line segments can be generated within a curve by duplicating the end-points of the desired line segment. If the smoothing method is **raw**, this indicates that the line should also be drawn as a curve but where the list of coordinates is such that the first coordinate pair (and every third coordinate pair thereafter) is a knot point on a cubic Bezier curve, and the other coordinates are control points on the cubic Bezier curve. Straight line segments can be generated within a curve by making control points equal to their neighbouring knot points. If the last point is a control point and not a knot point, the point is repeated (one or two times) so that it also becomes a knot point.

- **-splinesteps** *number*

  Specifies the degree of smoothness desired for curves: each spline will be approximated with *number* line segments. This option is ignored unless the **-smooth** option is true or **raw**.

##### 2. oval

Items of type **oval** appear as circular or oval regions on the display. Each oval may have an outline, a fill, or both. Ovals are created with widget commands of the following form:

```
pathName create oval x1 y1 x2 y2 ?option value ...?
pathName create oval coordList ?option value ...?
```

The arguments *x1*, *y1*, *x2*, and *y2* or *coordList* give the coordinates of two diagonally opposite corners of a rectangular region enclosing the oval. The oval will include the top and left edges of the rectangle not the lower or right edges. If the region is square then the resulting oval is circular; otherwise it is elongated in shape. After the coordinates there may be any number of *option*-*value* pairs, each of which sets one of the configuration options for the item. These same *option*-*value* pairs may be used in **itemconfigure** widget commands to change the item's configuration. An oval item becomes the current item when the mouse pointer is over any part that is painted or (when fully transparent) that would be painted if both the **-fill** and **-outline** options were non-empty.

The following standard options are supported by ovals:

| **-dash**                   | **-activedash**           |
| --------------------------- | ------------------------- |
| **-disableddash**           | **-dashoffset**           |
| **-fill**                   | **-activefill**           |
| **-disabledfill**           | **-offset**               |
| **-outline**                | **-activeoutline**        |
| **-disabledoutline**        | **-outlineoffset**        |
| **-outlinestipple**         | **-activeoutlinestipple** |
| **-disabledoutlinestipple** | **-stipple**              |
| **-activestipple**          | **-disabledstipple**      |
| **-state**                  | **-tags**                 |
| **-width**                  | **-activewidth**          |
| **-disabledwidth**          |                           |

There are no oval-specific options.



### 10. Menu

#### Description

> The **menu** command creates a new top-level window (given by the *pathName* argument) and makes it into a menu widget. That menu widget can either be used as a pop-up window or applied to a **[toplevel](https://www.tcl.tk/man/tcl8.6/TkCmd/toplevel.htm)** (with its **-menu** option) to make it into the menubar for that toplevel. Additional options, described above, may be specified on the command line or in the option database to configure aspects of the menu such as its colors and font. The **menu** command returns its *pathName* argument. At the time this command is invoked, there must not exist a window named *pathName*, but *pathName*'s parent must exist.
>
> A menu is a widget that displays a collection of one-line entries arranged in one or more columns. There exist several different types of entries, each with different properties. Entries of different types may be combined in a single menu. Menu entries are not the same as entry widgets. In fact, menu entries are not even distinct widgets; the entire menu is one widget.
>
> Menu entries are displayed with up to three separate fields. The main field is a label in the form of a text string, a bitmap, or an image, controlled by the **-label**, **-bitmap**, and **-image** options for the entry. If the **-accelerator** option is specified for an entry then a second textual field is displayed to the right of the label. The accelerator typically describes a keystroke sequence that may be used in the application to cause the same result as invoking the menu entry. This is a display option, it does not actually set the corresponding binding (which can be achieved using the **[bind](https://www.tcl.tk/man/tcl8.6/TkCmd/bind.htm)** command). The third field is an *indicator*. The indicator is present only for checkbutton or radiobutton entries. It indicates whether the entry is selected or not, and is displayed to the left of the entry's string.
>
> In normal use, an entry becomes active (displays itself differently) whenever the mouse pointer is over the entry. If a mouse button is released over the entry then the entry is *invoked*. The effect of invocation is different for each type of entry; these effects are described below in the sections on individual entries.
>
> Entries may be *disabled*, which causes their labels and accelerators to be displayed with dimmer colors. The default menu bindings will not allow a disabled entry to be activated or invoked. Disabled entries may be re-enabled, at which point it becomes possible to activate and invoke them again.
>
> Whenever a menu's active entry is changed, a <<MenuSelect>> virtual event is send to the menu. The active item can then be queried from the menu, and an action can be taken, such as setting context-sensitive help text for the entry.

#### Params

> Command-Line Name: **-postcommand**
>
> Database Name: **postCommand**
>
> Database Class: **Command**
>
> If this option is specified then it provides a Tcl command to execute each time the menu is posted. The command is invoked by the **post** widget command before posting the menu. Note that in Tk 8.0 on Macintosh and Windows, all post-commands in a system of menus are executed before any of those menus are posted. This is due to the limitations in the individual platforms' menu managers.
>
> 
>
> Command-Line Name: **-selectcolor**
>
> Database Name: **selectColor**
>
> Database Class: **Background**
>
> For menu entries that are check buttons or radio buttons, this option specifies the color to display in the indicator when the check button or radio button is selected.
>
> 
>
> Command-Line Name: **-tearoff**
>
> Database Name: **tearOff**
>
> Database Class: **TearOff**
>
> This option must have a proper boolean value, which specifies whether or not the menu should include a tear-off entry at the top. If so, it will exist as entry 0 of the menu and the other entries will number starting at 1. The default menu bindings arrange for the menu to be torn off when the tear-off entry is invoked. This option is ignored under Aqua/MacOS, where menus cannot be torn off.
>
> 
>
> Command-Line Name: **-tearoffcommand**
>
> Database Name: **tearOffCommand**
>
> Database Class: **TearOffCommand**
>
> If this option has a non-empty value, then it specifies a Tcl command to invoke whenever the menu is torn off. The actual command will consist of the value of this option, followed by a space, followed by the name of the menu window, followed by a space, followed by the name of the name of the torn off menu window. For example, if the option's value is “**a b**” and menu **.x.y** is torn off to create a new menu **.x.tearoff1**, then the command “**a b .x.y .x.tearoff1**” will be invoked. This option is ignored under Aqua/MacOS, where menus cannot be torn off.
>
> 
>
> Command-Line Name: **-title**
>
> Database Name: **title**
>
> Database Class: **Title**
>
> The string will be used to title the window created when this menu is torn off. If the title is NULL, then the window will have the title of the menubutton or the text of the cascade item from which this menu was invoked.
>
> 
>
> Command-Line Name: **-type**
>
> Database Name: **type**
>
> Database Class: **Type**
>
> This option can be one of **menubar**, **tearoff**, or **normal**, and is set when the menu is created. While the string returned by the configuration database will change if this option is changed, this does not affect the menu widget's behavior. This is used by the cloning mechanism and is not normally set outside of the Tk library.
>
> 
>
> Command-Line Name: **-accelerator**
>
> This option can set shutcut key to call the command.

**示例代码：**

```python
l = tk.Label(window, text='      ', bg='green')
l.pack()
# 第10步，定义一个函数功能，用来代表菜单选项的功能，这里为了操作简单，定义的功能比较简单
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter += 1
# 第5步，创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
menubar = tk.Menu(window)
# 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
filemenu = tk.Menu(menubar, tearoff=0)
# 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='File', menu=filemenu)
# 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()    # 添加一条分隔线
filemenu.add_command(label='Exit', command=window.quit) # 用tkinter里面自带的quit()函数
# 第7步，创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
editmenu = tk.Menu(menubar, tearoff=0)
# 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='Edit', menu=editmenu)
# 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元, 就会触发do_job的功能
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)
# 第8步，创建第二级菜单，即菜单项里面的菜单
submenu = tk.Menu(filemenu) # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
filemenu.add_cascade(label='Import', menu=submenu, underline=0) # 给放入的菜单submenu命名为Import
# 第9步，创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
submenu.add_command(label='Submenu_1', command=do_job)   # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1
# 第11步，创建菜单栏完成后，配置让菜单栏menubar显示出来
window.config(menu=menubar)
# 第12步，主窗口循环显示
window.mainloop()
```

> **Post()** --> 右键菜单栏的制作
>
> 1.Menu 类里面有一个 post 方法，它接收两个参数，即 x 和 y 坐标，它会在相应的位置弹出菜单。
>
> 2.利用 Menu 的 post 方法，还有 bind 方法
>
> ```python
> tk.Menu.post(event.x_root, event.y_root)
> ```



**测试效果：**

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808224139791-265028894.gif)

### 11. Frame 

#### Description　

框架，用来承载放置其他GUI元素，就是一个容器，是一个在 Windows 上分离小区域的部件, 它能将 Windows 分成不同的区,然后存放不同的其他部件. 同时一个 Frame 上也能再分成两个 Frame, Frame 可以认为是一种容器，Frame内部组件的坐标位置都是相对坐标，类似于HTML中的块元素。

> 实例化frame框架后须**设定高度及宽度**，若添加边框，须同时指定**bd及relief**属性。



#### Format:

```python
box = tk.Frame(master, *args)
```



#### Params:

| Params              | Description                                               |
| ------------------- | --------------------------------------------------------- |
| **container**       | The value must be a boolean. If true, it means that this window will be used as a container in which some other application will be embedded (for example, a Tk toplevel can be embedded using the **-use** option). The window will support the appropriate window manager protocols for things like geometry requests. The window should not have any children of its own in this application. This option may not be changed with the **configure** widget command. Note that **-borderwidth**, **-padx** and **-pady** are ignored when configured as a container since a container has no border. |
| **visual**          | Specifies visual information for the new window in any of the forms accepted by **[Tk_GetVisual](https://www.tcl.tk/man/tcl8.6/TkLib/GetVisual.htm)**. If this option is not specified, the new window will use the same visual as its parent. The **-visual** option may not be modified with the **configure** widget command. |
| **colormap**        | Specifies a colormap to use for the window. The value may be either **new**, in which case a new colormap is created for the window and its children, or the name of another window (which must be on the same screen and have the same visual as *pathName*), in which case the new window will use the colormap from the specified window. If the **-colormap** option is not specified, the new window uses the same colormap as its parent. This option may not be changed with the **configure** widget command. |
| **class**           | Specifies a class for the window. This class will be used when querying the option database for the window's other options, and it will also be used later for other purposes such as bindings. The **-class** option may not be changed with the **configure** widget command. |





### 13. Layout

#### 1. Grid

其实 grid 就是用表格的形式定位的。这里的参数 row 为行，colum 为列，padx 就是单元格左右间距，pady 就是单元格上下间距，ipadx是单元格内部元素与单元格的左右间距，ipady是单元格内部元素与单元格的上下间距。

**示例代码：**

```python
# grid 放置方法
for i in range(3):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
```

**测试效果：**

 ![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808235921409-1694739142.png)

#### 2. Pack

我们常用的pack(), 他会按照上下左右的方式排列.例如：

```python
tk.Label(window, text='P', fg='red').pack(side='top')    # 上
tk.Label(window, text='P', fg='red').pack(side='bottom') # 下
tk.Label(window, text='P', fg='red').pack(side='left')   # 左
tk.Label(window, text='P', fg='red').pack(side='right')  # 右
```



#### 3. Place

再接下来我们来看place(), 这个比较容易理解，就是给精确的坐标来定位，如此处给的(50, 100)，就是将这个部件放在坐标为(x=50, y=100)的这个位置, 后面的参数 anchor='nw'，就是前面所讲的锚定点是西北角。

> 布局方式：相对布局，绝对布局，表格布局

#### 绝对布局

```python
'''
绝对布局
'''
label1 = tkinter.Label(win, text="柳多妍", bg="pink")
label2 = tkinter.Label(win, text="多多", bg="yellow")
label3 = tkinter.Label(win, text="超级飞侠", bg="red")
# label1.pack()   # #默认没有布局，字有多长，背景也有多长，和其他label错落显示
# label2.pack()
# label3.pack()
label1.place(x=10, y=10)   # #固定坐标，按绝对布局显示，窗口大小的变化对布局没有影响
label2.place(x=50, y=50)
label3.place(x=100, y=100)
win.mainloop()   # #窗口持久化
```

![img](https://img-blog.csdnimg.cn/20190501092507313.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3hvb2ZseQ==,size_16,color_FFFFFF,t_70) ![img](https://img-blog.csdnimg.cn/20190501092609804.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3hvb2ZseQ==,size_16,color_FFFFFF,t_70)

#### 相对布局

```python
'''
相对布局,窗体改变对空间有影响
'''
label1 = tkinter.Label(win, text="柳多妍", bg="pink")
label2 = tkinter.Label(win, text="多多", bg="yellow")
label3 = tkinter.Label(win, text="超级飞侠", bg="red")
label1.pack(fill=tkinter.Y, side=tkinter.LEFT)    # #相对布局
label2.pack(fill=tkinter.X, side=tkinter.TOP)
label3.pack()
win.mainloop()   # #窗口持久化
```

![img](https://img-blog.csdnimg.cn/20190501100027904.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3hvb2ZseQ==,size_16,color_FFFFFF,t_70)

#### 表格布局

```python
'''
相对布局,窗体改变对空间有影响

'''
label1 = tkinter.Label(win, text="柳多妍", bg="pink")
label2 = tkinter.Label(win, text="多多", bg="yellow")
label3 = tkinter.Label(win, text="超级飞侠", bg="red")
label4 = tkinter.Label(win, text="小猪佩奇", bg="green")
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)
win.mainloop()   # #窗口持久化
```

![img](https://img-blog.csdnimg.cn/20190501100403220.png)

Grid(网格)布局管理器会将控件放置到一个二维的表格里。主控件被分割成一系列的行和列，表格中的每个单元(cell)都可以放置一个控件。

![img](https://images2017.cnblogs.com/blog/1127624/201708/1127624-20170824180611230-235131676.png)

![img](https://images2017.cnblogs.com/blog/1127624/201708/1127624-20170824180756121-794857759.png)

#### 注意：不要试图在一个主窗口中混合使用pack和grid



（3）sticky参数的使用

```python
from tkinter import *

tk=Tk()
#标签控件，显示文本和位图，展示在第一行
Label(tk,text="First").grid(row=0,sticky=E)#靠右
Label(tk,text="Second").grid(row=2,sticky=W)#第二行，靠左

#输入控件
Entry(tk).grid(row=0,column=1)
Entry(tk).grid(row=2,column=1)

#主事件循环
mainloop()
```

![img](https://images2017.cnblogs.com/blog/1127624/201708/1127624-20170824203829918-1226562134.png)



利用padx和pady，可以将框架边界区分开

```python
t = Tk()
t.title('与python聊天中')

#创建frame容器
frmLT = Frame(width=500, height=320, bg='white')
frmLC = Frame(width=500, height=150, bg='red')
frmLB = Frame(width=500, height=30)
frmRT = Frame(width=200, height=500)

frmLT.grid(row=0, column=0,padx=1,pady=3)
frmLC.grid(row=1, column=0,padx=1,pady=3)
frmLB.grid(row=2, column=0)
frmRT.grid(row=0, column=1, rowspan=3,padx=2,pady=3)

'''#固定容器大小
frmLT.grid_propagate(0)
frmLC.grid_propagate(0)
frmLB.grid_propagate(0)
frmRT.grid_propagate(0)'''

#添加按钮
btnSend = Button(frmLB, text='发 送', width = 8)#在frmLB容器中添加
btnSend.grid(row=2,column=0)
btnCancel = Button(frmLB, text='取消', width = 8)
btnCancel.grid(row=2,column=1,sticky=E)

#添加图片
imgInfo = PhotoImage(file = "python_logo.gif")
lblImage = Label(frmRT, image = imgInfo)
lblImage.image = imgInfo
lblImage.grid()

#固定容器大小
frmLT.grid_propagate(0)
frmLC.grid_propagate(0)
frmLB.grid_propagate(0)
frmRT.grid_propagate(0)
```



![img](https://images2017.cnblogs.com/blog/1127624/201708/1127624-20170824231549027-1210377031.png)



### 14. LabelFrame



### 15. OptionMenu

## More Widget

First import ttk





### 16. Combobox

<<ComboboxSelected>>

### 17. ScrolledText



### 18. Spinbox



### 19. PanedWindow



### 20. Treeview



### 21. Sizegrip



### 22. Notebook



### 23. Progressbar

#### 基本概念

  Progressbar 可以解释为进度条，主要是当做一个工作进度的指针，在这个控件中会有一个指针，由此指针可以了解工作进度

```python
Progressbar(obj, options, ...)
```

**Params：**
|参数|	含义|
|---|---|
|length	|进度条的长度，默认是100像素|
|mode	|可以有两种模式，下面作介绍|
|maximum	|进度条的最大值默认是100像素|
|name	|进度条的名称，供程序参考引用|
|orient	|进度条的方向，可以是HORIZONTAL(默认) 或者是 VERTICAL|
|value	|进度条的目前值|
|variable	|记录进度条目前的进度值|



**Mode**:

> **determinate**
>
> 一个指针会从起点移至终点，通常当我们知道所需工作时间时，可以使用此模式，这是默认模式。
>
> **indeterminate**
>
> 一个指针会在起点和终点间来回移动，通常当我们不知道工作所需时间时，可以使用此模式，主要目的是让用户知道程序仍然在继续工作

**Instance**


```python
import tkinter
import tkinter.ttk
root = tkinter.Tk()
root.geometry('150x120')

progressbarOne = tkinter.ttk.Progressbar(root)
progressbarOne.pack(pady=20)

# 进度值最大值
progressbarOne['maximum'] = 100
# 进度值初始值
progressbarOne['value'] = 20
# 横排 长度200 起点移至终点
progressbarTwo = tkinter.ttk.Progressbar(root, 
                                        orient=tkinter.HORIZONTAL,
                                        length=200, 
                                        mode='determinate')
progressbarTwo.pack(pady=20)
# 进度值最大值
progressbarTwo['maximum'] = 100
# 进度值初始值
progressbarTwo['value'] = 80

root.mainloop()
```
**注意：现在进度条还不能动！**

**动画设计**
  如果想要设计含动画效果的Progressbar，可以在每次更新Progressbar 对象的value值时调用update()方法，这时窗口可以依据value值重绘，这样就可以达到动画效果。

```python
import time
import tkinter
import tkinter.ttk

def show():
    for i in range(100):
        # 每次更新加1
        progressbarOne['value'] = i + 1
        # 更新画面
        root.update()
        time.sleep(0.05)

root = tkinter.Tk()
root.geometry('150x120')

progressbarOne = tkinter.ttk.Progressbar(root)
progressbarOne.pack(pady=20)
# 进度值最大值
progressbarOne['maximum'] = 100
# 进度值初始值
progressbarOne['value'] = 0

button = tkinter.Button(root, text='Running', command=show)
button.pack(pady=5)

root.mainloop()
```
例子：模拟真实下载，下载总量是10000B， 每次下载500B
```python
def show():
    # 设置进度条的目前值
    progressbarOne['value'] = 0
    # 设置进度条的最大值
    progressbarOne['maximum'] = maxbyte
    # 调用loading方法
    loading()

def loading():
    # 改变变量属性
    global byte
    # 每次运行500B
    byte += 500
    # 设置指针
    progressbarOne['value'] = byte
    if byte < maxbyte:
        # 经过100ms后再次调用loading方法
        progressbarOne.after(100, loading)


root = tkinter.Tk()
root.geometry('150x120')

# 设置下载初值
byte = 0
# 设置下载最大值
maxbyte = 10000

progressbarOne = tkinter.ttk.Progressbar(root)
progressbarOne.pack(pady=20)

button = tkinter.Button(root, text='Running', command=show)
button.pack(pady=5)

root.mainloop()
```
**Progressbar Function** 

```python
Progressbar.start()
Progressbar.step()
Progressbar.stop()
```

含义如下：

start(interval)：每隔interval时间移动一次指针。interval的默认值是50ms，每次移动指针调用一次step(amount)。在step()方法内的amount参数意义就是增值量

step(amount)：每次增加一次amount，默认值是1.0，在determinate模式下，指针不会超过maximum参数。在indeterminate模式下，当指针达到maximum参数值的前一格时，指针会回到起点

stop()：停止start()运行
例子：

```python
import time
import tkinter
import tkinter.ttk

def show():
    while progressbarOne.cget('value') <= progressbarOne['maximum']:
        progressbarOne.step(2)
        root.update()
        print(progressbarOne.cget('value'))
        time.sleep(0.05)

root = tkinter.Tk()
root.geometry('150x120')

progressbarOne = tkinter.ttk.Progressbar(root, length=200, 
                                         mode='determinate', 
                                         orient=tkinter.HORIZONTAL)
progressbarOne.pack(pady=20)

progressbarOne['maximum'] = 100
progressbarOne['value'] = 0

button = tkinter.Button(root, text='Running', command=show)
button.pack(pady=5)

root.mainloop()
```

使用start()方法启动动画，单击stop按钮停止

例子：
```python
import tkinter
import tkinter.ttk

def run():
    progressbarOne.start()

def stop():
    progressbarOne.stop()

root = tkinter.Tk()
root.geometry('150x120')

progressbarOne = tkinter.ttk.Progressbar(root, length=200, 
                                         mode='determinate', 
                                         orient=tkinter.HORIZONTAL)
progressbarOne.pack(padx=5, pady=10)

progressbarOne['maximum'] = 100
progressbarOne['value'] = 0

buttonRun = tkinter.Button(root, text='Run', width=6, 
                           command=run)
buttonRun.pack(padx=10, pady=5, side=tkinter.LEFT)

buttonStop = tkinter.Button(root, text='Stop', width=6, 
                            command=stop)
buttonStop.pack(padx=10, pady=5, side=tkinter.RIGHT)

root.mainloop()
```



### 24. Separator



### 25. Menubutton



## Something else

### lambda

#### Description

To transfer parameters to widget in tkinter, especially like Button. 

#### Format

```python
lambda params : expression
```

Return the outcome of expression.

**For a simple example:**

```python
Button( command = lambda params : function)
```



### bell

#### Description

> This command rings the bell on the display for *window* and returns an empty string. If the **-displayof** option is omitted, the display of the application's main window is used by default. The command uses the current bell-related settings for the display, which may be modified with programs such as **xset**.
>
> If **-nice** is not specified, this command also resets the screen saver for the screen. Some screen savers will ignore this, but others will reset so that the screen becomes visible again.

#### Format

```python
window.bell(displayof=0)
```



### Toplevel

顶级弹窗



## Variable management

### Synopsis

> 有些控件在执行时会更改内容，例如，文本框(Entry)，选项按钮(Radio button)等；
>
> 有些控件我们可以更改他们的内容，例如标签(Label)等，如果想要更改他们的内容，可以使用这些控件的参数，例如，textvariable、variable、onvalue等；
>
> 不过要将控件的参数以变量方式处理时，需要借助tkinter模块内的变量类别(Variable Classes)。
>
> 这个类别有4个子类别，每一个类别其实就是一个数据类型的构造方法，我们可以通过这4个子类别的数据类型将他们与控件相关的参数结合。

### Type

```python
x = IntVar()	# 整型变量，默认是0
x = DoubleVar()	# 浮点型变量，默认是0.0
x = StringVar()	# 字符串变量，默认是""
x = BooleanVar()	# 布尔型变量，True是1，False是0
```



### Operation

#### set

use set() to set the value of var.

```python
string.set(value)
```



#### get

use get() to get the value of var.

```python
string.get()
```



#### trace

```python
Srting.trace(string, index, mode, *args)
```

> *args`其实是传递三个参数，分别是`tk变量名称`、`index索引`、`mode模式
>
> 不过目前有关于`tk变量名称`和`index索引`部分尚未完成实际支持，第三个参数则可以列出是`r`还是`w`模式
>
> 由于我们所设计的程序并不需要传递参数，所以可以直接用`*args`当做参数内容
>
> `%s`是将变量传到`str()`函数中，结果是将变量转化适合人阅读的格式
>
> `%r`是将变量穿到`repr()`函数中，结果是将变量转化成适合机器阅读的格式，可以将%r后的变量理解为一个对象

#### mode : "w"

我们可以利用变量设置追踪`Widget`控件("w"模式)，当其内容发生改变时，让程序自动执行函数。

```python
string.trace("w", function)
```

#### mode : "r"

我们也可以设计当控件内容被读取时，执行追踪并执行特定函数。

```python
string.trace("r", function)
```



## Event response

Tkinter 使用所谓的 事件队列 (event sequences) 暴露接口以绑定 handler 到相关事件. 事件以字符串的形式给出:

`type` 字段是一个事件的关键字段. `modifer` 和 `detail` 字段则不是必要字段, 很多情况下这两个字段都不会被赋值. 这两个字段用以提供 `type` 所代表的事件的附加信息. `type` 字段描述事件种类, 比如 鼠标点击, 键位按下, 控件获得焦点 等.

| Event           | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| <Button>        | 某个鼠标按键在控件上被点击. `detail` 指定了哪一个按键被点击了, 比如, 鼠标左键点击为 <Button-1>, 鼠标中键点击为 <Button-2>, 鼠标右键点击为 <Button-3>, 向上滚动滑轮为 <Button-4>, 向下滚动滑轮为 <Button-5>. 如果在控件上按下鼠标的某个键并保持按下, Tkinter 将”抓住”该事件. 之后的鼠标事件, 比如 鼠标移动 或 鼠标按键释放 事件, 会被自动发送给该控件处理, 即使鼠标移动出该控件时依然如此. 鼠标相对当前控件的位置会被存储在 event 对象中的 x 和 y 字段中传递给回调函数. |
| <Motion>        | 鼠标在某个按键被按下时的移动事件. 鼠标左键点击为 <B1-Motion>, 鼠标中键点击为 <B2-Motion>, 鼠标右键点击为 <B3-Motion>. 鼠标相对当前控件的位置会被存储在 event 对象中的 x 和 y 字段中传递给回调函数. |
| <ButtonRelease> | 按钮点击释放事件. 鼠标左键点击为 <ButtonRelease-1>, 鼠标中键点击为 <ButtonRelease-2>, 鼠标右键点击为 <ButtonRelease-3>. 鼠标相对当前控件的位置会被存储在 event 对象中的 x 和 y 字段中传递给回调函数. |
| <Double-Button> | 鼠标双击事件. 鼠标左键点击为 <Double-Button-1>, 鼠标中键点击为 <Double-Button-2>, 鼠标右键点击为 <Double-Button-3>. Double 和 Triple 都可以被用作前缀. 注意: 如果同时绑定单击事件 (<Button-1>) 和双击事件 (<Double-Button-1>), 则两个回调都会被调用. |
| <Enter>         | 鼠标移入控件事件. 注意: 这个事件不是 Enter 键按下事件, Enter 按下事件是 <Return>. |
| <Leave>         | 鼠标移出控件事件.                                            |
| <FocusIn>       | 控件或控件的子空间获得键盘焦点.                              |
| <FocusOut>      | 控件丢失键盘焦点 (焦点移动到另一个控件).                     |
| <Return>        | Enter 点击事件. 键盘上的所有键位都可以被绑定. 特殊键位名称包括 Cancel, BackSpace, Tab, Return (Enter), Shift_L (任意 Shift), Control_L (任意 Control), Alt_L (任意 Alt), Pause, Caps_Lock, Escape, Prior (Page Up), Next (Page Down), End, Home, Left, Up, Right, Down, Print, Insert, Delete, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock, and Scroll_Lock |
| <Key>           | 键盘按键点击事件. 键值被存储在 event 对象中传递. (特殊键位会传递空键值). |
| a               | “a” 键被点击. 其他字符也可以如此定义. 特殊情况包括 空格 (<space>) 和 小于号 (<less>). 注意 “1” 是绑定键盘键位, 而 <1> 则是按钮绑定. |
| <Shift-Up>      | 在 shift 被按下时点击 up 键. 同样的, 也有 Alt-Up, Control-Up 事件. |
| <Configure>     | 控件大小改变事件. 新的控件大小会存储在 event 对象中的 width 和 height 属性传递. 有些平台上该事件也可能代表控件位置改变. |

1. 事件（event）：是指点击、按键等操作，在tkinter中，event是一个类，当某个事件发生时，生成一个event对象，不同类型的事件生成具有不同属性的event对象。
2. 事件处理（event handler）：是指在捕获到事件后，程序自动执行的操作，是回调函数（recall function）。
3. 事件绑定（event binding）：是当一个事件发生时程序能够做出响应。tkinter提供三种绑定方式：实例绑定bind（将某个事件处理绑定到某个组件上）、类绑定bind_class（将某个事件处理绑定到某类组件上）、应用绑定bind_all（将某个事件处理绑定到所有组件上）。

### Event description

**（1）事件格式：**

在Tkinter中，事件的描述格式为：**<[modifier-]-type[-detail]>**，其中：

- modifier：事件修饰符。如：Alt、Shit组合键和Double事件。
- type：事件类型。如：按键（Key）、鼠标（Button/Motion/Enter/Leave/Relase）、Configure等。
- detail：事件细节。如：鼠标左键（1）、鼠标中键（2）、鼠标右键（3）。

**注意大小写！！！**

| Type     | **Format**                            | **Discription**                                              |
| -------- | ------------------------------------- | ------------------------------------------------------------ |
| 鼠标事件 | <Button-1>                            | 鼠标点击（1-左键，2-中键，3-右键）                           |
|          | <Double-Button-1>                     | 鼠标双击（1-左键，2-中键，3-右键）                           |
|          | <B1-Motion>                           | 鼠标拖动（1-左键，2-中键，3-右键）                           |
|          | <ButtonRelease-1>                     | 鼠标按下之后释放（1-左键，2-中键，3-右键）                   |
|          | <Enter>                               | 鼠标进入控件范围（widget），不是键盘按键                     |
|          | <Leave>                               | 鼠标离开控件范围（widget）                                   |
| 键盘事件 | <Key>/<KeyPress>                      | 任意键盘按键（键值会以char的格式放入event对象）              |
|          | <BackSpace><Tab><Shift_L><Up><F1><F2> | 对应键盘按键                                                 |
| 组件事件 | <Configure>                           | 如果widget的大小发生改变，新的大小（width和height）会打包到event发往handler。 |
|          | <Activate>                            | 当组件从不可用变为可用                                       |
|          | <Deactivate>                          | 当组件从可用变为不可用                                       |
|          | <Destroy>                             | 当组件被销毁时                                               |
|          | <Expose>                              | 当组件从被遮挡状态变为暴露状态                               |
|          | <Map>                                 | 当组件由隐藏状态变为显示状态                                 |
|          | <Unmap>                               | 当组件由显示状态变为隐藏状态                                 |
|          | <FocusIn>                             | 当组件获得焦点时                                             |
|          | <FocusOut>                            | 当组件失去焦点时                                             |
|          | <Property>                            | 当组件属性发生改变时                                         |
|          | <Visibility>                          | 当组件变为可视状态时                                         |

**（2）事件对象：**

一个具体事件如<Button-1>是事件类（event class）的一个实例，事件类中设定了众多属性，其中部分属性是通用的，另一部分属性属于特定事件类型的，常用属性如下：

| **属性** | **属性说明**                                                 | **适用事件类型**                 |
| -------- | ------------------------------------------------------------ | -------------------------------- |
| char     | 如果按键事件产生通用ASCII字符，这个字符将赋值给event.char。（特殊ASCII字符，如delete等不属于该属性） | <KeyPress><KeyRelease>等按键事件 |
| keysym   | 如果按键事件产生特殊ASCII字符，这个字符将赋值给event.keysym。 | <KeyPress><KeyRelease>等按键事件 |
| x        | 鼠标当前位置横坐标，相对于组件左上角                         |                                  |
| y        | 鼠标当前位置纵坐标，相对于组件左上角                         |                                  |
| x_root   | 鼠标当前位置横坐标，相对于屏幕左上角                         |                                  |
| y_root   | 鼠标当前位置纵坐标，相对于屏幕左上角                         |                                  |
| width    | 组件大小发生改变后的宽度                                     | <Configure>                      |
| height   | 组件大小发生改变后的高度                                     | <Configure>                      |
| type     | 事件类型                                                     | ALL                              |
| num      | 鼠标按键                                                     |                                  |

### Binding method

Here are 3 ways to bind event:

> 1. ##### Widget object
>
>    > **command**
>    >
>    > For object which is simple doesn't need event object.
>    >
>    > **bind**
>    >
>    > For those objects have complex event interaction.
>
> 2. ##### Widget class
>
>    > **bind_class**
>    >
>    > Call bind_class function to bind all object in class with event.

实际应用：

快捷键的绑定

### bind

**Format:**

```python
widget.bind(event, function)
```

**事件**

> 1、我们的很多操作，比如我们点击了一下鼠标，这就是一 个事件，而操作系统会根据我们的相应的事件产生相应的消息，
> 操作系统把消息传递给我们的应用程序，然后我们的应用程序根据操作系统传入的数据执行相应的命令。
>
> 2、事件是我们触发的，消息是操作系统根据我们的事件产 生的，我们通常对于“消息”并不多关注，我们重视的是 “事件”。

 **事件及其绑定**

> 1、bind 函数的调用规则: 窗体对象.bind(事件类型，回调函数)
>
> 2、所谓的“回调函数”，就是这个函数我们不用去调用它， 当相应的事件发生的时候，它会自动取调用。比如当我们 的按钮被按下的时候，它会被自动调用。

**常用的事件**

> 1、我们在使用 bind 函数的时候，它的第一个参数就是事件的类型了。
>
> 2、<Button-1>表示鼠标左键单击，其中的1换成3表示右键被单击，为2的时候表示鼠标中键，感觉不算常用。
>
> 3、<KeyPress-A>表示 A 键被按下，其中的A可以换成其他的键位。
>
> 4、<Control-V>表示按下的是 Ctrl 和 V 键，V 可以换成其他键位。
>
> 5、<F1>表示按下的是 F1 键，对于 Fn 系列的，都可以随便换。

**再看绑定**

> 1.事件不仅可以与 Button 绑定，我们之前看过源代码，发现 bind 函数是定义在 Misc 类里面的，也就是说，这个 bind 可以被绝大多数组件类所使用。
>
> 2.也就是说，我们可以让“标签”来模拟“按钮”的作用。
>
> 3.因为标签是 Label 类，而 Label 类继承自 Widget，而 Widget 继承自 BaseWidget，而 Basewidget 继承自 Misc。
>
> 4.其实不仅是标签可以模拟 button，任何组件都可以模拟 它，只是那么有用。

```python
from tkinter import *

def testLabel(event):
    global base
    lb = Label(base, text = "这是一个Label组件", background = "green")
    lb.pack()

base = Tk()
obj = Label(base, text = "模拟按钮")
obj.bind("<Button-1>",testLabel)
obj.pack()
base.mainloop()
运行结果如下：
```

![img](https://img2018.cnblogs.com/blog/1494277/201810/1494277-20181023133354729-33014626.png)

> 1. 关于 bind 函数，还有两个版本的，不能说高级低级，只是使用的方面不同。
>
> 2. 可以在全程序级别的绑定，使用 bind_all，它的参数类 型和 bind 一样，它通常用于全局的快捷键，比如 F1 通常 是用来打开帮助文档。
>
> 3. 还可以绑定某些类别，使用 bind_class,它接受三个参数， 第一个参数是类名，第二个参数是事件类型，第三个参数 是相应的操作，
>
> 比如 w.bind_class(“Entry”, “<Control-V>”,my_paste)。它就是绑定了所有的所有的 输入框的 Ctrl+V 表示粘贴。

**解除绑定**

> 1.解除绑定我们使用 unbind 方法，它和 bind 的使用很相似。
>
> 2.不过 unbind 方法只需要一个参数就可以了，它只需要解除绑定的事件类型，因为它会解除该绑定事件类型的所有 回调函数

### bind_class

#### Format

```python
bind_class(className, sequence=None, func=None, add=None) 
```

Method of tkinter. Tk instance.

> Bind to widgets with bindtag CLASSNAME at event. SEQUENCE a call of function FUNC. An additional boolean parameter ADD specifies whether FUNC will be called additionally to the other bound function or
> whether it will replace the previous function. See bind for the return value.

目前实践情况来看，bind_class貌似会出现按钮点击效果脱标的情况。

## Function

### PhotroImage

```python
img = PhotoImage(path)
```

加载图片，并以对象形式保存，以作为参数传入函数中。

**注：<PhotroImage> 对象需设定为全局变量，否则会自动销毁，从而导致在mainloop的过程中无法正常显示。**




### 定时刷新

#### 1. 说明

由于tkinter一旦开始执行进入mainloop，就相当于进入一个界面死循环状态，出不来；如果想做定时刷新tkinter界面的控件数据，必须调用tkinter.TK()自带的after函数，这个函数可以设定定时执行某个任务的时间，使用别的python定时执行任务的模块是不行的。

#### 2. 使用方式

​       实现一个刷新数据函数调用tkinter.TK()自带的after函数，在调用mainloop函数之前，将这个刷新数据函数调用，则可以实现定时刷新数据功能，参考代码如下：

```python
import tkinter as tk

class Questions(tk.Tk):
    def __init__(self, *args, **kw):
        super().__init__()
        self.wm_title('CSSE1001 Queue')
        self.configure(background='white')
        self.wm_minsize(1440, 776)                  # 设置窗口最小化大小
        self.wm_maxsize(1440, 2800)                 # 设置窗口最大化大小
        self.resizable(width=False, height=True)    
        # 设置窗口宽度不可变，高度可变
        self.run()
        self.refresh_data()
        self.mainloop()
    
    def refresh_data(self):
        # 需要刷新数据的操作
        # 代码...     
        self.after(10000, self.refresh_data)   # 这里的10000单位为毫秒     
    def run(self):
        pass

if __name__ == '__main__':
    question = Questions()
```
#### 3. 额外补充别的定时执行任务程序

 介绍轻量级第三方模块schedule，需要使用 pip install schedule导入才能使用
使用时功能相对于crontab。

```python
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)              # 每隔10分钟执行一次任务
schedule.every().hour.do(job)                   # 每隔一小时执行一次任务
schedule.every().day.at("10:30").do(job)        # 每天10：30执行一次任务
schedule.every(5).to(10).days.do(job)           # 每5-10天执行一次任务
schedule.every().monday.do(job)                 # 每周一的这个时候执行一次任务
schedule.every().wednesday.at("13:15").do(job)  # 每周三13:15执行一次任务

while True:
    schedule.run_pending()
```



### after

#### Format

```python
Misc.after(timeinterval, func=None, *args)
```



#### Description

> Call function once after given time. (Call itself continuously)
>
> MS specifies the time in milliseconds. FUNC gives the function which shall be called. Additional parameters are given as parameters to the function call. Return identifier to cancel scheduling with after_cancel



#### Params

| Params       | Description                                           |
| ------------ | ----------------------------------------------------- |
| timeinterval | The interval of program running, **in milliseconds**. |
| function     | The function to be call every loop.                   |
| *args        | Other params used seledomly.                          |



**For a simple example:**

```python
import time
import tkinter as tk

def __writeText():
    text.insert(tk.END, str(time.time())+'\n')
    root.after(1000, __writeText)  # again forever

root = tk.Tk()
text = tk.Text(root)
text.pack()
root.after(1000, __writeText)
root.mainloop()
```

---

### askcolor

#### Format

```python
from tkinter import colorchooser,ttk
colorchooser.askcolor(color = None, *options)
```



#### Description

> pop up the color paint to ask for a color.
>
> **Return a tuple** composed of (RGB, Ox), RGB symbolize the value of color channel of (r,g,b), Ox symbolize the value of the color in Ox, which can be called directly.



#### Params





### Tag



tag_raise(firstRect)

---

## messagebox

### Synopsis

> **messagebox需额外引入**

messageBox：消息框，用于显示你应用程序的消息框。其实这里的messageBox就是我们平时看到的弹窗。 我们首先需要定义一个触发功能，来触发这个弹窗，这里我们就放上以前学过的button按钮，通过触发功能，调用messagebox吧，点击button按钮就会弹出提示对话框。下面给出messagebox提示信息的几种形式：

```python
tkinter.messagebox.showinfo(title='Hi', message='你好！')            # 提示信息对话窗
tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'
```

**测试效果：**

 ![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808233448829-65209831.png)![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808233531668-1546902314.png)

![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808233622649-1216743879.png)![img](https://images2018.cnblogs.com/blog/1372069/201808/1372069-20180808233706164-1056501102.png)



messagebox中工具函数如下：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424123825529.png)

### 消息提示框

> tkinter.messagebox.showinfo(title, message, icon=None, type=None)
>
> 返回值为点击的按键的值，包括“yes”（是）、“no”（否）、“retry”（重试）、“ok”（确定）、“cancel”（取消）、“ignore”（忽略）、”abort“（中止）。



### 消息警告框

> tkinter.messagebox.showwarning(title,message,icon= None,type= None)
>
> 返回值为点击的按键的值，按键值同上。



### 消息错误框

> tkinter.messagebox.showerror(title,message,icon= None,type= None)
>
> 返回值为点击的按键的值，按键值同上。



### 对话框

> tkinter.messagebox.**askquestion**(title,message,icon= None,type= None)
>
> 返回值为点击的按键的值，当单击的按钮值为“ok”（确定）时返回True，否则都为False
>
> 
>
> tkinter.messagebox.**askokcancel**(title,message,icon= None,type= None)
>
> 返回值为True或False，当单击的按钮值为“ok”（确定）时返回True，否则都为False
>
> 
>
> tkinter.messagebox.**askyesno**(title,message,icon= None,type= None)
>
> 返回值为True或False，当单击的按钮键值为“yes”（是）时返回True，否则都返回False
>
> 
>
> tkinter.messagebox.**askyesnocancel**(title,message,icon= None,type= None)
>
> 返回值为True、False、None，当单击的按键值为“yes”（是）时返回True、当单击的按键值为“cancel”（取消）时返回None，否则都返回False
>
> 
>
> tkinter.messagebox.**askretrycancel**(title,message,icon= None,type= None):
> 返回值为True或False，当单击的按钮值为“retry”（重试）时返回True，否则都为False

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424125014382.jpg)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424125044939.jpg)![在这里插入图片描述](https://img-blog.csdnimg.cn/2020042413385368.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQxNzkzOA==,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/2020042413393568.png)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424134034464.png)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424134131945.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424134213924.png)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424134243734.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQxNzkzOA==,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424125058874.jpg)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020042412495652.jpg)



默认情况下使用者在调用messagebox时只要设置提示区字符串即可。但如果有需要，可以通过如下两个选项来设置图标和按键

> **icon**：定制的图标区图标选项，该选项支持“error”、“info”、“question”、“warning”（默认为“info”图标）
>
>**type**：定制按钮的选项。该选项支持“abortretryignore”（中止、重试、忽略）、“ok”（确定）、“okcancel”（确定、取消）、“retrycancel”（重试、取消）、“yesno”（是、否）、“yesnocancel”（是、否、取消）（默认为“ok”按键）
> 
>**title**：messagebox消息框的标题
>
> **message**：提示区字符串

### 实例

下面代码通过两组单选钮让用户动态选择不同的icon和type选项的效果：

```python
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
def initWidgets(self):
    # 创建第一个Labelframe，用于选择图标类型
    topF = ttk.Frame(self.master)
    topF.pack(fill=BOTH)
    lf1 = ttk.Labelframe(topF, text='请选择图标类型')
    lf1.pack(side=LEFT, fill=BOTH, expand=1, padx=10, pady=5)
    i = 0
    self.iconVar = IntVar()
    self.icons = [None, 'error', 'info', 'question', 'warning']
    # 使用循环创建多个RadioButton，并放入Labelframe中
    for icon in self.icons:
        ttk.Radiobutton(lf1, text=icon if icon is not None else '默认', value=i,
                        variable=self.iconVar).pack(side=TOP, anchor=W)
        i += 1
    self.iconVar.set(0)
    #创建第二个labelframe，用于选择按钮类型
    lf2 = ttk.Labelframe(topF, text='选择按钮类型')
    lf2.pack(side=LEFT, fill=BOTH, expand=1, padx=10, pady=5)
    i = 0
    self.typeVar = IntVar()
    self.types = [None, 'abortretryignore', 'ok', 'okcancel', 'retrycancel', 'yesno', 'yesnocancel']
    # 利用循环创建多个Radiobutton，并放入Labelframe中
    for tp in self.types:
        ttk.Radiobutton(lf2, text=tp if tp is not None else '默认', value=i, variable=self.typeVar).pack(side=TOP,
                                                                                                       anchor=W)
        i += 1
    self.typeVar.set(0)
    #创建Frame，用于包含多个按钮来生成不同的消息框
    bottomF = ttk.Frame(self.master)
    bottomF.pack(fill=BOTH)
    # 创建8个按钮，并为之绑定事件处理方法
    ttk.Button(bottomF, text='showinfo', command=self.showinfo_clicked).pack(side=LEFT, fill=X, ipadx=5, ipady=5,
                                                                             padx=5, pady=5)
    ttk.Button(bottomF, text='showwarning', command=self.showwarning_clicked).pack(side=LEFT, fill=X, ipadx=5,
                                                                                   ipady=5, padx=5, pady=5)
    ttk.Button(bottomF, text='showerror', command=self.showerror_clicked).pack(side=LEFT, fill=X, ipadx=5, ipady=5,
                                                                               padx=5, pady=5)
    ttk.Button(bottomF, text='askquestion', command=self.askquestion_clicked).pack(side=LEFT, fill=X, ipadx=5,
                                                                                   ipady=5, padx=5, pady=5)
    ttk.Button(bottomF, text='askokcancel', command=self.askokcancel_clicked).pack(side=LEFT, fill=X, ipadx=5,
                                                                                   ipady=5, padx=5, pady=5)
    ttk.Button(bottomF, text='askyesno', command=self.askyesno_clicked).pack(side=LEFT, fill=X, ipadx=5, ipady=5,
                                                                             padx=5, pady=5)
    ttk.Button(bottomF, text='askyesnocancel', command=self.askyesnocancel_clicked).pack(side=LEFT, fill=X, ipadx=5,
                                                                                         ipady=5, padx=5, pady=5)
    ttk.Button(bottomF, text='askretrycancel', command=self.askretrycancel_clicked).pack(side=LEFT, fill=X, ipadx=5,
                                                                                         ipady=5, padx=5, pady=5)

def showinfo_clicked(self):
    print(messagebox.showinfo('Info', 'showinfo测试', icon=self.icons[self.iconVar.get()],
                              type=self.types[self.typeVar.get()]))

def showwarning_clicked(self):
    print(messagebox.showwarning('Warning', 'showwarning测试', icon=self.icons[self.iconVar.get()],
                                 type=self.types[self.typeVar.get()]))

def showerror_clicked(self):
    print(messagebox.showerror('Error', 'showerror测试', icon=self.icons[self.iconVar.get()],
                               type=self.types[self.typeVar.get()]))

def askquestion_clicked(self):
    print(messagebox.askquestion('Question', 'askquestion测试', icon=self.icons[self.iconVar.get()],
                                 type=self.types[self.typeVar.get()]))

def askokcancel_clicked(self):
    print(messagebox.askokcancel('Okcancel', 'askokcancel测试', icon=self.icons[self.iconVar.get()],
                                 type=self.types[self.typeVar.get()]))

def askyesno_clicked(self):
    print(messagebox.askyesno('Yesno', 'askyesno测试', icon=self.icons[self.iconVar.get()],
                              type=self.types[self.typeVar.get()]))

def askyesnocancel_clicked(self):
    print(messagebox.askyesnocancel('Yesnocancel', 'askyesnocancel', icon=self.icons[self.iconVar.get()],
                                    type=self.types[self.typeVar.get()]))

def askretrycancel_clicked(self):
    print(messagebox.askretrycancel('Retrycancel', 'askretrycancel', icon=self.icons[self.iconVar.get()],
                                    type=self.types[self.typeVar.get()]))
root = Tk()
root.title('message测试')
App(root)
root.mainloop()
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424135025143.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQxNzkzOA==,size_16,color_FFFFFF,t_70)





## File Dialog

### Description

### Function

| Function          | Dialog     | Description            |
| ----------------- | ---------- | ---------------------- |
| askopenfilename   | 文本对话框 | 返回打开的文件名       |
| askopenfilenames  | 文本对话框 | 返回打开的多个文件名   |
| askopenfile       | 文本对话框 | 返回打开的文件对象     |
| askopenfiles      | 文本对话框 | 返回打开的文件对象列表 |
| askdirectory      | 目录对话框 | 返回目录名             |
| asksaveasfile     | 保存对话框 | 返回保存的文件对象     |
| asksaveasfilename | 保存对话框 | 返回保存的文件名       |

### Options

| Params                            | Description                |
| --------------------------------- | -------------------------- |
| defaultextension                  | 文件默认后缀，默认自动添加 |
| filetypes=[(label1, pattern1),()] | 文件显示过滤器             |
| initialdir                        | 初始目录                   |
| initialfile                       | 初始文件                   |
| parent                            | 父窗口，默认根窗口         |
| title                             | 窗口标题                   |

上述(label1, pattern1)表示打开请求窗口后右下角显示的内容，表征为Label(*pattern)，Label可自定义，pattern必须为现存的文件格式。



### askopenfile

#### Format

```python
from tkinter import filedialog
filedialog.askopenfile(mode="r", **options)
```



#### Description



#### Params



---

## Simple Dialog

**Need import like `from tkinter import simpledialog`.**

### Description

> Pop up a simple dialog to get return of user, different from messagebox, simple dialog has more simple style and function.
>

### Fuction

| Function   | Description      |
| ---------- | ---------------- |
| askfloat   | 输入并返回浮点数 |
| askinteger | 输入并返回整数   |
| askstring  | 输入并返回字符串 |



### Params

| Params       | Description  |
| ------------ | ------------ |
| title        | 窗口标题     |
| prompt       | 窗口提示信息 |
| initialvalue | 初始值       |
| minvalue     | 最小值       |
| maxvalue     | 最大值       |



## Theme

It look like that all standard theme aren't supported on win10,64 bites, that means if you want to use any theme, you need to **define by yourself**, it seems not a easy deal, to learn it more, click [here](https://www.codingdict.com/sources/py/tkinter.ttk/14341.html) . 

And to download theme to click [here](https://wiki.tcl-lang.org/page/List+of+ttk+Themes) .

### Description

Only ttk support modify theme. 

Simple example:

```python
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")
```



## Instance

字符串转 md5 工具(Python3 下运行)：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import hashlib
import time

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("文本处理工具_v1.2")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=10,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)


    #功能函数
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
        #print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                #print(myMd5_Digest)
                #输出到界面
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
gui_start()
```

