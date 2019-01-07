from PyQt5.QtWidgets import QApplication, QMainWindow
from QtUI.Ui_SaleRegisterWindow import *


class SaleRegisterWindow(QMainWindow, Ui_SaleRegisterWindow):
    def __init__(self, parent=None):
        super(SaleRegisterWindow, self).__init__(parent)
        self.setupUi(self)