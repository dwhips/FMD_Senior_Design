# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fmd_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Brachialanalyzer(object):
    def setupUi(self, Brachialanalyzer):
        Brachialanalyzer.setObjectName("Brachialanalyzer")
        Brachialanalyzer.resize(644, 523)
        Brachialanalyzer.setStyleSheet("")
        self.grid = QtWidgets.QWidget(Brachialanalyzer)
        self.grid.setObjectName("grid")
        self.gridLayout = QtWidgets.QGridLayout(self.grid)
        self.gridLayout.setObjectName("gridLayout")
        self.print = QtWidgets.QLabel(self.grid)
        self.print.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.print.setObjectName("print")
        self.gridLayout.addWidget(self.print, 3, 0, 1, 1)
        self.ultrasoundimage = QtWidgets.QLabel(self.grid)
        self.ultrasoundimage.setText("")
        self.ultrasoundimage.setPixmap(QtGui.QPixmap(":/ultrasound_image/frame0.jpg"))
        self.ultrasoundimage.setObjectName("ultrasoundimage")
        self.gridLayout.addWidget(self.ultrasoundimage, 1, 2, 1, 1)
        self.centerclick = QtWidgets.QPushButton(self.grid)
        self.centerclick.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.centerclick.setObjectName("centerclick")
        self.gridLayout.addWidget(self.centerclick, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        Brachialanalyzer.setCentralWidget(self.grid)
        self.statusbar = QtWidgets.QStatusBar(Brachialanalyzer)
        self.statusbar.setObjectName("statusbar")
        Brachialanalyzer.setStatusBar(self.statusbar)

        self.retranslateUi(Brachialanalyzer)
        QtCore.QMetaObject.connectSlotsByName(Brachialanalyzer)

    def retranslateUi(self, Brachialanalyzer):
        _translate = QtCore.QCoreApplication.translate
        Brachialanalyzer.setWindowTitle(_translate("Brachialanalyzer", "MU Brachial Analyzer"))
        self.print.setText(_translate("Brachialanalyzer", "Place to print stuff from python"))
        self.centerclick.setText(_translate("Brachialanalyzer", "Confirm Center Click"))
import ultrasound_image_rc
