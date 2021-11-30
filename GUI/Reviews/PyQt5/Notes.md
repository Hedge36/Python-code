# 0. Question

> 1. 如何更好地和类衔接，交互，尤其是界面逻辑分开设计时，通过QT设计界面后如何在逻辑版块顺利导入使用？
> 2. 信号槽到底怎么接入？那个名字的由来？

```python
# 理清楚其中的对象究竟是谁，此处涉及多类继承，有两个类实例本身，
# 一个是self组件类，一个是self.ui窗口类
self.ui = ui.Ui_test()  # 创建UI对象
self.ui.setupUi(self)  # 构造UI界面
```

> UI分为三个部分：
>
> 1. UI设计界面
> 2. 界面组件设计
> 3. 窗体运行主程序

> 每一个组件都具有setgeometry方法，通过这个方法实现组件的部署，类似于place绝对布局，但是采用布局（水平、垂直、图表等）时，这个属性就会变成disable状态，其大小状态将会由布局管理器接管，但**对齐等操作暂时还不会**。

> 关于样式表的使用，pyqt采用qss样式表，其语法与css基本一致，具体可自行查找搜索。

# 1. Introduction

## 1.1 Synopsis

> Before all, you should know what is the difference between PyQt5 and Pyside6, for which the front is supported by a small private enterprise and the later is maintained by the company of Qt software, but in fact, it’s more mature for PyQt5 than Pyside6 for it was developed earlier. If there are something wrong with your PyQt5, you can try to use Pyside6. 
>
> Following come two official website:
>
> 1. **PyQt5** : https://www.riverbankcomputing.com/static/Docs/PyQt5/index.html
> 2. **Pyside6** : https://doc.qt.io/qtforpython/modules.html
>
> Last, they are analogous with similar grammar. So here PyQt5 is introduced mainly.

## 1.2 Basic Framework

### 1. Create window

```python
import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()

    w.show()    
    sys.exit(app.exec_())
```

> You can create a window like this, where the first statement is used to create a application where you can deploy a window(`Widget class`) created in the second statement, then it’s useless. The third statement is to display the window and tha last to exeucate the application. 

### 2. Attribute



### 3. Method

| 方法          | 说明         |
| ------------- | ------------ |
| SetObjectName | 设置对象名称 |
|               |              |
|               |              |



## 2. Sign and Slot

> 信号与槽是Qt编程的基础，信号是指在特定情况下发射出去的一个通告（类似于tkinter中的事件，但信号比事件描述更准确，更接近于计算机视角），GUI程序设计的主要内容就是对界面上各组件发射的特定信号进行响应，而槽则是对信号响应的函数（即回调函数）。槽实际上是一个函数，它可以直接被调用，但与一般函数不同的是，槽函数可以与一个信号关联，当信号被发射时，槽函数即自动被执行，Qt的类中一般都有内置的槽函数，如 `close()`等。

信号与槽函数的关联通过以下的方式：

```python
sender.signalName.connect(receiver.slotName)
```

其中：

> + send 表示发射信号的对象名称；
> + signName 表示信号的名称；
> + receiver 表示对信号作出响应的接收者的名称；
> + slotName 是接收者的响应槽函数的名称；

此外，你可以通过使用 `PyQt.QtCore.pyqtSignal()`来为一个类定义一个新的信号。要自定义信号，该类必须是`QObject`的子类，其语法为：

```python
pyqtSignal(types[, name, revision=0, arguments=[]])
```

其中，参数type为信号类型，其后的参数都为可选项，基本不使用。

信号需要定义为类属性，这样定义的信号是未绑定信号。当创建类的实例后，PyQt会自动将实例与信号绑定，从而生成了绑定的信号，一个绑定的信号具有 `connect`等方法。

可以通过`self.sender()`来获取发射信号的对象。



## 3. QWidget

> 窗口类型有三类，包括QWidget, QDialog, QMainWindow。QWidget是常用的基本窗口类型，常作为顶层窗口或者嵌入其他窗口中，QMainWindow则是主窗口，包括状态栏、工具栏、菜单栏、标题栏等，是最常用的窗口类型，QDialog是对话框窗口的基类，主要用来执行短期任务或者进行简单的互动。它没有状态栏窗口栏等。
>
> QMainWindow不能使用窗体布局，它有自己的布局，但是CenteralWidget可以。

### 3.1 QMainWindow

> 主窗口基本组成如下图所示，新版开始的QMainWindow自带各种工具状态栏，无需通过create方法创建，你可以通过remove方法删除它们。

![Untitled](/home/hedge/Typora/Temp-image/Untitled-1637836594469.png)

### 3. 2 QDialog

> QDialog类包括QMessageBox、QFileDialog、QFontDialog与QInputDialog等文本窗口，对话框可通过Esc键退出。

#### 3.2.1 QMessageBox

> 通过弹出式对话框实现一些简单信息的展示与交互，复杂窗口可通过QDialog自定义。

| Method      | Description |
| ----------- | ----------- |
| information | 消息框      |
| question    | 询问框      |
| waring      | 警告框      |
| ctitical    | 严重错误框  |
| about       | 关于信息框  |
| setTitle    | 设置标题    |
| setText     | 设置文本    |
| setIcon     | 设置图标    |

其中各对话框参数如下：

| Parameters    | Description        |
| ------------- | ------------------ |
| parent        | 父类               |
| title         | 标题               |
| text          | 文本               |
| buttons       | 标准按钮（固定值） |
| defaultButton | 默认选中按钮       |

标准按钮值：

| Type            | Description |
| --------------- | ----------- |
| QMessage.Ok     | 确认        |
| QMessage.Cancel | 取消        |
| QMessage.Yes    | 确认        |
| QMessage.No     | 取消        |
| QMessage.Abort  | 放弃        |
| QMessage.Retry  | 重试        |
| QMessage.Ignore | 忽略        |



#### 3.2.2 QInputDialog

> QInputDialog标准输入框，由一个文本框和确认取消按钮组成，其返回值包括标准输入与确认取消选择，其参数包括父类窗口，标题以及提示文本。

| Method    | Description        |
| --------- | ------------------ |
| getInt    | 获取标准整数输入   |
| getDouble | 获取标准浮点数输入 |
| getText   | 获取标准文本输入   |
| getItem   | 获取标准列表项输入 |

#### 3.2.3 QFontDialog

> QFontDialog字体对话框，选择显示文本样式，其返回值包括两部分，分别为QFont类型与布尔类型。

#### 3.2.4 QFileDialog

> QFileDialog标准文件对话框，用于打开对应的文件，返回值包括文件路径和布尔值。

| Method          | Description        |
| --------------- | ------------------ |
| getOpenFileName | 返回所选文件并打开 |
| getSaveFileName | 以指定文件名保存   |
| setFileMode     | 指定文件类型       |
| setFilter       | 设置过滤器         |

> 文件类型包括QFileDialog.AnyFile任意文件, QFileDialog.ExistingFile已存在文件, QFileDialog.Directory文件目录, QFileDialog.ExistingFiles已经存在的多个文件.

# 2. Basic Widget

## 1. QLabel

> QLabel对象作为一个占位符可以显示不可编辑的文本或图片，也可以放置一个GIF动画，还可以被用作提示标记作为其他控件。纯文本、链接或富文本可以显示在标签上。

### 1.1 Method

| Function/Method      | Description                                    |
| -------------------- | ---------------------------------------------- |
| setAlignment         | 按照固定值设置文本对齐方式，包括Qt.AlignLeft等 |
| setIndent            | 设置文本缩进值                                 |
| setPixmap            | 设置QLabel为一个图片                           |
| text                 | 获取QLable文本内容                             |
| setText              | 设置文本内容                                   |
| selectedText         | 返回选中文本内容                               |
| setBuddy             | 设置助记符及伙伴                               |
| setWordWrap          | 设置是否允许换行                               |
| setOpenExternalLinks | 设置是否允许打开外部链接                       |

### 1.2 Signal

| Signal        | Description  |
| ------------- | ------------ |
| linkActivated | 单击链接事件 |
| linkHovered   | 鼠标驻留事件 |



## 2. QLineEdit

> QLineEdit类是一个单行文本框控件，可以输入单行字符串。如果需要输入多行字符串，则需要使用QTextEdit类。

### 2.1 Method

| Method             | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| setAlignment       | 按照固定值设置文本对齐方式，包括Qt.AlignLeft等               |
| clear              | 清楚文本框内容                                               |
| text               | 获取QLable文本内容                                           |
| setText            | 设置文本内容                                                 |
| setEchoMode        | 文本框显示模式，包括QLineEdit.Normal以及密码等或不显示       |
| setPlaceholderText | 设置文本框浮现文字                                           |
| setMaxLength       | 设置文本框所允许输入的最大字符数                             |
| setReadOnly        | 设置文本框为只读模式                                         |
| setDragEnabled     | 设置文本框是否接受拖动                                       |
| selectall          | 全选文本                                                     |
| setfocus           | 设置焦点                                                     |
| setInputMask       | 设置输入掩码，采用ANSI90码                                   |
| setValidator       | 设置文本框的验证规则以限制输入，包括QIntValidator和QDouble,QRegexp验证器 |

其中输入掩码包括：

| String | Description        |
| ------ | ------------------ |
| A      | 必选字母           |
| a      | 非必选字母         |
| N      | 必选字母及数字     |
| n      | 非必选字母及数字   |
| X      | 必选任意字符       |
| x      | 非必选任意字符     |
| 9      | 必选数字           |
| 0      | 非必选数字         |
| D      | 必选非零数字       |
| d      | 非必选非零数字     |
| #      | 非必选数字加正负号 |
| H      | 必选十六进制符     |
| h      | 非必选16进制符     |
| B      | 必选二进制符       |
| b      | 非必选二进制符     |
| >      | 所有字母大写       |
| <      | 所有字母小写       |
| !      | 关闭大小写         |
| \      | 转义符             |



### 2.2 Signal

| Signal           | Description              |
| ---------------- | ------------------------ |
| selectionChanged | 当选中文本改变时发射信号 |
| textChanged      | 当修改文本内容时发射信号 |
| editingFinished  | 当编辑文本结束时发射信号 |



## 3. QTextEdit

> QTextEdit类是一个多行文本框框架，可以显示多行文本内容，当文本而你人超过控件显示范围时，可以显示水平或垂直滚动条，此外，它不仅可以显示文本，还可以显示HTML文档。

### 3.1 Method

| Method       | Description                  |
| ------------ | ---------------------------- |
| setPlainText | 设置文本框内容               |
| toPlainText  | 返回文本框内容               |
| setHtml      | 设置多行文本框内容为HTML文档 |
| toHtml       | 返回多行文本框的Html文档内容 |
| clear        | 清除文本框内容               |

### 3.2 Signal

|      |      |
| ---- | ---- |
|      |      |
|      |      |
|      |      |



## 4. QAbstractButton

> QAbstractButton类是一个抽象按钮类，是常用的按钮类包括QPushButton、QToolButton、QRadioButton和QCheckBox的父类。

### 4.0 Class

####  Method

| Method        | Description                                |
| ------------- | ------------------------------------------ |
| isDown        | 提示按钮是否被按下                         |
| isChecked     | 提示按钮是否已经标记                       |
| isEnable      | 提示按钮是否可以被用户点击                 |
| QCheckAble    | 提示按钮是否可以被标记                     |
| setAutoRepeat | 提示按钮在被用户长按时是否可以自动重复执行 |

#### Signal

| Signal   | Description        |
| -------- | ------------------ |
| Pressed  | 鼠标左键按下       |
| Released | 鼠标左键释放       |
| Clicked  | 鼠标左键按下后释放 |
| Toggled  | 按钮的标记状态改变 |

### 4.1 QPushButton

> QPushButton除了基类属性方法外，还具有特殊的方法，其中包括快捷键的设置，通过在Text中使用"&"助记符作为快捷键识别符，如："&Download"，快捷键即为"Alt+D"，并且会在显示时在首字母下标记下划线。

| Method       | Description            |
| ------------ | ---------------------- |
| setCheckable | 设置按钮是否已经被选中 |
| toggle       | 在按钮状态中切换       |
| setIcon      | 设置按钮上的图标       |
| setEnabled   | 设置按钮是否可用       |
| isChecked    | 返回按钮状态           |
| setDefault   | 设置按钮默认状态       |
| setText      | 设置按钮显示文本       |
| text         | 返回按钮显示文本       |

### 4.2 QRadioButton

> QRadioButton提供了一组可供选择的按钮和文本标签，用户可以选中其中一个标签，用于显示对应的文本信息，为用户提供多选一的选中，默认情况下它是独占（自动关闭其他单选按钮），如果需要多个组合，需要将它们放在QGroupBox或者QButtonBox中。
>
> 当单选按钮的状态切换到off或者on时就会触发toggle信号（这个状态有可能是其他单选按钮引起的），而clicked只在按钮被点击时触发。

| Method       | Description        |
| ------------ | ------------------ |
| setCheckable | 设置按钮是否被选中 |
| isChecked    | 返回单选按钮的状态 |
| setText      | 设置显示文本内容   |
| text         | 获取显示文本内容   |

### 4.3 QCheckBox

> QCheckBox复选框，复选框可以显示文本或者标签，用于向用户提供多选多的选择，同时QCheckBox还提供了第三种半选中状态来表示没有变化。

| Method      | Description                                 |
| ----------- | ------------------------------------------- |
| setChecked  | 设置复选框状态0,1,2表示选中，半选中，未选中 |
| isChecked   | 返回单选按钮的状态                          |
| setTristate | 设置复选框为一个三态复选框                  |
| setText     | 设置显示文本内容                            |
| text        | 获取显示文本内容                            |



## 5. QComboBox

> QComboBox下拉列表框是一个集按钮和下拉选项于一体的控件，其基本方法和信号如下。

### 5.1 Method

| Method                   | Description          |
| ------------------------ | -------------------- |
| addItem                  | 添加一个下拉选项     |
| addItems                 | 从列表中添加下拉选项 |
| Clear                    | 情况下拉选项         |
| count                    | 返回下拉选项个数     |
| currentText              | 返回当前选中文本     |
| itemText(i)              | 获取索引为i的文本    |
| currentIndex             | 返回当前选中项的索引 |
| setItemText(index, text) | 改变索引i的文本      |

### 5.2 Signal

| Signal              | Description                    |
| ------------------- | ------------------------------ |
| Activated           | 选中一个下拉选项时发射信号     |
| currentIndexChanged | 下拉选项改变时发射             |
| highlighted         | 选中一个已经选中下拉选项时发射 |



## 6. QSpinBox

> QSpinBox是一个计数器控件，允许用户选择一个整数值，可以通过单击上下键或者按键输入来增加减少当前显示值，浮点数值显示使用QDoubleSpinBox。

### 6.1 Method

| Method     | Description                  |
| ---------- | ---------------------------- |
| setMaximum | 设置计数器上限               |
| setMinimum | 设置计数器下限               |
| setRange   | 设置计数器最大值最小值及步长 |
| setValue   | 设置计数器当前值             |
| Value      | 返回计数器当前值             |
| singleStep | 设置计数器步长               |

### 6.2 Signal

| Signal       | Description |
| ------------ | ----------- |
| valueChanged |             |
|              |             |
|              |             |



## 7. QSlider

> QSlider滑动条提供了一个水平或者树枝方向的水平条，用于控制有界值，它允许用户沿水哦或者垂直方向在某一范围内移动滑块并将其转化为相应的整数值。

### 7.1 Method

| Method          | Description                  |
| --------------- | ---------------------------- |
| setMaximum      | 设置滑动条上限               |
| setMinimum      | 设置滑动条下限               |
| setRange        | 设置滑动条最大值最小值及步长 |
| setValue        | 设置滑动条当前值             |
| Value           | 返回滑动条当前值             |
| setSingleStep   | 设置滑动条步长               |
| setTickInterval | 设置标签刻度间隔             |
| setTickPosition | 设置刻度标签位置，固定值     |

### 7.2 Signal

| Signal         | Description |
| -------------- | ----------- |
| valueChanged   | 滑块值改变  |
| sliderPressed  | 按下滑块    |
| sliderMoved    | 拖动滑块    |
| sliderReleased | 释放滑块    |



## 8. QAbstractPainter

> PyQt5 绘图系统能渲染矢量图像、位图图像和轮廓字体文本。当我们想要更改或增强现有小部件，或者我们从头开始创建自定义小部件时，应用程序需要绘制。要进行绘图，我们使用 PyQt5 工具包提供的绘画 API。
>
> 在 PyQt5 中，一般可以通过 QPainter、QPen 和 QBrush 这三个类来实现绘图功能。此外，QPixmap 的作用是加载并呈现本地图像，而图像的呈现本质上也是通过绘图方式实现的，所以 QPixmap 也可以被视为绘图的一个类。

### 8.1 QPainter

QPainter 类在 QWidget（控件）上执行绘图操作，它是一个绘制工具，为大部分图形界面提供了高度优化的函数，使用 QPainter 类可以绘制从简单的直线到复杂的饼图等。它也可以画文本和图像。

**QPainter** 可以在任何继承自 **QPaintDevice** 的对象上进行绘制。QpaintDevice 子类有QImage、QOpenGLPaintDevice、QWidget 等。所以, QPainter 可以在QImage、QOpenGLPaintDevice、QWidget 上进行绘制图形。

Painter的核心功能是绘图，但该类还提供了几个功能，允许您自定义QPainter的设置及其渲染质量，以及其他启用剪切的功能。此外，您可以通过指定painter的合成模式来控制不同形状的合并方式。

绘制操作在 `QWidget.paintEvent()` 中完成。绘制方法必须放在 QtGui.QPainter 对象的 `begin()` 和 `end()` 之间。`isActive()` 函数指示painter 是否处于活动状态。painter 由 `begin()` 函数和带有 `QPaintDevice` 参数的构造函数激活。end()函数和析构函数将其停用。

QPainter 类在控件或其他绘图设备上执行较低级别的图形绘制功能，并通过如下所示的方法进行绘制。

| 方法                                  | 描述                                            |
| :------------------------------------ | :---------------------------------------------- |
| begin                                 | 开始在目标设备上绘制                            |
| drawPoint(x, y)                       | 在指定位置绘制一个点                            |
| drawArc                               | 在起始角度和最终角度之间画弧                    |
| drawEllipse                           | 在一个矩形内画一个椭圆                          |
| drawLine(int x1,int y1,int x2,int y2) | 绘制一条指定了端点坐标的线                      |
| drawPixmap                            | 从图像文件中提取Pixmap并将其显示在指定的位置    |
| drawPolygon                           | 使用坐标数组绘制多边形                          |
| drawRect(int x,int y,int w,int h)     | 以给定的高度和宽度从左上角坐标(x,y)绘制一个矩形 |
| drawText                              | 显示给定坐标处的文字                            |
| fillRect                              | 使用QColor参数填充矩形                          |
| setBrush                              | 设置画笔风格                                    |
| setPen                                | 设置用于绘制的笔的颜色、大小和样式              |

还可以设置画笔风格（PenStyle），这是一个枚举类，可以由 QPainter 类绘制。画笔风格如表：

| 枚举类型          | 描述                 |
| :---------------- | :------------------- |
| Qt.NoPen          | 没有线               |
| Qt.SolidLine      | 一条简单的线         |
| Qt.DashLine       | 由一些像素分隔的短线 |
| Qt.DotLine        | 由一些像素分隔的点   |
| Qt.DashDotLine    | 轮流交替的点和短线   |
| Qt.DashDotDotLine | 一条短线，两个点     |
| Qt.MPenStyle      | 画笔风格的掩码       |

Painter 与 QPaintDevice 和 QPaintEngine 类一起构成了 Qt 绘画系统的基础。QPainter 是用于执行绘图操作的类。QPaintDevice 表示可以使用 QPainter 绘制的设备。 QPaintEngine 提供 painter 用于绘制到不同类型设备上的界面。如果 painter 处于活动状态，则 device() 返回 painter 绘制的绘图设备，paintEngine() 返回 painter 当前正在操作的绘制引擎。

有时需要让别人在不寻常的 QPaintDevice 上绘画。 QPainter 支持静态函数来执行此操作，setRedirected()。

警告：当 paintdevice 是一个小部件时，QPainter 只能在 paintEvent() 函数内或 paintEvent() 调用的函数中使用。

您可以根据自己的喜好自定义几种设置以进行 QPainter 绘制：

> - `font()` 是用于绘制文本的字体。如果 painter `isActive()`，您可以分别使用 `fontInfo()` 和 `fontMetrics()` 函数检索有关当前设置字体及其度量的信息。
> - `brush()` 定义用于填充形状的颜色或图案。
> - `pen()` 定义用于绘制线条或边界的颜色或点画。
> - `backgroundMode()` 定义是否有 `background()`，即它是 `Qt.OpaqueMode` 或 `Qt.TransparentMode` 的实例。
> 	`background()` 仅在 `backgroundMode()` 为 `Qt.OpaqueMode` 且 `pen()` 为点画时适用。在这种情况下，它描述了点画中背景像素的颜色。
> - `brushOrigin()` 定义平铺画笔的原点，通常是小部件背景的原点。
> - `viewport()`，`window()`，`worldTransform()` 组成 painter 的坐标转换系统。
> - `hasClipping()`告诉 painter 是否剪切。
> - `layoutDirection()` 定义绘制文本时 painter 使用的布局方向。
> - `worldMatrixEnabled()`指示是否启用了世界转换。
> - `viewTransformEnabled()`指示是否启用了视图转换。

请注意，其中一些设置会镜像某些绘图设备中的设置，例如： `QWidget.font()` 和 `QPainter.begin()` 函数（或等效的 QPainter 构造函数）从 paint 设备复制这些属性。

您可以通过调用 `save()` 函数随时保存 QPainter 的状态，该函数将所有可用设置保存在内部堆栈中。`restore()` 函数会弹回它们，即恢复原先的状态。

QPainter 提供绘制大多数基元的函数：`drawPoint()`，`drawPoints()`，`drawLine()`，`drawRect()`，`drawRoundedRect()`，`drawEllipse()`，`drawArc()`，`drawPie()`，`drawChord()`，`drawPolyline()`，`drawPolygon()`，`drawConvexPolygon()` 和 `drawCubicBezier()`。两个便捷函数 `drawRects()` 和 `drawLines()` 使用当前的笔和画笔在给定的 QRects 或 QLines 数组中绘制给定数量的矩形或线。

QPainter 类还提供 `fillRect()` 函数，该函数使用给定的 QBrush 填充给定的 QRect，以及擦除给定矩形内的区域的 `eraseRect()` 函数。

| Method                   | Description                                  |
| :----------------------- | :------------------------------------------- |
| drawLine(line)           | Draw a QLine instance                        |
| drawLine(line)           | Draw a QLineF instance                       |
| drawLine(x1, y1, x2, y2) | Draw a line between x1, y2 and x2, y2 (int)  |
| drawLine(p1, p2)         | Draw a line between p1 and p2 (both QPoint)  |
| drawLine(p1, p2)         | Draw a line between p1 and p2 (both QPointF) |

### 8.2 QPen

> QPen（钢笔）是一个基本的图形对象，用于绘制直线、曲线或者给轮廓画出矩形、椭圆形、多边形及其他形状等。



### 8.3 QBrush

> QBrush 也是图像的一个基本元素。是用来填充一些物体的背景图用的，比如矩形，椭圆，多边形等。有三种类型：预定义、渐变和纹理。



### 8.4 颜色

> 颜色是一个物体显示的 RGB 的混合色。RBG 值的范围是 0~255。我们有很多方式去定义一个颜色，最常见的方式就是 RGB 和 16 进制表示法，也可以使用 RGBA，增加了一个透明度的选项，透明度值的范围是0~1，0 代表完全透明。



### 8.5 贝塞尔曲线

> 贝塞尔曲线是立方线。PyQt5 中的贝塞尔曲线可以使用 QPainterPath 创建。绘制器路径是由许多图形构建基块（如矩形、椭圆、线条和曲线）组成的对象。



### 8.6 图像类

在 PyQt5 中常用的图像类有 4 个，即 QPixmap、QImage、QPicture 和 QBitmap：

> - QPixmap 是专门为绘图而设计的，在绘制图片时需要使用 QPixmap。
> - QImage 提供了一个与硬件无关的图像表示函数，可以用于图片的像素级访问。
> - QPicture 是一个绘图设备类，它继承自 QPainter 类。可以使用 QPainter 的 `begin()` 函数在 QPicture 上绘图，使用 `end()` 函数结束绘图，使用 QPicture 的 `save()` 函数将 QPainter 所使用过的绘图指令保存到文件中。
> - QBitmap 是一个继承自 QPixmap 的简单类，它提供了 `1bit` 深度的二值图像的类。QBitmap 提供的单色图像，可以用来制作游标（QCursor）或者笔刷（QBrush）。

#### 8.6.1 QPixmap

QPixmap 类用于绘图设备的图像显示，它可以作为一个 QPaintDevice 对象，也可以加载到一个控件中，通常是标签或按钮，用于在标签或按钮上显示图像。

QPixmap 可以读取的图像文件类型有 BMP、GIF、JPG、JPEG、PNG、PBM、PGM、PPM、XBM、XPM等。

QPixmap 类中的常用方法：

| Method     | Description                   |
| ---------- | ----------------------------- |
| copy       | 从QRect对象复制到QPixmap对象  |
| fromImage  | 从QImage对象转换到QPixmap对象 |
| grabWidget | 从给定的窗口创建一个像素图    |
| grabWindow | 在窗口中创建数据的像素图      |
| load       | 加载图片为Pixmap对象          |
| save       | 将QPixmap对象保存为文件       |
| toImage    | 将QPixmap对象转化为QImage对象 |

#### 15.6.2 鼠标绘图

下面的代码重写了 QtWidgets.QMainWindow 的鼠标左键移动事件，令鼠标移动画出点：

```python
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

COLORS = [
    # 17 undertones https://lospec.com/palette-list/17undertones
    '#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
    '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
    '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]


class Canvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(800, 600)
        # 设置背景
        pixmap.fill(QtGui.QColor(200, 200, 20, 50))
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor('#000000')

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self, e):
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return  # Ignore the first time.

        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None


class QPaletteButton(QtWidgets.QPushButton):

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24, 24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.canvas = Canvas()

        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)
        l.addLayout(palette)

        self.setCentralWidget(w)

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

也可以像下面的方式实现：按下鼠标左键在白色画布上进行绘制，实现了简单的涂鸦板功能。

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QPoint


class Winform(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle("绘图例子")
		self.pix = QPixmap()
		self.lastPoint = QPoint()
		self.endPoint = QPoint()
		self.initUi()

	def initUi(self):
		#窗口大小设置为600*500
		self.resize(600, 500)
		# 画布大小为400*400，背景为白色
		self.pix = QPixmap(400, 400)
		self.pix.fill(Qt.white)

	def paintEvent(self, event):
		pp = QPainter(self.pix)
		# 根据鼠标指针前后两个位置绘制直线
		pp.drawLine(self.lastPoint, self.endPoint)
		# 让前一个坐标值等于后一个坐标值，
		# 这样就能实现画出连续的线
		self.lastPoint = self.endPoint
		painter = QPainter(self)
		painter.drawPixmap(0, 0, self.pix)

	def mousePressEvent(self, event):
		# 鼠标左键按下
		if event.button() == Qt.LeftButton:
			self.lastPoint = event.pos()
			self.endPoint = self.lastPoint

	def mouseMoveEvent(self, event):
		# 鼠标左键按下的同时移动鼠标
		if event.buttons() and Qt.LeftButton:
			self.endPoint = event.pos()
			#进行重新绘制
			self.update()

	def mouseReleaseEvent(self, event):
		# 鼠标左键释放
		if event.button() == Qt.LeftButton:
			self.endPoint = event.pos()
			#进行重新绘制
			self.update()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Winform()
	form.show()
	sys.exit(app.exec_())
```



### 8.7 双缓冲绘图

演示使用双缓冲技术绘制矩形，避免出现重影。其完整代码如下：

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QPoint


class Winform(QWidget):
	def __init__(self, parent=None):
		super(Winform, self).__init__(parent)
		self.setWindowTitle("双缓冲绘图例子")
		self.pix = QPixmap()
		self.lastPoint = QPoint()
		self.endPoint = QPoint()
		# 辅助画布
		self.tempPix = QPixmap()
		# 标志是否正在绘图
		self.isDrawing = False
		self.initUi()

	def initUi(self):
		#窗口大小设置为600*500
		self.resize(600, 500)
		# 画布大小为400*400，背景为白色
		self.pix = QPixmap(400, 400)
		self.pix.fill(Qt.white)

	def paintEvent(self, event):
		painter = QPainter(self)
		x = self.lastPoint.x()
		y = self.lastPoint.y()
		w = self.endPoint.x() - x
		h = self.endPoint.y() - y

		# 如果正在绘图，就在辅助画布上绘制
		if self.isDrawing:
			# 将以前pix中的内容复制到tempPix中，保证以前的内容不消失
			self.tempPix = self.pix
			pp = QPainter(self.tempPix)
			pp.drawRect(x, y, w, h)
			painter.drawPixmap(0, 0, self.tempPix)
		else:
			pp = QPainter(self.pix)
			pp.drawRect(x, y, w, h)
			painter.drawPixmap(0, 0, self.pix)

	def mousePressEvent(self, event):
		# 鼠标左键按下
		if event.button() == Qt.LeftButton:
			self.lastPoint = event.pos()
			self.endPoint = self.lastPoint
			self.isDrawing = True

	def mouseReleaseEvent(self, event):
		# 鼠标左键释放
		if event.button() == Qt.LeftButton:
			self.endPoint = event.pos()
			#进行重新绘制
			self.update()
			self.isDrawing = False


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Winform()
	form.show()
	sys.exit(app.exec_())
```

在这个例子中，按下鼠标左键时标志正在绘图，当释放鼠标左键时则取消正在绘图的标志。运行程序，绘图正常，没有重影。

在这个例子中，需要添加一个辅助画布，如果正在绘图，也就是还没有释放鼠标左键时，就在这个辅助画布上进行；只有释放鼠标左键时，才在真正的画布上绘图。

**双缓冲技术总结**：

在这个例子中，要实现使用鼠标在界面上绘制一个任意大小的矩形而不出现重影，需要两个画布，它们都是 QPixmap 实例，其中 tempPix 作为临时缓冲区，当拖动鼠标绘制矩形时，将内容先绘制到 tempPix 上，然后再将 tempPix 绘制到界面上；pix 作为缓冲区，用来保存已经完成的绘制。当释放鼠标按键完成矩形的绘制后，则将 tempPix 的内容复制到 pix 上。为了在绘制时不出现重影，而且保证以前绘制的内容不消失，那么每一次绘制都是在原来的图形上进行的，所以需要在绘制 tempPix 之前，先将 pix 的内容复制到 tempPix 上。因为这里有两个 QPixmap 对象，也可以说有两个缓冲区，所以称之为“双缓冲绘图”。



## 9. QClipboard

> QClipboard类提供了对系统剪贴板的访问，可以在程序之间进行复制和粘贴，QApplication都提供了一个静态方法clipboard来返回对剪贴板对象的音乐。此外QClipboard提供了以下方法：

| Method      | Description                |
| ----------- | -------------------------- |
| clear       | 清除剪贴板内容             |
| setImage    | 将QImage对象复制到剪贴板中 |
| setMimeData | 将Mime数据设置为剪贴板     |
| setPixmap   | 从剪切板中复制Pixmap对象   |
| setText     | 从剪贴板中复制文本         |
| text        | 从剪贴板中索引文本         |

其提供的信号有`dataChanged`，当剪贴板内容发生变化时，信号即被发射。



## 10. QCalendar

QCalendar是一个日历控件，提供了基于月份的视图，允许用户通过鼠标或者键盘来选择日期，默认为当前日期

| Methods           | Description                                                  |
| :---------------- | :----------------------------------------------------------- |
| setDateRange      | Sets the lower and upper date available for selection        |
| setFirstDayOfWeek | Determines the day of the first column in the calendarThe predefined day constants are Qt.Monday、Qt.Tuesday、Qt.Wednesday、Qt.Thursday、Qt.Friday、Qt.Saturday、Qt.Sunday |
| setMinimumDate    | Sets the lower date for selection                            |
| setMaximumDate    | Sets the upper date for selection                            |
| setSelectedDate   | Sets a QDate object as the selected date                     |
| showToday         | Shows the month of today                                     |
| selectedDate      | Retrieves the selected date                                  |
| setGridvisible    | Turns the calendar grid on or off                            |



## 11. QDateTimeEdit

> QDateTimeEdit是一个运行用户编辑日期时间的控件，可以使用键盘和上下键增加和减少日期时间值。它包括两个子类，分别是QDateEdit和QTImeEdit,分别用于处理日期和时间，主要的是不要混用，即使用QDateEdit获取编辑时间。

| Methods                | Description                                 |
| ---------------------- | ------------------------------------------- |
| setDisplayFormat       | 设置日期格式:<br />yyyy、MM、dd、HH、mm、ss |
| setMinimumDate         | 设置控件的最小日期                          |
| setMaximumDate         | 设置控件的最大日期                          |
| time                   | 返回编辑的时间                              |
| date                   | 返回编辑的日期                              |
| setCalendarPopup(Bool) | 设置日期控件是否显示                        |

常用信号如下：

| Signal          | Description  |
| --------------- | ------------ |
| dateChanged     | 日期改变     |
| timeChanged     | 时间改变     |
| dateTimeChanged | 日期时间改变 |



## 12. QMenuBar

> 在QMainWindow对象的标题栏下方，水平的QMenuBar被保留显示QMenu对象。QMenu类提供了一个可以添加到菜单栏的小控件，也用于创建上下文惨淡和弹出菜单，每一个QMenu对象都可以包含一个或者多个QAction对象或者级联的QMenu对象。

| Methods      | Description                                   |
| ------------ | --------------------------------------------- |
| menuBar      | 返回主窗口的QMenuaBar对象                     |
| addMenu      | 在菜单栏中添加一个新的QMenu对象               |
| addAction    | 向QMenu对象中添加一个操作对象，包括文本和图标 |
| setEnabled   | 将操作按钮状态设置为启用或者禁用              |
| addSeperator | 在菜单栏添加一条分隔线                        |
| clear        | 删除菜单栏内容                                |
| setShortcut  | 将快捷键绑定到操作按钮                        |
| setText      | 设置文本                                      |
| setTitle     | 设置QMenu小控件标题                           |
| text         | 返回文本                                      |
| title        | 返回小标题                                    |

其对应信号为triggered[QAction]类。



## 13. ToolBar

> QToolBar工具栏是由文本按钮、图标或其他小控件按钮组成的可移动面板，通常位于菜单栏下方。

| Methods        | Description      |
| -------------- | ---------------- |
| addAction      | 添加工具按钮     |
| addSeperator   | 添加分隔线       |
| addWidget      | 添加控件         |
| addToolBar     | 添加新的工具栏   |
| setMovabel     | 设置工具栏可移动 |
| setOrientation | 设置工具栏的方向 |

每次单击工具栏中的按钮对象时，都将发射actionTriggered信号。



## 14. QStatusBar

> QStatusBar状态栏，MainWindow的底部保留的水平条作为窗口的状态栏，用于显示永久或者临时的状态信息。

| Methods            | Description  |
| ------------------ | ------------ |
| addWidget          | 添加控件     |
| removeWidget       | 删除控件     |
| addPermanentWidget | 添加永久控件 |
| showMessage        | 显示信息     |
| clearMessage       | 清楚信息     |



## 15. QPrinter

> 打印图像是图像处理软件中的一个常用功能。打印图像实际上是在 QPaintDevice 中画图，与平常在QWidget、QPixmap 和 QImage 中画图一样，都是创建一个 QPainter 对象进行画图的，只是打印使用的是 QPrinter，它本质上也是一个 QPaintDevice（绘图设备）。

可通过如下方法实例化显示一个打印窗口：

```python
printer = QPrinter()
printDialog = QPrintDialog(printer, self)
```



# 3. Advanced Widget

## 1. QTableTree

> 表格与树解决的是如何在一个控件中有规律地呈现更多的数据。PyQt5提供了两种控件类用于解决该问题，其中一种是表格结构的控件类；另一种是树形结构的控件类。
>
> 以下的控件用于数据展示，都比较麻烦，故此处不做展开说明。

### 1.1 QTableView

> QTableView中可以使用自定义的数据类型来显示数据，通过setModel来绑定数据源。具体细节较多，懒得介绍。



### 1.2 QListView

> QListView用于展示数据。



### 1.3 QListWidget

> QListWidget类是一个基于条目的接口，用于从列表中删除或添加条目，其中每个条目都是一个QListWidgetItem对象，同时，它可以多项选择。



### 1.4 QTableWidget

> QTableWidget是Qt程序中常用的显示数据表格的空间，类似于DataGrid,是QTableView的子类，它使用标准的数据模型。



### 1.5 QTreeWidget

> 树形结构



## 2. Container

### 2.1 QTabWidget

> QTabWidget选项卡控件，提供了一个选项卡和一个页面区域，默认显示第一个选项卡的页面。

| Methods          | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| addTab           | 将一个控件添加到选项卡中                                   |
| insertTab        | 将选项卡插入到指定位置                                     |
| removeTab        | 根据索引删除指定选项卡                                     |
| setCurrentIndex  | 设置当前显示选项卡索引                                     |
| setCurrentWidget | 设置当前可见页面                                           |
| setTabBar        | 设置选项卡小控件                                           |
| setTabPostion    | 设置选项卡的位置:<br />QTabWidget.North, South, West, East |
| setTabText       | 设置选项卡显示文本                                         |

常用信号为currentChanged，当前页面切换时发射。



### 2.2 QStackedWidget

> QStackedWidget栈堆窗口控件，可以填充一些小控件，但同时只有一个控件能显示，此外，它具有自己独特的布局QStackedLayout，与QTabWidget类似，常与QListWidget连接，用于显示侧向选项卡时窗口。



### 2.3 QDockWidget

> QDockWidget是一个可以停靠在QMainWindow内的窗口控件，它可以保持在浮动状态或者在指定位置作为子窗口，类似于vs中的侧边栏。

| Methods         | Description          |
| --------------- | -------------------- |
| setWidget       | 设置控件             |
| setFloating     | 设置窗口是否可以浮动 |
| setAllowedAreas | 设置窗口允许停靠区域 |
| setFeatures     | 设置停靠窗口功能属性 |



### 2.4 QMdiArea

> Multiple Document Interface，多文档界面应用程序占用较少的内存资源，子窗口都可以发那个在主窗口容器中，这个容器控件被成为QMdiArea,它通常占据QMainWindow的中间控件，其内可以布置任何子窗口QMdiSubWindow类，进行级联排布。

| Methods              | Description    |
| -------------------- | -------------- |
| addSubWindow         | 添加一个子窗口 |
| removeSubWindow      | 删除一个子窗口 |
| setActibeSubWindow   | 激活一个子窗口 |
| cascadeSubWindows    | 级联显示子窗口 |
| tileSubWindows       | 屏幕显示子窗口 |
| closeActiveSubWindow | 关闭活动子窗口 |
| subWindowList        | 返回子窗口列表 |
| setWidget            | 设置子窗口控件 |

### 2.5 QScrollBar

> 可以看到，前面介绍的几种窗口控件共同点是新建一些窗口来装载更多的控件，而QScrollBar则时间提供了水平或者垂直的滚动条来扩大当前窗口的有效装载面积，从而装载更多的控件。



## 3. QLCDNumber

# 4. Thread

> 一般情况下，应用程序都是单线程运行，但是对于GUI程序来说，单线程满足不了需求，为了解决这个问题，QT提供了三种多线程技术，包括计时器模块，多线程模块和事件响应模块。

## 1. QTImer

> QTimer定时器，提供周期性或单词的定时器以执行指定任务，计时器会以一定的间隔不断发射timeout信号直至停止，但如今更多使用多线程技术。
>
> QTimer位于QtCore中。

| Methods | Description                          |
| ------- | ------------------------------------ |
| start   | 启动或重新启动计时器，时间间隔为毫秒 |
| Stop    | 停止计时器                           |

常用信号如下：

| Signal     | Description                    |
| ---------- | ------------------------------ |
| singleShot | 在给定时间间隔后调用一个槽函数 |
| tineout    | 计时器超时                     |



## 2. QThread

> QThread是Qt线程中最核心的底层类，由于其跨平台性，QThread要隐藏其所有与平台有关的代码。
>
> 要使用QThread开始一个线程，可以自定义一个子类，然后重载其run函数，通过start函数启动线程即可。

| Methods | Description          |
| ------- | -------------------- |
| start   | 启动线程             |
| wait    | 阻止线程直至满足条件 |
| sleep   | 休眠线程             |

常用信号:

| Methods  | Description     |
| -------- | --------------- |
| started  | 开始执行run函数 |
| finished | 完成业务逻辑    |



## 3. ProcessEvents

> 事件响应包括两个部分，一个是信号与槽，另一个是processEvents方法，它的作用就是用于进程阻塞时刷新网页。



## 4. HTML

> PyQt5使用QWebEngineView控件来展示HTMl页面，对老版本的QWebView类不再维护，QWebEngineView基于谷歌Chromium内核引擎，可以很好地支持HTML5。
>
> 其常用load和setHtml方法来加载一个本地或在线网页。

| Methods                      | Description  |
| ---------------------------- | ------------ |
| load(QUrl())                 | 加载一个网页 |
| setHtml                      | 设置HTML内容 |
| runJavaScript(str, Callable) | 调用Js       |

JS调用PyQt5暂时省略。

> **Alter！目前该库支持存在问题，暂无法使用！**



## 5. Event Response

> 信号与槽等属于对事件的高级封装，最原始的Qt事件类型有许多，常用的包括键盘事件、鼠标事件、拖放事件、滚轮事件、绘屏事件、定时事件等，通常通过重载对应的函数实现事件响应（mousePressEvent, keyPressEvent, paintEvent, QObject.event），具体的事件分发与函数重载此处省略。

# 5. Layout

> 五种布局方式：绝对布局、水平布局、垂直布局、网格布局、表单布局，此外，还有嵌套布局用于设置更加复杂的界面。

## 1. Absolute



## 2. QHBoxLayout



## 3. QVBoxLayout



## 4.GridLayout



## 5. FormLayout



## 6. QSplitter

> QSplitter是一个特殊的布局管理器，它允许动态地拖动子控件之间的边界。

| Methods        | Description             |
| -------------- | ----------------------- |
| addWidget      | 将控件添加到QSplitter中 |
| indexOf        | 返回控件索引位置        |
| insertWidget   | 插入控件                |
| setOrientation | 设置布局方向            |
| setSizes       | 设置控件初始化大小      |
| count          | 返回控件数              |



# 6. Slot and Signal

## 1. Synopsis

实现信号和槽的绑定的基本步骤：

> 1. 自定义或使用内置信号；
> 2. 通过connect方法绑定信号与槽；
> 3. 自定义或使用内置槽函数；

### 1.1 Slot

> 自定义槽函数，不同参数数量及类型的槽函数。

```python
class MyWidget(QWidget):
    def Value(self):
        pass
    def Value2(self, params):
        pass
```

### 1.2 Signal

> 通过类成员变量定义信号对象。需要注意的是自定义信号定义在类`__init__`方法之前。

```python
class MyWidget(QWidget):
    # Noparam
    signal1 = PyQt5.QtCore.pyqtSignal()
    # With a int param
    signal2 = PyQt5.QtCore.pyqtSignal(int)
    # With two different type params
    signal3 = PyQt5.QtCore.pyqtSignal([int], [str])
    # With two different type and two dimension params
    signal2 = PyQt5.QtCore.pyqtSignal([int,str], [int, int])
    
    def emitsignal():
       	signal.emit(params)
```

### 1.3 Connect

> 一般情况下，采用下面的连接方式即可满足多数需求。

```python
widget.Signal[params].connect(Slot)
```

> 对于信号参数小于槽函数需要的参数的类型，可以通过lambda传递。

### 1.4 装饰器信号与槽

> 通过`QtCore.QMetaObject.connectSlotsByName`来符合名字要求的信号与槽的自动捆绑，其中对于槽函数需要使用装饰器，其基本表达如下：

```python
@PyQt5.QtCore.pyqtSlot(params)
def on_sender_signal(self, params)
	pass
```



## 2. Mutilple Form

> 多窗口信息交互，一般是子窗口发射自定义或内置信号至主窗口，主窗口获取信息。



# 7. Graph and Animate

## 1. Style

> PyQt5的默认窗口样式是基于当前操作系统的原生窗口样式，在不同操作系统下显示的是不一样的，在常用的Linux及Mac系统中显示效果较理想，但在Windows中则不那么美观了，所以设计者需要根据自己的需求进行设计。

### 1.1 Theme Style

```python
SetStyle(QStyle)	# 对单个控件设置主题风格
QStyleFactory.keys()	# 获得当前平台支持的原有的Qstyle样式
QApplication.setStyle(QStyleFactory.create("WindowsXP"))	
# 全局设置
```

### 1.2 Form Style

> PyQt5用setWindowFlags方法来设置窗口样式，包括以下几种基本样式：
>
> + Qt.Widget，默认窗口，有最大小化及关闭按钮；
> + Qt.Window，普通窗口，有最大小化及关闭按钮；
> + Qt.Dialog，对话框窗口，有问号和关闭窗口；
> + Qt.Popup，弹出窗口，无边框；
> + Qt.ToolTip，提示窗口，无任务栏；
> + Qt.SplashScreen，闪屏，无边框无任务栏；
> + Qt.SubWindow，子窗口，无按钮有标题；

自定义顶层窗口外观标志：

| 样式                         | 说明                             |
| ---------------------------- | -------------------------------- |
| MSWindowsFixedSizeDialogHint | 窗口无法调节大小                 |
| FramelessWindowHint          | 窗口无边框                       |
| CustomizeWindowHint          | 有边框无标题栏和按钮，不能移动   |
| WindowTitleHint              | 添加标题栏和关闭按钮             |
| WindowSystemMenuHint         | 添加系统目录和一个关闭按钮       |
| WindowMaximizeButtonHint     | 激活最大化和关闭按钮，禁用最小化 |
| WindowMinimizeButtonHint     | 激活最小化和关闭按钮，禁用最大化 |
| WindowMinMaxButtonHint       | 激活最大最小化和关闭按钮         |
| WindowCloseButtonHint        | 添加一个关闭按钮                 |
| WindowContextHelpButtonHint  | 添加问号和关闭按钮               |
| WindowStaysOnTopHint         | 窗口始终位于顶层                 |
| WindowStaysOnBottomHint      | 窗口始终位于底层                 |

### 1.3 绘图

> 在PyQt5中图像类有四个，即为QPixmap, QImage, QPicture和QBitmap。
>
> + `QPixmap`，专门为绘图而设计，在绘制图片时需要使用QPixmap；
> + `QImage`，提供了一个与硬件无关的图像表示函数，可以用于图片的**像素级访问**；
> + `QPicture`，绘图设备类，继承自QPainter类。可以使用QPainter的begin方法**绘图**，并使用end方法结束绘图，使用save方法来保存图片。
> + `QBitmap`，继承自QPainter，它提供了1bit深度的**二值图像**的类。QBitmap提供的单色图像，可以用来制作游标或者笔刷。

其中。可以通过scaled方法调整图片大小。



## 2. QSS

> QSS是Qt的样式表，是用来自定义控件样式外观的一种机制。QSS大量参考了CSS的内容，但是功能少很多。其语法规则与css基本一致，遵循对象[属性]{样式}，id即objectname，不一样的是类选择器无需`.`，带有点的类选择器不包括其子类。
>
> QSS样式表的使用可以通过setStyleSheet方法来实现。

### 2.1 加载QSS

创建一个加载QSS样式表的公共类：

```python
class QSSLoader:
    def __init__(self):
        pass

    @staticmethod
    def read_qss_file(qss_file_name):
        with open(qss_file_name, 'r',  encoding='UTF-8') as file:
            return file.read()
```

在代码中加载qss样式表：

```python
app = QApplication(sys.argv)
window = MainWindow()

style_file = './style.qss'
style_sheet = QSSLoader.read_qss_file(style_file)
window.setStyleSheet(style_sheet)

window.show()
sys.exit(app.exec_())
```

### 2.2 QPalette

```python
palette = QPalette()
palette.setColor(QPalette.Background, Qt.red)
window.setPalette(palette)
```

### 2.3 QMovie

```python
movie = QMovie()
label.setMovie(movie)	# 设置gif
```

### 2.4 Bg

> 除了上述两种方式外，还有一种QPainter方法绘图，同时可以通过self.rect获取图像大小，及时进行重绘从而实现随窗口大小变化动态调整。



## 3. Mask

> Mask的作用是为调用它的控件增加一个遮罩，遮住所选区域以外的部分，是指看起来是透明的，你可以通过setMask方法来设置它，它包括一个参数QBitmap或者QRegion对象，此处调用QPixmap的mask'方法来获取自身的遮罩，是一个QBitmap对象。



# 8. Extensions

## 1. Pyinstaller



## 2. SQL Sever

> PyQt5 library contains **QtSql** module. It is an elaborate class system to communicate with many SQL based databases. Its **QSqlDatabase** provides access through a Connection object. Following is the list of currently available SQL drivers:

| Driver Type |                     Description                      |
| :---------: | :--------------------------------------------------: |
|      **QDB2**      |                   IBM DB2                    |
|      **QIBASE**      |          Borland InterBase Driver          |
|      **QMYSQL**      |                MySQL Driver                |
|      **QOCI**      |         Oracle Call Interface Driver         |
|      **QODBC**      | ODBC Driver (includes Microsoft SQL Server) |
|      **QPSQL**      |              PostgreSQL Driver              |
|      **QSQLITE**      |         SQLite version 3 or above         |
|      **QSQLITE2**      |             SQLite version 2             |

对于SQL3：

| Methods |                    Description                     |
| :----: | :----------------------------------------------------------: |
|   **setDatabaseName()**    | Sets the name of the database with which connection is sought |
|   **setHostName()**    | Sets the name of the host on which the database is installed |
|   **setUserName()**    |   Specifies the user name for connection    |
|   **setPassword()**    | Sets the connection object’s password if any |
|   **commit()**    | Commits the transactions and returns true if successful |
|   **rollback()**    |      Rolls back the database transaction       |
|   **close()**    |               Closes the connection               |

**QSqlQuery** class has the functionality to execute and manipulate SQL commands. Both DDL and DML type of SQL queries can be executed. First step is to create SQlite database using the following statements −

```python
db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('sportsdatabase.db')
```

Next, obtain Query object with **QSqlQuery()** method and call its most important method exec_(), which takes as an argument a string containing SQL statement to be executed.

```python
query = QtSql.QSqlQuery()
query.exec_("create table sportsmen(id int primary key, " "firstname varchar(20), lastname varchar(20))")
```

The following script creates a SQLite database sports.db with a table of sportsperson populated with five records.

```python
import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def createDB():
   db = QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('sportsdatabase.db')

   if not db.open():
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Critical)
      msg.setText("Error in Database Creation")
      retval = msg.exec_()
      return False
   query = QSqlQuery()

   query.exec_("create table sportsmen(
      id int primary key, ""firstname varchar(20), lastname varchar(20))")

   query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
   query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
   query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
   query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
   query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
   return True

if __name__ == '__main__':
   app = QApplication(sys.argv)
   createDB()
```

To confirm that the SQLite database is created with above records added in sportsmen table in it, use a SQLite Gui utility called **SQLiteStudio**.

![Database Handling](/home/hedge/Typora/Temp-image/database_handling.jpg)

**QSqlTableModel** class in PyQt is a high-level interface that provides editable data model for reading and writing records in a single table. This model is used to populate a **QTableView** object. It presents to the user a scrollable and editable view that can be put on any top level window.

A QSqlTableModel object is declared in the following manner −

```python
model = QtSql.QSqlTableModel()
```

Its editing strategy can be set to any of the following −

| Edit Strategy                 | Description                                                  |
| ----------------------------- | ------------------------------------------------------------ |
| QSqlTableModel.OnFieldChange  | All changes will be applied immediately                      |
| QSqlTableModel.OnRowChange    | Changes will be applied when the user selects a different row |
| QSqlTableModel.OnManualSubmit | All changes will be cached until either submitAll() or revertAll() is called |

### Example

In the following example, sportsperson table is used as a model and the strategy is set as −

```python
model.setTable('sportsmen') 
model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
   model.select()
```

QTableView class is part of Model/View framework in PyQt. The QTableView object is created as follows −

```python
view = QtGui.QTableView()
view.setModel(model)
view.setWindowTitle(title)
return view
```

This QTableView object and two QPushButton widgets are added to the top level QDialog window. Clicked() signal of add button is connected to addrow() which performs insertRow() on the model table.

```python
button.clicked.connect(addrow)
def addrow():
   print model.rowCount()
   ret = model.insertRows(model.rowCount(), 1)
   print ret
```

The Slot associated with the delete button executes a lambda function that deletes a row, which is selected by the user.

```python
btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
```

The complete code is as follows −

```python
import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def initializeModel(model):
   model.setTable('sportsmen')
   model.setEditStrategy(QSqlTableModel.OnFieldChange)
   model.select()
   model.setHeaderData(0, Qt.Horizontal, "ID")
   model.setHeaderData(1, Qt.Horizontal, "First name")
   model.setHeaderData(2, Qt.Horizontal, "Last name")

def createView(title, model):
   view = QTableView()
   view.setModel(model)
   view.setWindowTitle(title)
   return view

def addrow():
   print (model.rowCount())
   ret = model.insertRows(model.rowCount(), 1)
   print (ret)

def findrow(i):
   delrow = i.row()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   db = QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('sportsdatabase.db')
   model = QSqlTableModel()
   delrow = -1
   initializeModel(model)

   view1 = createView("Table Model (View 1)", model)
   view1.clicked.connect(findrow)

   dlg = QDialog()
   layout = QVBoxLayout()
   layout.addWidget(view1)

   button = QPushButton("Add a row")
   button.clicked.connect(addrow)
   layout.addWidget(button)

   btn1 = QPushButton("del a row")
   btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
   layout.addWidget(btn1)

   dlg.setLayout(layout)
   dlg.setWindowTitle("Database Demo")
   dlg.show()
   sys.exit(app.exec_())
```

The above code produces the following output −

![Database Handling Output](/home/hedge/Typora/Temp-image/database_handling_output.jpg)

Try adding and deleting a few records and go back to SQLiteStudio to confirm the transactions.



## 3. Pandas

> ptpandas extensions support for pandas. Alert that It must install manually.



## 4. Matplotlib





## 5. PyQtGraph

> 尽管PyQtGraph没有Matplotlib便捷，但是由于它是基于PyQt开发的，在性能上比后者有优势，该库需要单独安装。

