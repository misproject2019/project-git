# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recommend.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 640)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.frame.setMinimumSize(QtCore.QSize(360, 640))
        self.frame.setStyleSheet("QFrame{\n"
"background-image: url(:/back/back.png);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 570, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgba(230, 51, 76, 230);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 570, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgba(230, 51, 76, 230);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 20, 201, 41))
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
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(30, 90, 301, 181))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(230, 51, 76);\n"
"    border-radius:4px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(230, 51, 76);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 40, 241, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setChecked(False)
        self.checkBox_4.setAutoExclusive(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(False)
        self.checkBox.setAutoExclusive(True)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setChecked(False)
        self.checkBox_7.setAutoExclusive(True)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 0, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setAutoExclusive(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 310, 301, 181))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(230, 51, 76);\n"
"    border-radius:4px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(230, 51, 76);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 40, 281, 122))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.gridLayoutWidget_2.setFont(font)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_15 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_15.setFont(font)
        self.checkBox_15.setAutoExclusive(True)
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout_2.addWidget(self.checkBox_15, 1, 2, 1, 1)
        self.checkBox_16 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_16.setFont(font)
        self.checkBox_16.setAutoExclusive(True)
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout_2.addWidget(self.checkBox_16, 0, 2, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setAutoExclusive(True)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_2.addWidget(self.checkBox_9, 2, 0, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setToolTipDuration(-1)
        self.checkBox_11.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_11.setAutoExclusive(True)
        self.checkBox_11.setAutoRepeatInterval(100)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_2.addWidget(self.checkBox_11, 1, 0, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setAutoExclusive(True)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_2.addWidget(self.checkBox_10, 1, 1, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setChecked(False)
        self.checkBox_12.setAutoExclusive(True)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout_2.addWidget(self.checkBox_12, 0, 0, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_14.setFont(font)
        self.checkBox_14.setAutoExclusive(True)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout_2.addWidget(self.checkBox_14, 0, 1, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_13.setFont(font)
        self.checkBox_13.setAutoExclusive(True)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout_2.addWidget(self.checkBox_13, 2, 1, 1, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 90, 321, 181))
        self.widget.setStyleSheet("QWidget{\n"
"border-radius:20px;\n"
"background-image: url(:/back/back.png);\n"
"border: 2px solid rgb(230, 51, 76);\n"
"}\n"
"QLabel{\n"
"border: rgb(255, 255, 255);}")
        self.widget.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 211, 50))
        self.label_2.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(230, 51, 76);")
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(40, 110, 261, 1))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 130, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("border:1px solid rgb(230, 51, 76);\n"
"border-radius:20px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_email1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_email1.setEnabled(True)
        self.lineEdit_email1.setGeometry(QtCore.QRect(40, 60, 261, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.lineEdit_email1.setFont(font)
        self.lineEdit_email1.setStyleSheet("background:transparent;\n"
"border:0px solid rgb(255, 255, 255);")
        self.lineEdit_email1.setMaxLength(50)
        self.lineEdit_email1.setFrame(False)
        self.lineEdit_email1.setObjectName("lineEdit_email1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.pushButton.setText(_translate("Form", "進行推薦"))
        self.label.setText(_translate("Form", "不知道要吃什麼嗎？"))
        self.groupBox.setTitle(_translate("Form", "選擇一個店家類型"))
        self.checkBox_4.setText(_translate("Form", "咖啡店"))
        self.checkBox.setText(_translate("Form", "餐廳"))
        self.checkBox_7.setText(_translate("Form", "酒吧"))
        self.checkBox_5.setText(_translate("Form", "麵包店"))
        self.groupBox_2.setTitle(_translate("Form", "選擇一個料理特色"))
        self.checkBox_15.setText(_translate("Form", "法式"))
        self.checkBox_16.setText(_translate("Form", "韓式"))
        self.checkBox_9.setText(_translate("Form", "港式"))
        self.checkBox_11.setText(_translate("Form", "美式"))
        self.checkBox_10.setText(_translate("Form", "義式"))
        self.checkBox_12.setText(_translate("Form", "中式"))
        self.checkBox_14.setText(_translate("Form", "日式"))
        self.checkBox_13.setText(_translate("Form", "台式"))
        self.label_2.setText(_translate("Form", "請輸入地址或附近地標"))
        self.pushButton_3.setText(_translate("Form", "確定"))

import back_rc
