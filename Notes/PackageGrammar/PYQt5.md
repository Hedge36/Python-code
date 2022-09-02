- # pyqt5-基础

- PyQt5是一套来自Digia的Qt5应用框架和Python的粘合剂。支持Python2.x和Python3.x版本。

- PyQt5以一套Python模块的形式来实现功能。它包含了超过620个类，600个方法和函数。它是一个多平台的工具套件，它可以运行在所有的主流操作系统中，包含Unix，Windows和Mac OS。PyQt5采用双重许可模式。开发者可以在GPL和社区授权之间选择。

- PyQt5的类被划分在几个模块中，下面列出了这些模块：

- - QtCore ：模块包含了非GUI的功能设计。这个模块被用来实现时间，文件和目录，不同数据类型，流，URL，mime类型，线程和进程。
  - QtGui：模块包含的类用于窗口化的系统结构，事件处理，2D绘图，基本图形，字体和文本。
  - QtWidgets：模块包含的类提供了一套UI元素来创建经典桌面风格用户界面。
  - QtMultimedia：模块包含的类用于处理多媒体内容和链接摄像头和无线电功能的API。
  - QtBluetooth：模块包含的类用于扫描蓝牙设备，并且和他们建立连接互动。
  - QtNetwork：模块包含的类用于网络编程，这些类使TCP/IP和UDP客户端/服务端编程更加容易和轻便。
  - QtPositioning：模块包含的类用于多种可获得资源的位置限定，包含卫星定位，Wi-Fi，或一个文本文件。
  - Enginio：模块用于解决客户端访问Qt云服务托管。
  - QtWebSockets：模块用于解决客户端访问Qt云服务托管。
  - QtWebKit：包含的关于浏览器的类用于解决基于WebKit2的支持库。
  - QtWebKitWidgets：模块包含的关于WebKit1的类基本解决浏览器使用基于QtWidgets应用问题。
  - QtXml：QtXml 模块包含的类用于解析XML文件。这个模块提供SAX和DOM API解决方法。
  - QtSvg：模块提供类用于显示SVG文件内容。Scalable Vector Graphics (SVG) 是一种语言，用XML来描述二维图形和图形应用程序。
  - QtSql：模块提供类驱动数据库工作。
  - QtTest：模块包含了方法提供PyQt5应用的单元测试。

- PyQt5不向后兼容PyQt4；这是一些在PyQt5中的重要改变。然而，将旧代码迁移到新的版本中并不是非常困难。不同点如下：

- Python 模块已经被改写. 一些模块被舍弃 (QtScript), 部分的模块被分割成子模块 (QtGui, QtWebKit).
  新的模块被引进, 包含 QtBluetooth, QtPositioning, 和 Enginio.
  PyQt5 只支持最新风格的信号和槽的写法. SIGNAL()和SLOT()的调用将不会被长时间支持.
  PyQt5 不支持任何在Qt 5.0版本中弃用或取消的API.
  安装

- ```
  pip install pyqt5
  1
  ```

- ## 1、示例：简单的窗口

- ```
  import sys
  from PyQt5.QtWidgets import QApplication, QWidget
   
  def show_w():
      '显示窗口'
   
      app = QApplication(sys.argv) # 所有的PyQt5应用必须创建一个应用（Application）对象。
      # sys.argv参数是一个来自命令行的参数列表。
   
      w = QWidget() # Qwidget组件是PyQt5中所有用户界面类的基础类。我们给QWidget提供了默认的构造方法。
      # 默认构造方法没有父类。没有父类的widget组件将被作为窗口使用。
   
      w.resize(500, 500) # resize()方法调整了widget组件的大小。它现在是500px宽，500px高。
      w.move(500, 100) # move()方法移动widget组件到一个位置，这个位置是屏幕上x=500,y=200的坐标。
      w.setWindowTitle('Simple') # 设置了窗口的标题。这个标题显示在标题栏中。
      w.show() # show()方法在屏幕上显示出widget。一个widget对象在这里第一次被在内存中创建，并且之后在屏幕上显示。
   
      sys.exit(app.exec_()) # 应用进入主循环。在这个地方，事件处理开始执行。主循环用于接收来自窗口触发的事件，
      # 并且转发他们到widget应用上处理。如果我们调用exit()方法或主widget组件被销毁，主循环将退出。
      # sys.exit()方法确保一个不留垃圾的退出。系统环境将会被通知应用是怎样被结束的。
   
  if __name__ == '__main__':
   
      show_w()
  123456789101112131415161718192021222324
  ```

- ## 2、示例：应用图标、按钮、窗口关闭

- 引入相关模块

- ```
  import sys
  from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
      QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
      QLineEdit)
  from PyQt5.QtGui import QFont,QIcon
  from PyQt5.QtCore import QCoreApplication
   
  1234567
  ```

- 应用图标是一个常常显示在标题栏左上方角落的小图片。

- ```
  # ##***应用图标***## #
  class AppIcon(QWidget):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          self.setGeometry(300, 300, 300, 220) # 窗口在屏幕上显示，并设置了它的尺寸。resize()和remove()合而为一的方法。
          # 前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。
          self.setWindowTitle('Icon') # 创建一个窗口标题
          self.setWindowIcon(QIcon('t1.jpg')) # 创建一个QIcon对象并接收一个我们要显示的图片路径作为参数。
          self.show()
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = AppIcon()
      sys.exit(app.exec_())
   
  1234567891011121314151617181920
  ```

- 提示文本

- ```
  # ##***提示文本***## #
  class PromptText(QWidget):
   
      def __init__(self):
          super().__init__()
          self.initUI()
   
      def initUI(self):
          QToolTip.setFont(QFont('SansSerif', 10))  # 这个静态方法设置了用于提示框的字体。
          # 这里使用10px大小的SansSerif字体。
          self.setToolTip('This is a <b>QWidget</b> widget')  # 调用setTooltip()方法创建提示框。
          # 可以在提示框中使用富文本格式。
          btn = QPushButton('Button', self)  # 创建按钮
          btn.setToolTip('This is a <b>QPushButton</b> widget')  # 设置按钮提示框
          btn.resize(btn.sizeHint())  # 改变按钮大小
          btn.move(300, 100)  # 移动按钮位置
          self.setGeometry(300, 100, 600, 600)
          self.setWindowTitle('Tooltips')
          self.show()
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = PromptText()
      sys.exit(app.exec_())
   
  1234567891011121314151617181920212223242526
  ```

- 按钮：

- ```
  QPushButton(string text, QWidget parent = None)
  # text参数是将显示在按钮中的内容。
  # parent参数是一个用来放置我们按钮的组件。在下文例子中将会是QWidget组件。
  # 一个应用的组件是分层结构的。在这个分层内，大多数组件都有父类。没有父类的组件是顶级窗口。
  1234
  ```

- 明显的关闭窗口的方法是点击标题栏的X标记。

- ```
  # ##***关闭窗口***## #
  class CloseW(QWidget):
  
     def __init__(self):
         super().__init__()
         self.initUI()
  
     def initUI(self):
         qbtn = QPushButton('Quit', self)  # 创建了一个按钮。按钮是一个QPushButton类的实例。
         # 构造方法的第一个参数是显示在button上的标签文本。第二个参数是父组件。
         # 父组件是Example组件，它继承了QWiget类。
         qbtn.clicked.connect(QCoreApplication.instance().quit)
         qbtn.resize(qbtn.sizeHint())
         qbtn.move(500, 50)
         self.setGeometry(300, 100, 600, 600)
         self.setWindowTitle('excise')
         self.show()
  
  if __name__ == '__main__':
     app = QApplication(sys.argv)
     ex = CloseW()
     sys.exit(app.exec_())
  12345678910111213141516171819202122
  ```

- ## 信号&槽机制

- ```
  qbtn.clicked.connect(QCoreApplication.instance().quit)
  1
  ```

- 在PyQt5中，事件处理系统由信号&槽机制建立。如果我们点击了按钮，信号clicked被发送。槽可以是Qt内置的槽或Python 的一个方法调用。QCoreApplication类包含了主事件循环；它处理和转发所有事件。instance()方法给我们返回一个实例化对象。注意QCoreAppli类由QApplication创建。点击信号连接到quit()方法，将结束应用。事件通信在两个对象之间进行：发送者和接受者。发送者是按钮，接受者是应用对象。

- Message Box

- 默认的，如果我们点击了标题栏上的x按钮，QWidget会被关闭。又是我们希望修改这个默认动作。举个例子，如果我们有个文件在编辑器内打开，并且我们对这个文件做了一些修改。 我们显示一个message box来确认这个动作。

- ```
  # ##***Message Box***## #
  class MessageBox(QWidget):
   
      def __init__(self):
          super().__init__()
          self.initUI()
   
      def initUI(self):
          qbtn = QPushButton('Quit', self)  # 创建了一个按钮。按钮是一个QPushButton类的实例。
          # 构造方法的第一个参数是显示在button上的标签文本。第二个参数是父组件。
          # 父组件是Example组件，它继承了QWiget类。
          qbtn.clicked.connect(QCoreApplication.instance().quit)
          qbtn.resize(qbtn.sizeHint())
          qbtn.move(500, 50)
          self.setGeometry(300, 100, 600, 600)
          self.setWindowTitle('excise')
          self.show()
   
      def closeEvent(self, event):
   
          reply = QMessageBox.question(self, 'Message',
                                       "Are you sure to quit?", QMessageBox.Yes |
                                       QMessageBox.No, QMessageBox.No)
          if reply == QMessageBox.Yes:
              event.accept()
          else:
              event.ignore()
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = MessageBox()
      sys.exit(app.exec_())
      ```
  如果我们关闭一个QWidget，QCloseEvent类事件将被生成。要修改组件动作我们需要重新实现closeEvent()事件处理方法。
  
  1234567891011121314151617181920212223242526272829303132333435
  ```

- reply = QMessageBox.question(self, ‘Message’, “Are you sure to quit?”, QMessageBox.Yes |[QMessageBox.No](http://qmessagebox.no/), [QMessageBox.No](http://qmessagebox.no/))

- ```
  我们实现一个带两个按钮的message box：YES和No按钮。代码中第一个字符串的内容被显示在标题栏上。第二个字符串是对话框上显示的文本。第三个参数指定了显示在对话框上的按钮集合。最后一个参数是默认选中的按钮。这个按钮一开始就获得焦点。返回值被储存在reply变量中。
  
  123
  ```

- if reply == QMessageBox.Yes:
  event.accept()
  else:
  event.ignore()
  \```
  在这里我们测试一下返回值。代码逻辑是如果我们点击Yes按钮，我们接收到的事件关闭事件，这将导致了组件的关闭和应用的结束。否则不是点击Yes按钮的话我们将忽略将关闭事件。

- 屏幕居中窗口

- ```
  # ##***屏幕居中窗口***## #
  class CenterW(QWidget):
   
      def __init__(self):
          super().__init__()
          self.initUI()
   
      def initUI(self):
          self.resize(250, 150)
          self.center()  # 将窗口居中放置的代码在自定义的center()方法中。
          self.setWindowTitle('Center')
          self.show()
   
      def center(self):
   
          qr = self.frameGeometry() # 获得主窗口的一个矩形特定几何图形。这包含了窗口的框架。
          cp = QDesktopWidget().availableGeometry().center() # 算出相对于显示器的绝对值。
          # 并且从这个绝对值中，我们获得了屏幕中心点。
          qr.moveCenter(cp) # 矩形已经设置好了它的宽和高。现在我们把矩形的中心设置到屏幕的中间去。
          # 矩形的大小并不会改变。
          self.move(qr.topLeft()) # 移动了应用窗口的左上方的点到qr矩形的左上方的点，因此居中显示在我们的屏幕上。
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = CenterW()
      sys.exit(app.exec_())
   
  12345678910111213141516171819202122232425262728
  ```

- ## 3、菜单和工具栏

- 菜单是位于菜单栏的一组命令操作。工具栏是应用窗体中由按钮和一些常规命令操作组成的组件。

- 主窗口

- QMainWindow类提供了一个应用主窗口。默认创建一个拥有状态栏、工具栏和菜单栏的经典应用窗口骨架。

- 状态栏

- 状态栏是用来显示状态信息的组件。状态栏又QMainWindow组件帮助创建完成（依赖于QMainWindow组件）。

- ```
  # ##***状态栏***## #
  class StatusBar(QMainWindow):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          self.statusBar().showMessage('Ready')
   
          self.setGeometry(300, 300, 250, 150)
          self.setWindowTitle('Statusbar')
          self.show()
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = StatusBar()
      sys.exit(app.exec_())
  12345678910111213141516171819
  ```

- 为了得到状态栏，我们调用了QtGui.QMainWindow类的statusBar()方法。第一次调用这个方法创建了一个状态栏。随后方法返回状态栏对象。然后用showMessage()方法在状态栏上显示一些信息。

- **菜单栏**

- 菜单栏是GUI应用的常规组成部分。是位于各种菜单中的一组命令操作（Mac OS 对待菜单栏有些不同。为了获得全平台一致的效果，我们可以在代码中加入一行：menubar.setNativeMenuBar(False)）。

- ```
  # ##***菜单栏***## #
  class MenuBar(QMainWindow):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          exitAction = QAction(QIcon('t2.jpg'), '&Exit', self)
          exitAction.setShortcut('Ctrl+Q')
          exitAction.setStatusTip('Exit application')
          exitAction.triggered.connect(qApp.quit)
   
          self.statusBar()
   
          menubar = self.menuBar()
          fileMenu = menubar.addMenu('&File')
          fileMenu.addAction(exitAction)
   
          self.setGeometry(300, 300, 300, 200)
          self.setWindowTitle('Menubar')
          self.show()
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = MenuBar()
      sys.exit(app.exec_())
  12345678910111213141516171819202122232425262728
  ```

- 在上面的例子中，我们创建了有一个菜单项的菜单栏。这个菜单项包含一个选中后中断应用的动作。

- ```
  exitAction = QAction(QIcon('t2.jpg'), '&Exit', self)
  exitAction.setShortcut('Ctrl+Q')
  exitAction.setStatusTip('Exit application')
  123
  ```

- QAction是一个用于菜单栏、工具栏或自定义快捷键的抽象动作行为。在上面的三行中，我们创建了一个有指定图标和文本为’Exit’的标签。另外，还为这个动作定义了一个快捷键。第三行创建一个当我们鼠标浮于菜单项之上就会显示的一个状态提示。

- 工具栏

- 菜单可以集成所有命令，这样我们可以在应用中使用这些被集成的命令。工具栏提供了一个快速访问常用命令的方式。

- ```
  # ##***工具栏***## #
  class ToolBar(QMainWindow):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          exitAction = QAction(QIcon('t3.jpg'), 'Exit', self)
          exitAction.setShortcut('Ctrl+Q')
          exitAction.triggered.connect(qApp.quit)
   
          self.toolbar = self.addToolBar('Exit')
          self.toolbar.addAction(exitAction)
   
          self.setGeometry(300, 300, 300, 200)
          self.setWindowTitle('Toolbar')
          self.show()
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = ToolBar()
      sys.exit(app.exec_())
  123456789101112131415161718192021222324
  ```

- 上述例子中，我们创建了一个简单的工具栏。工具栏有一个动作，当这个退出动作被触发时应用将会被中断。

- **组件组合**

- 在上面的例子中，我们创建了菜单栏、工具栏和状态栏。下面我们将创建一个中心组件。

- ```
  # ##***组件组合***## #
  class Combination(QMainWindow):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          textEdit = QTextEdit()
          self.setCentralWidget(textEdit)
   
          exitAction = QAction(QIcon('t2.jpg'), 'Exit', self)
          exitAction.setShortcut('Ctrl+Q')
          exitAction.setStatusTip('Exit application')
          exitAction.triggered.connect(self.close)
   
          self.statusBar()
   
          menubar = self.menuBar()
          fileMenu = menubar.addMenu('&File')
          fileMenu.addAction(exitAction)
   
          toolbar = self.addToolBar('Exit')
          toolbar.addAction(exitAction)
   
          self.setGeometry(300, 300, 350, 250)
          self.setWindowTitle('Main window')
          self.show()
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = Combination()
      sys.exit(app.exec_())
  123456789101112131415161718192021222324252627282930313233
  ```

- 示例代码创建了一个带有菜单栏、工具栏和状态栏的经典GUI应用骨架。

- ```
  textEdit = QTextEdit()
  self.setCentralWidget(textEdit)
  12
  ```

- 在这里我们创建了一个文本编辑框组件。我们将它设置成QMainWindow的中心组件。中心组件占据了所有剩下的空间。

- ## 4、布局管理

- 布局管理是GUI编程中的一个重要方面。布局管理是一种如何在应用窗口上防止组件的一种方法。我们可以通过两种基础方式来管理布局。我们可以使用绝对定位和布局类。

- 4.1 绝对定位

- 程序指定了组件的位置并且每个组件的大小用像素作为单位来丈量。当你使用了绝对定位，我们需要知道下面的几点限制：

- 如果我们改变了窗口大小，组件的位置和大小并不会发生改变。
  在不同平台上，应用的外观可能不同
  改变我们应用中的字体的话可能会把应用弄得一团糟。
  如果我们决定改变我们的布局，我们必须完全重写我们的布局，这样非常乏味和浪费时间。

- ```
  # ##***绝对定位***## #
  class AbsPosition(QWidget):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          lbl1 = QLabel('Zetcode', self)
          lbl1.move(15, 10)
   
          lbl2 = QLabel('tutorials', self)
          lbl2.move(35, 40)
   
          lbl3 = QLabel('for programmers', self)
          lbl3.move(55, 70)
   
          self.setGeometry(300, 300, 250, 150)
          self.setWindowTitle('Absolute')
          self.show()
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = AbsPosition()
      sys.exit(app.exec_())
  12345678910111213141516171819202122232425
  ```

- 我们使用move()方法来定位我们的组件。在上面的例子中我们使用move()方法定位了一些标签组件。在使用move()方法时，我们给move()方法提供了x和y坐标作为参数。move()使用的坐标系统是从左上角开始计算的。x值从左到右增长。y值从上到下增长。

- 4.2 箱布局
  布局管理器的布局管理类非常灵活，实用。它是将组件定位在窗口上的首选方式。QHBoxLayout和QVBoxLayout是两个基础布局管理类，他们水平或垂直的线性排列组件。想象一下我们需要在右下角排列两个按钮。为了使用箱布局，我们将使用一个水平箱布局和垂直箱布局来实现。同样为了使用一些必要的空白，我们将添加一些拉伸因子。

- ```
  # ##***箱布局***## #
  class BoxLayout(QWidget):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          okButton = QPushButton("OK")
          cancelButton = QPushButton("Cancel")
   
          # 创建了一个水平箱布局，并且增加了一个拉伸因子和两个按钮。拉伸因子在两个按钮之前增加了一个可伸缩空间。
          # 这会将按钮推到窗口的右边。
          hbox = QHBoxLayout()
          hbox.addStretch(1)
          hbox.addWidget(okButton)
          hbox.addWidget(cancelButton)
   
          # 为了创建必要的布局，把水平布局放置在垂直布局内。拉伸因子将把包含两个按钮的水平箱布局推到窗口的底边。
          vbox = QVBoxLayout()
          vbox.addStretch(1)
          vbox.addLayout(hbox)
   
          self.setLayout(vbox)
   
          self.setGeometry(300, 300, 300, 150)
          self.setWindowTitle('Buttons')
          self.show()
           
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = BoxLayout()
      sys.exit(app.exec_())
  123456789101112131415161718192021222324252627282930313233
  ```

- 例子在右下角放置了两个按钮。当我们改变应用窗口大小时，它们会相对于应用窗口不改变位置。在这个例子中我们使用了QHBoxLayout和QVBoxLayout两个布局类。

- 4.3 网格布局
  最常用的布局类是网格布局。这个布局使用行了列分割空间。要创建一个网格布局，我们需要使用QGridLayout类。

- ```
  # ##***网格布局***## #
  class GridLayout(QWidget):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
   
          grid = QGridLayout() # 实例化QGridLayout类
          self.setLayout(grid) # 把QGridLayout类设为应用窗口的布局。
   
          names = ['Cls', 'Bck', '', 'Close',
                   '7', '8', '9', '/',
                   '4', '5', '6', '*',
                   '1', '2', '3', '-',
                   '0', '.', '=', '+']
   
          positions = [(i, j) for i in range(5) for j in range(4)]
   
          for position, name in zip(positions, names):
   
              if name == '':
                  continue
              button = QPushButton(name)
              grid.addWidget(button, *position)
   
          self.move(300, 150)
          self.setWindowTitle('Calculator')
          self.show()
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = GridLayout()
      sys.exit(app.exec_())
  123456789101112131415161718192021222324252627282930313233343536
  ```

- 4.4 文本审阅窗口示例

- 在网格中，组件可以跨多列或多行。在这个例子中，我们对它进行一下说明。

- ```
  # ##***文本审阅***## #
  class TextReview(QWidget):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          title = QLabel('Title')
          author = QLabel('Author')
          review = QLabel('Review')
   
          titleEdit = QLineEdit()
          authorEdit = QLineEdit()
          reviewEdit = QTextEdit()
   
          grid = QGridLayout()
          grid.setSpacing(10) # 创建了一个网格布局并且设置了组件之间的间距。
   
          grid.addWidget(title, 1, 0)
          grid.addWidget(titleEdit, 1, 1)
   
          grid.addWidget(author, 2, 0)
          grid.addWidget(authorEdit, 2, 1)
   
          grid.addWidget(review, 3, 0)
          grid.addWidget(reviewEdit, 3, 1, 5, 1) # 如果我们向网格布局中增加一个组件，我们可以提供组件的跨行
          # 和跨列参数。在这个例子中，我们让reviewEdit组件跨了5行。
   
          self.setLayout(grid)
   
          self.setGeometry(300, 300, 350, 300)
          self.setWindowTitle('Review')
          self.show()
           
           
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = TextReview()
      sys.exit(app.exec_())
  12345678910111213141516171819202122232425262728293031323334353637383940
  ```

- 我们创建了包含三个标签，两个单行编辑框和一个文本编辑框组件的窗口。布局使用了QGridLayout布局。

- ## 5、事件和信号

- ### 5.1 事件

- 所有的GUI应用都是事件驱动的。事件主要由应用的用户操作产生的。但是事件可能由其他条件触发，比如：一个网络连接，一个窗口管理器，一个定时器，这些动作都可能触发事件的产生。当我们调用应用的exec_()方法时，应用进入了主循环。主循环用于检测事件的产生并且将事件送到用于处理的对象中去。

- 在事件模型，有三个参与者：

- 事件源
  事件对象
  事件目标

- **事件源**是状态发生改变的对象。它产生了**事件**。**事件对象**(evnet)封装了事件源中的状态变化。**事件目标**是想要被通知的对象。事件源对象代表了处理一个事件直到事件目标做出响应的任务。

- PyQt5有一个独一无二的信号和槽机制来处理事件。**信号和槽用于对象之间的通信**。当指定事件发生，一个事件信号会被发射。槽可以被任何Python脚本调用。当和槽连接的信号被发射时，槽会被调用。

- ### 5.2 信号&槽

- 在我们的例子中，我们显示了一个QtGui.QLCDNumber和一个QtGui.QSlider类。我们拖动滑块条的把手，lcd数字会变化。

- ```
  import sys
  from PyQt5.QtCore import Qt
  from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                               QVBoxLayout, QApplication)
   
   
  class EventsSignals(QWidget):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          lcd = QLCDNumber(self) # 显示一个LCD数字。
          sld = QSlider(Qt.Horizontal, self) # 提供了一个水平滑动条。
   
          vbox = QVBoxLayout()
          vbox.addWidget(lcd)
          vbox.addWidget(sld)
   
          self.setLayout(vbox)
          sld.valueChanged.connect(lcd.display) # 滑块条的valueChanged信号和lcd数字显示的display槽连接在一起。
          #发送者是一个发送了信号的对象。接受者是一个接受了信号的对象。槽是对信号做出反应的方法。
   
          self.setGeometry(300, 300, 250, 150)
          self.setWindowTitle('Signal & slot')
          self.show()
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = EventsSignals()
      sys.exit(app.exec_())
  123456789101112131415161718192021222324252627282930313233
  ```

- ### 5.3 重写事件处理函数

- PyQt中的事件处理通常通过重写事件处理函数来处理。

- ```
  import sys
  from PyQt5.QtCore import Qt
  from PyQt5.QtWidgets import QWidget, QApplication
   
   
  class Rewrite(QWidget):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          self.setGeometry(300, 300, 250, 150)
          self.setWindowTitle('Event handler')
          self.show()
   
      def keyPressEvent(self, e):
          if e.key() == Qt.Key_Escape:
              self.close()
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = Rewrite()
      sys.exit(app.exec_())
  12345678910111213141516171819202122232425
  ```

- 在我们的例子中，我们重写了keyPressEvent()事件处理函数。如果我们点击了Esc按钮，应用将会被终止。

- ### 5.4 事件发送者

- 有时需要方便的知道哪一个组件是信号发送者。因此，PyQt5拥有了sender()方法来解决这个问题。

- ```
  import sys
  from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
   
   
  class EventSender(QMainWindow):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          btn1 = QPushButton("Button 1", self)
          btn1.move(30, 50)
   
          btn2 = QPushButton("Button 2", self)
          btn2.move(150, 50)
   
          btn1.clicked.connect(self.buttonClicked)
          btn2.clicked.connect(self.buttonClicked)
   
          self.statusBar()
   
          self.setGeometry(300, 300, 290, 150)
          self.setWindowTitle('Event sender')
          self.show()
   
      def buttonClicked(self):
          sender = self.sender()
          self.statusBar().showMessage(sender.text() + ' was pressed')
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = EventSender()
      sys.exit(app.exec_())
  1234567891011121314151617181920212223242526272829303132333435
  ```

- 在我们的例子中，我们有两个按钮。在buttonClikced()方法中，我们调用sender()方法来判断哪一个按钮是我们按下的。两个按钮都连接到了同一个槽中。

- 我们调用sender()方法判断发送信号的信号源是哪一个。然后在应用的状态栏上显示被按下的按钮的标签内容。

- ### 5.5 发送信号

- 从QObejct生成的对象可以发送信号。在下面的例子中我们将会看到怎样去发送自定义的信号。

- ```
  import sys
  from PyQt5.QtCore import pyqtSignal, QObject
  from PyQt5.QtWidgets import QMainWindow, QApplication
   
   
  class Communicate(QObject):
      closeApp = pyqtSignal() # 信号使用了pyqtSignal()方法创建，并且成为外部类Communicate类的属性。
   
   
  class SendSignal(QMainWindow):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          self.c = Communicate()
          self.c.closeApp.connect(self.close) # 把自定义的closeApp信号连接到QMainWindow的close()槽上。
   
          self.setGeometry(300, 300, 290, 150)
          self.setWindowTitle('Emit signal')
          self.show()
   
      def mousePressEvent(self, event):
          self.c.closeApp.emit() # 当我们在窗口上点击一下鼠标，closeApp信号会被发射。应用中断。
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = SendSignal()
      sys.exit(app.exec_())
  
  1234567891011121314151617181920212223242526272829303132
  ```

- 我们创建一个新的信号叫做closeApp。当触发鼠标点击事件时信号会被发射。信号连接到了QMainWindow的close()方法。

- ## 6、对话框

- 对话框窗口或对话框是大多数主流GUI应用不可缺少的部分。对话是两个或更多人之间的会话。在计算机应用中，对话框是一个用来和应用对话的窗口。对话框可以用来输入数据，修改数据，改变应用设置等等。

- ### 6.1 输入对话框

- QInputDialog提供了一个简单便利的对话框用于从用户那儿获得只一个值。输入值可以是字符串，数字，或者一个列表中的列表项。

- ```
  import sys
  from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                               QInputDialog, QApplication)
   
   
  class InputDialog(QWidget):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          self.btn = QPushButton('Dialog', self)
          self.btn.move(20, 20)
          self.btn.clicked.connect(self.showDialog)
   
          self.le = QLineEdit(self)
          self.le.move(130, 22)
   
          self.setGeometry(300, 300, 290, 150)
          self.setWindowTitle('Input dialog')
          self.show()
   
      def showDialog(self):
          # 这一行会显示一个输入对话框。第一个字符串参数是对话框的标题，第二个字符串参数是对话框内的消息文本。
          # 对话框返回输入的文本内容和一个布尔值。如果我们点击了Ok按钮，布尔值就是true，反之布尔值是false
          # （也只有按下Ok按钮时，返回的文本内容才会有值）。
          text, ok = QInputDialog.getText(self, 'Input Dialog',
                                          'Enter your name:')
   
          if ok:
              self.le.setText(str(text)) # 把我们从对话框接收到的文本设置到单行编辑框组件上显示。
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = InputDialog()
      sys.exit(app.exec_())
  
  123456789101112131415161718192021222324252627282930313233343536373839
  ```

- 例子中有一个按钮和一个单行编辑框组件。按下按钮会显示输入对话框用于获得一个字符串值。在对话框中输入的值会在单行编辑框组件中显示。

- ### 6.2 颜色选择对话框

- QColorDialog类提供了一个用于选择颜色的对话框组件。

- ```
  import sys
  from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                               QColorDialog, QApplication)
  from PyQt5.QtGui import QColor
   
   
  class ColorChoose(QWidget):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          col = QColor(0, 0, 0) # 初始化QtGuiQFrame组件的背景颜色。
   
          self.btn = QPushButton('Dialog', self)
          self.btn.move(20, 20)
   
          self.btn.clicked.connect(self.showDialog)
   
          self.frm = QFrame(self)
          self.frm.setStyleSheet("QWidget { background-color: %s }"
                                 % col.name())
          self.frm.setGeometry(130, 22, 100, 100)
   
          self.setGeometry(300, 300, 250, 180)
          self.setWindowTitle('Color dialog')
          self.show()
   
      def showDialog(self):
          col = QColorDialog.getColor() # 弹出颜色选择框。
   
          if col.isValid():
              # 如果我们选中一个颜色并且点了ok按钮，会返回一个有效的颜色值。如果我们点击了Cancel按钮，
              # 不会返回选中的颜色值。我们使用样式表来定义背景颜色。
              self.frm.setStyleSheet("QWidget { background-color: %s }"
                                     % col.name())
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = ColorDialog()
      sys.exit(app.exec_())
  
  1234567891011121314151617181920212223242526272829303132333435363738394041424344
  ```

- 例子中显示了一个按钮和一个QFrame。将QFrame组件的背景设置为黑色。使用颜色选择框类，我们可以改变它的颜色。

- ### 6.3 字体选择框

- QFontDialog是一个用于选择字体的对话框组件。

- ```
  import sys
  from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                               QSizePolicy, QLabel, QFontDialog, QApplication)
   
   
  class FontChoose(QWidget):
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          vbox = QVBoxLayout()
   
          btn = QPushButton('Dialog', self)
          btn.setSizePolicy(QSizePolicy.Fixed,
                            QSizePolicy.Fixed)
   
          btn.move(20, 20)
   
          vbox.addWidget(btn)
   
          btn.clicked.connect(self.showDialog)
   
          self.lbl = QLabel('Knowledge only matters', self)
          self.lbl.move(130, 20)
   
          vbox.addWidget(self.lbl)
          self.setLayout(vbox)
   
          self.setGeometry(300, 300, 250, 180)
          self.setWindowTitle('Font dialog')
          self.show()
   
      def showDialog(self):
          font, ok = QFontDialog.getFont() # 弹出一个字体对话框。getFont()方法返回字体名字和布尔值。
          # 如果用户点击了OK，布尔值为True；否则为False。
          if ok:
              self.lbl.setFont(font) # 如果我们点击了Ok按钮，标签字体会被改变。
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = FontChoose()
      sys.exit(app.exec_())
  123456789101112131415161718192021222324252627282930313233343536373839404142434445
  ```

- 在我们的例子中，我们有一个按钮和一个表情。通过字体选择对话框，我们可以改变标签的字体。

- ### 6.4 文件对话框

- 文件对话框是用于让用户选择文件或目录的对话框。可以选择文件的打开和保存。

- ```
  import sys
  from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                               QAction, QFileDialog, QApplication)
  from PyQt5.QtGui import QIcon
   
   
  class FileDialog(QMainWindow): # 基于QMainWindow组件，因为我们中心需要设置一个文本编辑框组件。
      def __init__(self):
          super().__init__()
   
          self.initUI()
   
      def initUI(self):
          self.textEdit = QTextEdit()
          self.setCentralWidget(self.textEdit)
          self.statusBar()
   
          openFile = QAction(QIcon('open.png'), 'Open', self)
          openFile.setShortcut('Ctrl+O')
          openFile.setStatusTip('Open new File')
          openFile.triggered.connect(self.showDialog)
   
          menubar = self.menuBar()
          fileMenu = menubar.addMenu('&File')
          fileMenu.addAction(openFile)
   
          self.setGeometry(300, 300, 350, 300)
          self.setWindowTitle('File dialog')
          self.show()
   
      def showDialog(self):
          # 弹出文件选择框。第一个字符串参数是getOpenFileName()方法的标题。第二个字符串参数指定了对话框的工作目录。
          # 默认的，文件过滤器设置成All files (*)。
          fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
   
          # 选中文件后，读出文件的内容，并设置成文本编辑框组件的显示文本
          if fname[0]:
              f = open(fname[0], 'r')
   
              with f:
                  data = f.read()
                  self.textEdit.setText(data)
   
   
  if __name__ == '__main__':
      app = QApplication(sys.argv)
      ex = FileDialog()
      sys.exit(app.exec_())
  123456789101112131415161718192021222324252627282930313233343536373839404142434445464748
  ```

- 示例中显示了一个菜单栏，中间设置了一个文本编辑框组件，和一个状态栏。点击菜单项会显示QtGui.QFileDialog（文件选择框）对话框，用于选择一个文件。文件的内容会被读取并在文本编辑框组件中显示。