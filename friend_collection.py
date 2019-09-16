# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:59:34 2019

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
import friend_collection_ui
import collection



class MyWindow(QMainWindow, friend_collection_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_9.clicked.connect(self.runcollection)
        self.pushButton_8.clicked.connect(self.runcollection)

        db.child("user").child("A").child("name").get().val()
        self.pushButton_2.setText(db.child("user").child("A").child("name").get().val())
		
        db.child("user").child("B").child("name").get().val()
        self.pushButton_3.setText(db.child("user").child("B").child("name").get().val())
		
        db.child("user").child("嗨").child("name").get().val()
        self.pushButton_4.setText(db.child("user").child("嗨").child("name").get().val())
    
    def runcollection(self):
        self.close()
        self.c=collection.MyWindow()
        self.c.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
