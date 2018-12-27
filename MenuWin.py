from PyQt5.QtWidgets import QApplication, QMainWindow
from QtUI.Ui_MenuWindow import *


class MenuWindow(QMainWindow, Ui_MenuWindow):
    def __init__(self, parent=None):
        super(MenuWindow, self).__init__(parent)
        self.setupUi(self)