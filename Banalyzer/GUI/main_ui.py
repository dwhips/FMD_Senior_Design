import sys

from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton, QFileDialog

from file_Screen import Ui_filescreen
from fmd_screen import Ui_Banalyzer
from start_page import Ui_start_screen
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
import sys


class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_start_screen()
        self.ui.setupUi(self)
        self.ui.fmd_button.clicked.connect(self.ChooseFMD)

    def MainMenu(self):
        self.ui = Ui_start_screen()
        self.ui.setupUi(self)
        self.ui.fmd_button.clicked.connect(self.ChooseFMD)

    def ChooseFMD(self):
        self.ui = Ui_filescreen()
        self.ui.setupUi(self)
        self.ui.run_btn.clicked.connect(self.Run)
        self.ui.back_btn1.clicked.connect(self.MainMenu)
        self.ui.chooseFile_btn.clicked.connect(self.ChooseFile)

    def ChooseFile(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')
        #self.ui.name1_in.setText(name)

    def Run(self):
        self.ui = Ui_Banalyzer()
        self.ui.setupUi(self)
        self.ui.back_btn.clicked.connect(self.ChooseFMD)


app = QtWidgets.QApplication([])
application = mywindow()
#application.showMaximized()
application.show()
sys.exit(app.exec())