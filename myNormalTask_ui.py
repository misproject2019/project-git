# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myNormalTask.ui'
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
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QGroupBox\" name=\"groupBox\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>10</x>\n"
"     <y>60</y>\n"
"     <width>340</width>\n"
"     <height>561</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"font\">\n"
"    <font>\n"
"     <family>Microsoft YaHei UI</family>\n"
"     <pointsize>12</pointsize>\n"
"    </font>\n"
"   </property>\n"
"   <property name=\"layoutDirection\">\n"
"    <enum>Qt::LeftToRight</enum>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">QGroupBox{\n"
"    border: 1px solid rgb(230, 51, 76);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(230, 51, 76);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}</string>\n"
"   </property>\n"
"   <property name=\"title\">\n"
"    <string>我的一般任務</string>\n"
"   </property>\n"
"   <widget class=\"QPushButton\" name=\"pushButton_2\">\n"
"    <property name=\"geometry\">\n"
"     <rect>\n"
"      <x>20</x>\n"
"      <y>90</y>\n"
"      <width>300</width>\n"
"      <height>41</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>PushButton</string>\n"
"    </property>\n"
"   </widget>\n"
"   <widget class=\"QPushButton\" name=\"pushButton_3\">\n"
"    <property name=\"geometry\">\n"
"     <rect>\n"
"      <x>20</x>\n"
"      <y>140</y>\n"
"      <width>300</width>\n"
"      <height>41</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>PushButton</string>\n"
"    </property>\n"
"   </widget>\n"
"   <widget class=\"QPushButton\" name=\"pushButton_5\">\n"
"    <property name=\"geometry\">\n"
"     <rect>\n"
"      <x>20</x>\n"
"      <y>40</y>\n"
"      <width>300</width>\n"
"      <height>41</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>PushButton</string>\n"
"    </property>\n"
"   </widget>\n"
"  </widget>\n"
"  <widget class=\"QPushButton\" name=\"pushButton_arrow\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>0</x>\n"
"     <y>0</y>\n"
"     <width>50</width>\n"
"     <height>50</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string/>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 340, 561))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
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
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 90, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("text-align:left;")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("task_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 140, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("text-align:left;")
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 40, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("text-align:left;")
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_arrow = QtWidgets.QPushButton(self.frame)
        self.pushButton_arrow.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.pushButton_arrow.setText("")
        self.pushButton_arrow.setObjectName("pushButton_arrow")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "我的一般任務"))

import back_rc
