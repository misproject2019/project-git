# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:54:44 2019

@author: Julia
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(378, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 40, 341, 581))
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
        self.pushButton_5 = QtWidgets.QPushButton(self.mytask)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 40, 311, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.mytask)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 100, 311, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.mytask)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 160, 311, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.mytask)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 470, 311, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.mytask, "")
        self.alltask = QtWidgets.QWidget()
        self.alltask.setObjectName("alltask")
        self.pushButton_2 = QtWidgets.QPushButton(self.alltask)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 40, 311, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.alltask)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 100, 311, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.alltask)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 160, 311, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.alltask)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 460, 311, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.tabWidget.addTab(self.alltask, "")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 0, 201, 41))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "返回"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mytask), _translate("MainWindow", "         地圖          "))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "返回"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.alltask), _translate("MainWindow", "       美食清單      "))
        self.label_2.setText(_translate("MainWindow", "共同收藏夾"))