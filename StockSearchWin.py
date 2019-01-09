from PyQt5.QtWidgets import QApplication, QMainWindow
from QtUI.Ui_StockSearchWindow import *


class StockSearchWindow(QMainWindow, Ui_StockSearchWindow):
    def __init__(self, parent=None):
        super(StockSearchWindow, self).__init__(parent)
        self.setupUi(self)