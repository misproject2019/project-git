# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:46:17 2019

@author: Julia
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from accept_ui import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
