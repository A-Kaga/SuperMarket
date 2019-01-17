from PyQt5.QtWidgets import QApplication, QMainWindow
from QtUI.Ui_SaleSearchWindow import *


class SaleSearchWindow(QMainWindow, Ui_SaleSearchWindow):
    def __init__(self, parent=None):
        super(SaleSearchWindow, self).__init__(parent)
        self.setupUi(self)