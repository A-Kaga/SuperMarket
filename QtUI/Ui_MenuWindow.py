# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\SuperMarket\QtUI\UI\MenuWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        MenuWindow.setObjectName("MenuWindow")
        MenuWindow.resize(800, 601)
        self.centralwidget = QtWidgets.QWidget(MenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.WareRegister_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.WareRegister_PushButton.setGeometry(QtCore.QRect(350, 170, 81, 81))
        self.WareRegister_PushButton.setObjectName("WareRegister_PushButton")
        self.PurchaseRegister_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.PurchaseRegister_PushButton.setGeometry(QtCore.QRect(240, 270, 81, 81))
        self.PurchaseRegister_PushButton.setObjectName("PurchaseRegister_PushButton")
        self.SaleRegister_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaleRegister_PushButton.setGeometry(QtCore.QRect(450, 270, 81, 81))
        self.SaleRegister_PushButton.setObjectName("SaleRegister_PushButton")
        self.StockSearch_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.StockSearch_PushButton.setGeometry(QtCore.QRect(450, 420, 81, 81))
        self.StockSearch_PushButton.setObjectName("StockSearch_PushButton")
        self.SaleSearch_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaleSearch_PushButton.setGeometry(QtCore.QRect(240, 420, 81, 81))
        self.SaleSearch_PushButton.setObjectName("SaleSearch_PushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 120, 821, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 801, 131))
        self.textBrowser.setObjectName("textBrowser")
        MenuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MenuWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MenuWindow)
        self.statusbar.setObjectName("statusbar")
        MenuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

    def retranslateUi(self, MenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MenuWindow.setWindowTitle(_translate("MenuWindow", "功能菜单"))
        self.WareRegister_PushButton.setText(_translate("MenuWindow", "商品注册"))
        self.PurchaseRegister_PushButton.setText(_translate("MenuWindow", "进货登记"))
        self.SaleRegister_PushButton.setText(_translate("MenuWindow", "销货登记"))
        self.StockSearch_PushButton.setText(_translate("MenuWindow", "库存查询"))
        self.SaleSearch_PushButton.setText(_translate("MenuWindow", "销售查询"))
        self.textBrowser.setHtml(_translate("MenuWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">欢迎使用SG集团供销存管理系统</span></p></body></html>"))

