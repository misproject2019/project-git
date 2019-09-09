# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:26:39 2019

@author: Julia
"""

import pyrebase 
config ={
    "apiKey": "AIzaSyAMpfbvKqf5vK-dzz5H2Osu6CJ5d1ionA0",
    "authDomain": "misproject-65629.firebaseapp.com",
    "databaseURL": "https://misproject-65629.firebaseio.com",
    "projectId": "misproject-65629",
    "storageBucket": "misproject-65629.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import showTask_ui
import main
import myNormalTask
import AlldailyTask
import mydailyTask
import allNormalTask

class showTaskwindow(QMainWindow,showTask_ui.Ui_MainWindow):
    def __init__(self):
        super(showTaskwindow, self).__init__()
        self.setupUi(self)
        self.pushButton_arrow.setStyleSheet('QPushButton{border-image:url(arrow.png)}')
        self.pushButton_arrow.clicked.connect(self.main)
        self.pushButton_more.clicked.connect(self.alldaily)
        self.toolButton_7.clicked.connect(self.run2)
        self.toolButton_8.clicked.connect(self.mydaily)
        self.toolButton_9.clicked.connect(self.run4)

    def main(self):
        self.close()
        self.c=main.Mainwindow()
        self.c.show()
    def mydaily(self):
        self.close()
        self.c=mydailyTask.MyWindow()
        self.c.show()
    def run2(self):
        self.close()
        self.c=allNormalTask.MyWindow()
        self.c.show()
    def alldaily(self):
        self.close()
        self.c=AlldailyTask.alldailyWindow()
        self.c.show()
    def run4(self):
        self.close()
        self.c=myNormalTask.MyWindow()
        self.c.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = showTaskwindow()
    Win.show()
    sys.exit(app.exec())
