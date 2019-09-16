# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:58:25 2019

@author: Julia
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
import user_register_ui
import FirstWindow
import npc
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

class Registerwindow(QMainWindow, user_register_ui.Ui_MainWindow):

    def __init__(self):
        super(Registerwindow, self).__init__()
        self.setupUi(self)
        self.pushButton_submit.clicked.connect(self.validate)
        self.pushButton_login.clicked.connect(self.login)
    def submit(self):
        if self.lineEdit_name.text() != "" and self.lineEdit_email.text() != "" and self.lineEdit_email.text().count("@") == 1 and self.lineEdit_email.text().count(".") > 0 and self.lineEdit_pass.text() != "":
            data=db.child("user").get()
            for user in data.each():
                if self.lineEdit_name.text() == db.child("user").child(user.key()).child("name").get().val() or self.lineEdit_email.text() == db.child("user").child(user.key()).child("Email").get().val():
                    self.show_MSG("提示","名稱或帳號已被使用")
                    return 1
        else:
            self.show_MSG("提示","請輸入完整資訊")
            return 1
    def validate(self):
        if self.submit() == 1:
            pass
        else:
            data = {"name":self.lineEdit_name.text(),
                    "Email":self.lineEdit_email.text(),
                    "password":self.lineEdit_pass.text(),
                    "gender":self.comboBox.currentText(),
                    "age":self.spinBox_age.value(),
                    "restid":"0",
                    "friend":"no",
                    "collection":"no"}
            db.child("user").child(self.lineEdit_name.text()).set(data)
            npc.NPCwindow.userid=self.lineEdit_name.text()
            self.reset()
            self.close()
            self.c=npc.NPCwindow()
            self.c.show()
            
    def login(self):
        self.reset()
        self.close()
        self.c=FirstWindow.Signinwindow()
        self.c.show()
    def reset(self):
        self.lineEdit_name.setText("")
        self.lineEdit_email.setText("")
        self.lineEdit_pass.setText("")
    def show_MSG(self,title,message):
        QMessageBox.information(None,title,message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = Registerwindow()
    Win.show()
    sys.exit(app.exec())
