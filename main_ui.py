# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
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
"}")
        self.pushButton_search = QtWidgets.QPushButton(Dialog)
        self.pushButton_search.setGeometry(QtCore.QRect(310, 0, 50, 50))
        self.pushButton_search.setText("")
        self.pushButton_search.setFlat(False)
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_userinfo = QtWidgets.QPushButton(Dialog)
        self.pushButton_userinfo.setGeometry(QtCore.QRect(260, 0, 50, 50))
        self.pushButton_userinfo.setText("")
        self.pushButton_userinfo.setObjectName("pushButton_userinfo")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 540, 61, 51))
        font = QtGui.QFont()
        font.setFamily("華康粗圓體")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(230, 51, 76);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3lines = QtWidgets.QPushButton(Dialog)
        self.pushButton_3lines.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.pushButton_3lines.setText("")
        self.pushButton_3lines.setObjectName("pushButton_3lines")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(230, 51, 76);")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 159, 640))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.widget.setFont(font)
        self.widget.setMouseTracking(False)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.pushButton_discount = QtWidgets.QPushButton(self.widget)
        self.pushButton_discount.setGeometry(QtCore.QRect(10, 140, 141, 37))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_discount.setFont(font)
        self.pushButton_discount.setStyleSheet("QPushButton{\n"
"text-align: left;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(230, 51, 76);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"border-style: inset; \n"
"}")
        self.pushButton_discount.setFlat(True)
        self.pushButton_discount.setObjectName("pushButton_discount")
        self.pushButton_friend = QtWidgets.QPushButton(self.widget)
        self.pushButton_friend.setGeometry(QtCore.QRect(10, 220, 141, 37))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_friend.setFont(font)
        self.pushButton_friend.setStyleSheet("QPushButton{\n"
"text-align: left;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(230, 51, 76);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"border-style: inset; \n"
"}")
        self.pushButton_friend.setFlat(True)
        self.pushButton_friend.setObjectName("pushButton_friend")
        self.pushButton_shop = QtWidgets.QPushButton(self.widget)
        self.pushButton_shop.setGeometry(QtCore.QRect(10, 260, 141, 37))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_shop.setFont(font)
        self.pushButton_shop.setStyleSheet("QPushButton{\n"
"text-align: left;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(230, 51, 76);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"border-style: inset; \n"
"}")
        self.pushButton_shop.setFlat(True)
        self.pushButton_shop.setObjectName("pushButton_shop")
        self.pushButton_task = QtWidgets.QPushButton(self.widget)
        self.pushButton_task.setGeometry(QtCore.QRect(10, 100, 141, 37))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_task.setFont(font)
        self.pushButton_task.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_task.setStyleSheet("QPushButton{\n"
"text-align: left;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(230, 51, 76);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"border-style: inset; \n"
"}")
        self.pushButton_task.setAutoDefault(False)
        self.pushButton_task.setDefault(False)
        self.pushButton_task.setFlat(True)
        self.pushButton_task.setObjectName("pushButton_task")
        self.pushButton_favorite = QtWidgets.QPushButton(self.widget)
        self.pushButton_favorite.setGeometry(QtCore.QRect(10, 180, 141, 37))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_favorite.setFont(font)
        self.pushButton_favorite.setStyleSheet("QPushButton{\n"
"text-align: left;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(230, 51, 76);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"border-style: inset; \n"
"}")
        self.pushButton_favorite.setFlat(True)
        self.pushButton_favorite.setObjectName("pushButton_favorite")
        self.pushButton_rest = QtWidgets.QPushButton(self.widget)
        self.pushButton_rest.setGeometry(QtCore.QRect(10, 400, 141, 37))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_rest.setFont(font)
        self.pushButton_rest.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_rest.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_rest.setAutoFillBackground(False)
        self.pushButton_rest.setStyleSheet("QPushButton{\n"
"text-align: left;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(230, 51, 76);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"border-style: inset; \n"
"}")
        self.pushButton_rest.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_rest.setAutoDefault(False)
        self.pushButton_rest.setFlat(True)
        self.pushButton_rest.setObjectName("pushButton_rest")
        self.pushButton_npc = QtWidgets.QPushButton(self.widget)
        self.pushButton_npc.setGeometry(QtCore.QRect(50, 30, 50, 50))
        self.pushButton_npc.setText("")
        self.pushButton_npc.setObjectName("pushButton_npc")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "推薦"))
        self.label.setText(_translate("Dialog", "Bestieat"))
        self.pushButton_discount.setText(_translate("Dialog", "   折價卷"))
        self.pushButton_friend.setText(_translate("Dialog", "   好友"))
        self.pushButton_shop.setText(_translate("Dialog", "   商城"))
        self.pushButton_task.setText(_translate("Dialog", "   任務"))
        self.pushButton_favorite.setText(_translate("Dialog", "   我的收藏"))
        self.pushButton_rest.setText(_translate("Dialog", "   我是店家"))

import back_rc
