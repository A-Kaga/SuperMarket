from PyQt5.QtWidgets import QApplication, QDialog
from QtUI.Ui_StockDialog import *


class StockDialog(QDialog, Ui_StockDialog):
    def __init__(self, parent=None):
        super(StockDialog, self).__init__(parent)
        self.setupUi(self)