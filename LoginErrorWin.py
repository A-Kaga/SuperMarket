# import sys
from PyQt5.QtWidgets import QApplication, QDialog
from QtUI.Ui_LoginErrorWindow import *

'''
Login Account
Id = AKaga
Password = 123456
'''

class LoginErrorWindow(QDialog, Ui_LoginErrorWindow):
    def __init__(self, parent=None):
        super(LoginErrorWindow, self).__init__(parent)
        self.setupUi(self)
    
    '''
    def ShowWin(self):
        app = QApplication(sys.argv)
        LoginError = self.ErrorWindow()
        LoginError.show()
        sys.exit(app.exec_())
    '''

'''
def ShwoWin():
    LoginError = ErrorWindow()
    LoginError.show()
    # sys.exit(app.exec_())
'''

'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    LoginError = ErrorWindow()
    LoginError.show()
    sys.exit(app.exec_())
'''