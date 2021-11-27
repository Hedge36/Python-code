import sys

from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtCore import pyqtSlot

import Ui_UI as ui


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = ui.Ui_test()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面

# =================自定义功能函数=================================

# ==========由connectSlotsByName() 自动连接的槽函数===============
    @pyqtSlot(str)
    def on_btnLoginconfirm_clicked_str(self):
        print("Yes")
        account = self.ui.accountin.text()
        password = self.ui.passwordin.text()
        if account == password:
            self.ui.editTotal.setText("")


# =============自定义槽函数===============================


# ============窗体测试程序 ================================
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyWidget()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
