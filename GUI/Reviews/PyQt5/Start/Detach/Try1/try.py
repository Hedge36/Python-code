import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        """主窗口初始化，设置窗口基本属性。"""
        super(Window, self).__init__(parent)
        self.setWindowTitle("第二次尝试")   # 窗口标题
        self.resize(400, 300)   # 窗口大小
        self.center()
        self.status = self.statusBar()  # 获取窗口下方状态栏
        self.status.showMessage("Welcome for your use!", 3000)
        # 第二个参数表示时间（毫秒），表示信息显示时长，默认为0,表示始终存在
        self.setWindowIcon(QtGui.QIcon('star.ico'))

    def SetUI(self):
        # Widget控件区
        self.closebtn = QtWidgets.QPushButton("关闭窗口")
        self.closebtn.clicked.connect(self.closewindow)
        self.closebtn.setToolTip("轻击关闭窗口")    # 提示语
        self.pic = QtWidgets.QLabel()
        self.pic.setPixmap(QtGui.QPixmap("1.png"))
        self.linklabel = QtWidgets.QLabel("<a href='#'>还没注册？点击退出吧～</a>")
        self.linklabel.setOpenExternalLinks(False)
        self.linklabel.setAlignment(QtCore.Qt.AlignRight)
        tip1 = QtWidgets.QLabel("姓名:")
        self.ques1 = QtWidgets.QLineEdit()
        self.ques1.setPlaceholderText("Name")
        tip2 = QtWidgets.QLabel("名次:")
        self.ques2 = QtWidgets.QLineEdit()
        self.ques2.setPlaceholderText("Rank")
        check1 = QtGui.QIntValidator(1, 999)
        self.ques2.setValidator(check1)
        self.ques2.setMaxLength()
        self.query = QtWidgets.QPushButton("查询")
        self.query.setMaximumWidth(250)
        self.query.clicked.connect(self.showinfo)

        # 布局设置区
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.closebtn)
        layout.addWidget(self.pic)
        layout.addStretch(10)
        self.addxline(layout, tip1, self.ques1)
        self.addxline(layout, tip2, self.ques2)
        layout.addWidget(self.query, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(self.linklabel)

        # 主窗口设置
        self.centerwidget = QtWidgets.QWidget()
        self.centerwidget.setLayout(layout)
        self.setCentralWidget(self.centerwidget)

    def addxline(self, layout, label, ques):
        """创建一个水平布局，包括一个标签和一个输入框。"""
        sublay = QtWidgets.QHBoxLayout()
        layout.addLayout(sublay)
        sublay.addStretch(20)
        sublay.addWidget(label)
        sublay.addStretch(1)
        sublay.addWidget(ques)
        sublay.addStretch(20)

    def center(self):
        """窗口居中显示"""
        screensize = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screensize.width()-size.width())/2,
                  (screensize.height()-size.height())/2)

    def closewindow(self):
        """关闭窗口"""
        qApp = QtWidgets.QApplication.instance()
        # instance方法可以获取当前在主循环的窗口对象
        qApp.quit()

    def showinfo(self):
        dialog = QtWidgets.QDialog()
        info = QtWidgets.QLabel("你也配拥有排名？？？", dialog)
        info.setGeometry(30, 30, 100, 30)
        dialog.setWindowTitle("Alter")
        dialog.setWindowModality(QtCore.Qt.ApplicationModal)    # 窗口置顶
        dialog.exec()


app = QtWidgets.QApplication(sys.argv)
window = Window()
window.SetUI()
window.show()
sys.exit(app.exec())
