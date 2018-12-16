# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\SuperMarket\QtUI\LoginWindow_test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Login_PushButton_Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Login_PushButton_Submit.setGeometry(QtCore.QRect(300, 370, 141, 51))
        self.Login_PushButton_Submit.setObjectName("Login_PushButton_Submit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(150, 50, 481, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 220, 361, 91))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Login_Label_UserName = QtWidgets.QLabel(self.widget)
        self.Login_Label_UserName.setObjectName("Login_Label_UserName")
        self.gridLayout.addWidget(self.Login_Label_UserName, 0, 0, 1, 1)
        self.Login_LineEdit_UserName = QtWidgets.QLineEdit(self.widget)
        self.Login_LineEdit_UserName.setObjectName("Login_LineEdit_UserName")
        self.gridLayout.addWidget(self.Login_LineEdit_UserName, 0, 1, 1, 1)
        self.Login_Label_Password = QtWidgets.QLabel(self.widget)
        self.Login_Label_Password.setObjectName("Login_Label_Password")
        self.gridLayout.addWidget(self.Login_Label_Password, 1, 0, 1, 1)
        self.Login_LineEdit_Password = QtWidgets.QLineEdit(self.widget)
        self.Login_LineEdit_Password.setObjectName("Login_LineEdit_Password")
        self.gridLayout.addWidget(self.Login_LineEdit_Password, 1, 1, 1, 1)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuSuperMarket_Management_System = QtWidgets.QMenu(self.menubar)
        self.menuSuperMarket_Management_System.setObjectName("menuSuperMarket_Management_System")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSuperMarket_Management_System.menuAction())

        self.retranslateUi(LoginWindow)
        self.Login_PushButton_Submit.clicked.connect(LoginWindow.close)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)
        LoginWindow.setTabOrder(self.Login_LineEdit_UserName, self.Login_LineEdit_Password)
        LoginWindow.setTabOrder(self.Login_LineEdit_Password, self.Login_PushButton_Submit)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.Login_PushButton_Submit.setText(_translate("LoginWindow", "提交"))
        self.textBrowser.setHtml(_translate("LoginWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">SuperMarket Management System</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Login</span></p></body></html>"))
        self.Login_Label_UserName.setText(_translate("LoginWindow", "用户名"))
        self.Login_Label_Password.setText(_translate("LoginWindow", "密  码"))
        self.menuSuperMarket_Management_System.setTitle(_translate("LoginWindow", "SuperMarket Management System"))

