# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\SuperMarket\QtUI\UI\FunctionWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginErrorWindow(object):
    def setupUi(self, LoginErrorWindow):
        LoginErrorWindow.setObjectName("LoginErrorWindow")
        LoginErrorWindow.resize(638, 451)
        self.textBrowser = QtWidgets.QTextBrowser(LoginErrorWindow)
        self.textBrowser.setGeometry(QtCore.QRect(190, 110, 251, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(LoginErrorWindow)
        self.pushButton.setGeometry(QtCore.QRect(270, 320, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(LoginErrorWindow)
        self.pushButton.clicked.connect(LoginErrorWindow.close)
        QtCore.QMetaObject.connectSlotsByName(LoginErrorWindow)

    def retranslateUi(self, LoginErrorWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginErrorWindow.setWindowTitle(_translate("LoginErrorWindow", "登录错误"))
        self.textBrowser.setHtml(_translate("LoginErrorWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">蠢驴</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">账号/密码错了</p></body></html>"))
        self.pushButton.setText(_translate("LoginErrorWindow", "行吧"))

