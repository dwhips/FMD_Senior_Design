# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QWidget


class Ui_start_screen(QWidget):
    def setupUi(self, start_screen):

        #Get the size of the screen
        width = QDesktopWidget().screenGeometry(-1).width()
        height = QDesktopWidget().screenGeometry(-1).height()

        windowwidth = width/2
        windowheight = height/1.5

        self.start_screen = QtWidgets.QWidget()
        self.start_screen.setObjectName("start_screen")
        start_screen.resize(width/2, height/1.5)
        start_screen.setStyleSheet("background: rgb(177, 185, 199)")
        self.welcome_message = QtWidgets.QLabel(self.start_screen)
        self.welcome_message.setGeometry(QtCore.QRect(windowwidth*0.1, windowheight*0.1, windowwidth*0.8, windowheight/7))
        self.welcome_message.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.welcome_message.setFont(font)
        self.welcome_message.setScaledContents(True)
        self.welcome_message.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_message.setObjectName("welcome_message")
        self.fmd_button = QtWidgets.QPushButton(self.start_screen)
        self.fmd_button.setGeometry(QtCore.QRect(windowwidth*0.1, windowheight*0.3, windowwidth*0.25, windowheight*0.2))
        self.fmd_button.setStyleSheet("background:rgb(255, 255, 255)")
        self.fmd_button.setObjectName("fmd_button")
        self.integral_btn = QtWidgets.QPushButton(self.start_screen)
        self.integral_btn.setGeometry(QtCore.QRect(windowwidth*0.6, windowheight*0.3, windowwidth*0.25, windowheight*0.2))
        self.integral_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.integral_btn.setObjectName("integral_btn")

        start_screen.setCentralWidget(self.start_screen)

        self.retranslateUi(start_screen)
        QtCore.QMetaObject.connectSlotsByName(start_screen)

    def retranslateUi(self, start_screen):
        _translate = QtCore.QCoreApplication.translate
        start_screen.setWindowTitle(_translate("start_screen", "MU Brachial Analyzer"))
        self.welcome_message.setText(_translate("start_screen", "Welcome to the Brachial FMD Analzyer Software!"))
        self.fmd_button.setText(_translate("start_screen", "Flow Mediated Dilation"))
        self.integral_btn.setText(_translate("start_screen", "Flow Measurement"))
