# encoding: utf-8
import sys
from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import RCTWindow_ui
import main
from RTaskCheckInfo import*
from firebase import firebase
import pyrebase

global restid
fb = firebase.FirebaseApplication("https://misproject-65629.firebaseio.com/", None)

class RCTWindow(QWidget, RCTWindow_ui.Ui_Form1):
    global restid
    restna=""
    def __init__(self, parent = None):
        super(RCTWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.confirmInfo)
        self.pushButton_2.clicked.connect(self.resetInfo)
        self.pushButton_arrow.setStyleSheet('QPushButton{border-image:url(arrow.png)}')
        self.pushButton_arrow.clicked.connect(self.Restmain)
        self.RPeriod_start.setDateTime(QDateTime.currentDateTime())
        self.RPeriod_start.setMinimumDateTime(QDateTime.currentDateTime())
        self.RPeriod_end.setMinimumDateTime(QDateTime.currentDateTime().addDays(1))
        self.RPeriod_end.setMaximumDateTime(QDateTime.currentDateTime().addDays(30))
        self.label_nowUser.setText(self.restna)
        
    def Restmain(self):
        self.close()
        self.c=main.Mainwindow()
        self.c.show()
        
        
    def confirmInfo(self):
        Combotext = str(self.comboBox.currentText())
        if not (self.lineEdit.text()=="") & (self.lineEdit_2.text() ==""):
            if self.lineEdit_2.text().isdigit() & (int(self.lineEdit_2.text())>=50)& (int(self.lineEdit_2.text())<=95):
                Mtask=fb.get('/MTask',None)
                if self.lineEdit.text() not in Mtask:
                    print("Task Name: "+self.lineEdit.text()+"\n"+"Discount: "+self.lineEdit_2.text())
                    if (Combotext=="出示優惠畫面"):
                        print("Prerequisite: Show Discount DM")
                    elif (Combotext=="打卡"):
                        print("Prerequisite: HashTag")
                    RTaskCheckInfo.RTNAME=self.lineEdit.text()
                    RTaskCheckInfo.RTDISC=self.lineEdit_2.text()
                    RTaskCheckInfo.Prerequisite=str(self.comboBox.currentText())
                    RTaskCheckInfo.pre_detail=self.textEdit_taskDetail.toPlainText()
                    RTaskCheckInfo.Start=self.RPeriod_start.dateTime().toString('yyyy-MM-dd HH:mm')
                    RTaskCheckInfo.End=self.RPeriod_end.dateTime().toString('yyyy-MM-dd HH:mm')
                    self.close()
                    self.current = RTaskCheckInfo()
                    self.current.show()
                else:
                    self.show_MSG("提示","已有相同任務名稱")
            else:
                self.show_MSG("提示","優惠請輸入數字(50~95)")
        else:
            self.show_MSG("提示","請輸入任務名稱")
            self.lineEdit.setText("")

        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
    def resetInfo(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")

    def show_MSG(self,title,message):
        QMessageBox.information(None,title,message)
if __name__ == "__main__":
	app = QApplication(sys.argv)
	RestaCTWin = RCTWindow()
	RestaCTWin.show()
	sys.exit(app.exec_())