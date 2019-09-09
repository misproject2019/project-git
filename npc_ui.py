# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'npc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 640)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setStyleSheet("QDialog{\n"
"background-image: url(:/back/back.png);\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 120, 171, 50))
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("華康粗圓體")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(230, 51, 76);")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(120, 30, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.radioButton_girl = QtWidgets.QRadioButton(Dialog)
        self.radioButton_girl.setGeometry(QtCore.QRect(10, 170, 151, 131))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.radioButton_girl.setFont(font)
        self.radioButton_girl.setMouseTracking(True)
        self.radioButton_girl.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.radioButton_girl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_girl.setAutoFillBackground(False)
        self.radioButton_girl.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("girl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_girl.setIcon(icon)
        self.radioButton_girl.setIconSize(QtCore.QSize(111, 111))
        self.radioButton_girl.setCheckable(True)
        self.radioButton_girl.setChecked(False)
        self.radioButton_girl.setAutoRepeat(False)
        self.radioButton_girl.setAutoExclusive(True)
        self.radioButton_girl.setObjectName("radioButton_girl")
        self.radioButton_other = QtWidgets.QRadioButton(Dialog)
        self.radioButton_other.setGeometry(QtCore.QRect(190, 170, 151, 131))
        self.radioButton_other.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_other.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("other.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_other.setIcon(icon1)
        self.radioButton_other.setIconSize(QtCore.QSize(111, 111))
        self.radioButton_other.setObjectName("radioButton_other")
        self.pushButton_npc = QtWidgets.QPushButton(Dialog)
        self.pushButton_npc.setGeometry(QtCore.QRect(120, 530, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_npc.setFont(font)
        self.pushButton_npc.setStyleSheet("background-color:rgb(230, 51, 76);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_npc.setObjectName("pushButton_npc")
        self.radioButton_boy = QtWidgets.QRadioButton(Dialog)
        self.radioButton_boy.setGeometry(QtCore.QRect(10, 310, 151, 131))
        self.radioButton_boy.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_boy.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("boy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_boy.setIcon(icon2)
        self.radioButton_boy.setIconSize(QtCore.QSize(111, 111))
        self.radioButton_boy.setObjectName("radioButton_boy")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "選擇喜愛小精靈"))
        self.label_7.setText(_translate("Dialog", "專屬小精靈"))
        self.pushButton_npc.setText(_translate("Dialog", "送出"))

import back_rc
