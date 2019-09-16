# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addfriend.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.frame.setStyleSheet("QFrame{\n"
"background-image: url(:/back/back.png);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_arrow = QtWidgets.QPushButton(self.frame)
        self.pushButton_arrow.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.pushButton_arrow.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_arrow.setIcon(icon)
        self.pushButton_arrow.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_arrow.setObjectName("pushButton_arrow")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(130, 30, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(35, 190, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:5px;\n"
"border: 2px solid rgb(230, 51, 76);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(35, 130, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(35, 560, 291, 47))
        font = QtGui.QFont()
        font.setFamily("華康粗圓體")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color:rgb(230, 51, 76);\n"
"    border-radius:20px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "好友名字"))
        self.label_2.setText(_translate("MainWindow", "在下方輸入"))
        self.pushButton_2.setText(_translate("MainWindow", "加入好友"))

import back_rc
