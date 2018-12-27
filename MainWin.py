import sys
import function
import pymysql
# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from QtUI.Ui_MainWindow import Ui_MainWindow

import QtUI.Ui_LoginWindow
import QtUI.Ui_LoginErrorWindow

import LoginWin
import LoginErrorWin
import MenuWin
import WareRegisterWin

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.login = LoginWin.LoginWindow() # 登录界面
        self.login_error = LoginErrorWin.LoginErrorWindow() # 账号密码不匹配提示界面
        self.menu = MenuWin.MenuWindow()  # 功能界面
        self.wareRegister = WareRegisterWin.WareRegisterWindow() #商品信息注册界面

        self.Login_PushButton.clicked.connect(self.login.show)
        self.Login_PushButton.clicked.connect(self.close)
        self.login.Login_PushButton_Submit.clicked.connect(self.LoginCheck)
        self.menu.WareRegister_PushButton.clicked.connect(self.wareRegister.show)

    def LoginCheck(self):
    # 检查登录信息
        user_name = self.login.Login_LineEdit_UserName.text()
        password = self.login.Login_LineEdit_Password.text()

        db = function.connect_database()
        cursor = db.cursor()
        check_sql = 'SELECT PASSWORD FROM ADMIN WHERE ID=%s'
        cursor.execute(check_sql, user_name)
        result = cursor.fetchone()
    # 这里有问题：
    # 如果账号不在数据库内，会跳 TypeError: 'NoneType' object is not subscriptable
        if str(result[0]) == str(password):
            self.menu.show()
            self.login.close()
        else:
            self.login_error.show()
            self.login.Login_LineEdit_UserName.clear()
            self.login.Login_LineEdit_Password.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = MainWindow()
    Main.show()
    sys.exit(app.exec_())