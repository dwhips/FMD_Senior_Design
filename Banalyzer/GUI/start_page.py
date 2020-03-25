# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDesktopWidget


class Ui_start_screen(object):
    def setupUi(self, start_screen):

        #Get the size of the screen
        width = QDesktopWidget().screenGeometry(-1).width()
        height = QDesktopWidget().screenGeometry(-1).height()

        start_screen.setObjectName("start_screen")
        start_screen.resize(width/2, height/1.5)
        start_screen.setStyleSheet("background: rgb(177, 185, 199)")
        self.welcome_message = QtWidgets.QLabel(start_screen)
        self.welcome_message.setGeometry(QtCore.QRect(250, 70, 1500, 342))
        self.welcome_message.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.welcome_message.setFont(font)
        self.welcome_message.setScaledContents(True)
        self.welcome_message.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_message.setObjectName("welcome_message")
        self.fmd_button = QtWidgets.QPushButton(start_screen)
        self.fmd_button.setGeometry(QtCore.QRect(250, 500, 282, 162))
        self.fmd_button.setStyleSheet("background:rgb(255, 255, 255)")
        self.fmd_button.setObjectName("fmd_button")
        self.integral_btn = QtWidgets.QPushButton(start_screen)
        self.integral_btn.setGeometry(QtCore.QRect(750, 500, 282, 162))
        self.integral_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.integral_btn.setObjectName("integral_btn")

        self.retranslateUi(start_screen)
        QtCore.QMetaObject.connectSlotsByName(start_screen)

    def retranslateUi(self, start_screen):
        _translate = QtCore.QCoreApplication.translate
        start_screen.setWindowTitle(_translate("start_screen", "MU Brachial Analyzer"))
        self.welcome_message.setText(_translate("start_screen", "Welcome to the Brachial FMD Analzyer Software!"))
        self.fmd_button.setText(_translate("start_screen", "Flow Mediated Dilation"))
        self.integral_btn.setText(_translate("start_screen", "Flow Measurement"))
