# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mycollection.ui'
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
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(40, 120, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("text-align:left;\n"
"color: rgb(230, 51, 76);")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 190, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("text-align:left;\n"
"color: rgb(230, 51, 76);")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_arrow = QtWidgets.QPushButton(self.frame)
        self.pushButton_arrow.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.pushButton_arrow.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_arrow.setIcon(icon)
        self.pushButton_arrow.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_arrow.setObjectName("pushButton_arrow")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(40, 170, 271, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(40, 240, 271, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "我的收藏"))
        self.pushButton_2.setText(_translate("MainWindow", "朋友揪團"))
        self.label.setText(_translate("MainWindow", "收藏清單"))

import back_rc
