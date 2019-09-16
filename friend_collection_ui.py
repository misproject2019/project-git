# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'friend_collection.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(360, 640)
        MainWindow.setAnimated(True)
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
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(15, 85, 331, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setToolTipDuration(-1)
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.mytask = QtWidgets.QWidget()
        self.mytask.setObjectName("mytask")
        self.pushButton_8 = QtWidgets.QPushButton(self.mytask)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 450, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgba(230, 51, 76, 230);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.mytask, "")
        self.alltask = QtWidgets.QWidget()
        self.alltask.setObjectName("alltask")
        self.pushButton_2 = QtWidgets.QPushButton(self.alltask)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.alltask)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 50, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.alltask)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 90, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.alltask)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 450, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgba(230, 51, 76, 230);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.tabWidget.addTab(self.alltask, "")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_8.setText(_translate("MainWindow", "返回"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mytask), _translate("MainWindow", "         地圖         "))
        self.pushButton_2.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "1"))
        self.pushButton_4.setText(_translate("MainWindow", "1"))
        self.pushButton_9.setText(_translate("MainWindow", "返回"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.alltask), _translate("MainWindow", "      美食清單      "))
        self.label_2.setText(_translate("MainWindow", "共同收藏夾"))

import back_rc
