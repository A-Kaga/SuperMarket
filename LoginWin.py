import sys
import function
from PyQt5.QtWidgets import QApplication, QMainWindow
from QtUI.Ui_LoginWindow import *

import LoginErrorWin

'''
Login Account
Id = AKaga
Password = 123456
'''

class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)

        # self.Login_PushButton_Submit.clicked.connect(self.password_check)
'''  
    def password_check(self):
        user_name = self.Login_LineEdit_UserName.text()
        password = self.Login_LineEdit_Password.text()

        db = function.connect_database()
        cursor = db.cursor()
        check_sql = 'SELECT PASSWORD FROM ADMIN WHERE ID=%s'
        cursor.execute(check_sql, user_name)

        result = cursor.fetchone()
        if str(result[0]) == str(password):
            self.close()
        else:
            FunctionWin.ShwoWin()
            self.Login_LineEdit_UserName.clear()
            self.Login_LineEdit_Password.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = LoginWindow()
    Login.show()
    Login.Login_PushButton_Submit.clicked.connect(Login.password_check)
    sys.exit(app.exec_())
'''