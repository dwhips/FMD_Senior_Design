# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confidence_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QFileDialog, QDesktopWidget, QCheckBox

import sys

sys.path.append('../')  # could be hacky
import Global.gbl_fmd_class_list as gbl_fmd
import FMD.FMDClass as class_file


class Ui_confidence_screen(QWidget):
    def setupUi(self, confidence_screen):

        # Get the size of the screen
        width = QDesktopWidget().screenGeometry(-1).width()
        height = QDesktopWidget().screenGeometry(-1).height()

        # width and height of the created window
        windowwidth = width/2
        windowheight = height/1.5

        # Create the confidence screen widget
        self.confidence_screen = QtWidgets.QWidget()
        self.confidence_screen.setObjectName("confidence_screen")
        self.confidence_screen.setStyleSheet("background: rgb(177,185,199)")

        # Create the Scrolling List
        self.frame_list = QtWidgets.QListWidget(self.confidence_screen)
        self.frame_list.setGeometry(QtCore.QRect(windowwidth*0.7, windowheight*0.1, windowwidth*0.25, windowheight*0.7))
        self.frame_list.setStyleSheet("background:rgb(255, 255, 255)")
        self.frame_list.setObjectName("frame_list")
        item = QtWidgets.QListWidgetItem()
        self.frame_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.frame_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.frame_list.addItem(item)

        # Make the threshold slider
        self.threshold_slider = QtWidgets.QSlider(self.confidence_screen)
        self.threshold_slider.setGeometry(QtCore.QRect(windowwidth * 0.1, windowheight * 0.85, windowwidth * 0.8, windowheight * 0.1))
        self.threshold_slider.setOrientation(QtCore.Qt.Horizontal)
        self.threshold_slider.setObjectName("threshold_slider")
        self.threshold_slider.setRange(0, 255)
        # self.threshold_slider.valueChanged.connect(self.SliderChanged)  ADD the functionality later

        # Create the screen title
        self.screen_title = QtWidgets.QLabel(self.confidence_screen)
        self.screen_title.setGeometry(QtCore.QRect(windowwidth*0.1, windowheight*0.05, windowwidth*0.6, windowheight*0.1))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.screen_title.setFont(font)
        self.screen_title.setAlignment(QtCore.Qt.AlignCenter)
        self.screen_title.setObjectName("screen_title")

        # Create the Accept Button
        self.accept_btn = QtWidgets.QPushButton(self.confidence_screen)
        self.accept_btn.setGeometry(QtCore.QRect(windowwidth*0.2, windowheight*0.7, windowwidth*0.1, windowheight*0.05))
        self.accept_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.accept_btn.setObjectName("accept_btn")

        # Discard Button
        self.discard_btn = QtWidgets.QPushButton(self.confidence_screen)
        self.discard_btn.setGeometry(QtCore.QRect(windowwidth*0.4, windowheight*0.7, windowwidth*0.1, windowheight*0.05))
        self.discard_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.discard_btn.setObjectName("discard_btn")

        # Add a back button here?

        # Set the central widget
        confidence_screen.setCentralWidget(self.confidence_screen)

        self.retranslateUi(self.confidence_screen)
        QtCore.QMetaObject.connectSlotsByName(self.confidence_screen)

    def retranslateUi(self, confidence_screen):
        _translate = QtCore.QCoreApplication.translate
        confidence_screen.setWindowTitle(_translate("confidence_screen", "MU Brachial Analyzer"))
        __sortingEnabled = self.frame_list.isSortingEnabled()
        self.frame_list.setSortingEnabled(False)
        item = self.frame_list.item(0)
        item.setText(_translate("confidence_screen", "Frame0"))
        item = self.frame_list.item(1)
        item.setText(_translate("confidence_screen", "Frame1"))
        item = self.frame_list.item(2)
        item.setText(_translate("confidence_screen", "Frame2"))
        self.frame_list.setSortingEnabled(__sortingEnabled)
        self.screen_title.setText(_translate("confidence_screen", "Manual Frame Editor"))
        self.accept_btn.setText(_translate("confidence_screen", "Accept"))
        self.discard_btn.setText(_translate("confidence_screen", "Discard"))
