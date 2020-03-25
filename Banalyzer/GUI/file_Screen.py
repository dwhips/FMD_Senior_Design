# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget


class Ui_filescreen(QWidget):
    def setupUi(self, filescreen):

        self.filescreen = QtWidgets.QWidget()
        self.filescreen.setObjectName("filescreen")
        self.filescreen.setStyleSheet("background: rgb(177, 185, 199)")
        self.instructions = QtWidgets.QLabel(self.filescreen)
        self.instructions.setGeometry(QtCore.QRect(90, 60, 1500, 342))
        self.instructions.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.instructions.setFont(font)
        self.instructions.setObjectName("instructions")

        #First Column Label
        self.file_label = QtWidgets.QLabel(self.filescreen)
        self.file_label.setGeometry(QtCore.QRect(625, 350, 300, 200))
        self.file_label.setAlignment(Qt.AlignCenter)
        font.setPointSize(12)
        self.file_label.setFont(font)
        self.file_label.setObjectName("file_label")

        #Second Column Label
        self.name_label = QtWidgets.QLabel(self.filescreen)
        self.name_label.setGeometry(QtCore.QRect(225, 350, 300, 200))
        self.name_label.setAlignment(Qt.AlignCenter)
        font.setPointSize(12)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")

        self.run_btn = QtWidgets.QPushButton(self.filescreen)
        self.run_btn.setGeometry(QtCore.QRect(1200, 500, 442, 262))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.run_btn.setFont(font)
        self.run_btn.setStyleSheet("background: rgb(255, 255, 255)")
        self.run_btn.setObjectName("run_btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.filescreen)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 500, 350, 822))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_files = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_files.setContentsMargins(5, 0, 0, 0)
        self.layout_files.setObjectName("layout_files")
        self.file1_in_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.file1_in_2.setStyleSheet("background: rgb(255, 255, 255)")
        self.file1_in_2.setObjectName("file1_in_2")
        self.layout_files.addWidget(self.file1_in_2)
        self.file2_in = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.file2_in.setStyleSheet("background: rgb(255, 255, 255)")
        self.file2_in.setObjectName("file2_in")
        self.layout_files.addWidget(self.file2_in)
        self.file3_in = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.file3_in.setStyleSheet("background: rgb(255, 255, 255)")
        self.file3_in.setObjectName("file3_in")
        self.layout_files.addWidget(self.file3_in)
        self.file4_in = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.file4_in.setStyleSheet("background: rgb(255, 255, 255)\n"
"")
        self.file4_in.setObjectName("file4_in")
        self.layout_files.addWidget(self.file4_in)

        #section for the second column
        self.verticalLayoutWidget2 = QtWidgets.QWidget(self.filescreen)
        self.verticalLayoutWidget2.setGeometry(QtCore.QRect(600, 500, 350, 822))
        self.verticalLayoutWidget2.setObjectName("verticalLayoutWidget2")
        self.layout_names = QtWidgets.QVBoxLayout(self.verticalLayoutWidget2)
        self.layout_names.setContentsMargins(5, 0, 0, 0)
        self.layout_names.setObjectName("layout_names")
        self.name1_in = QtWidgets.QTextEdit(self.verticalLayoutWidget2)
        self.name1_in.setStyleSheet("background: rgb(255, 255, 255)")
        self.name1_in.setObjectName("name1_in")
        self.layout_names.addWidget(self.name1_in)
        self.name2_in = QtWidgets.QTextEdit(self.verticalLayoutWidget2)
        self.name2_in.setStyleSheet("background: rgb(255, 255, 255)")
        self.name2_in.setObjectName("name2_in")
        self.layout_names.addWidget(self.name2_in)
        self.name3_in = QtWidgets.QTextEdit(self.verticalLayoutWidget2)
        self.name3_in.setStyleSheet("background: rgb(255, 255, 255)")
        self.name3_in.setObjectName("name3_in")
        self.layout_names.addWidget(self.name3_in)
        self.name4_in = QtWidgets.QTextEdit(self.verticalLayoutWidget2)
        self.name4_in.setStyleSheet("background: rgb(255, 255, 255)\n"
                                    "")
        self.name4_in.setObjectName("name4_in")
        self.layout_names.addWidget(self.name4_in)

        filescreen.setCentralWidget(self.filescreen)

        self.retranslateUi(filescreen)
        QtCore.QMetaObject.connectSlotsByName(filescreen)

    def retranslateUi(self, filescreen):
        _translate = QtCore.QCoreApplication.translate
        filescreen.setWindowTitle(_translate("filescreen", "MU Brachial Analyzer"))
        self.instructions.setText(_translate("filescreen", "Choose Files For Analysis"))
        self.file_label.setText(_translate("filescreen", "File Path"))
        self.name_label.setText(_translate("filescreen", "File Name"))
        self.run_btn.setText(_translate("filescreen", "RUN"))
        self.file1_in_2.setHtml(_translate("filescreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
