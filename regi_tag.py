# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regi_tag.ui'
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
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(230, 51, 76);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(230, 51, 76);")
        self.label_2.setObjectName("label_2")
        self.back_Button = QtWidgets.QPushButton(self.frame)
        self.back_Button.setGeometry(QtCore.QRect(20, 570, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.back_Button.setFont(font)
        self.back_Button.setStyleSheet("background-color:rgb(230, 51, 76);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.back_Button.setObjectName("back_Button")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 20, 51, 33))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.next_Button = QtWidgets.QPushButton(self.frame)
        self.next_Button.setGeometry(QtCore.QRect(190, 570, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.next_Button.setFont(font)
        self.next_Button.setStyleSheet("background-color:rgb(230, 51, 76);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.next_Button.setObjectName("next_Button")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 110, 334, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setStyleSheet("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 1, 2, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setStyleSheet("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 2, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setStyleSheet("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 1, 1, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setStyleSheet("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 2, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setStyleSheet("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 2, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setStyleSheet("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 1, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 350, 331, 161))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_10 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setStyleSheet("")
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_3.addWidget(self.checkBox_10, 2, 0, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_14.setFont(font)
        self.checkBox_14.setStyleSheet("")
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout_3.addWidget(self.checkBox_14, 0, 1, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setStyleSheet("")
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_3.addWidget(self.checkBox_9, 1, 0, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setStyleSheet("")
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout_3.addWidget(self.checkBox_12, 0, 0, 1, 1)
        self.checkBox_16 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_16.setFont(font)
        self.checkBox_16.setStyleSheet("")
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout_3.addWidget(self.checkBox_16, 0, 2, 1, 1)
        self.checkBox_15 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_15.setFont(font)
        self.checkBox_15.setStyleSheet("")
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout_3.addWidget(self.checkBox_15, 1, 2, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_13.setFont(font)
        self.checkBox_13.setStyleSheet("")
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout_3.addWidget(self.checkBox_13, 1, 1, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setStyleSheet("")
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_3.addWidget(self.checkBox_11, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "料理特色"))
        self.label_2.setText(_translate("MainWindow", "店家類型"))
        self.back_Button.setText(_translate("MainWindow", "返回"))
        self.label.setText(_translate("MainWindow", "標籤"))
        self.next_Button.setText(_translate("MainWindow", "下一步"))
        self.checkBox_8.setText(_translate("MainWindow", "早餐/早午餐"))
        self.checkBox_5.setText(_translate("MainWindow", "吃到飽"))
        self.checkBox_6.setText(_translate("MainWindow", "自助餐"))
        self.checkBox_7.setText(_translate("MainWindow", "小吃店"))
        self.checkBox_3.setText(_translate("MainWindow", "酒吧"))
        self.checkBox_4.setText(_translate("MainWindow", "飲料店"))
        self.checkBox_2.setText(_translate("MainWindow", "咖啡店"))
        self.checkBox.setText(_translate("MainWindow", "餐廳"))
        self.checkBox_10.setText(_translate("MainWindow", "港式"))
        self.checkBox_14.setText(_translate("MainWindow", "日式"))
        self.checkBox_9.setText(_translate("MainWindow", "美式"))
        self.checkBox_12.setText(_translate("MainWindow", "中式"))
        self.checkBox_16.setText(_translate("MainWindow", "韓式"))
        self.checkBox_15.setText(_translate("MainWindow", "法式"))
        self.checkBox_13.setText(_translate("MainWindow", "義式"))
        self.checkBox_11.setText(_translate("MainWindow", "台式"))

import back_rc
