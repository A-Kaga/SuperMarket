from PyQt5.QtWidgets import QApplication, QDialog
from QtUI.Ui_ErrorDialog import *


class ErrorDialog(QDialog, Ui_ErrorDialog):
    def __init__(self, parent=None):
        super(ErrorDialog, self).__init__(parent)
        self.setupUi(self)