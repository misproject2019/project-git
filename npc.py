# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:43:49 2019

@author: Julia
"""

import sys
from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox
import npc_ui
import FirstWindow
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

class NPCwindow(QDialog, npc_ui.Ui_Dialog):
    userid=""
    def __init__(self):
        super(NPCwindow, self).__init__()
        self.setupUi(self)
        self.pushButton_npc.clicked.connect(self.npc)

    def npc(self,btn):
        if self.radioButton_girl.isChecked()==True:
            db.child("user").child(self.userid).update({"npc": "girl.png"})
            self.close()
            self.c=FirstWindow.Signinwindow()
            self.c.show()
        elif self.radioButton_boy.isChecked() == True:
            db.child("user").child(self.userid).update({"npc": "boy.png"})
            self.close()
            self.c=FirstWindow.Signinwindow()
            self.c.show()
        elif self.radioButton_other.isChecked() == True:
            db.child("user").child(self.userid).update({"npc": "other.png"})
            self.close()
            self.c=FirstWindow.Signinwindow()
            self.c.show()
        else:
            self.show_MSG("提示","請選擇你的小精靈")
    def show_MSG(self,title,message):
        QMessageBox.information(None,title,message)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = NPCwindow()
    Win.show()
    sys.exit(app.exec())