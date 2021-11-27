# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hedge/pythonspace/Python-code/GUI/Review Materials/Pyqt5/Start/UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import test_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_test(object):
    def setupUi(self, test):
        test.setObjectName("test")
        test.resize(389, 303)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "../../../../../../../../../../.designer/backup/Github/Somethingelse/Pixiv/figure/56066120_p0_master1200.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        test.setWindowIcon(icon)
        test.setStyleSheet("background-image: url(:/image/image/56066120_p0_master1200.jpg);\n"
                           "bakground-size:contain;")
        test.setLocale(QtCore.QLocale(
            QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.gridLayout_2 = QtWidgets.QGridLayout(test)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loginconfirm = QtWidgets.QPushButton(test)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loginconfirm.setFont(font)
        self.loginconfirm.setLocale(QtCore.QLocale(
            QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.loginconfirm.setObjectName("loginconfirm")
        self.horizontalLayout_3.addWidget(self.loginconfirm)
        spacerItem = QtWidgets.QSpacerItem(
            13, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.signconfirm = QtWidgets.QPushButton(test)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.signconfirm.setFont(font)
        self.signconfirm.setObjectName("signconfirm")
        self.horizontalLayout_3.addWidget(self.signconfirm)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(test)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 13)
        self.gridLayout.setHorizontalSpacing(60)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(test)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.passwordin = QtWidgets.QLineEdit(test)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.passwordin.sizePolicy().hasHeightForWidth())
        self.passwordin.setSizePolicy(sizePolicy)
        self.passwordin.setMinimumSize(QtCore.QSize(100, 0))
        self.passwordin.setBaseSize(QtCore.QSize(130, 2))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordin.setFont(font)
        self.passwordin.setObjectName("passwordin")
        self.horizontalLayout.addWidget(self.passwordin)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label = QtWidgets.QLabel(test)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading |
                                QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.accountin = QtWidgets.QLineEdit(test)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.accountin.sizePolicy().hasHeightForWidth())
        self.accountin.setSizePolicy(sizePolicy)
        self.accountin.setMinimumSize(QtCore.QSize(100, 0))
        self.accountin.setBaseSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.accountin.setFont(font)
        self.accountin.setLocale(QtCore.QLocale(
            QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.accountin.setObjectName("accountin")
        self.horizontalLayout_2.addWidget(self.accountin)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.label_2.setBuddy(self.passwordin)
        self.label.setBuddy(self.accountin)

        self.retranslateUi(test)
        QtCore.QMetaObject.connectSlotsByName(test)

    def retranslateUi(self, test):
        _translate = QtCore.QCoreApplication.translate
        test.setWindowTitle(_translate("test", "test"))
        self.loginconfirm.setText(_translate("test", "登陆"))
        self.signconfirm.setText(_translate("test", "注册"))
        self.label_3.setToolTip(_translate(
            "test", "<html><head/><body><p><span style=\" font-family:\'mysh,Helvetica Neue,Arial,sans-serif\'; font-size:16px;\">我是谁</span></p></body></html>"))
        self.label_3.setText(_translate("test", "Login"))
        self.label_2.setText(_translate("test", "密码"))
        self.label.setText(_translate("test", "帐号"))
