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
        self.wareRegister = WareRegisterWin.WareRegisterWindow()  #商品信息注册界面
        
        '''
        注意！！！
        这里跳过了登录操作
        上线前记得修改！！！

        把menu.show()改成LoginCheck
        '''

        self.Login_PushButton.clicked.connect(self.menu.show)
        self.Login_PushButton.clicked.connect(self.close)
        
        self.login.Login_PushButton_Submit.clicked.connect(self.LoginCheck)
        self.menu.WareRegister_PushButton.clicked.connect(self.wareRegister.show)

        self.wareRegister.Clear_PushButton.clicked.connect(self.Register_DataClear)
        self.wareRegister.Submit_PushButton.clicked.connect(self.Register_Action)


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

    def Register_DataClear(self):
        self.wareRegister.Name_LineEdit.clear()
        self.wareRegister.ID_LineEdit.clear()
        self.wareRegister.Format_LineEdit.clear()
        self.wareRegister.Quantity_SpinBox.clear()
        self.wareRegister.PurchasePrice_LineEdit.clear()
        self.wareRegister.SellPrice_LineEdit.clear()
        self.wareRegister.MaxStock_SpinBox.clear()
        self.wareRegister.MinStock_SpinBox.clear()

    def Register_Action(self):
        ware_data = []
        ware_data.append(self.wareRegister.Name_LineEdit.text())
        ware_data.append(int(self.wareRegister.ID_LineEdit.text()))
        ware_data.append(int(self.wareRegister.Format_LineEdit.text()))
        ware_data.append(int(self.wareRegister.Quantity_SpinBox.text()))
        ware_data.append(int(self.wareRegister.PurchasePrice_LineEdit.text()))
        ware_data.append(int(self.wareRegister.SellPrice_LineEdit.text()))
        ware_data.append(int(self.wareRegister.MaxStock_SpinBox.text()))
        ware_data.append(int(self.wareRegister.MinStock_SpinBox.text()))

        insert_sql = """INSERT INTO ware_data
                     (name, ware_id, format, quantity, purchase_price, sell_price, max_stock, min_stock) 
                     VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
        db = function.connect_database()
        cursor = db.cursor()
        while True:
            try:
                cursor.execute(insert_sql, ware_data)
            except Exception as e:
                print(e)
                db.rollback()
                self.Register_DataClear()
                break
            else:
                db.commit()
                break
        cursor.close()
        db.close()
        '''
        下一步：
        完善商品注册功能
        创建错误提示（重复id，商品信息不完全，商品数据格式错误balabala）窗口
        创建录入成功窗口
        '''
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = MainWindow()
    Main.show()
    sys.exit(app.exec_())