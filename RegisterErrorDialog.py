from PyQt5.QtWidgets import QApplication, QDialog
from QtUI.Ui_RegisterErrorDialog import *


class RegisterErrorDialog(QDialog, Ui_RegisterErrorDialog):
    def __init__(self, parent=None):
        super(RegisterErrorDialog, self).__init__(parent)
        self.setupUi(self)