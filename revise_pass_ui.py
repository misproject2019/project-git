# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'revise_pass.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 640)
        Dialog.setStyleSheet("QDialog{\n"
"background-image: url(:/back/back.png);\n"
"}\n"
"")
        self.lineEdit_again = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_again.setGeometry(QtCore.QRect(50, 325, 271, 34))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.lineEdit_again.setFont(font)
        self.lineEdit_again.setStyleSheet("background:transparent;")
        self.lineEdit_again.setFrame(False)
        self.lineEdit_again.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_again.setObjectName("lineEdit_again")
        self.lineEdit_pass = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_pass.setGeometry(QtCore.QRect(50, 180, 271, 34))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.lineEdit_pass.setFont(font)
        self.lineEdit_pass.setStyleSheet("background:transparent;")
        self.lineEdit_pass.setFrame(False)
        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 130, 87, 50))
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(230, 51, 76);")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(200, 550, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setStyleSheet("background-color:rgb(230, 51, 76,230);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(130, 30, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_submit = QtWidgets.QPushButton(Dialog)
        self.pushButton_submit.setGeometry(QtCore.QRect(50, 550, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_submit.setFont(font)
        self.pushButton_submit.setStyleSheet("background-color:rgb(230, 51, 76,230);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 270, 104, 50))
        self.label_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(230, 51, 76);")
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(50, 210, 261, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(50, 350, 261, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "新密碼   "))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))
        self.label_6.setText(_translate("Dialog", "修改密碼"))
        self.pushButton_submit.setText(_translate("Dialog", "送出"))
        self.label_2.setText(_translate("Dialog", "再次輸入  "))

import back_rc
