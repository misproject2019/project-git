# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:16:12 2019

@author: Julia
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import recom_rest_ui
import recom_rest_info

class Resultwindow(QMainWindow, recom_rest_ui.Ui_MainWindow):
    restName=""
    def __init__(self):
        super(Resultwindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.recomAgain)
        self.pushButton_2.clicked.connect(self.confirm)
        self.label_2.setText(self.restName)
    def recomAgain(self):
        self.close()
    def confirm(self):
        self.close()
        self.c=recom_rest_info.InfoWindow()
        self.c.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = Resultwindow()
    Win.show()
    sys.exit(app.exec())