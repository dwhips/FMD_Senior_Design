# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brachial_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Banalyzer(object):
    def setupUi(self, Banalyzer):
        Banalyzer.setObjectName("Banalyzer")
        Banalyzer.resize(800, 600)
        Banalyzer.setAutoFillBackground(False)
        Banalyzer.setStyleSheet("background:rgb(177, 185, 199)")
        self.main_screen = QtWidgets.QWidget(Banalyzer)
        self.main_screen.setObjectName("main_screen")
        self.layout = QtWidgets.QStackedWidget(self.main_screen)
        self.layout.setGeometry(QtCore.QRect(30, 20, 721, 511))
        self.layout.setObjectName("layout")
        self.start_page = QtWidgets.QWidget()
        self.start_page.setObjectName("start_page")
        self.layout.addWidget(self.start_page)
        self.fmd_screen = QtWidgets.QWidget()
        self.fmd_screen.setObjectName("fmd_screen")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.fmd_screen)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(520, 100, 160, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.buttons = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.buttons.setContentsMargins(0, 0, 0, 0)
        self.buttons.setObjectName("buttons")
        self.accept_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.accept_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.accept_btn.setObjectName("accept_btn")
        self.buttons.addWidget(self.accept_btn)
        self.retry_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.retry_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.retry_btn.setObjectName("retry_btn")
        self.buttons.addWidget(self.retry_btn)
        self.manual_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.manual_btn.setStyleSheet("background:rgb(255, 255, 255)")
        self.manual_btn.setObjectName("manual_btn")
        self.buttons.addWidget(self.manual_btn)
        self.crop_image = QtWidgets.QLabel(self.fmd_screen)
        self.crop_image.setGeometry(QtCore.QRect(60, 120, 411, 321))
        self.crop_image.setAutoFillBackground(False)
        self.crop_image.setText("")
        self.crop_image.setPixmap(QtGui.QPixmap("frame0.jpg"))
        self.crop_image.setScaledContents(False)
        self.crop_image.setObjectName("crop_image")
        self.pushButton = QtWidgets.QPushButton(self.fmd_screen)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 62, 19))
        self.pushButton.setStyleSheet("background:rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.layout.addWidget(self.fmd_screen)
        Banalyzer.setCentralWidget(self.main_screen)

        self.retranslateUi(Banalyzer)
        self.layout.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Banalyzer)

    def retranslateUi(self, Banalyzer):
        _translate = QtCore.QCoreApplication.translate
        Banalyzer.setWindowTitle(_translate("Banalyzer", "MU Brachial Analyzer"))
        self.accept_btn.setText(_translate("Banalyzer", "Acceptable"))
        self.retry_btn.setText(_translate("Banalyzer", "Retry"))
        self.manual_btn.setText(_translate("Banalyzer", "Manual"))
        self.pushButton.setText(_translate("Banalyzer", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Banalyzer()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
