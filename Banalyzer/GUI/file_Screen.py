# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QFileDialog, QDesktopWidget

import sys

sys.path.append('../')  # could be hacky
import Global.gbl_fmd_class_list as gbl_fmd
import FMD.FMDClass as class_file


class Ui_filescreen(QWidget):
    def setupUi(self, filescreen):
        # Get the size of the screen
        width = QDesktopWidget().screenGeometry(-1).width()
        height = QDesktopWidget().screenGeometry(-1).height()

        # width and height of the created window
        windowwidth = width / 2
        windowheight = height / 1.5

        # Create the file screen widget
        self.filescreen = QtWidgets.QWidget()
        self.filescreen.setObjectName("filescreen")
        self.filescreen.setStyleSheet("background: rgb(177, 185, 199)")

        # Create the instructions label
        self.instructions = QtWidgets.QLabel(self.filescreen)
        self.instructions.setGeometry(
            QtCore.QRect(windowwidth * 0.1, windowheight * 0.1, windowwidth * 0.7, windowheight * 0.2))
        self.instructions.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.instructions.setFont(font)
        self.instructions.setObjectName("instructions")

        # Second Column Label (File path)
        self.path_label = QtWidgets.QLabel(self.filescreen)
        self.path_label.setGeometry(
            QtCore.QRect(windowwidth * 0.25, windowheight * 0.3, windowwidth * 0.1, windowheight * 0.05))
        self.path_label.setAlignment(Qt.AlignCenter)
        font.setPointSize(12)
        self.path_label.setFont(font)
        self.path_label.setObjectName("file_label")

        # First Column Label (Name)
        self.name_label = QtWidgets.QLabel(self.filescreen)
        self.name_label.setGeometry(
            QtCore.QRect(windowwidth * 0.05, windowheight * 0.3, windowwidth * 0.1, windowheight * 0.05))
        self.name_label.setAlignment(Qt.AlignCenter)
        font.setPointSize(12)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")

        # Run button
        self.run_btn = QtWidgets.QPushButton(self.filescreen)
        self.run_btn.setGeometry(
            QtCore.QRect(windowwidth * 0.6, windowheight * 0.7, windowwidth * 0.25, windowheight * 0.2))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.run_btn.setFont(font)
        self.run_btn.setStyleSheet("background: rgb(255, 255, 255)")
        self.run_btn.setObjectName("run_btn")
        self.run_btn.clicked.connect(
            self.SaveFileData)  # needs to verify boxes are full, files exist etx. a lot of exception handling here

        # Create the First Column Layout (name layout)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.filescreen)
        self.verticalLayoutWidget.setGeometry(
            QtCore.QRect(windowwidth * 0.02, windowheight * 0.35, windowwidth * 0.18, windowheight * 0.57))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_names = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_names.setContentsMargins(5, 0, 0, 0)
        self.layout_names.setObjectName("layout_names")
        self.name1 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.name1.setStyleSheet("background: rgb(255, 255, 255)")
        self.name1.setObjectName("name1")
        self.layout_names.addWidget(self.name1)
        self.name2 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.name2.setStyleSheet("background: rgb(255, 255, 255)")
        self.name2.setObjectName("name2")
        self.layout_names.addWidget(self.name2)
        self.name3 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.name3.setStyleSheet("background: rgb(255, 255, 255)")
        self.name3.setObjectName("name3")
        self.layout_names.addWidget(self.name3)
        self.name4 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.name4.setStyleSheet("background: rgb(255, 255, 255)\n"
                                    "")
        self.name4.setObjectName("name4")
        self.layout_names.addWidget(self.name4)

        # section for the second column layout
        self.verticalLayoutWidget2 = QtWidgets.QWidget(self.filescreen)
        self.verticalLayoutWidget2.setGeometry(
            QtCore.QRect(windowwidth * 0.2, windowheight * 0.35, windowwidth * 0.18, windowheight * 0.57))
        self.verticalLayoutWidget2.setObjectName("verticalLayoutWidget2")
        self.layout_paths = QtWidgets.QVBoxLayout(self.verticalLayoutWidget2)
        self.layout_paths.setContentsMargins(5, 0, 0, 0)
        self.layout_paths.setObjectName("layout_paths")
        self.path1 = QtWidgets.QTextEdit(self.verticalLayoutWidget2)
        self.path1.setStyleSheet("background: rgb(255, 255, 255)")
        self.path1.setObjectName("path1")
        self.layout_paths.addWidget(self.path1)
        self.path2 = QtWidgets.QTextEdit(self.verticalLayoutWidget2)
        self.path2.setStyleSheet("background: rgb(255, 255, 255)")
        self.path2.setObjectName("path2")
        self.layout_paths.addWidget(self.path2)
        self.path3 = QtWidgets.QTextEdit(self.verticalLayoutWidget2)
        self.path3.setStyleSheet("background: rgb(255, 255, 255)")
        self.path3.setObjectName("path3")
        self.layout_paths.addWidget(self.path3)
        self.path4 = QtWidgets.QTextEdit(self.verticalLayoutWidget2)
        self.path4.setStyleSheet("background: rgb(255, 255, 255)\n"
                                    "")
        self.path4.setObjectName("path4")
        self.layout_paths.addWidget(self.path4)

        # Set up the study name box
        self.study = QtWidgets.QTextEdit(self.filescreen)
        self.study.setGeometry(
            QtCore.QRect(windowwidth * 0.6, windowheight * 0.35, windowwidth * 0.15, windowheight * 0.07))
        self.study.setStyleSheet("background: rgb(255, 255, 255)")

        # Study name box label
        self.study_label = QtWidgets.QLabel(self.filescreen)
        self.study_label.setGeometry(
            QtCore.QRect(windowwidth * 0.62, windowheight * 0.3, windowwidth * 0.1, windowheight * 0.05))
        self.study_label.setAlignment(Qt.AlignCenter)

        # Patient Name Box
        self.patient = QtWidgets.QTextEdit(self.filescreen)
        self.patient.setGeometry(
            QtCore.QRect(windowwidth * 0.6, windowheight * 0.5, windowwidth * 0.15, windowheight * 0.07))
        self.patient.setStyleSheet("background: rgb(255, 255, 255)")

        # Patient Name Box Label
        self.patient_label = QtWidgets.QLabel(self.filescreen)
        self.patient_label.setGeometry(
            QtCore.QRect(windowwidth * 0.62, windowheight * 0.45, windowwidth * 0.1, windowheight * 0.05))
        self.patient_label.setAlignment(Qt.AlignCenter)


        # Back button
        self.back_btn1 = QtWidgets.QPushButton(self.filescreen)
        self.back_btn1.setGeometry(
            QtCore.QRect(windowwidth * 0.01, windowheight * 0.01, windowwidth * 0.05, windowheight * 0.03))
        self.back_btn1.setStyleSheet("background:rgb(255, 255, 255)")
        self.back_btn1.setObjectName("back_btn")

        # Choose File Button
        self.chooseFile_btn = QtWidgets.QPushButton(self.filescreen)
        self.chooseFile_btn.setGeometry(
            QtCore.QRect(windowwidth * 0.4, windowheight * 0.4, windowwidth * 0.15, windowheight * 0.05))
        self.chooseFile_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.chooseFile_btn.setObjectName("chooseFile_btn")
        self.chooseFile_btn.clicked.connect(self.ChooseFile)  # !!!!!!!!!!!!

        # Set the central widget
        filescreen.setCentralWidget(self.filescreen)

        self.retranslateUi(filescreen)
        QtCore.QMetaObject.connectSlotsByName(filescreen)

    # opens up file browser and adds it to text box
    def ChooseFile(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open File')
        file_path = file_path[0]
        # TODO get the file to verify its open
        self.path1.setText(file_path)

    def SaveFileData(self):
        # file and name need new var names. do path and name instead
        name = self.name1.toPlainText()
        path = self.path1.toPlainText()
        study_name = self.study.toPlainText()
        gbl_fmd.class_list = [class_file.classFMD(name, path, study_name)]
        print("path 1: ", path)
        print("name 1: ", name)
        # in order to stop the code from crashing later, we will need to verify that these blocks are full
        # otherwise the code might assume they are full and try to access the vars later

    def retranslateUi(self, filescreen):
        _translate = QtCore.QCoreApplication.translate
        filescreen.setWindowTitle(_translate("filescreen", "MU Brachial Analyzer"))
        self.instructions.setText(_translate("filescreen", "Choose Files For Analysis"))
        self.back_btn1.setText(_translate("filescreen", "Back"))
        self.chooseFile_btn.setText(_translate("filescreen", "Choose File"))
        self.path_label.setText(_translate("filescreen", "File Path"))
        self.name_label.setText(_translate("filescreen", "Test Name"))
        self.study_label.setText(_translate("filescreen", "Study Name"))
        self.patient_label.setText(_translate("filescreen", "Patient Name"))
        self.run_btn.setText(_translate("filescreen", "RUN"))
        self.name1.setHtml(_translate("filescreen",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
