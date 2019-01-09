# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\SuperMarket\QtUI\UI\StockSearch.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StockSearchWindow(object):
    def setupUi(self, StockSearchWindow):
        StockSearchWindow.setObjectName("StockSearchWindow")
        StockSearchWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(StockSearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 801, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(180, 290, 441, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.WareID_Label = QtWidgets.QLabel(self.widget)
        self.WareID_Label.setObjectName("WareID_Label")
        self.horizontalLayout.addWidget(self.WareID_Label)
        self.WareID_LineEdit = QtWidgets.QLineEdit(self.widget)
        self.WareID_LineEdit.setObjectName("WareID_LineEdit")
        self.horizontalLayout.addWidget(self.WareID_LineEdit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        StockSearchWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StockSearchWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        StockSearchWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StockSearchWindow)
        self.statusbar.setObjectName("statusbar")
        StockSearchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StockSearchWindow)
        QtCore.QMetaObject.connectSlotsByName(StockSearchWindow)

    def retranslateUi(self, StockSearchWindow):
        _translate = QtCore.QCoreApplication.translate
        StockSearchWindow.setWindowTitle(_translate("StockSearchWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("StockSearchWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">库存查询界面</span></p></body></html>"))
        self.WareID_Label.setText(_translate("StockSearchWindow", "商品编号"))
        self.pushButton.setText(_translate("StockSearchWindow", "提交"))

