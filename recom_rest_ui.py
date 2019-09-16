# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recom_rest.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(270, 218)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 270, 219))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(255, 250, 248);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAcceptDrops(False)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setIndent(0)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 150, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(230, 51, 76,230);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 10, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAcceptDrops(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setIndent(0)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 80, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 150, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color:rgb(230, 51, 76,230);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(210, 80, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAcceptDrops(False)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setIndent(0)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "今天就吃"))
        self.pushButton_2.setText(_translate("MainWindow", "確認店家"))
        self.label.setText(_translate("MainWindow", "<推薦>"))
        self.pushButton.setText(_translate("MainWindow", "重新推薦"))
        self.label_4.setText(_translate("MainWindow", "吧！"))

