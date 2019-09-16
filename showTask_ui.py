# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showTask.ui'
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
        self.pushButton_arrow = QtWidgets.QPushButton(self.frame)
        self.pushButton_arrow.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.pushButton_arrow.setText("")
        self.pushButton_arrow.setObjectName("pushButton_arrow")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, 341, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.mytask = QtWidgets.QWidget()
        self.mytask.setObjectName("mytask")
        self.groupBox_3 = QtWidgets.QGroupBox(self.mytask)
        self.groupBox_3.setGeometry(QtCore.QRect(2, 280, 331, 251))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(230, 51, 76);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(230, 51, 76);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.toolButton_9 = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_9.setGeometry(QtCore.QRect(240, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.toolButton_9.setFont(font)
        self.toolButton_9.setStyleSheet("background-color:rgb(230, 51, 76 ,230);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")
        self.toolButton_9.setObjectName("toolButton_9")
        self.groupBox_4 = QtWidgets.QGroupBox(self.mytask)
        self.groupBox_4.setGeometry(QtCore.QRect(2, 10, 331, 251))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_4.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(230, 51, 76);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(230, 51, 76);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.groupBox_4.setObjectName("groupBox_4")
        self.toolButton_8 = QtWidgets.QToolButton(self.groupBox_4)
        self.toolButton_8.setGeometry(QtCore.QRect(240, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.toolButton_8.setFont(font)
        self.toolButton_8.setStyleSheet("background-color:rgb(230, 51, 76 ,230);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")
        self.toolButton_8.setObjectName("toolButton_8")
        self.tabWidget.addTab(self.mytask, "")
        self.alltask = QtWidgets.QWidget()
        self.alltask.setObjectName("alltask")
        self.groupBox = QtWidgets.QGroupBox(self.alltask)
        self.groupBox.setGeometry(QtCore.QRect(2, 10, 331, 251))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(230, 51, 76);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(230, 51, 76);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("text-align:left;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("task_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 80, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("text-align:left;")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_more = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_more.setGeometry(QtCore.QRect(240, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_more.setFont(font)
        self.pushButton_more.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_more.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_more.setAutoFillBackground(False)
        self.pushButton_more.setStyleSheet("background-color: rgba(230, 51, 76, 230);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_more.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_more.setAutoDefault(False)
        self.pushButton_more.setFlat(False)
        self.pushButton_more.setObjectName("pushButton_more")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 130, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("text-align:left;")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.alltask)
        self.groupBox_2.setGeometry(QtCore.QRect(2, 280, 331, 251))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(230, 51, 76);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(230, 51, 76);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.toolButton_7 = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_7.setGeometry(QtCore.QRect(240, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.toolButton_7.setFont(font)
        self.toolButton_7.setStyleSheet("background-color:rgb(230, 51, 76,230);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")
        self.toolButton_7.setObjectName("toolButton_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 30, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("text-align:left;")
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 80, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("text-align:left;")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 130, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("text-align:left;")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.alltask, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "一般任務"))
        self.toolButton_9.setText(_translate("MainWindow", "more..."))
        self.groupBox_4.setTitle(_translate("MainWindow", "每日任務"))
        self.toolButton_8.setText(_translate("MainWindow", "more..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mytask), _translate("MainWindow", "      我的任務      "))
        self.groupBox.setTitle(_translate("MainWindow", "每日任務"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_more.setText(_translate("MainWindow", "more..."))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.groupBox_2.setTitle(_translate("MainWindow", "一般任務"))
        self.toolButton_7.setText(_translate("MainWindow", "more..."))
        self.pushButton_6.setText(_translate("MainWindow", "4"))
        self.pushButton_4.setText(_translate("MainWindow", "5"))
        self.pushButton_5.setText(_translate("MainWindow", "6"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.alltask), _translate("MainWindow", "      所有任務      "))

import back_rc
