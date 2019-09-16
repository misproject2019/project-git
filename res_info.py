# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg_info.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QUrl
import regi_info
import res_fixed
import RCTWindow
import pyrebase
import main
import FirstWindow
import RCTWindow

config ={
    "apiKey": "AIzaSyAMpfbvKqf5vK-dzz5H2Osu6CJ5d1ionA0",
    "authDomain": "misproject-65629.firebaseapp.com",
    "databaseURL": "https://misproject-65629.firebaseio.com",
    "projectId": "misproject-65629",
    "storageBucket": "misproject-65629.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

class InfoWindow(QMainWindow,regi_info.Ui_InfoWindow):
    restid = ""
    restna=""
    def __init__(self, parent = None):
        super(InfoWindow, self).__init__(parent)
        self.setupUi(self)
        self.fixed_Button.clicked.connect(self.fixedInfo)
        self.mission_Button.clicked.connect(self.createTask)
        self.label.setText(db.child("restaurant").child(self.restid).child("name").get().val())
        self.add_label.setText(db.child("restaurant").child(self.restid).child("address").get().val())
        time = db.child("restaurant").child(self.restid).child("time").get().val()
        opening_time = "\n".join(time)
        self.time_label.setText(opening_time)
        self.pn_label.setText(db.child("restaurant").child(self.restid).child("phone").get().val())
        self.score_label.setText(str(db.child("restaurant").child(self.restid).child("rating").get().val()))
        self.pushButton_arrow.setStyleSheet('QPushButton{border-image:url(arrow.png)}')
        self.webEngineView.setUrl(QUrl(db.child("restaurant").child(self.restid).child("photos").get().val()))
        RCTWindow.RCTWindow.restna=db.child("restaurant").child(self.restid).child("name").get().val()
        self.pushButton_arrow.setStyleSheet('QPushButton{border-image:url(arrow.png)}')
        self.pushButton_arrow.clicked.connect(self.main)
    
    def main(self):
        self.close()
        self.c=main.Mainwindow()
        self.c.show()
    def fixedInfo(self):
        self.close()
        self.f=res_fixed.FixedWindow()
        self.f.show()
    def createTask(self):
        self.close()
        self.f=RCTWindow.RCTWindow()
        self.f.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InfoWindow()
    window.show()
    sys.exit(app.exec_())