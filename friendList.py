# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:35:14 2019

@author: Julia
"""

import sys
from PyQt5.QtWidgets import QDialog, QApplication,QPushButton,QFrame,QLabel
import friendList_ui
import main
import addfriend
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

class friendWindow(QDialog,friendList_ui.Ui_Dialog):
    def __init__(self, parent = None):
        super(friendWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_arrow.clicked.connect(self.toMain)
        self.pushButton.clicked.connect(self.addFriend)
        self.widget.setVisible(False)
        if db.child("user").child(self.userid).child("friend").get().val() == "no":
            lb1 = QLabel(self)
            lb1.setGeometry(50, 100, 261, 50)
            lb1.setText("目前沒有好友")
            lb1.setStyleSheet('color: rgb(230, 51, 76);font: 12pt "Microsoft YaHei UI";')
        else:
            data=db.child("user").child(self.userid).child("friend").get()
            i=10
            j=50
            z=430
            for user in data.each():
                bu = QPushButton(self.scrollAreaWidgetContents)
                bu.setGeometry(40, i, 261, 50)
                bu.setText(db.child("user").child(self.userid).child("friend").child(user.key()).get().val())
                bu.setStyleSheet('color: rgb(230, 51, 76);font: 12pt "Microsoft YaHei UI";text-align:left')
                bu.setFlat(True)
                bu.clicked.connect(self.btnClickEvent)
                line = QFrame(self.scrollAreaWidgetContents)
                line.setGeometry(40, j, 261, 16)
                line.setFrameShape(QFrame.HLine)
                line.setFrameShadow(QFrame.Sunken)
                self.scrollAreaWidgetContents.setMinimumSize(200,z)
                i=i+50
                j=j+50
                z=z+50

    def addFriend(self):
        self.close()
        self.c=addfriend.MyWindow()
        self.c.show()
    def toMain(self):
        self.close()
        self.c=main.Mainwindow()
        self.c.show()
    def mousePressEvent(self, event):
        self.widget.setVisible(False)
    def btnClickEvent(self):
        self.widget.setVisible(True)
        sender = self.sender()
        self.label_email.setText(db.child("user").child(sender.text()).child("Email").get().val())
        self.label_name.setText(sender.text())
        self.label_gender.setText(db.child("user").child(sender.text()).child("gender").get().val())
        self.label_age.setText(str(db.child("user").child(sender.text()).child("age").get().val()))
        npc=db.child("user").child(sender.text()).child("npc").get().val()
        if npc == "other.png":
            self.label_8.setStyleSheet('QLabel{border-image:url(other.png)}')
        elif npc == "girl.png":
            self.label_8.setStyleSheet('QLabel{border-image:url(girl.png)}')
        elif npc == "boy.png":
            self.label_8.setStyleSheet('QLabel{border-image:url(boy.png)}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = friendWindow()
    Win.show()
    sys.exit(app.exec())