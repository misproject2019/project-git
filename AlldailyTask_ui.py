# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlldailyTask.ui'
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
        self.frame.setStyleSheet("QFrame{\n"
"background-image: url(:/back/back.png);\n"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QGroupBox\" name=\"groupBox\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>10</x>\n"
"     <y>70</y>\n"
"     <width>340</width>\n"
"     <height>541</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"font\">\n"
"    <font>\n"
"     <family>Yu Gothic UI</family>\n"
"     <pointsize>12</pointsize>\n"
"    </font>\n"
"   </property>\n"
"   <property name=\"layoutDirection\">\n"
"    <enum>Qt::LeftToRight</enum>\n"
"   </property>\n"
"   <property name=\"title\">\n"
"    <string>每日任務</string>\n"
"   </property>\n"
"   <widget class=\"QPushButton\" name=\"pushButton\">\n"
"    <property name=\"geometry\">\n"
"     <rect>\n"
"      <x>30</x>\n"
"      <y>30</y>\n"
"      <width>300</width>\n"
"      <height>41</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string/>\n"
"    </property>\n"
"   </widget>\n"
"   <widget class=\"QPushButton\" name=\"pushButton_2\">\n"
"    <property name=\"geometry\">\n"
"     <rect>\n"
"      <x>30</x>\n"
"      <y>80</y>\n"
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
"      <x>30</x>\n"
"      <y>130</y>\n"
"      <width>300</width>\n"
"      <height>41</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>PushButton</string>\n"
"    </property>\n"
"   </widget>\n"
"   <widget class=\"QPushButton\" name=\"pushButton_4\">\n"
"    <property name=\"geometry\">\n"
"     <rect>\n"
"      <x>30</x>\n"
"      <y>180</y>\n"
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
"      <x>30</x>\n"
"      <y>230</y>\n"
"      <width>300</width>\n"
"      <height>41</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>PushButton</string>\n"
"    </property>\n"
"   </widget>\n"
"   <widget class=\"QPushButton\" name=\"pushButton_6\">\n"
"    <property name=\"geometry\">\n"
"     <rect>\n"
"      <x>30</x>\n"
"      <y>280</y>\n"
"      <width>300</width>\n"
"      <height>41</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>PushButton</string>\n"
"    </property>\n"
"   </widget>\n"
"   <widget class=\"QPushButton\" name=\"pushButton_7\">\n"
"    <property name=\"geometry\">\n"
"     <rect>\n"
"      <x>30</x>\n"
"      <y>330</y>\n"
"      <width>300</width>\n"
"      <height>41</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>PushButton</string>\n"
"    </property>\n"
"   </widget>\n"
"   <widget class=\"QPushButton\" name=\"pushButton_8\">\n"
"    <property name=\"geometry\">\n"
"     <rect>\n"
"      <x>30</x>\n"
"      <y>380</y>\n"
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
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(20, 41, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("text-align:left;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("task_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 90, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("text-align:left;")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 140, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("text-align:left;")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 190, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("text-align:left;")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 240, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("text-align:left;")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 290, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("text-align:left;")
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 340, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("text-align:left;")
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 390, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("text-align:left;")
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_arrow = QtWidgets.QPushButton(self.frame)
        self.pushButton_arrow.setGeometry(QtCore.QRect(0, 0, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_arrow.setFont(font)
        self.pushButton_arrow.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(230, 51, 76);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(230, 51, 76);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.pushButton_arrow.setText("")
        self.pushButton_arrow.setObjectName("pushButton_arrow")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "每日任務"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.pushButton_4.setText(_translate("Form", "PushButton"))
        self.pushButton_5.setText(_translate("Form", "PushButton"))
        self.pushButton_6.setText(_translate("Form", "PushButton"))
        self.pushButton_7.setText(_translate("Form", "PushButton"))
        self.pushButton_8.setText(_translate("Form", "PushButton"))

import back_rc
