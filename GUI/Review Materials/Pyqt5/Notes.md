

```python
import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400,200)
    w.move(300,300)
    w.setWindowTitle('第一个基于PyQt5的桌面应用')
    w.show()
    
    # 进入程序的主循环、并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())

```



ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
pyqt5-tools 5.15.4.3.2 requires pyqt5==5.15.4, but you have pyqt5 5.12.3 which is incompatible.
pyqt5-plugins 5.15.4.2.2 requires pyqt5==5.15.4, but you have pyqt5 5.12.3 which is incompatible.



ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
spyder 5.1.5 requires pyqt5<5.13, but you have pyqt5 5.15.4 which is incompatible.
