# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'revise_npc.ui'
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
        self.pushButton_cancel = QtWidgets.QPushButton(self.frame)
        self.pushButton_cancel.setGeometry(QtCore.QRect(200, 530, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setStyleSheet("background-color:rgb(230, 51, 76);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_submit = QtWidgets.QPushButton(self.frame)
        self.pushButton_submit.setGeometry(QtCore.QRect(42, 530, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_submit.setFont(font)
        self.pushButton_submit.setStyleSheet("background-color:rgb(230, 51, 76);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.radioButton_other = QtWidgets.QRadioButton(self.frame)
        self.radioButton_other.setGeometry(QtCore.QRect(190, 180, 151, 131))
        self.radioButton_other.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_other.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("other.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_other.setIcon(icon)
        self.radioButton_other.setIconSize(QtCore.QSize(111, 111))
        self.radioButton_other.setObjectName("radioButton_other")
        self.radioButton_boy = QtWidgets.QRadioButton(self.frame)
        self.radioButton_boy.setGeometry(QtCore.QRect(10, 320, 151, 131))
        self.radioButton_boy.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_boy.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("boy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_boy.setIcon(icon1)
        self.radioButton_boy.setIconSize(QtCore.QSize(111, 111))
        self.radioButton_boy.setObjectName("radioButton_boy")
        self.radioButton_girl = QtWidgets.QRadioButton(self.frame)
        self.radioButton_girl.setGeometry(QtCore.QRect(10, 180, 151, 131))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.radioButton_girl.setFont(font)
        self.radioButton_girl.setMouseTracking(True)
        self.radioButton_girl.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.radioButton_girl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_girl.setAutoFillBackground(False)
        self.radioButton_girl.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("girl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_girl.setIcon(icon2)
        self.radioButton_girl.setIconSize(QtCore.QSize(111, 111))
        self.radioButton_girl.setCheckable(True)
        self.radioButton_girl.setChecked(False)
        self.radioButton_girl.setAutoRepeat(False)
        self.radioButton_girl.setAutoExclusive(True)
        self.radioButton_girl.setObjectName("radioButton_girl")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(120, 30, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 130, 171, 50))
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_cancel.setText(_translate("MainWindow", "取消"))
        self.pushButton_submit.setText(_translate("MainWindow", "確認"))
        self.label_7.setText(_translate("MainWindow", "更改小精靈"))
        self.label.setText(_translate("MainWindow", "選擇喜愛小精靈"))

import back_rc
