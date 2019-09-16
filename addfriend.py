# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:56:40 2019

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
import addfriend_ui
import friendList

class MyWindow(QMainWindow,addfriend_ui.Ui_MainWindow):
    userid=""
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.add)
        self.pushButton_arrow.clicked.connect(self.tolist)
    def add(self):
        db.child("user").child(self.userid).child("friend").push(self.lineEdit.text())
        self.close()
        self.c=friendList.friendWindow()
        self.c.show()
    def tolist(self):
        self.close()
        self.c=friendList.friendWindow()
        self.c.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
