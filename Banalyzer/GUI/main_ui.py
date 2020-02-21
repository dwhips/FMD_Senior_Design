import sys

from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton

from b_ui2 import Ui_Banalyzer
from start_page import Ui_start_screen
from PyQt5 import QtWidgets
import sys


class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_start_screen()
        self.ui.setupUi(self)
        self.ui.fmd_button.clicked.connect(self.ChooseFMD)

    def ChooseFMD(self):
        self.ui = Ui_Banalyzer()
        self.ui.setupUi(self)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())