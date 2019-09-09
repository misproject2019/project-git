# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:32:01 2019

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
import myNormalTask_ui
import showTask

class MyWindow(QMainWindow, myNormalTask_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_arrow.setStyleSheet('QPushButton{border-image:url(arrow.png)}')
        self.pushButton_arrow.clicked.connect(self.main)
      
        a=db.child("RTask").child("喔").child("rt_Disc").get().val()
        self.pushButton_2.setText(a)
      
        a=db.child("RTask").child("我窩").child("rt_Disc").get().val()
        self.pushButton_3.setText(a)
        
    def main(self):
        self.close()
        self.c=showTask.showTaskwindow()
        self.c.show()
      

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
