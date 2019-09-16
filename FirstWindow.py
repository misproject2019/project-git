# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 01:20:55 2019

@author: Julia
"""

import sys
from PyQt5.QtWidgets import QDialog,QWidget, QApplication,QMessageBox
import logo_ui
import user_register
import user_signin_ui
import main
import user_info
import revise_pass
import revise_npc
import res_info
import recommend
import friendList
import addfriend
import mycollection
import res_main
na=""
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
class Logowindow(QWidget,logo_ui.Ui_Form):
    
    def __init__(self):
        super(Logowindow, self).__init__()
        self.setupUi(self)
        self.pushButton.setStyleSheet('QPushButton{border-image:url(white.png)}')
        self.pushButton.clicked.connect(self.logo)
    def logo(self):
        self.hide()
        self.s=Signinwindow()
        self.s.show()
    
class Signinwindow(QDialog, user_signin_ui.Ui_Dialog):
    global na
    def __init__(self, parent = None):
        super(Signinwindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_signin.clicked.connect(self.signin)
        self.pushButton_register.clicked.connect(self.register)

    def signin(self):
        data=db.child("user").get()
        for user in data.each():
            if db.child("user").child(user.key()).child("Email").get().val() == self.lineEdit_email1.text() :
                if str(self.lineEdit_pass1.text()) == str(db.child("user").child(user.key()).child("password").get().val()):
                    global na
                    na=db.child("user").child(user.key()).child("name").get().val()
                    user_info.Userinfowindow.userid=na
                    user_info.Userinfowindow.currentEmail = self.lineEdit_email1.text()
                    revise_pass.ReviseInfowindow.userid=na
                    revise_npc.ReviseNPCwindow.userid=na
                    main.Mainwindow.userid=na
                    friendList.friendWindow.userid=na
                    addfriend.MyWindow.userid=na
                    mycollection.MyWindow.userid=na
                    res_main.RegiWindow.userid=na
                    main.Mainwindow.restid = db.child("user").child(user.key()).child("restid").get().val()
                    res_info.InfoWindow.restid = db.child("user").child(user.key()).child("restid").get().val()
                    recommend.RecomWindow.userid=na
                    self.reset()
                    self.close()
                    self.c=main.Mainwindow()
                    self.c.show()
                    break
                else:
                    self.show_MSG("提示","帳號或密碼錯誤")
                    self.reset()
                    break

    def register(self):
        self.close()
        self.r=user_register.Registerwindow()
        self.r.show()
    def reset(self):
        self.lineEdit_pass1.setText("")
    def show_MSG(self,title,message):
        QMessageBox.information(None,title,message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    FirstWin = Logowindow()
    FirstWin.show()
    sys.exit(app.exec())