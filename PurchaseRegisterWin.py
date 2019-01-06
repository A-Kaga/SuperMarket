from PyQt5.QtWidgets import QApplication, QMainWindow
from QtUI.Ui_PurchaseRegisterWindow import *


class PurchaseRegisterWindow(QMainWindow, Ui_PurchaseRegisterWindow):
    def __init__(self, parent=None):
        super(PurchaseRegisterWindow, self).__init__(parent)
        self.setupUi(self)