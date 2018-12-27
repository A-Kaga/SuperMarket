from PyQt5.QtWidgets import QApplication, QMainWindow
from QtUI.Ui_WareRegisterWindow import *


class WareRegisterWindow(QMainWindow, Ui_WareRegisterWindow):
    def __init__(self, parent=None):
        super(WareRegisterWindow, self).__init__(parent)
        self.setupUi(self)