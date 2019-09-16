# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:08:26 2019

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
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QFrame
import mycollection_ui
import collection

class MyWindow(QMainWindow, mycollection_ui.Ui_MainWindow):
    userid=""
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_9.clicked.connect(self.runcollection)
        self.pushButton_8.clicked.connect(self.runcollection)
        
        if db.child("user").child(self.userid).child("collection").get().val() == "no":
            lb1 = QLabel(self.alltask)
            lb1.setGeometry(40, 10, 261, 50)
            lb1.setText("目前沒有收藏")
            lb1.setStyleSheet('color: rgb(230, 51, 76);font: 12pt "Microsoft YaHei UI";')
        else:
            data=db.child("user").child(self.userid).child("collection").get()
            i=10
            j=14
            for user in data.each():
                bu = QLabel(self.alltask)
                bu.setGeometry(40, i, 261, 50)
                bu.setText(db.child("user").child(self.userid).child("collection").child(user.key()).get().val())
                bu.setStyleSheet('color: rgb(230, 51, 76);font: 12pt "Microsoft YaHei UI";text-align:left')
                line = QFrame(self)
                line.setGeometry(40, j, 261, 50)
                line.setFrameShape(QFrame.HLine)
                line.setFrameShadow(QFrame.Sunken)
                i=i+50
                j=j+50
    
    def runcollection(self):
        self.close()
        self.c=collection.MyWindow()
        self.c.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())