# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_screen.ui'
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
        self.name1.setStyleSheet("background: rgb(0, 204, 102)")
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
        self.name4.setStyleSheet("background: rgb(255, 255, 255)")
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
        self.path1.setStyleSheet("background: rgb(0, 204, 102)")
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
        self.path4.setStyleSheet("background: rgb(255, 255, 255)")
        self.path4.setObjectName("path4")
        self.layout_paths.addWidget(self.path4)

        # Create the baseline checkboxes
        baseline_checkbox1 = QCheckBox("Baseline", self.filescreen)
        baseline_checkbox1.move(windowwidth*0.4, windowheight*0.35)
        baseline_checkbox1.resize(windowwidth*0.08, windowheight*0.05)

        baseline_checkbox2 = QCheckBox("Baseline", self.filescreen)
        baseline_checkbox2.move(windowwidth*0.4, windowheight*0.5)
        baseline_checkbox2.resize(windowwidth*0.08, windowheight*0.05)

        baseline_checkbox3 = QCheckBox("Baseline", self.filescreen)
        baseline_checkbox3.move(windowwidth*0.4, windowheight*0.65)
        baseline_checkbox3.resize(windowwidth*0.08, windowheight*0.05)

        baseline_checkbox4 = QCheckBox("Baseline", self.filescreen)
        baseline_checkbox4.move(windowwidth*0.4, windowheight*0.8)
        baseline_checkbox4.resize(windowwidth*0.08, windowheight*0.05)


        # link to FIleIndexCLick when user clicks on name or file path textbox. Indicates the block currently selected
        self.name1.mousePressEvent = lambda x: self.FileIndexClick(1)
        self.name2.mousePressEvent = lambda x: self.FileIndexClick(2)
        self.name3.mousePressEvent = lambda x: self.FileIndexClick(3)
        self.name4.mousePressEvent = lambda x: self.FileIndexClick(4)
        self.path1.mousePressEvent = lambda x: self.FileIndexClick(1)
        self.path2.mousePressEvent = lambda x: self.FileIndexClick(2)
        self.path3.mousePressEvent = lambda x: self.FileIndexClick(3)
        self.path4.mousePressEvent = lambda x: self.FileIndexClick(4)

        self.FileIndexClick(1)


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

    # BETTER NAME!!! this updates the row color and the global index for selecting files 1-4
    def FileIndexClick(self, i_file):
        # reset path text background color
        self.path1.setStyleSheet("background: rgb(255, 255, 255)")
        self.path2.setStyleSheet("background: rgb(255, 255, 255)")
        self.path3.setStyleSheet("background: rgb(255, 255, 255)")
        self.path4.setStyleSheet("background: rgb(255, 255, 255)")
        # reset name text background color
        self.name1.setStyleSheet("background: rgb(255, 255, 255)")
        self.name2.setStyleSheet("background: rgb(255, 255, 255)")
        self.name3.setStyleSheet("background: rgb(255, 255, 255)")
        self.name4.setStyleSheet("background: rgb(255, 255, 255)")

        # no cases in python, so if else
        # change selected blocks to green
        if i_file == 1:
            self.name1.setStyleSheet("background: rgb(0, 204, 102)")
            self.path1.setStyleSheet("background: rgb(0, 204, 102)")
            self.i_file_selected = 1
        elif i_file == 2:
            self.name2.setStyleSheet("background: rgb(0, 204, 102)")
            self.path2.setStyleSheet("background: rgb(0, 204, 102)")
            self.i_file_selected = 2
        elif i_file == 3:
            self.name3.setStyleSheet("background: rgb(0, 204, 102)")
            self.path3.setStyleSheet("background: rgb(0, 204, 102)")
            self.i_file_selected = 3
        elif i_file == 4:
            self.name4.setStyleSheet("background: rgb(0, 204, 102)")
            self.path4.setStyleSheet("background: rgb(0, 204, 102)")
            self.i_file_selected = 4
        else:
            x = 0
            print("FileIndexClick edge case reached")
            # file number should be impossible. its not supported

    # opens up file browser and adds it to text box
    def ChooseFile(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open File')
        file_path = file_path[0]
        # TODO get the file to verify its open
        if self.i_file_selected == 1:
            self.path1.setText(file_path)
        elif self.i_file_selected == 2:
            self.path2.setText(file_path)
        elif self.i_file_selected == 3:
            self.path3.setText(file_path)
        elif self.i_file_selected == 4:
            self.path4.setText(file_path)
        else:
            print("Reach choose file edge case")

    def SaveFileData(self):
        # file and name need new var names. do path and name instead
        study_name = self.study.toPlainText()
        patient_name = self.patient.toPlainText()

        path1 = self.path1.toPlainText()
        path2 = self.path2.toPlainText()
        path3 = self.path3.toPlainText()
        path4 = self.path4.toPlainText()

        list = []
        # TODO if path is not empty but study is, prompt user to fill it in (red text)
        if path1 != "" :
            name = self.name1.toPlainText()
            list.append(class_file.classFMD(name, path1, study_name, patient_name))
        if path2 != "":
            name = self.name2.toPlainText()
            list.append(class_file.classFMD(name, path2, study_name, patient_name))
        if path3 != "":
            name = self.name3.toPlainText()
            list.append(class_file.classFMD(name, path3, study_name, patient_name))
        if path4 != "":
            name = self.name4.toPlainText()
            list.append(class_file.classFMD(name, path4, study_name, patient_name))
        gbl_fmd.class_list = list
        gbl_fmd.i_class = 0

    def retranslateUi(self, filescreen):
        _translate = QtCore.QCoreApplication.translate
        filescreen.setWindowTitle(_translate("filescreen", "MU Brachial Analyzer"))
        self.instructions.setText(_translate("filescreen", "Choose Files For Analysis"))
        self.back_btn1.setText(_translate("filescreen", "Back"))
        self.chooseFile_btn.setText(_translate("filescreen", "Choose File"))
        self.path_label.setText(_translate("filescreen", "File Path"))
        self.name_label.setText(_translate("filescreen", "Test Name"))
        self.study_label.setText(_translate("filescreen", "Study Name"))
        self.patient_label.setText(_translate("filescreen", "Patient ID"))
        self.run_btn.setText(_translate("filescreen", "RUN"))
        self.name1.setHtml(_translate("filescreen",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
