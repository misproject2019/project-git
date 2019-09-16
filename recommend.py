# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 18:43:49 2019

@author: Julia
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
import recommend_ui
import recom_rest
import main
import test
import recom_rest_info
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

from database import DataBase
df = DataBase("早餐早午餐中式.txt")
class RecomWindow(QWidget, recommend_ui.Ui_Form):
    userid = ""
    def __init__(self, parent = None):
        super(RecomWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.recommend)
        self.pushButton_2.clicked.connect(self.toMain)
        self.checkBox.toggled.connect(lambda: self.btnstate(self.checkBox))
        self.groupBox_2.setVisible(False)
        self.pushButton_3.clicked.connect(self.correct)
    def correct(self):
        
        self.widget.setVisible(False)
    def btnstate(self, btn):
        if self.checkBox.isChecked():
            self.groupBox_2.setVisible(True)
        else:
            self.groupBox_2.setVisible(False)
    def recommend(self):
        '''test.a="A"
        print(test.a)'''
        category = [self.checkBox, self.checkBox_4, self.checkBox_5, self.checkBox_7]
        restaurant = [self.checkBox_9, self.checkBox_10, self.checkBox_11, self.checkBox_12, self.checkBox_13, self.checkBox_14, self.checkBox_15, self.checkBox_16]
        for cate in category:
            if cate.isChecked():
                cate_input = cate.text()
                print(cate_input)
        if self.checkBox.isChecked():
            for res in restaurant:
                if res.isChecked():
                    res_input = res.text()
                    print(res_input)
        '''data=db.child("restaurant").get()
        for rest in data.each():
            if cate_input == db.child("restaurant").child(rest.key()).child("tag1").get().val() and res_input == db.child("restaurant").child(rest.key()).child("tag2").get().val():
                recom_rest.Resultwindow.restName=db.child("restaurant").child(rest.key()).child("name").get().val()
                recom_rest_info.InfoWindow.restName=rest.key()
                self.c=recom_rest.Resultwindow()
                self.c.show()
                df.add_user(self.userid,rest.key(),"5")'''
    def toMain(self):
        self.close()
        self.c=main.Mainwindow()
        self.c.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = RecomWindow()
    myWin.show()
    sys.exit(app.exec_())