GUI-tkinter/tcl

## Before all

> If you have any question, please seek the  [Docs](https://www.tcl.tk/doc/)  for answer. Learn more by refering to the  [tutorial](https://www.tcl.tk/man/tcl8.5/tutorial/tcltutorial.html) .
>
> Tip : There are somethings different with normal.
>

## 1. Synopsis

> **Tcl**：工具命令语言，英文全称为Tool Command Language，它是一个非常强大，易学习动态编程语言，应用广泛。包括网页和桌面应用，网络，管理，测试，除此之外，还有很多其他应用。开源和商业友好，Tcl是一个成熟但不断发展的语言，是真正的跨平台，易于部署，高度可扩展的语言。
>
> **Tk**：图形用户界面工具包，英文为graphical user interface toolkit，它将开发桌面应用程序带到比传统方法更高水平。 Tk是Tcl和许多其他动态语言的标准图形用户界面，能产生丰富的本地应用程序，并且无需改变，就可在Windows，Mac OS X、Linux和更多平台上运行。

**略过cmd窗口只需将后缀名 .py 改为 .pyw 即可**



## 2. Standard Attribute

> Standard properties are the common properties of all controls, such as size, font, color, and so on. You can get all attributes' name of the widget through `widget.keys()` and get value of certain attribute through `cget(option)`.

**And you can index them by `widget.cget("Attribute")` .**

| 属性        | 描述                |
| ----------- | ------------------- |
| Dimension   | 控件大小            |
| Color       | 控件颜色            |
| Font        | 控件字体            |
| Anchor      | 锚点，文字对齐位置  |
| Relief      | 控件样式            |
| Bitmap      | 位图                |
| Cursor      | 光标                |
| Image       | **图片；只支持GIF** |
| justify     | 对齐方式            |
| padx/pady   | 外边距              |
| ipadx/ipady | 内边距              |
| destroy     | 销毁组件            |
| highlight-  | 具有焦点特性        |
| active-     | 具有焦点效果        |
| select-     | 选中效果            |

> 边框(relief)包括六种样式：flat, raised, groove, ridge, solid, sunken.
>
> 位图(Bitmap)内置的图片对应值包括有："error", "hourglass", "info", "questhead, "question", "waring", "gray12", "gray25", "gray50", "gray75"，此外，**Bitmap不能和Image同时使用，否则默认情况下位图会失效**。
>
> 鼠标样式过多，不一一列举，使用频率较低，不展开叙述。

#### About config

> 1. **传参**
>
>    label(text = ''who ")
>
> 2. **字典索引赋值**
>
>    label['text'] = 'who'
>
> 3. **config方法**
>
>    label.config(text = 'who')

#### About Image

> `tk.PhotoImage` only support **.gif** and **.png** file, but **it doesn't raise an error** with other format, can't indicate image either, if you post a image of `.jpg` or formats else, you can use method below.

```python
from PIL import Image, ImageTk
background_image = ImageTk.PhotoImage(Image.open(filepath))
background_label = tk.Label(window, image=background_image)
```

> It's worth mentioning that if you define image as a **local** variable, it will be distroyed after call, and can't be shown normally. To solve this problem, you need to define it as **global** variable to maintain it.

#### About color

> backgroundcolor of window is `"SystemButtonFace"`, you can index it by `Tk().cget('bg')` .
>
> **And ld/thinkness is need when you refer to the highlightcolor and else.**
>
> Here is the common color of tkinter.
>

<img src="E:/工具/Typora/Temp/SouthEast.png" alt="img"  />

## 3. Base Widget

### Tk

> Tk object 是基本的窗口类，是控件的容器，实际上，它并不属于Widget（组件）类。

#### 1.  Create

```python
tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
```

> `Tk` 类被初始化时无参数。此时会创建一个 Tk 顶级控件，通常是应用程序的主窗口。每个实例都有自己关联的 Tcl 解释器。
>
> 此外，其更多具体属性，可以通过其wm属性进行修改，具体语法如下：

```python
Tk.wm_attributes(attr, values)
```



#### 2. Basic

##### 2.1 Title

> 修改窗体的名字,也可在创建时使用className参数来命名；

```python
root.title('name')  　　 
```

##### 2.2 Icon

> 修改窗体图标

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

##### 2.3 Main

> 撤销主窗口，即初始化创建的Tk窗口，仅保留弹窗及其他对话框。

```python
tk.withdraw()
```

#### 3. Dimension

```python
tk.geometry(width,height,x,y)	# 窗口初始大小
tk.maxsize(width, height)	# 拖拽时窗口的最大宽度和高度
tk.minsize(width, height)	# 拖拽时窗口的最小宽度和高度
tk.state(state)				# 设置窗口状态
tk.resizable(width=False, height=False)	# 锁定窗口大小
# tk.resizable(0, 0)
tk.iconify()				# 窗口最小化
```

##### 示例：**屏幕居中显示**

```python
window.update()
x, y = window.maxsize() # 获取当前屏幕像素
width, height = 200, 200
x, y = int(x/2-width/2), int(y/2-height/2)  # 计算屏幕中心坐标
window.geometry("%dx%d+%d+%d"%(width, height,x,y))  # 居中显示
```

#### 4.  Operation

##### 4.1 关闭窗口

```python
window.quit() 
```

##### 4.2 刷新窗口

```python
root.update_idletasks()
root.update() 
```



### Layout

#### 1. Grid

> 其实 grid 就是用表格的形式定位的。这里的参数 row 为行，colum 为列，padx 就是单元格左右间距，pady 就是单元格上下间距，ipadx是单元格内部元素与单元格的左右间距，ipady是单元格内部元素与单元格的上下间距，**column/rowspan表示跨列/行合并**，Stick表示Widget控件对齐方式，仅包括tk.N/S/W/E，表示上下左右对齐，可以同时指定多个，用"+"连接。
>
> 此外，可以通过父容器的row/columnconfigure(number, params)方法调控特定的行或列属性

**示例代码：**

```python
# grid 放置方法
for i in range(3):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
```



#### 2. Pack

> 我们常用的pack(), 它会按照上下左右的方式进行**相对式排列**，我们可以通过传递`side`参数来修改对齐方向。此外，还有一些其他参数：

| 参数   | 值            | 说明                               |
| ------ | ------------- | ---------------------------------- |
| fill   | tk.X, Y, BOTH | 填充所有的分配区间                 |
| expend | True, False   | 设置填充格式，是否填充所有父类空间 |

```python
tk.Label(window, text='P', fg='red').pack(side='top')    # 上
tk.Label(window, text='P', fg='red').pack(side='bottom') # 下
tk.Label(window, text='P', fg='red').pack(side='left')   # 左
tk.Label(window, text='P', fg='red').pack(side='right')  # 右
```



#### 3. Place

> 再接下来我们来看place(), 这个比较容易理解，就是给精确的坐标来定位，如此处给的(50, 100)，就是将这个部件放在坐标为(x=50, y=100)的这个位置, 后面的参数 anchor='nw'，就是前面所讲的锚定点是西北角。
>
> 此外，我们也可以采用相对坐标进行相对布局，向place中传入relx,relwidth表示控件采用相对坐标(0-1)和相对大小(0-1)。

```python
label1 = tkinter.Label(win, text="柳多妍", bg="pink")
label2 = tkinter.Label(win, text="多多", bg="yellow")
label3 = tkinter.Label(win, text="超级飞侠", bg="red")
# label1.pack()   # #默认没有布局，字有多长，背景也有多长，和其他label错落显示
# label2.pack()
# label3.pack()
label1.place(x=10, y=10)   # #固定坐标，按绝对布局显示，窗口大小的变化对布局没有影响
label2.place(x=50, y=50)
label3.place(relx=1, rely=0)
win.mainloop()   # #窗口持久化
```

> **注意：不要试图在一个主窗口中混合使用pack和grid。**

#### 4. Common Attribute

> 此外，其Layout本质也是一个可操作的类，其具有以下属性或方法，如果只想要查询对应布局的属性，可通过类名_属性，如：pack_slaves().

| 属性或方法 | 参数 | 说明                                  |
| ---------- | ---- | ------------------------------------- |
| slaves     | 无   | 返回所有容器内的Widget控件            |
| info       | 无   | 返回pack选项的对应值                  |
| forget     | 无   | 隐藏Widget控件，显示只需再次布局      |
| location   | x,y  | 传回单位所在位置，如果不在返回(-1,-1) |
| size       | 无   | 返回Widget控件的大小                  |
| propagate  | bool | 父窗口大小是否由子控件决定            |

---

### 1. Label

> Label()方法可以用于在窗口中建立文字或图像标签。
>
> 此外，Label的textvariable暂时未发现可以直接使用的方法（其他控件可直接调用），若直接调用label标签会始终无法读取变量值，可通过Label["text"] = string 实现动态改变文本。

**常用属性**

| 属性       | 值    | 说明                                                         |
| ---------- | ----- | ------------------------------------------------------------ |
| compound   | loc   | 图像与文字共存时，图像相对于文字的位置                       |
| underline  | int   | 文字在指定宽度后文字下划线                                   |
| wraplength | int   | 文字在指定宽度后自动换行，以像素计                           |
| font       | tuple | 文本格式，按照以下顺序family, size, weight, slant, underline, overstrike |



### 2. Button

#### 2.1 Synopsis

> Button（按钮）部件是一个标准的Tkinter窗口部件，用来实现各种按钮。按钮能够包含文本或图象，并且你能够将按钮与一个Python函数或方法相关联。当这个按钮被按下时，Tkinter自动调用相关联的函数或方法。
>
> 按钮仅能显示一种字体，但是这个文本可以跨行。另外，这个文本中的一个字母可以有下划线，例如标明一个快捷键。默认情况，Tab键用于将焦点移动到一个按钮部件。

#### 2.2 Params

| Params       | Optional | Discription                     |
| ------------ | -------- | ------------------------------- |
| command      | True     | 指定按钮消息的回调函数；        |
| state        | True     | 指定按钮的状态（disabled）；    |
| text         | False    | 指定按钮上显示的文本；          |
| textvariable | True     | 可变文本，与StringVar等配合着用 |

> **Tip：可以通过lambda函数，向command函数传递带参的函数！**



### 3. Entry

#### 3.1 Synopsis

> Entry是tkinter类中提供的的一个**单行文本输入域**，用来输入显示一行文本，收集键盘输入(类似 HTML 中的 text)，超过长度限制的内容会被自动隐藏。
>

#### 3.2 Params

| 参数              | 值                            | 描述                                 |
| ----------------- | ----------------------------- | ------------------------------------ |
| selectbackground  | color                         | 设置文本框背景色                     |
| selectforeground  | color                         | 设置文本框的前景色                   |
| selectborderwidth | int                           | 设置文本框边界宽度                   |
| state             | "normal","disable","readonly" | 设置文本                             |
| show              | str                           | 设置文本内容展示样式，常用于密码保护 |
| xscrollcommand    | bool                          | 在x轴使用滚动条                      |

#### 3.3 Method

> 文本框除了上述参数外，还有其他一些常用的方法用以实现基本的输入输出。

| 方法   | 值          | 描述                                              |
| ------ | ----------- | ------------------------------------------------- |
| get    | 无          | 获取文本框当前文字内容                            |
| insert | index,s     | 向文本框index位置插入s文本                        |
| delete | first, last | 删除first到last-1位置的文本内容，结尾用tk.END表示 |



### 4. Text

> Text控件主要处理多行的输入， 可以通过scrollcommand来添加滚动条。

#### Params

> + **-autoseparators**
>
> Specifies a boolean that says whether separators are automatically inserted in the undo stack. Only meaningful when the **-undo** option is true.
>
> + **-blockcursor**
>
> Specifies a boolean that says whether the blinking insertion cursor should be drawn as a character-sized rectangular block. If false (the default) a thin vertical line is used for the insertion cursor.
>
> + **-endline**
>
> Specifies an integer line index representing the line of the underlying textual data store that should be just after the last line contained in the widget. This allows a text widget to reflect only a portion of a larger piece of text. Instead of an integer, the empty string can be provided to this configuration option, which will configure the widget to end at the very last line in the textual data store.
>
> + **-inactiveselectbackground**
>
> Specifies the colour to use for the selection (the **sel** tag) when the window does not have the input focus. If empty, **{}**, then no selection is shown when the window does not have the focus.
>
> + **-insertunfocussed**
>
> Specifies how to display the insertion cursor when the widget does not have the focus. Must be **none** (the default) which means to not display the cursor, **hollow** which means to display a hollow box, or **solid** which means to display a solid box. Note that **hollow** and **solid** will appear very similar when the **-blockcursor** option is false.
>
> + **-maxundo**
>
> Specifies the maximum number of compound undo actions on the undo stack. A zero or a negative value imply an unlimited undo stack.
>
> + **-spacing1**
>
> Requests additional space above each text line in the widget, using any of the standard forms for screen distances. If a line wraps, this option only applies to the first line on the display. This option may be overridden with **-spacing1** options in tags.
>
> + **-spacing2**
>
> For lines that wrap (so that they cover more than one line on the display) this option specifies additional space to provide between the display lines that represent a single line of text. The value may have any of the standard forms for screen distances. This option may be overridden with **-spacing2** options in tags.
>
> + **-spacing3**
>
> Requests additional space below each text line in the widget, using any of the standard forms for screen distances. If a line wraps, this option only applies to the last line on the display. This option may be overridden with **-spacing3** options in tags.
>
> + **-startline**
>
> Specifies an integer line index representing the first line of the underlying textual data store that should be contained in the widget. This allows a text widget to reflect only a portion of a larger piece of text. Instead of an integer, the empty string can be provided to this configuration option, which will configure the widget to start at the very first line in the textual data store.
>
> + **-state**
>
> Specifies one of two states for the text: **normal** or **disabled**. If the text is disabled then characters may not be inserted or deleted and no insertion cursor will be displayed, even if the input focus is in the widget.
>
> + **-tabs**
>
> Specifies a set of tab stops for the window. The option's value consists of a list of screen distances giving the positions of the tab stops, each of which is a distance relative to the left edge of the widget (excluding borders, padding, etc). Each position may optionally be followed in the next list element by one of the keywords **left**, **right**, **center**, or **numeric**, which specifies how to justify text relative to the tab stop. **Left** is the default; it causes the text following the tab character to be positioned with its left edge at the tab position. **Right** means that the right edge of the text following the tab character is positioned at the tab position, and **center** means that the text is centered at the tab position. **Numeric** means that the decimal point in the text is positioned at the tab position; if there is no decimal point then the least significant digit of the number is positioned just to the left of the tab position; if there is no number in the text then the text is right-justified at the tab position. For example, “**-tabs {2c left 4c 6c center}**” creates three tab stops at two-centimeter intervals; the first two use left justification and the third uses center justification.If the list of tab stops does not have enough elements to cover all of the tabs in a text line, then Tk extrapolates new tab stops using the spacing and alignment from the last tab stop in the list. Tab distances must be strictly positive, and must always increase from one tab stop to the next (if not, an error is thrown). The value of the **-tabs** option may be overridden by **-tabs** options in tags.If no **-tabs** option is specified, or if it is specified as an empty list, then Tk uses default tabs spaced every eight (average size) characters. To achieve a different standard spacing, for example every 4 characters, simply configure the widget with “**-tabs "[expr {4 \* [font measure $font 0]}] left" -tabstyle wordprocessor**”.
>
> + **-tabstyle**
>
> Specifies how to interpret the relationship between tab stops on a line and tabs in the text of that line. The value must be **tabular** (the default) or **wordprocessor**. Note that tabs are interpreted as they are encountered in the text. If the tab style is **tabular** then the *n*'th tab character in the line's text will be associated with the *n*'th tab stop defined for that line. If the tab character's x coordinate falls to the right of the *n*'th tab stop, then a gap of a single space will be inserted as a fallback. If the tab style is **wordprocessor** then any tab character being laid out will use (and be defined by) the first tab stop to the right of the preceding characters already laid out on that line. The value of the **-tabstyle** option may be overridden by **-tabstyle** options in tags.
>
> + **-undo**
>
> Specifies a boolean that says whether the undo mechanism is active or not.
>
> + **-wrap**
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

##### search

```python
text.search(key, start, end)
```

> 使用search方法进行检索查找关键词，这个方法传回找到的字符的第一个位置索引。
>
> 

#### Bookmark

> Text可以通过在特殊位置设置书签方便查询，书签虽然不会显示，但会在编辑系统内被记录，tkinter中默认的书签有两个，分别为INSERT和CURRENT，它们的相对位置可以参考前文，以下为书签常用的方法：
>
> + `index(mark)`:传回指定书签的行和列；
> + `mark_names()`:传回Text对象所有的书签；
> + `mark_set(mark, index)`:在指定位置设置书签；
> + `mark_unset(mark)`:取消指定书签设置

#### Tags

> Tags是指一个区域文字，然后我们可以为这个区域起一个名字作为标签，此后我们可以通过标签对区域内的文字进行索引，修改其属性，其支持的操作如下：

| 方法       | 值                 | 说明                                 |
| ---------- | ------------------ | ------------------------------------ |
| tag_add    | name,start[,end]   | 将指定区域的文字用name作为其标签标记 |
| tag_config | name, options      | 设置标签内文字格式                   |
| tag_delete | name               | 删除标签且移除相应的属性             |
| tag_remove | name, start[, end] | 仅删除标签不移除其相应的属性         |

> index中包括一个特殊参数：tk.SEL，指选中文本索引，其中SEL_FIRST为第一个字符对应索引，SEL_LAST为最后一个字符对应索引。

#### ClipBoard

> 复制粘贴等功能已经内置在tkinter中了，此处介绍其函数实现。
>
> 1. clipboard_get() **#获取剪贴板内容**
> 2. clipboard_clear() **#清除剪贴板内容**
> 3. clipboard_append("xxooxx") **#向剪贴板追加内容**
> 4. selection_get() **# 获取选中内容**

#### Undo

> Text有一个撤回复原功能，在这之前必须要将Text中的Undo参数赋值True才可使用。具体方法如下：
>
> 1. **edit_redo()**:复原
> 2. **edit_undo()**:撤销



### 5. Listbox

列表框是一个显示一系列选项的Widget控件，用户可以进行单项或多项的选择。

| 参数             | 值                                 | 说明                   |
| ---------------- | ---------------------------------- | ---------------------- |
| listvariable     | 列表或元组                         | 用于显示序列类变量     |
| selectmode       | browse, single, multiple, extended | 选项选取模式及拖拽选取 |
| x/yscrollcommand | bool                               | 是否使用滚动条         |

除了基本的insert, delete, get选项外，Listbox还支持以下方法：

| 参数               | 值     | 说明                   |
| ------------------ | ------ | ---------------------- |
| size               | 无     | 返回列表项目数量       |
| selection_set      | index: | 选取特定索引对应选项   |
| curselection       | 无     | 返回选取项目的索引号   |
| selection_includes | index  | 检查指定索引是否被选取 |
| nearest            | y      | 返回最接近项目的索引值 |



### 6. Radiobutton

#### 6.1 Description

> In fact, radiobutton is a label, it's just achieved by changing text of label. Showing a choose circle and text first, and then change to a fonticon with two circle and text. Simultaneously, binded with event <Button-1>, so that can make choose true.
>
> Additionally, you can set a variable to make a just one choose from mulitiple radiobutton, and set a initial value to make one selected as default.
>
> Flag as following.

```python
choice = tk.Radiobutton(master, *args)
```

#### 6.2 Params

| Params       | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| command      | 此选项设置为每当更改单选按钮的状态时必须调用的过程。         |
| selectcolor  | 选中时单选按钮的颜色。                                       |
| selectimage  | 选择时在radiobutton上显示的图像。                            |
| state        | 它表示单选按钮的状态。 Radiobutton的默认状态为NORMAL。但是，我们可以将其设置为DISABLED以使radiobutton无响应。 |
| text         | 要在radiobutton上显示的文本。                                |
| textvariable | 它是String类型，表示小部件显示的文本。                       |
| value        | 每个radiobutton的值在用户打开时分配给控制变量。              |
| variable     | 它是控制变量，用于跟踪用户的选择。它在所有radiobutton之间共享。 |
| indicatoron  | 盒子按钮，用于多个单选快速排列                               |

#### 6.3 Method

| Function   | Description                                     |
| ---------- | ----------------------------------------------- |
| deselect() | 用于转动单选按钮。                              |
| flash()    | 用于在有效和正常颜色之间闪烁几次无线电按钮。    |
| invoke()   | 它用于调用Radiobutton状态更改时关联的任何过程。 |
| select()   | 用于选择radiobutton。                           |



### 7. Checkbutton　　

> 复选框，与单选框不同的是，它的框是方形框，同时它可以有多个不同的值。点击这个按钮将会在不同的值间切换，选择和取消选择。

| 属性               | 值    | 描述                        |
| ------------------ | ----- | --------------------------- |
| activebackground   | color | 鼠标在复选框上时的背景色    |
| disabledforeground | color | 不可操作时的颜色            |
| offvalue/onvalue   | bool  | 控制变量，未选中/选中时的值 |



### 8. Scale

#### 8.1 Synopsis

> Scale可以翻译为尺度，即常用的拉动条，可以根据尺位返回相应的数字。

```python
Scale(master, params)
```

#### 8.2 Params

| 参数         | 值                  | 说明                     |
| ------------ | ------------------- | ------------------------ |
| digits       | \                   | 尺度数值，常绑定数值变量 |
| variable     | \                   | 绑定变量                 |
| from_        | int/float           | 尺度条起始值             |
| to           | int/float           | 尺度条终止值             |
| label        | str                 | 尺度条文字标签，默认没有 |
| orient       | horizonal, vertical | 尺度条方向               |
| repeatdelay  | int/float           | 聚焦拖动操作延迟         |
| resolution   | int/float           | 尺度每次更改的值         |
| showvalue    | bool                | 是否显示刻度当前值       |
| tickinterval | int/float           | 尺度条的标记刻度         |
| troughcolor  | color               | 槽颜色                   |
| command      | fuction             | 尺度条移动时触发函数     |



### 9. Canvas

#### 9.1 Synopsis　　

> Canvas画布提供绘图功能(直线、椭圆、多边形、矩形) 可以包含图形或位图，用来绘制图表和图，创建图形编辑器，实现定制窗口部件。
>

#### 9.2 Create

##### 1. Line

> Items of type **line** appear on the display as one or more connected line segments or curves. Line items support coordinate indexing operations using the **dchars**, **index** and **insert** widget commands. Lines are created with widget commands of the following form:
>

```
pathName create line x1 y1... xn yn ?option value ...?
pathName create line coordList ?option value ...?
```

> The arguments *x1* through *yn* or *coordList* give the coordinates for a series of two or more points that describe a series of connected line segments. After the coordinates there may be any number of *option*-*value* pairs, each of which sets one of the configuration options for the item. These same *option*-*value* pairs may be used in **itemconfigure** widget commands to change the item's configuration. A line item is the current item whenever the mouse pointer is over any segment of the line, whether drawn or not and whether or not the line is smoothed.
>

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

  > Indicates whether or not arrowheads are to be drawn at one or both ends of the line. *Where* must have one of the values **none** (for no arrowheads), **first** (for an arrowhead at the first point of the line), **last** (for an arrowhead at the last point of the line), or **both** (for arrowheads at both ends). This option defaults to **none**. When requested to draw an arrowhead, Tk internally adjusts the corresponding line end point so that the rendered line ends at the neck of the arrowhead rather than at its tip so that the line doesn't extend past the edge of the arrowhead. This may trigger a **Leave** event if the mouse is hovering this line end. Conversely, when removing an arrowhead Tk adjusts the corresponding line point the other way round, which may trigger an **Enter** event.

- **-arrowshape** *shape*

  > This option indicates how to draw arrowheads. The *shape* argument must be a list with three elements, each specifying a distance in any of the forms described in the **COORDINATES** section above. The first element of the list gives the distance along the line from the neck of the arrowhead to its tip. The second element gives the distance along the line from the trailing points of the arrowhead to the tip, and the third element gives the distance from the outside edge of the line to the trailing points. If this option is not specified then Tk picks a “reasonable” shape.

- **-capstyle** *style*

  > Specifies the ways in which caps are to be drawn at the endpoints of the line. *Style* may have any of the forms accepted by **[Tk_GetCapStyle](https://www.tcl.tk/man/tcl8.6/TkLib/GetCapStyl.htm)** (**butt**, **projecting**, or **round**). If this option is not specified then it defaults to **butt**. Where arrowheads are drawn the cap style is ignored.

- **-joinstyle** *style*

  > Specifies the ways in which joints are to be drawn at the vertices of the line. *Style* may have any of the forms accepted by **[Tk_GetJoinStyle](https://www.tcl.tk/man/tcl8.6/TkLib/GetJoinStl.htm)** (**bevel**, **miter**, or **round**). If this option is not specified then it defaults to **round**. If the line only contains two points then this option is irrelevant.

- **-smooth** *smoothMethod*

  > *smoothMethod* must have one of the forms accepted by **[Tcl_GetBoolean](https://www.tcl.tk/man/tcl8.6/TclLib/GetInt.htm)** or a line smoothing method. Only **true** and **raw** are supported in the core (with **bezier** being an alias for **true**), but more can be added at runtime. If a boolean false value or empty string is given, no smoothing is applied. A boolean truth value assumes **true** smoothing. If the smoothing method is **true**, this indicates that the line should be drawn as a curve, rendered as a set of quadratic splines: one spline is drawn for the first and second line segments, one for the second and third, and so on. Straight-line segments can be generated within a curve by duplicating the end-points of the desired line segment. If the smoothing method is **raw**, this indicates that the line should also be drawn as a curve but where the list of coordinates is such that the first coordinate pair (and every third coordinate pair thereafter) is a knot point on a cubic Bezier curve, and the other coordinates are control points on the cubic Bezier curve. Straight line segments can be generated within a curve by making control points equal to their neighbouring knot points. If the last point is a control point and not a knot point, the point is repeated (one or two times) so that it also becomes a knot point.

- **-splinesteps** *number*

  > Specifies the degree of smoothness desired for curves: each spline will be approximated with *number* line segments. This option is ignored unless the **-smooth** option is true or **raw**.

##### 2. oval

> Items of type **oval** appear as circular or oval regions on the display. Each oval may have an outline, a fill, or both. Ovals are created with widget commands of the following form:
>

```
pathName create oval x1 y1 x2 y2 ?option value ...?
pathName create oval coordList ?option value ...?
```

> The arguments *x1*, *y1*, *x2*, and *y2* or *coordList* give the coordinates of two diagonally opposite corners of a rectangular region enclosing the oval. The oval will include the top and left edges of the rectangle not the lower or right edges. If the region is square then the resulting oval is circular; otherwise it is elongated in shape. After the coordinates there may be any number of *option*-*value* pairs, each of which sets one of the configuration options for the item. These same *option*-*value* pairs may be used in **itemconfigure** widget commands to change the item's configuration. An oval item becomes the current item when the mouse pointer is over any part that is painted or (when fully transparent) that would be painted if both the **-fill** and **-outline** options were non-empty.
>

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

##### 3. Arc

```python
create_arc(x1, y1, x2, y2, extent, style, options)
```

其他参数包括：

| 参数    | 值                   | 说明                                   |
| ------- | -------------------- | -------------------------------------- |
| extent  | angle                | 绘制圆弧的度数                         |
| fill    | color                | 填充圆弧的颜色                         |
| outline | color                | 圆弧线条颜色                           |
| start   | angle                | 圆弧初始度数                           |
| stipple | ？                   | 绘制位图圆弧                           |
| style   | arc, chord, pleslice | 控制圆弧的类型，分别为圆弧，环形与扇形 |

##### 4. Polygon

```python
create_polygon(x1, y1, x2, y2,...., options)
```

参数包括：

| 参数    | 值   | 说明 |
| ------- | ---- | ---- |
| dash    | /    | 略   |
| stipple | /    | 略   |

##### 5. text

```python
create_text(x, y, text, options)
```

无其他特殊参数。

##### 6. create_image

```python
create_image(x, y, options)
```

无特殊参数

#### 9.3 Method

##### delete

##### 基本动画

```python
canvas.move(ID, xMove, yMove)
canvas.update()
```

| 参数  | 值        | 说明                     |
| ----- | --------- | ------------------------ |
| ID    | id        | 对象编号（操作返回对象） |
| xMove | int/float | 水平方向移动的距离       |
| yMove | int/float | 竖直方向移动的距离       |



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

> 1. **-postcommand**
>
> 	If this option is specified then it provides a Tcl command to execute each time the menu is posted. The command is invoked by the **post** widget command before posting the menu. Note that in Tk 8.0 on Macintosh and Windows, all post-commands in a system of menus are executed before any of those menus are posted. This is due to the limitations in the individual platforms' menu managers.
>
> 2. **-selectcolor**
>
> 	For menu entries that are check buttons or radio buttons, this option specifies the color to display in the indicator when the check button or radio button is selected.
>
> 3. **-tearoff** 
>
> 	This option must have a proper boolean value, which specifies whether or not the menu should include a tear-off entry at the top. If so, it will exist as entry 0 of the menu and the other entries will number starting at 1. The default menu bindings arrange for the menu to be torn off when the tear-off entry is invoked. This option is ignored under Aqua/MacOS, where menus cannot be torn off.
>
> 4. **-tearoffcommand**
>
> 	If this option has a non-empty value, then it specifies a Tcl command to invoke whenever the menu is torn off. The actual command will consist of the value of this option, followed by a space, followed by the name of the menu window, followed by a space, followed by the name of the name of the torn off menu window. For example, if the option's value is “**a b**” and menu **.x.y** is torn off to create a new menu **.x.tearoff1**, then the command “**a b .x.y .x.tearoff1**” will be invoked. This option is ignored under Aqua/MacOS, where menus cannot be torn off.
>
> 5. **-title** 
>
> 	The string will be used to title the window created when this menu is torn off. If the title is NULL, then the window will have the title of the menubutton or the text of the cascade item from which this menu was invoked.
>
> 6. **-type** 
> This option can be one of **menubar**, **tearoff**, or **normal**, and is set when the menu is created. While the string returned by the configuration database will change if this option is changed, this does not affect the menu widget's behavior. This is used by the cloning mechanism and is not normally set outside of the Tk library.
>
> 7. **-accelerator**
>
> 	Specifies a string to display at the right side of the menu entry. Normally describes an accelerator keystroke sequence that may be used to invoke the same function as the menu entry. **This is a display option, it does not actually set the corresponding binding (which can be achieved using the *bind* command).** This option is not available for separator or tear-off entries.

常用命令：

```python
add_cascade()	# 添加子菜单
add_command()	# 添加命令
add_separator()	# 添加分隔符
add_checkbutton()	# 添加复选框


```

> **Post()** --> 右键菜单栏的制作
>
> 1. Menu 类里面有一个 post 方法，它接收两个参数，即 x 和 y 坐标，它会在相应的位置弹出菜单；
> 2. 利用 Menu 的 post 方法，还有 bind 方法；
>
> ```python
> def showpopup(event):
> 	tk.Menu.post(event.x_root, event.y_root)
>     
> root.bind("<Button-3>", showpopup)
> ```



### 11. Frame 

#### Description　

> 框架，用来承载放置其他GUI元素，就是一个容器，是一个在 Windows 上分离小区域的部件, 它能将 Windows 分成不同的区,然后存放不同的其他部件. 同时一个 Frame 上也能再分成两个 Frame, Frame 可以认为是一种容器，Frame内部组件的坐标位置都是相对坐标，类似于HTML中的块元素。
>
> 实例化frame框架后须**设定高度及宽度**，若添加边框，须同时指定**bd及relief**属性。

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



### 12. LabelFrame

> 标签框架是一个特殊的容器控件，类似于普通框架，同时在框架内设置有一个标签，常常置于左上角，并用实线闭合，可以组合复选框盒子使用，基本用法与框架一致，因此此处不再补充叙述。



### 13. Toplevel

#### 13.1 Synopsis

> Toplevel（顶级窗口）组件类似于 Frame 组件，但 Toplevel 组件是一个独立的顶级窗口，这种窗口通常拥有标题栏、边框等部件。
>
> Toplevel 组件通常用在显示额外的窗口、对话框和其他弹出窗口上。

#### 13.2 Params

| 选项                | 含义                                                         |
| :------------------ | :----------------------------------------------------------- |
| background          | 1. 设置背景颜色 2. 默认值由系统指定 3. 为了防止更新，可以将颜色值设置为空字符串 |
| borderwidth         | 设置边框宽度                                                 |
| class_              | 默认值是 Toplevel                                            |
| colormap            | 1. 有些显示器只支持 256 色（有些可能更少），这种显示器通常提供一个颜色映射来指定要使用要使用的 256 种颜色 2. 该选项允许你指定用于该组件以及其子组件的颜色映射 3. 默认情况下，Toplevel 使用与其父组件相同的颜色映射 4. 使用此选项，你可以使用其他窗口的颜色映射代替（两窗口必须位于同个屏幕并且具有相同的视觉特性） 5. 你也可以直接使用 "new" 为 Toplevel 组件分配一个新的颜色映射 6. 一旦创建 Toplevel 组件实例，你就无法修改这个选项的值 |
| container           | 1. 该选项如果为 True，意味着该窗口将被用作容器，一些其它应用程序将被嵌入  2. 默认值是 False |
| cursor              | 1. 指定当鼠标在 Toplevel 上飘过的时候的鼠标样式 2. 默认值由系统指定 |
| highlightbackground | 指定当 Toplevel 没有获得焦点的时候高亮边框的颜色             |
| highlightcolor      | 指定当 Toplevel 获得焦点的时候高亮边框的颜色                 |
| highlightthickness  | 指定高亮边框的宽度                                           |
| menu                | 设置该选项为 Toplevel 窗口提供菜单栏                         |
| takefocus           | 1. 指定该组件是否接受输入焦点（用户可以通过 tab 键将焦点转移上来） 2. 默认值是 False |



### 14. OptionMenu

> OptionMenu 可以翻译为下拉式菜单，用户可以从中选择一项。其基本语法如下：

```python
OptionMenu(master, options, *values)
```

> 其创建只需要传递列表作为选项即可，其基本的赋值读取等方法与文本框等一致。

### 15. Message

> Message主要是可以显示短消息，其功能与Label类似，但是使用起来更加灵活，可以自动分行，对于一些不想再调整的文本内容，可以用Message展示，此外，其基本语法与Label一致，不赘述。

### 16. Scrollbar

> 滚动条，可以设置在Listbox，Text和Canvas等控件上，通过x/yscrollcommand=scrollbar.set方法绑定。

| 参数 | 值   | 说明                          |
| ---- | ---- | ----------------------------- |
| jump | int  | 每次拖动触发command的最小距离 |

### 17. PanedWindow

> PanedWindow可以翻译为面板，是一个 Widget 容器组件，可以在此容器内建立任意数量的子控件。不过一般是在此控件内建立几个子控件，以特定的方向进行排列。

| 参数       | 值                  | 说明         |
| ---------- | ------------------- | ------------ |
| handlepad  | int                 | 面板显示宽度 |
| handlesize | int                 | 面板显示大小 |
| orient     | horizontal/vertical | 面板配置方向 |
| sashcursor | cursor              | 分隔线光标   |
| sashrelief | relief              | 分隔线样式   |
| showhandle | bool                | 滑块属性     |

> 其次，我们可以通过add(child, option)方法来插入子对象。



## 4. Advanced Widget

> Provided in module ttk in tkinter, before you use them, you need to import.
>

### 1. Combobox

> Combobox可以翻译为组合框，这是tkinter.ttk 的Widget组件，它的特性与 OptionMenu 类似，可以说是 Entry和下拉菜单的组合，其基本语法如下：

```python
Combobox(master, options)
```

> 其中，用value表示其选项内容。其默认值设置可以通过current(index)方法实现。此外，当Combobox中的选项内容改变时，会产生虚拟的<ComboboxSelected>>事件，根据这个特性可绑定对应的回调函数。

### 2. ScrolledText

> 

### 3. Spinbox

> Spinbox是一种输入控件，它是Entry和Button的组合题，它允许用户单击鼠标改变文本框的值，也可以直接输入数值。

```python
Spinbox(master, params)
```

| 参数           | 值        | 说明                 |
| -------------- | --------- | -------------------- |
| from_          | int/float | 起始值               |
| command        | function  | 回调函数             |
| repeatdelay    | int/float | 延迟                 |
| increment      | int/float | 每次操作增值         |
| format         | \         | 格式符               |
| to             | int/float | 终止值               |
| xscrollcommand | bool      | x轴滚动条            |
| values         | tuple     | 用于表示非数值型数据 |

### 5. Treeview

#### 5.1 Synopsis

> Treeview是ttk的控件，主要提供多栏显示功能，我们可以称为树状表格数据，在设计时也可以在左边栏设计成树状结构或者层次结构，用户可以显示或隐藏如何部分，这个**最左边的栏称为图标栏**（对应参数为text），同时可以通过image参数向其中传递图片，排序可以通过将所有的值读取排序后重新赋值。其基本的语法如下:

```python
Treeview(master, options)
```

#### 5.2 Params

| 参数           | 值                          | 说明                                                         |
| -------------- | --------------------------- | ------------------------------------------------------------ |
| columns        | names                       | 要显示的列表头（比实际显示列数少一）                         |
| displaycolumns | index                       | 列表头展示顺序                                               |
| selectmode     | browse, extended, none      | 鼠标选中项目效果                                             |
| show           | "tree", "heading", "#index" | “tree”表示仅显示第一列（即图标列），“headings”表示显示除一列的其他列 |
| height         | int                         | 表格显示的行数                                               |
| command        | function                    | 回调函数                                                     |
| minwidth       | int                         | 表格的最小列宽                                               |

#### 5.3 Method

| 方法      | 值                                        | 说明                                  |
| --------- | ----------------------------------------- | ------------------------------------- |
| insert    | id, index, text, values, tag              | 插入数据                              |
| heading   | index, text                               | 定义行                                |
| column    | index, [anchor, width, minwidth, stretch] | 定义列的格式                          |
| get_child | item                                      | 获取item的一个元组id值                |
| move      | id, parent, index                         | 将id所指项目移至parent层次的index位置 |

#### 5.4 Event

> 1. << TreeviewSelect>>，代表选择变化是发生；
> 2. << TreeviewOpen>>，item的open=True时发生；
> 3. << TreeviewClose>>，item的open=False时发生；

#### 5.5 Hierarchy

> 层级式树状表格，即在insert的参数id中创建相应的项目id即可，无时为""。

```python
id = tree.insert("", index=tk.END, text="ID")
tree.insert(id, index=tk.END, text=text, values=values)
```



### 6. Sizegrip



### 7. Notebook

> Notebook 可以理解为选项卡，同样属于容器类组件，通过add方法向其添加组件，其基本属性与其他容器类保持一致。
>

### 8. Progressbar

#### 基本概念

> Progressbar 可以解释为进度条，主要是当做一个工作进度的指针，在这个控件中会有一个指针，由此指针可以了解工作进度。
>

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

> 1. **determinate**
>
> 	一个指针会从起点移至终点，通常当我们知道所需工作时间时，可以使用此模式，这是默认模式。
>
> 2. **indeterminate**
>
> 	一个指针会在起点和终点间来回移动，通常当我们不知道工作所需时间时，可以使用此模式，主要目的是让用户知道程序仍然在继续工作。
>

**Instance**


```python
progressbarOne = tkinter.ttk.Progressbar(root)
progressbarOne.pack(pady=20)

# 进度值最大值
progressbarOne['maximum'] = 100
# 进度值初始值
progressbarOne['value'] = 20
# 横排 长度200 起点移至终点
progressbarTwo = tkinter.ttk.Progressbar(root,              							orient=tkinter.HORIZONTAL,
                        length=200, mode='determinate')
progressbarTwo.pack(pady=20)
# 进度值最大值
progressbarTwo['maximum'] = 100
# 进度值初始值
progressbarTwo['value'] = 80
```
**注意：现在进度条还不能动！**

> **动画设计**
>   如果想要设计含动画效果的Progressbar，可以在每次更新Progressbar 对象的value值时调用update()方法，这时窗口可以依据value值重绘，这样就可以达到动画效果。

```python
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

> 1. **start(interval)**：每隔interval时间移动一次指针。interval的默认值是50ms，每次移动指针调用一次step(amount)。在step()方法内的amount参数意义就是增值量；
> 2. **step(amount)**：每次增加一次amount，默认值是1.0，在determinate模式下，指针不会超过maximum参数。在indeterminate模式下，当指针达到maximum参数值的前一格时，指针会回到起点；
> 3. **stop()**：停止start()运行；

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



### 9. Separator

> 在设计GUI时需要适时添加一些分割线，使得整体的视觉效果更好，在ttk中有Separator模块来实现这一功能。
>
> 其中，Orient朝向设置包括水平(HORIZONTAL)和竖直(VERTICAL)方向，同时，你可以通过在打包函数中传递 `fill` 参数来实现铺满 (fill=X/Y) 。

```python
sep = Separator(master, orient, params)
```



### 10. Menubutton



## 5. Something else

### lambda

#### Description

> To transfer parameters to widget in tkinter, especially like Button. 
>

#### Format

```python
lambda params : expression
```

> Return the outcome of expression.
>

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



## 6. Variable management

### Synopsis

> 有些控件在执行时会更改内容，例如，文本框(Entry)，选项按钮(Radio button)等；
>
> 有些控件我们可以更改他们的内容，例如标签(Label)等，如果想要更改他们的内容，可以使用这些控件的参数，例如，textvariable、variable、onvalue等；
>
> 不过要将控件的参数以变量方式处理时，需要借助tkinter模块内的变量类别(Variable Classes)。这个类别有4个子类别，每一个类别其实就是一个数据类型的构造方法，我们可以通过这4个子类别的数据类型将他们与控件相关的参数结合。
>

### Type

```python
x = IntVar()		# 整型变量，默认是0
x = DoubleVar()		# 浮点型变量，默认是0.0
x = StringVar()		# 字符串变量，默认是""
x = BooleanVar()	# 布尔型变量，True是1，False是0
```

### Operation

#### set

> use set() to set the value of var.
>

```python
string.set(value)
```

#### get

> use get() to get the value of var.
>

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
> 由于我们所设计的程序并不需要传递参数，所以可以直接用`*args`当做参数内容。
>
> `%s`是将变量传到`str()`函数中，结果是将变量转化适合人阅读的格式
>
> `%r`是将变量穿到`repr()`函数中，结果是将变量转化成适合机器阅读的格式，可以将%r后的变量理解为一个对象

##### mode : "w"

> 我们可以利用变量设置追踪`Widget`控件("w"模式)，当其内容**发生改变**时，让程序自动执行函数，称为变动追踪。
>

```python
string.trace("w", function)
```

##### mode : "r"

> 我们也可以设计当控件内容**被读取**时，执行追踪并执行特定函数，称为读取追踪。
>

```python
string.trace("r", function)
```



## 7. Event response

> Tkinter 使用所谓的 事件队列 (event sequences) 暴露接口以绑定 handler 到相关事件. 事件以字符串的形式给出:
>
> `type` 字段是一个事件的关键字段. `modifer` 和 `detail` 字段则不是必要字段, 很多情况下这两个字段都不会被赋值. 这两个字段用以提供`type` 所代表的事件的附加信息. `type` 字段描述事件种类, 比如鼠标点击, 键位按下, 控件获得焦点 等.

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
| <a>             | “a” 键被点击. 其他字符也可以如此定义. 特殊情况包括 空格 (<space>) 和 小于号 (<less>). 注意 “1” 是绑定键盘键位, 而 <1> 则是按钮绑定. |
| <Shift-Up>      | 在 shift 被按下时点击 up 键. 同样的, 也有 Alt-Up, Control-Up 事件. |
| <Configure>     | 控件大小改变事件. 新的控件大小会存储在 event 对象中的 width 和 height 属性传递. 有些平台上该事件也可能代表控件位置改变. |

> 1. **事件**（event）：是指点击、按键等操作，在tkinter中，event是一个类，当某个事件发生时，生成一个event对象，不同类型的事件生成具有不同属性的event对象。
> 2. **事件处理**（event handler）：是指在捕获到事件后，程序自动执行的操作，是回调函数（recall function）。
> 3. **事件绑定**（event binding）：是当一个事件发生时程序能够做出响应。tkinter提供三种绑定方式：实例绑定bind（将某个事件处理绑定到某个组件上）、类绑定bind_class（将某个事件处理绑定到某类组件上）、应用绑定bind_all（将某个事件处理绑定到所有组件上）。
>

### Event description

**（1）事件格式：**

> 在Tkinter中，事件的描述格式为：**<[modifier-]-type[-detail]>**，其中：
>
> - modifier：事件修饰符。如：Alt、Shit组合键和Double事件。
> - type：事件类型。如：按键（Key）、鼠标（Button/Motion/Enter/Leave/Relase）、Configure等。
> - detail：事件细节。如：鼠标左键（1）、鼠标中键（2）、鼠标右键（3）。
>

**注意大小写！！！**

| Type     | **Format**                      | **Discription**                                              |
| -------- | ------------------------------- | ------------------------------------------------------------ |
| 鼠标事件 | <Button-1>                      | 鼠标点击（1-左键，2-中键，3-右键，4-上滚，5-下滚）           |
|          | <Double-Button-1>               | 鼠标双击（1-左键，2-中键，3-右键）                           |
|          | <B1-Motion>                     | 鼠标拖动（1-左键，2-中键，3-右键）                           |
|          | <ButtonRelease-1>               | 鼠标按下之后释放（1-左键，2-中键，3-右键）                   |
|          | <Enter>                         | 鼠标进入控件范围（widget），不是键盘按键                     |
|          | <Leave>                         | 鼠标离开控件范围（widget）                                   |
| 键盘事件 | <Key>/<KeyPress>                | 任意键盘按键（键值会以char的格式放入event对象）              |
|          | <FocusIn><Focunsout>            | 键盘聚焦进入或聚焦退出                                       |
|          | <BackSpace><Tab><F1><Control-A> | 对应键盘按键                                                 |
| 组件事件 | <Configure>                     | 如果widget的大小发生改变，新的大小（width和height）会打包到event发往handler。 |
|          | <Activate>                      | 当组件从不可用变为可用                                       |
|          | <Deactivate>                    | 当组件从可用变为不可用                                       |
|          | <Destroy>                       | 当组件被销毁时                                               |
|          | <Expose>                        | 当组件从被遮挡状态变为暴露状态                               |
|          | <Map>                           | 当组件由隐藏状态变为显示状态                                 |
|          | <Unmap>                         | 当组件由显示状态变为隐藏状态                                 |
|          | <FocusIn>                       | 当组件获得焦点时                                             |
|          | <FocusOut>                      | 当组件失去焦点时                                             |
|          | <Property>                      | 当组件属性发生改变时                                         |
|          | <Visibility>                    | 当组件变为可视状态时                                         |

[To learn more.](https://www.tcl.tk/man/tcl8.6/TkCmd/keysyms.htm) 

**（2）事件对象：**

> 一个具体事件如<Button-1>是事件类（event class）的一个实例，事件类中设定了众多属性，其中部分属性是通用的，另一部分属性属于特定事件类型的，常用属性如下：
>

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

> 事件不仅可以与 Button 绑定，我们之前看过源代码，发现 bind 函数是定义在 Misc 类里面的，也就是说，这个 bind 可以被绝大多数组件类所使用。
>
> 也就是说，我们可以让“标签”来模拟“按钮”的作用。因为标签是 Label 类，而 Label 类继承自 Widget，而 Widget 继承自 BaseWidget，而 Basewidget 继承自 Misc。
>
> 其实不仅是标签可以模拟 button，任何组件都可以模拟它，只是不那么有用。

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

### Protocols

> 窗口管理程序与应用程序的通信协议，包括通过右上角关闭窗口时的协议管理，可通过借此调整关闭流程。

```python
window.protocol(protocols, callback)
```



## 8. Function


### 定时刷新

#### 1. 说明

> 由于tkinter一旦开始执行进入mainloop，就相当于进入一个界面死循环状态，出不来；如果想做定时刷新tkinter界面的控件数据，必须调用tkinter.TK()自带的after函数，这个函数可以设定定时执行某个任务的时间，使用别的python定时执行任务的模块是不行的。
>

#### 2. 使用方式

> 实现一个刷新数据函数调用tkinter.TK()自带的after函数，在调用mainloop函数之前，将这个刷新数据函数调用，则可以实现定时刷新数据功能，参考代码如下：
>

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

>  介绍轻量级第三方模块schedule，需要使用 pip install schedule导入才能使用，使用时功能相对于crontab。

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
from tkinter import colorchooser
colorchooser.askcolor(color = None, *options)
```

#### Description

> pop up the color paint to ask for a color.
>
> **Return a tuple** composed of (RGB, Ox), RGB symbolize the value of color channel of (r,g,b), Ox symbolize the value of the color in Ox, which can be called directly.



### Tag



tag_raise(firstRect)

---



## 9. Messagebox

### Synopsis

> **messagebox需额外引入**

消息框，用于显示应用程序的消息框，即平时看到的弹窗。 首先需要一个触发器来触发这个弹窗，常用button按钮的command功能，通过触发可以调出messagebox，点击button按钮就会弹出提示对话框。下面给出messagebox提示信息的几种形式：

```python
tkinter.messagebox.showinfo(title='Hi', message='你好！')            # 提示信息对话窗
tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
```

messagebox中工具函数如下：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424123825529.png)

> 除了Title和Message之外，还有其他参数**Option，包括以下值：

| 参数    | 值                             | 说明                             |
| ------- | ------------------------------ | -------------------------------- |
| default | "Yes", "No", "Cancel", "Retry" | 设置弹窗的默认按键               |
| icon    | Info, error, question, warning | 设置弹窗的显示图标，必须为预设值 |
| parent  | bool                           | 设置弹窗关闭后返回父窗口并聚焦   |



### Dialog

> tkinter.messagebox.**askquestion**(title,message,icon= None,type= None)
>
> 返回值为点击的按键的值，当单击的按钮值为“ok”（确定）时返回True，否则都为False
>
> tkinter.messagebox.**askokcancel**(title,message,icon= None,type= None)
>
> 返回值为True或False，当单击的按钮值为“ok”（确定）时返回True，否则都为False
>
> tkinter.messagebox.**askyesno**(title,message,icon= None,type= None)
>
> 返回值为True或False，当单击的按钮键值为“yes”（是）时返回True，否则都返回False
>
> tkinter.messagebox.**askyesnocancel**(title,message,icon= None,type= None)
>
> 返回值为True、False、None，当单击的按键值为“yes”（是）时返回True、当单击的按键值为“cancel”（取消）时返回None，否则都返回False
>
> tkinter.messagebox.**askretrycancel**(title,message,icon= None,type= None)
>
> 返回值为True或False，当单击的按钮值为“retry”（重试）时返回True，否则都为False

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424125014382.jpg)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424125044939.jpg)![在这里插入图片描述](https://img-blog.csdnimg.cn/2020042413385368.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQxNzkzOA==,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/2020042413393568.png)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424134034464.png)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424134131945.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424134213924.png)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424134243734.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQxNzkzOA==,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200424125058874.jpg)![在这里插入图片描述](https://img-blog.csdnimg.cn/2020042412495652.jpg)

默认情况下使用者在调用messagebox时只要设置提示区字符串即可。但如果有需要，可以通过如下两个选项来设置图标和按键

> **icon**：定制的图标区图标选项，该选项支持“error”、“info”、“question”、“warning”（默认为“info”图标）
>
>**type**：定制按钮的选项。该选项支持“abortretryignore”（中止、重试、忽略）、“ok”（确定）、“okcancel”（确定、取消）、“retrycancel”（重试、取消）、“yesno”（是、否）、“yesnocancel”（是、否、取消）（默认为“ok”按键）
> 
>**title**：messagebox消息框的标题
>
> **message**：提示区字符串

## 10. File Dialog

### Description

```python
from tkinter import filedialog
```

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

#### Description

> 提交一个对话框，向用户请求需要打开的文件对象，返回文件的绝对路径。

#### Format

```python
from tkinter import filedialog
filedialog.askopenfile(mode="r", **options)
```

#### Params



---

## 11. Simple Dialog

**Need import like `from tkinter import simpledialog`.**

### Description

> Pop up a simple dialog to get return of user, different from messagebox, simple dialog has more simple style and function.

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



## 12. Theme

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



## 13. Instance

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

