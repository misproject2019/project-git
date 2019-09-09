# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:59:01 2019

@author: Julia
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 361, 591))
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
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.mytask = QtWidgets.QWidget()
        self.mytask.setObjectName("mytask")
        self.textEdit_2 = QtWidgets.QTextEdit(self.mytask)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 90, 311, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.mytask)
        self.label.setGeometry(QtCore.QRect(20, 30, 201, 41))
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.mytask)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 470, 311, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.mytask, "")
        self.alltask = QtWidgets.QWidget()
        self.alltask.setObjectName("alltask")
        self.textEdit = QtWidgets.QTextEdit(self.alltask)
        self.textEdit.setGeometry(QtCore.QRect(10, 90, 311, 41))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.alltask)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 201, 41))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.alltask)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 470, 311, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.alltask, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "在下方輸入"))
        self.pushButton_3.setText(_translate("MainWindow", "加入好友"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mytask), _translate("MainWindow", "   好友e-mail    "))
        self.label_2.setText(_translate("MainWindow", "在下方輸入"))
        self.pushButton_2.setText(_translate("MainWindow", "加入好友"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.alltask), _translate("MainWindow", "       好友名字      "))
