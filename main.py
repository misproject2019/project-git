# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:55:16 2019

@author: Julia
"""

import sys
from PyQt5.QtWidgets import QDialog, QApplication
import main_ui
import user_info
import res_main
import showTask
import revise_npc
import res_info
import recommend
import runmycollection
import runcollection
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

class Mainwindow(QDialog, main_ui.Ui_Dialog):
    userid=""
    restid=""
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self.widget.setVisible(False)
        self.pushButton_3lines.setStyleSheet('QPushButton{border-image:url(3lines.png)}')
        self.pushButton_3lines.clicked.connect(self.sidebar)
        self.pushButton_userinfo.setStyleSheet('QPushButton{border-image:url(user.png)}')
        self.pushButton_userinfo.clicked.connect(self.userinfo)
        self.pushButton_search.setStyleSheet('QPushButton{border-image:url(search.png)}')
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton.clicked.connect(self.recommend)
        
        self.pushButton_npc.clicked.connect(self.reviseNPC)
        self.pushButton_rest.clicked.connect(self.restCheck)
        self.pushButton_task.clicked.connect(self.task)
        self.pushButton_favorite.clicked.connect(self.runmycollection1)
        npc=db.child("user").child(self.userid).child("npc").get().val()
        if npc == "other.png":
            self.pushButton_npc.setStyleSheet('QPushButton{border-image:url(other.png)}')
        elif npc == "girl.png":
            self.pushButton_npc.setStyleSheet('QPushButton{border-image:url(girl.png)}')
        elif npc == "boy.png":
            self.pushButton_npc.setStyleSheet('QPushButton{border-image:url(boy.png)}')
        
    def mousePressEvent(self, event):
        if event.x() > 160:
            self.widget.setVisible(False)
    def sidebar(self):
        self.widget.setVisible(True)
    def userinfo(self):
        self.close()
        self.c=user_info.Userinfowindow()
        self.c.show()
    def search(self):
        pass
    def recommend(self):
        self.close()
        self.c=recommend.RecomWindow()
        self.c.show()
    
    def reviseNPC(self):
        self.close()
        self.c=revise_npc.ReviseNPCwindow()
        self.c.show()
    def task(self):
        self.close()
        self.c=showTask.showTaskwindow()
        self.c.show()
    def restCheck(self):
        if self.restid == "0":
            self.close()
            self.m = res_main.RegiWindow()
            self.m.show()
        else:
            self.close()
            self.i = res_info.InfoWindow()
            self.i.show()
    def runmycollection1(self):
        self.close()
        self.c=runmycollection.MyWindow()
        self.c.show()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = Mainwindow()
    Win.show()
    sys.exit(app.exec())