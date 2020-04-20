# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'excel_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDesktopWidget, QFileDialog


class Ui_excel_screen(QWidget):
    def setupUi(self, excel_screen):


        # Get the size of the screen
        width = QDesktopWidget().screenGeometry(-1).width()
        height = QDesktopWidget().screenGeometry(-1).height()

        # Height of the actual window for the application
        windowwidth = width/2
        windowheight = height/1.5

        # Create the excel screen widget
        self.excel_screen = QtWidgets.QWidget()
        self.excel_screen.setObjectName("excel_screen")
        self.excel_screen.setStyleSheet("background:rgb(177, 185, 199)")

        # Excel Folder Text Box
        self.excel_folder = QtWidgets.QTextBrowser(self.excel_screen)
        self.excel_folder.setGeometry(QtCore.QRect(windowwidth*0.1, windowheight*0.2, windowwidth*0.25, windowheight*0.2))
        self.excel_folder.setStyleSheet("background:rgb(255, 255, 255)")
        self.excel_folder.setObjectName("excel_folder")

        # Excel Folder Label
        self.folder_label = QtWidgets.QLabel(self.excel_screen)
        self.folder_label.setGeometry(QtCore.QRect(windowwidth*0.15, windowheight*0.12, windowwidth*0.2, windowheight*0.05))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.folder_label.setFont(font)
        self.folder_label.setObjectName("folder_label")

        # Choose Folder Button
        self.choose_folder_btn = QtWidgets.QPushButton(self.excel_screen)
        self.choose_folder_btn.setGeometry(QtCore.QRect(windowwidth*0.4, windowheight*0.25, windowwidth*0.2,windowheight*0.1 ))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choose_folder_btn.setFont(font)
        self.choose_folder_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.choose_folder_btn.setObjectName("choose_folder_btn")
        self.choose_folder_btn.clicked.connect(self.ChooseFolder)

        # Excel File Name Text Box
        self.excel_file_name = QtWidgets.QTextBrowser(self.excel_screen)
        self.excel_file_name.setGeometry(QtCore.QRect(windowwidth*0.1, windowheight*0.5, windowwidth*0.25, windowheight*0.2))
        self.excel_file_name.setStyleSheet("background:rgb(255, 255, 255)")
        self.excel_file_name.setObjectName("excel_file_name")

        # Excel File Name Box Label
        self.excel_filename_label = QtWidgets.QLabel(self.excel_screen)
        self.excel_filename_label.setGeometry(QtCore.QRect(windowwidth*0.15, windowheight*0.42, windowwidth*0.2, windowheight*0.05))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.excel_filename_label.setFont(font)
        self.excel_filename_label.setObjectName("excel_filename_label")

        # Back Button
        self.back_btn = QtWidgets.QPushButton(self.excel_screen)
        self.back_btn.setGeometry(QtCore.QRect(windowwidth * 0.01, windowheight * 0.01, windowwidth * 0.05, windowheight * 0.03))
        self.back_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.back_btn.setObjectName("back_btn")
        font = QtGui.QFont()
        font.setPointSize(16)

        # OK Button
        self.ok_btn = QtWidgets.QPushButton(self.excel_screen)
        self.ok_btn.setGeometry(QtCore.QRect(windowwidth * 0.65, windowheight * 0.5, windowwidth * 0.25, windowheight * 0.2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ok_btn.setFont(font)
        self.ok_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.ok_btn.setObjectName("ok_btn")

        # Set the central widget
        excel_screen.setCentralWidget(self.excel_screen)

        self.retranslateUi(self.excel_screen)
        QtCore.QMetaObject.connectSlotsByName(self.excel_screen)

    def ChooseFolder(self):
        OutputFolder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        self.excel_folder.setText(OutputFolder)

    def retranslateUi(self, excel_screen):
        _translate = QtCore.QCoreApplication.translate
        excel_screen.setWindowTitle(_translate("excel_screen", "MU Brachial Analyzer"))
        self.folder_label.setText(_translate("excel_screen", "Excel File Folder"))
        self.choose_folder_btn.setText(_translate("excel_screen", "Choose Folder"))
        self.excel_filename_label.setText(_translate("excel_screen", "Excel File Name"))
        self.back_btn.setText(_translate("excel_screen", "Back"))
        self.ok_btn.setText(_translate("excel_screen", "OK"))
