import sys

from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton, QFileDialog

from file_Screen import Ui_filescreen
from fmd_screen import Ui_Banalyzer
from start_page import Ui_start_screen
from excel_screen import Ui_excel_screen
from confidence_screen import Ui_confidence_screen
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
import sys


class mywindow(QMainWindow):

    #initiate the program
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_start_screen()
        self.ui.setupUi(self)
        self.ui.fmd_button.clicked.connect(self.ChooseFMD)

    #Go back to the main menu from the File screen
    def MainMenu(self):
        self.ui = Ui_start_screen()
        self.ui.setupUi(self)
        self.ui.fmd_button.clicked.connect(self.ChooseFMD)

    #Creates the FMD screen
    def ChooseFMD(self):
        self.ui = Ui_filescreen()
        self.ui.setupUi(self)
        self.ui.run_btn.clicked.connect(self.Run)
        self.ui.back_btn1.clicked.connect(self.MainMenu)

    #Moves to the run screen
    def Run(self):
        self.ui = Ui_Banalyzer()
        self.ui.setupUi(self)
        self.ui.back_btn.clicked.connect(self.ChooseFMD)
        self.ui.excel_btn.clicked.connect(self.ExcelScreen)
        self.ui.manual_btn.clicked.connect(self.Confidence)

    # Moves to Excel Screen
    def ExcelScreen(self):
        self.ui = Ui_excel_screen()
        self.ui.setupUi(self)
        self.ui.back_btn.clicked.connect(self.ChooseFMD)

    # Move to the Confidence Screen
    def Confidence(self):
        self.ui = Ui_confidence_screen()
        self.ui.setupUi(self)
        # self.ui.done_btn.clicked.connect(self.Run)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())