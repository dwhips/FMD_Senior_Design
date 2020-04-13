# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brachial_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.QtWidgets import QDesktopWidget

import GUI.GUIHelper as GUIHelper

import sys
sys.path.append('../')  # could be hacky
import Global.gbl_fmd_class_list as gbl_fmd
import FMD.FMDClass as class_file
import FMD.FMDProcessing as fmd_proc


# might need to edge case checks, so maybe breakout into a function?
# do Restart_iClass?
gbl_fmd.i_class = 0

class Ui_Banalyzer(QWidget):
    def setupUi(self, Banalyzer):
        # Get the size of the screen
        width = QDesktopWidget().screenGeometry(-1).width()
        height = QDesktopWidget().screenGeometry(-1).height()

        # Get the width and height of the window
        windowwidth = width / 2
        windowheight = height / 1.5

        # Create the FMD Screen widget
        Banalyzer.setObjectName("Banalyzer")
        Banalyzer.setAutoFillBackground(True)
        Banalyzer.setStyleSheet("background:rgb(177, 185, 199)")
        self.main_screen = QtWidgets.QWidget(Banalyzer)
        self.main_screen.setObjectName("main_screen")
        self.fmd_screen = QtWidgets.QWidget()
        self.fmd_screen.setObjectName("fmd_screen")

        # Create the layout for the buttons
        self.verticalLayoutWidget = QtWidgets.QWidget(self.fmd_screen)
        self.verticalLayoutWidget.setGeometry(
            QtCore.QRect(windowwidth * 0.75, windowheight * 0.2, windowwidth * 0.2, windowheight * 0.5))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.buttons = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.buttons.setContentsMargins(0, 0, 0, 0)
        self.buttons.setObjectName("buttons")

        # gives test name and other info about current frame/selection process
        # Create the welcome message
        self.title = QtWidgets.QLabel(self.fmd_screen)
        self.title.setGeometry(
            QtCore.QRect(windowwidth * 0.1, windowheight * 0.1, windowwidth * 0.8, windowheight / 7))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setScaledContents(True)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        # accept button (verifies users measure)
        self.accept_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.accept_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.accept_btn.setObjectName("accept_btn")
        self.accept_btn.clicked.connect(lambda: fmd_proc.PerformFMD(gbl_fmd.class_list[-1].file_path,
                                                                    self.crop_image))
        self.accept_btn.clicked.connect(self.UpdateTitle)

        self.buttons.addWidget(self.accept_btn)

        # Retry Button
        self.retry_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.retry_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.retry_btn.setObjectName("retry_btn")
        self.buttons.addWidget(self.retry_btn)

        # Manual select button
        self.manual_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.manual_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.manual_btn.setObjectName("manual_btn")
        self.buttons.addWidget(self.manual_btn)

        # Cropped FMD Image
        self.crop_image = QtWidgets.QLabel(self.fmd_screen)
        self.crop_image.setGeometry(
            QtCore.QRect(windowwidth * 0.1, windowheight * 0.2, windowwidth * 0.55, windowheight * 0.5))
        self.crop_image.setAutoFillBackground(False)
        self.crop_image.setText("")
        # setting it below is replaced by SetFirstFrame
        # self.crop_image.setPixmap(QtGui.QPixmap("frame0.jpg"))
        # self.crop_image.setPixmap(QtGui.QPixmap(gbl_fmd.class_list[-1].file_path))  # !!!!!!!
        self.crop_image.mousePressEvent = self.GetPos  # !!!!!!!!!!!!!
        self.crop_image.setScaledContents(True)
        self.crop_image.setObjectName("crop_image")
        # for pixel dimensions
        image_width = self.crop_image.frameGeometry().width()
        image_height = self.crop_image.frameGeometry().height()
        gbl_fmd.class_list[-1].SetWidgetSize(image_width, image_height)
        fmd_proc.SetFirstFrame(gbl_fmd.class_list[-1].file_path, self.crop_image)

        # Back Button
        self.back_btn = QtWidgets.QPushButton(self.fmd_screen)
        self.back_btn.setGeometry(
            QtCore.QRect(windowwidth * 0.01, windowheight * 0.01, windowwidth * 0.05, windowheight * 0.03))
        self.back_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.back_btn.setObjectName("pushButton")

        # Set the central widget
        Banalyzer.setCentralWidget(self.fmd_screen)

        # runtime updates
        self.retranslateUi(Banalyzer)
        QtCore.QMetaObject.connectSlotsByName(Banalyzer)
        self.UpdateTitle()

    def UpdateTitle(self):
        index = str(0)
        title_string = gbl_fmd.class_list[-1].test_name+" ("+index+"/"+str(len(gbl_fmd.class_list))+")"
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("start_screen", title_string))

    # i dont want this here. I need to break it out
    # THIS SHIT DONT WORK
    def GetPos(self, event):
        # x = event.pos().x()
        x = event.x()
        y = event.y()
        gbl_fmd.class_list[-1].UpdateXY(x, y)
        print(gbl_fmd.class_list[-1].GetXY())
        color = (0, 255, 0)
        GUIHelper.AddPixmapCircle(self.crop_image, gbl_fmd.class_list[-1].GetXY(), color)
        paint = QtGui.QPainter(self.crop_image.pixmap())
        paint.setPen(QtGui.QColor(color[0], color[1], color[2]))
        paint.drawPoint(x, y)
        self.crop_image.repaint()
        print("Testing class xy in brachial_ui: ", gbl_fmd.class_list[-1].CheckXY())
        fmd_proc.VerifyFrame1(gbl_fmd.class_list[-1].file_path, self.crop_image)
        print("GetPos crashing here?")

    def retranslateUi(self, Banalyzer):
        _translate = QtCore.QCoreApplication.translate
        Banalyzer.setWindowTitle(_translate("Banalyzer", "MU Brachial Analyzer"))
        self.accept_btn.setText(_translate("Banalyzer", "Acceptable"))
        self.retry_btn.setText(_translate("Banalyzer", "Retry"))
        self.manual_btn.setText(_translate("Banalyzer", "Manual"))
        self.back_btn.setText(_translate("Banalyzer", "Back"))
        # self.title.setText(_translate("start_screen", "Study info"))
