# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MTaskCheckInfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 640)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 10, 191, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 150, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(81, 200, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(61, 250, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(60, 310, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 400, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 460, 112, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.taskname = QtWidgets.QLabel(Form)
        self.taskname.setGeometry(QtCore.QRect(180, 150, 101, 21))
        self.taskname.setText("")
        self.taskname.setObjectName("taskname")
        self.label_disc = QtWidgets.QLabel(Form)
        self.label_disc.setGeometry(QtCore.QRect(180, 200, 101, 21))
        self.label_disc.setText("")
        self.label_disc.setObjectName("label_disc")
        self.label_pre = QtWidgets.QLabel(Form)
        self.label_pre.setGeometry(QtCore.QRect(180, 250, 101, 21))
        self.label_pre.setText("")
        self.label_pre.setObjectName("label_pre")
        self.label_date = QtWidgets.QLabel(Form)
        self.label_date.setGeometry(QtCore.QRect(180, 310, 101, 21))
        self.label_date.setText("")
        self.label_date.setObjectName("label_date")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "每日任務資訊確認"))
        self.label_2.setText(_translate("Form", "任務名稱"))
        self.label_3.setText(_translate("Form", "優惠"))
        self.label_4.setText(_translate("Form", "優惠條件"))
        self.label_5.setText(_translate("Form", "執行日期"))
        self.pushButton.setText(_translate("Form", "確定送出"))
        self.pushButton_2.setText(_translate("Form", "上一步"))

