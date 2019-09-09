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
from addfriend_ui import *




class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
		
        self.pushButton_2.clicked.connect(self.main)
	
    def main(self):
        data=yes
        db.child("user").child("A").child("friend").update(data)
'''
        data = {"tag1":str(cate_input),
                "tag2":str(res_input)}
            db.child("user").child(0).update(yes)
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
