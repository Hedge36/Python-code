import sys
from PySide6 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()


widget.show()
sys.exit(app.exec())
