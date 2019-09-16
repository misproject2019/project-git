# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regi_menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PhotoWindow(object):
    def setupUi(self, PhotoWindow):
        PhotoWindow.setObjectName("PhotoWindow")
        PhotoWindow.resize(360, 640)
        self.centralwidget = QtWidgets.QWidget(PhotoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.frame.setMinimumSize(QtCore.QSize(360, 640))
        self.frame.setStyleSheet("QFrame{\n"
"background-image: url(:/back/back.png);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 261, 391))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.confirm_Button = QtWidgets.QPushButton(self.frame)
        self.confirm_Button.setGeometry(QtCore.QRect(130, 560, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.confirm_Button.setFont(font)
        self.confirm_Button.setStyleSheet("background-color:rgb(230, 51, 76);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.confirm_Button.setObjectName("confirm_Button")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 30, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        PhotoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PhotoWindow)
        QtCore.QMetaObject.connectSlotsByName(PhotoWindow)

    def retranslateUi(self, PhotoWindow):
        _translate = QtCore.QCoreApplication.translate
        PhotoWindow.setWindowTitle(_translate("PhotoWindow", "MainWindow"))
        self.confirm_Button.setText(_translate("PhotoWindow", "確認"))
        self.label.setText(_translate("PhotoWindow", "菜單"))

import back_rc
