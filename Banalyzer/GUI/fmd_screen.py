# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brachial_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.QtWidgets import QDesktopWidget, QSlider

import GUI.GUIHelper as GUIHelper

import sys
sys.path.append('../')  # could be hacky
import Global.gbl_fmd_class_list as gbl_fmd
import FMD.FMDClass as class_file
import FMD.FMDProcessing as fmd_proc

# might need to edge case checks, so maybe breakout into a function?
# do Restart_iClass?

class Ui_Banalyzer(QWidget):
    def setupUi(self, Banalyzer):
        i_class = gbl_fmd.i_class
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
        # if the user is still verifying the files, this will just switch to the first frame of the next file
        self.accept_btn.clicked.connect(lambda: fmd_proc.PerformFMD(gbl_fmd.class_list[i_class].file_path,
                                                                    self.crop_image))
        self.accept_btn.clicked.connect(self.UpdateTitle)

        self.buttons.addWidget(self.accept_btn)

        # Retry Button
        self.excel_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.excel_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.excel_btn.setObjectName("excel_btn")
        self.buttons.addWidget(self.excel_btn)

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
        # self.crop_image.setPixmap(QtGui.QPixmap(gbl_fmd.class_list[i_class].file_path))  # !!!!!!!
        # TODO might need a lock to make sure the current i_class isnt already verified
        self.crop_image.mousePressEvent = self.GetPos  # !!!!!!!!!!!!!
        self.crop_image.setScaledContents(True)
        self.crop_image.setObjectName("crop_image")
        # for pixel dimensions
        image_width = self.crop_image.frameGeometry().width()
        image_height = self.crop_image.frameGeometry().height()
        gbl_fmd.class_list[i_class].SetWidgetSize(image_width, image_height)
        # update the crop image to the first frame of the first inputted file
        fmd_proc.SetFirstFrame(gbl_fmd.class_list[i_class].file_path, self.crop_image)

        # Back Button
        self.back_btn = QtWidgets.QPushButton(self.fmd_screen)
        self.back_btn.setGeometry(
            QtCore.QRect(windowwidth * 0.01, windowheight * 0.01, windowwidth * 0.05, windowheight * 0.03))
        self.back_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.back_btn.setObjectName("pushButton")

        # Threshold slider
        self.thresh_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.fmd_screen)
        self.thresh_slider.setGeometry(
            QtCore.QRect(windowwidth * 0.1, windowheight * 0.85, windowwidth * 0.8, windowheight * 0.1))
        self.thresh_slider.setRange(0, 255)
        self.thresh_slider.valueChanged.connect(self.SliderChanged)

        # Measure Width slider
        self.area_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.fmd_screen)
        self.area_slider.setGeometry(
            QtCore.QRect(windowwidth * 0.1, windowheight * 0.75, windowwidth * 0.4, windowheight * 0.1))
        self.area_slider.setRange(0, 100)
        self.area_slider.valueChanged.connect(self.AreaSliderChanged)

        # Set the central widget
        Banalyzer.setCentralWidget(self.fmd_screen)

        # runtime updates
        self.retranslateUi(Banalyzer)
        QtCore.QMetaObject.connectSlotsByName(Banalyzer)
        self.UpdateTitle()

    def UpdateTitle(self):
        i_class = gbl_fmd.i_class

        g = gbl_fmd.class_list
        # have raceondition in PerformFMD
        if i_class >= len(gbl_fmd.class_list):
            i_class = 0

        index = str(gbl_fmd.i_class+1)
        title_string = gbl_fmd.class_list[i_class].test_name+" ("+ index +"/"+str(len(gbl_fmd.class_list))+")"
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("start_screen", title_string))

    # i dont want this here. I need to break it out
    # THIS SHIT DONT WORK
    def GetPos(self, event):
        i_class = gbl_fmd.i_class
        # x = event.pos().x()
        x = event.x()
        y = event.y()
        gbl_fmd.class_list[i_class].UpdateXY(x, y)
        print(gbl_fmd.class_list[i_class].GetXY())
        # color = (0, 255, 0)
        # GUIHelper.AddPixmapCircle(self.crop_image, gbl_fmd.class_list[i_class].GetXY(), color)
        # paint = QtGui.QPainter(self.crop_image.pixmap())
        # paint.setPen(QtGui.QColor(color[0], color[1], color[2]))
        # paint.drawPoint(x, y)
        # maybe repaint collision?
        # self.crop_image.repaint()
        print("Testing class xy in brachial_ui: ", gbl_fmd.class_list[i_class].CheckXY())
        fmd_proc.VerifyFrame1(gbl_fmd.class_list[i_class].file_path, self.crop_image)
        print("GetPos crashing here?")

    def SliderChanged(self):
        i_class = gbl_fmd.i_class
        slider_val = self.thresh_slider.value()
        print(slider_val)
        gbl_fmd.class_list[i_class].threshold = ['binary', slider_val]
        # update the image to the current thresh
        fmd_proc.VerifyFrame1(gbl_fmd.class_list[i_class].file_path, self.crop_image)

    def AreaSliderChanged(self):
        i_class = gbl_fmd.i_class
        slider_val = self.area_slider.value()
        print(slider_val)
        gbl_fmd.class_list[i_class].artery_slider_width = slider_val

        # update the global bounds (x)
        widge_width = gbl_fmd.class_list[i_class].opencv_widge_size[0]
        left_bound = 0 + slider_val
        right_bound = widge_width - slider_val
        gbl_fmd.class_list[i_class].artery_slider_coord = [left_bound, right_bound]

        # update user image
        fmd_proc.VerifyFrame1(gbl_fmd.class_list[i_class].file_path, self.crop_image)

    def retranslateUi(self, Banalyzer):
        _translate = QtCore.QCoreApplication.translate
        Banalyzer.setWindowTitle(_translate("Banalyzer", "MU Brachial Analyzer"))
        self.accept_btn.setText(_translate("Banalyzer", "Acceptable"))
        self.excel_btn.setText(_translate("Banalyzer", "Save To Excel"))
        self.manual_btn.setText(_translate("Banalyzer", "Manual"))
        self.back_btn.setText(_translate("Banalyzer", "Back"))
        # self.title.setText(_translate("start_screen", "Study info"))
