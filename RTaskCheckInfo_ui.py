# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RTaskCheckInfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 640)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.frame.setStyleSheet("QFrame{\n"
"background-image: url(:/back/back.png);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_disc = QtWidgets.QLabel(self.frame)
        self.label_disc.setGeometry(QtCore.QRect(140, 140, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        self.label_disc.setFont(font)
        self.label_disc.setText("")
        self.label_disc.setObjectName("label_disc")
        self.valid_start = QtWidgets.QLabel(self.frame)
        self.valid_start.setGeometry(QtCore.QRect(140, 420, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.valid_start.setFont(font)
        self.valid_start.setText("")
        self.valid_start.setObjectName("valid_start")
        self.la_pre_detail = QtWidgets.QLabel(self.frame)
        self.la_pre_detail.setGeometry(QtCore.QRect(40, 250, 281, 151))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        self.la_pre_detail.setFont(font)
        self.la_pre_detail.setStyleSheet("border-radius:5px;")
        self.la_pre_detail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.la_pre_detail.setFrameShadow(QtWidgets.QFrame.Plain)
        self.la_pre_detail.setText("")
        self.la_pre_detail.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.la_pre_detail.setWordWrap(False)
        self.la_pre_detail.setObjectName("la_pre_detail")
        self.valid_end = QtWidgets.QLabel(self.frame)
        self.valid_end.setGeometry(QtCore.QRect(140, 451, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.valid_end.setFont(font)
        self.valid_end.setText("")
        self.valid_end.setObjectName("valid_end")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 89, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(230, 51, 76);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 199, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(230, 51, 76);")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 20, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(230, 51, 76);")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(41, 540, 125, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(230, 51, 76,230);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(190, 540, 125, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(230, 51, 76,230);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 420, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(230, 51, 76);")
        self.label_5.setObjectName("label_5")
        self.taskname = QtWidgets.QLabel(self.frame)
        self.taskname.setGeometry(QtCore.QRect(140, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        self.taskname.setFont(font)
        self.taskname.setText("")
        self.taskname.setObjectName("taskname")
        self.label_pre = QtWidgets.QLabel(self.frame)
        self.label_pre.setGeometry(QtCore.QRect(140, 199, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        self.label_pre.setFont(font)
        self.label_pre.setText("")
        self.label_pre.setObjectName("label_pre")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "任務名稱"))
        self.label_4.setText(_translate("Form", "條    件"))
        self.label.setText(_translate("Form", "任務資訊確認"))
        self.label_3.setText(_translate("Form", "優    惠"))
        self.pushButton_2.setText(_translate("Form", "上一步"))
        self.pushButton.setText(_translate("Form", "確定送出"))
        self.label_5.setText(_translate("Form", "執行日期"))

import back_rc
