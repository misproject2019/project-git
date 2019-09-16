# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 23:21:24 2019

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
from PyQt5.QtWidgets import QApplication, QMainWindow
import collection_ui
import friend_collection
import main
import mycollection

class MyWindow(QMainWindow, collection_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.mycollection)
        self.pushButton_2.clicked.connect(self.friendcollection)
        self.pushButton_arrow.clicked.connect(self.main)
    def mycollection(self):
        self.close()
        self.c=mycollection.MyWindow()
        self.c.show()
    def friendcollection(self):
        self.close()
        self.c=friend_collection.MyWindow()
        self.c.show()
    def main(self):
        self.close()
        self.c=main.Mainwindow()
        self.c.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
