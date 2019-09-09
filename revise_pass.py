# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 23:09:54 2019

@author: Julia
"""
import sys
from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox
import revise_pass_ui
import user_info
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

class ReviseInfowindow(QDialog,revise_pass_ui.Ui_Dialog):
    userid=""
    def __init__(self):
        super(ReviseInfowindow, self).__init__()
        self.setupUi(self)
        self.pushButton_submit.clicked.connect(self.submit)
        self.pushButton_cancel.clicked.connect(self.cancel)
    def submit(self):
        if self.lineEdit_pass.text() == self.lineEdit_again.text():
            db.child("user").child(self.userid).update({"password":self.lineEdit_again.text()})
            self.show_MSG("提示","更改密碼成功")
            self.reset()
            self.close()
            self.c=main.Mainwindow()
            self.c.show()
        else:
            self.show_MSG("提示","密碼不相符")
    def cancel(self):
        self.close()
        self.u=user_info.Userinfowindow()
        self.u.show()
    def reset(self):
        self.lineEdit_pass.setText("")
        self.lineEdit_again.setText("")
    def show_MSG(self,title,message):
        QMessageBox.information(None,title,message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = ReviseInfowindow()
    Win.show()
    sys.exit(app.exec())