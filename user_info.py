# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 23:04:46 2019

@author: Julia
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication
import user_info_ui
import main
import FirstWindow
import revise_pass
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

class Userinfowindow(QWidget,user_info_ui.Ui_Form):
    currentEmail=""
    userid=""
    def __init__(self):
        super(Userinfowindow, self).__init__()
        self.setupUi(self)
        self.pushButton_arrow.setStyleSheet('QPushButton{border-image:url(arrow.png)}')
        self.pushButton_arrow.clicked.connect(self.toMain)
        self.pushButton_logout.clicked.connect(self.logout)
        self.pushButton_revise.clicked.connect(self.revisepass)
        
        self.label_email.setText(self.currentEmail)
        self.label_name.setText(self.userid)
        self.label_gender.setText(db.child("user").child(self.userid).child("gender").get().val())
        self.label_age.setText(str(db.child("user").child(self.userid).child("age").get().val()))
    def toMain(self):
        self.close()
        self.c=main.Mainwindow()
        self.c.show()
    def logout(self):
        self.close()
        self.c=FirstWindow.Signinwindow()
        self.c.show()
    def revisepass(self):
        self.close()
        self.r=revise_pass.ReviseInfowindow()
        self.r.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = Userinfowindow()
    Win.show()
    sys.exit(app.exec())