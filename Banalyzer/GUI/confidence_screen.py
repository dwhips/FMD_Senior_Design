# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confidence_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QFileDialog, QDesktopWidget, QCheckBox
import cv2

import sys

sys.path.append('../')  # could be hacky
import Global.gbl_fmd_class_list as gbl_fmd
import FMD.FMDClass as class_file
import FMD.FMDProcessing as fmd_proc
import GUI.GUIHelper as GUI


class Ui_confidence_screen(QWidget):
    def setupUi(self, confidence_screen):
        # Get the size of the screen
        width = QDesktopWidget().screenGeometry(-1).width()
        height = QDesktopWidget().screenGeometry(-1).height()

        # width and height of the created window
        windowwidth = width / 2
        windowheight = height / 1.5

        # Create the confidence screen widget
        self.confidence_screen = QtWidgets.QWidget()
        self.confidence_screen.setObjectName("confidence_screen")
        self.confidence_screen.setStyleSheet("background: rgb(177,185,199)")

        # Cropped FMD Image
        self.crop_image = QtWidgets.QLabel(self.confidence_screen)
        self.crop_image.setGeometry(
            QtCore.QRect(windowwidth * 0.1, windowheight * 0.2, windowwidth * 0.55, windowheight * 0.5))
        self.crop_image.setAutoFillBackground(False)
        self.crop_image.setText("")
        self.crop_image.mousePressEvent = self.GetPos
        self.crop_image.setScaledContents(True)
        self.crop_image.setObjectName("crop_image")

        # Create the Scrolling List
        self.frame_list = QtWidgets.QListWidget(self.confidence_screen)
        self.frame_list.setGeometry(
            QtCore.QRect(windowwidth * 0.7, windowheight * 0.1, windowwidth * 0.25, windowheight * 0.7))
        self.frame_list.setStyleSheet("background:rgb(255, 255, 255)")
        self.frame_list.setObjectName("frame_list")
        framefile_list = self.SetListFrames()
        pix_frames_sorted = self.GetFailedFrames(framefile_list)
        self.frame_list.currentItemChanged.connect(lambda: self.ListClicked(pix_frames_sorted))

        # Make the threshold slider
        self.threshold_slider = QtWidgets.QSlider(self.confidence_screen)
        self.threshold_slider.setGeometry(
            QtCore.QRect(windowwidth * 0.1, windowheight * 0.85, windowwidth * 0.8, windowheight * 0.1))
        self.threshold_slider.setOrientation(QtCore.Qt.Horizontal)
        self.threshold_slider.setObjectName("threshold_slider")
        self.threshold_slider.setRange(0, 255)
        self.threshold_slider.valueChanged.connect(
            lambda: self.SliderChanged(pix_frames_sorted[self.frame_list.currentRow()]))

        # Create the screen title
        self.screen_title = QtWidgets.QLabel(self.confidence_screen)
        self.screen_title.setGeometry(
            QtCore.QRect(windowwidth * 0.1, windowheight * 0.05, windowwidth * 0.6, windowheight * 0.1))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.screen_title.setFont(font)
        self.screen_title.setAlignment(QtCore.Qt.AlignCenter)
        self.screen_title.setObjectName("screen_title")

        # Create the Accept Button
        self.accept_btn = QtWidgets.QPushButton(self.confidence_screen)
        self.accept_btn.setGeometry(
            QtCore.QRect(windowwidth * 0.2, windowheight * 0.7, windowwidth * 0.1, windowheight * 0.05))
        self.accept_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.accept_btn.setObjectName("accept_btn")

        # Discard Button
        self.discard_btn = QtWidgets.QPushButton(self.confidence_screen)
        self.discard_btn.setGeometry(
            QtCore.QRect(windowwidth * 0.4, windowheight * 0.7, windowwidth * 0.1, windowheight * 0.05))
        self.discard_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.discard_btn.setObjectName("discard_btn")

        # Create the Done Button
        self.done_btn = QtWidgets.QPushButton(self.confidence_screen)
        self.done_btn.setGeometry(
            QtCore.QRect(windowwidth * 0.88, windowheight * 0.93, windowwidth * 0.1, windowheight * 0.05))
        self.done_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.done_btn.setObjectName("done_btn")

        # Set the central widget
        confidence_screen.setCentralWidget(self.confidence_screen)

        self.retranslateUi(self.confidence_screen)
        QtCore.QMetaObject.connectSlotsByName(self.confidence_screen)

    # when list clicked, change to that index
    def ListClicked(self, pix_array):
        i = self.frame_list.currentRow()
        print(str(i))
        self.LoadFailedFrame(pix_array[i])

    # TODO later just have pix arr values stored in gbl class? too big?
    # gets pixvalues of failed frames
    def GetFailedFrames(self, ff_list):
        # get frames needed
        frames_sorted = fmd_proc.GetiFrameiFilePixels(ff_list)

        if len(frames_sorted) == 0:
            print("No diam values are unreasonable")
        else:  # update pixmap to index 0
            self.LoadFailedFrame(frames_sorted[0])
        return frames_sorted

    # updates the pixmap and processes it
    def LoadFailedFrame(self, pix_array):
        gbl_fmd.i_class = 0  # TODO make i_class equal to the class given by file
        fmd_proc.Populate(pix_array, self.crop_image, False)

    # gets user click position
    def GetPos(self, event):
        i_class = gbl_fmd.i_class
        # x = event.pos().x()
        x = event.x()
        y = event.y()
        gbl_fmd.class_list[i_class].UpdateXY(x, y)
        print(gbl_fmd.class_list[i_class].GetXY())

    # updates the processing with new thresholding once adjusted
    def SliderChanged(self, pix_array):
        # TODO make sure gblfmd is right
        i_class = gbl_fmd.i_class
        slider_val = self.threshold_slider.value()
        print(slider_val)
        gbl_fmd.class_list[i_class].threshold = ['binary', slider_val]
        # update the image to the current thresh
        self.LoadFailedFrame(pix_array)

    # gets the failed frames index and file index of conf level based on the flag and adds to list
    def SetListFrames(self):
        failed_i_file_arr = []
        failed_i_frame_arr = []
        for i_file in range(len(gbl_fmd.class_list)):
            frames_conf = gbl_fmd.class_list[i_file].percent_dif_flag
            file_name = gbl_fmd.class_list[i_file].test_name
            for i_frame in range(len(frames_conf)):
                if frames_conf[i_frame]:
                    failed_i_file_arr.append(i_file)
                    failed_i_frame_arr.append(i_frame)
                    list_name = "Frame: " + str(i_frame) + " " + file_name
                    list_widge = QtWidgets.QListWidgetItem('%s' % list_name)
                    list_widge.setBackground(QtGui.QColor('red'))
                    self.frame_list.addItem(list_widge)

        return [failed_i_file_arr, failed_i_frame_arr]

    def retranslateUi(self, confidence_screen):
        _translate = QtCore.QCoreApplication.translate
        confidence_screen.setWindowTitle(_translate("confidence_screen", "MU Brachial Analyzer"))
        __sortingEnabled = self.frame_list.isSortingEnabled()
        self.frame_list.setSortingEnabled(False)
        self.frame_list.setSortingEnabled(__sortingEnabled)
        self.screen_title.setText(_translate("confidence_screen", "Manual Frame Editor"))
        self.accept_btn.setText(_translate("confidence_screen", "Accept"))
        self.discard_btn.setText(_translate("confidence_screen", "Discard"))
        self.done_btn.setText(_translate("confidence_screen", "Done"))
