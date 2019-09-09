# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 22:27:32 2019

@author: Julia
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import recom_rest_info_ui
import main
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

class InfoWindow(QMainWindow,recom_rest_info_ui.Ui_MainWindow):
    restName=""
    def __init__(self, parent = None):
        super(InfoWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.toMain)
        
        self.label_3.setText(db.child("restaurant").child(self.restName).child("name").get().val())
        self.label_7.setText(db.child("restaurant").child(self.restName).child("address").get().val())
        self.label_8.setText(db.child("restaurant").child(self.restName).child("phone").get().val())
        self.label_9.setText(db.child("restaurant").child(self.restName).child("time").get().val())
    def toMain(self):
        self.close()
        self.c=main.Mainwindow()
        self.c.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = InfoWindow()
    Win.show()
    sys.exit(app.exec())