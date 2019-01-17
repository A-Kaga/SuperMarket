# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\SuperMarket\QtUI\UI\SaleRegisterWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SaleRegisterWindow(object):
    def setupUi(self, SaleRegisterWindow):
        SaleRegisterWindow.setObjectName("SaleRegisterWindow")
        SaleRegisterWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SaleRegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 801, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.Submit_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Submit_PushButton.setGeometry(QtCore.QRect(440, 470, 93, 28))
        self.Submit_PushButton.setObjectName("Submit_PushButton")
        self.Clear_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_PushButton.setGeometry(QtCore.QRect(290, 470, 93, 28))
        self.Clear_PushButton.setObjectName("Clear_PushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 150, 421, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.SaleID_LineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.SaleID_LineEdit.setObjectName("SaleID_LineEdit")
        self.gridLayout.addWidget(self.SaleID_LineEdit, 1, 1, 1, 1)
        self.Time_Label = QtWidgets.QLabel(self.layoutWidget)
        self.Time_Label.setObjectName("Time_Label")
        self.gridLayout.addWidget(self.Time_Label, 0, 0, 1, 1)
        self.Quantity_SpinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.Quantity_SpinBox.setObjectName("Quantity_SpinBox")
        self.gridLayout.addWidget(self.Quantity_SpinBox, 3, 1, 1, 1)
        self.WareID_Label = QtWidgets.QLabel(self.layoutWidget)
        self.WareID_Label.setObjectName("WareID_Label")
        self.gridLayout.addWidget(self.WareID_Label, 2, 0, 1, 1)
        self.SaleID_Label = QtWidgets.QLabel(self.layoutWidget)
        self.SaleID_Label.setObjectName("SaleID_Label")
        self.gridLayout.addWidget(self.SaleID_Label, 1, 0, 1, 1)
        self.Quantity_Label = QtWidgets.QLabel(self.layoutWidget)
        self.Quantity_Label.setObjectName("Quantity_Label")
        self.gridLayout.addWidget(self.Quantity_Label, 3, 0, 1, 1)
        self.WareID_LineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.WareID_LineEdit.setObjectName("WareID_LineEdit")
        self.gridLayout.addWidget(self.WareID_LineEdit, 2, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 0, 1, 1, 1)
        SaleRegisterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SaleRegisterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        SaleRegisterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SaleRegisterWindow)
        self.statusbar.setObjectName("statusbar")
        SaleRegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SaleRegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(SaleRegisterWindow)

    def retranslateUi(self, SaleRegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        SaleRegisterWindow.setWindowTitle(_translate("SaleRegisterWindow", "商品注册"))
        self.textBrowser.setHtml(_translate("SaleRegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">销货登记界面</span></p></body></html>"))
        self.Submit_PushButton.setText(_translate("SaleRegisterWindow", "提交"))
        self.Clear_PushButton.setText(_translate("SaleRegisterWindow", "清空"))
        self.Time_Label.setText(_translate("SaleRegisterWindow", "销售时间"))
        self.WareID_Label.setText(_translate("SaleRegisterWindow", "商品代码"))
        self.SaleID_Label.setText(_translate("SaleRegisterWindow", "销售编号"))
        self.Quantity_Label.setText(_translate("SaleRegisterWindow", "销售数量"))
        self.dateEdit.setDisplayFormat(_translate("SaleRegisterWindow", "yyyy/MM/dd dddd"))

