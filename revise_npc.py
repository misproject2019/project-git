# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 23:14:25 2019

@author: Julia
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import revise_npc_ui
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

class ReviseNPCwindow(QMainWindow, revise_npc_ui.Ui_MainWindow):
    userid=""
    def __init__(self):
        super(ReviseNPCwindow, self).__init__()
        self.setupUi(self)
        self.pushButton_submit.clicked.connect(self.submit)
        self.pushButton_cancel.clicked.connect(self.cancel)

    def submit(self,btn):
        if self.radioButton_girl.isChecked()==True:
            db.child("user").child(self.userid).update({"npc": "girl.png"})
            self.close()
            self.c=main.Mainwindow()
            self.c.show()
        elif self.radioButton_boy.isChecked() == True:
            db.child("user").child(self.userid).update({"npc": "boy.png"})
            self.close()
            self.c=main.Mainwindow()
            self.c.show()
        elif self.radioButton_other.isChecked() == True:
            db.child("user").child(self.userid).update({"npc": "other.png"})
            self.close()
            self.c=main.Mainwindow()
            self.c.show()
    def cancel(self):
        self.close()
        self.c=main.Mainwindow()
        self.c.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = ReviseNPCwindow()
    Win.show()
    sys.exit(app.exec())