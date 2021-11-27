import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import Widget
import test_rc

app = QtWidgets.QApplication(sys.argv)


window = Widget.QmyWidget()

window.show()
sys.exit(app.exec())
