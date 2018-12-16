import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from QtUI.Ui_LoginWindow_test import *

class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = LoginWindow()
    Login.show()
    sys.exit(app.exec_())
