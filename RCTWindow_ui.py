# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RestaCreateTask.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(340, 640)
        font = QtGui.QFont()
        font.setPointSize(9)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(150, 250, 131, 24))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 250, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 190, 113, 26))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 380, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 130, 113, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 520, 131, 34))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 520, 112, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.RPeriod_start = QtWidgets.QDateTimeEdit(Form)
        self.RPeriod_start.setGeometry(QtCore.QRect(130, 380, 194, 26))
        self.RPeriod_start.setDate(QtCore.QDate(2019, 8, 20))
        self.RPeriod_start.setMaximumDate(QtCore.QDate(2022, 12, 31))
        self.RPeriod_start.setMinimumDate(QtCore.QDate(2019, 8, 20))
        self.RPeriod_start.setCalendarPopup(True)
        self.RPeriod_start.setObjectName("RPeriod_start")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 430, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.RPeriod_end = QtWidgets.QDateTimeEdit(Form)
        self.RPeriod_end.setGeometry(QtCore.QRect(130, 430, 194, 26))
        self.RPeriod_end.setDate(QtCore.QDate(2019, 8, 21))
        self.RPeriod_end.setMaximumDate(QtCore.QDate(2022, 12, 31))
        self.RPeriod_end.setMinimumDate(QtCore.QDate(2019, 8, 21))
        self.RPeriod_end.setCalendarPopup(True)
        self.RPeriod_end.setObjectName("RPeriod_end")
        self.textEdit_taskDetail = QtWidgets.QTextEdit(Form)
        self.textEdit_taskDetail.setGeometry(QtCore.QRect(20, 290, 301, 71))
        self.textEdit_taskDetail.setObjectName("textEdit_taskDetail")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(110, 30, 31, 18))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_nowUser = QtWidgets.QLabel(Form)
        self.label_nowUser.setGeometry(QtCore.QRect(150, 30, 161, 18))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_nowUser.setFont(font)
        self.label_nowUser.setObjectName("label_nowUser")
        self.pushButton_arrow = QtWidgets.QPushButton(Form)
        self.pushButton_arrow.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.pushButton_arrow.setText("")
        self.pushButton_arrow.setObjectName("pushButton_arrow")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "創建任務"))
        self.comboBox.setItemText(0, _translate("Form", "出示優惠畫面"))
        self.comboBox.setItemText(1, _translate("Form", "打卡"))
        self.label_4.setText(_translate("Form", "條件"))
        self.label_2.setText(_translate("Form", "任務名稱"))
        self.label_5.setText(_translate("Form", "起始日期"))
        self.pushButton.setText(_translate("Form", "確認任務資訊"))
        self.label_3.setText(_translate("Form", "優惠"))
        self.pushButton_2.setText(_translate("Form", "重新設定"))
        self.label_6.setText(_translate("Form", "結束日期"))
        self.textEdit_taskDetail.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">條件詳細說明..</p></body></html>"))
        self.label_7.setText(_translate("Form", "Hi! "))
        self.label_nowUser.setText(_translate("Form", "TextLabel"))
