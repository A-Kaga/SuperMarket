# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\SuperMarket\QtUI\UI\PurchaseRegisterWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PurchaseRegisterWindow(object):
    def setupUi(self, PurchaseRegisterWindow):
        PurchaseRegisterWindow.setObjectName("PurchaseRegisterWindow")
        PurchaseRegisterWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(PurchaseRegisterWindow)
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
        self.layoutWidget.setGeometry(QtCore.QRect(240, 150, 341, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PurchaseID_LineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.PurchaseID_LineEdit.setObjectName("PurchaseID_LineEdit")
        self.gridLayout.addWidget(self.PurchaseID_LineEdit, 1, 1, 1, 1)
        self.Time_Label = QtWidgets.QLabel(self.layoutWidget)
        self.Time_Label.setObjectName("Time_Label")
        self.gridLayout.addWidget(self.Time_Label, 0, 0, 1, 1)
        self.PurchaseID_Label = QtWidgets.QLabel(self.layoutWidget)
        self.PurchaseID_Label.setObjectName("PurchaseID_Label")
        self.gridLayout.addWidget(self.PurchaseID_Label, 1, 0, 1, 1)
        self.WareID_LineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.WareID_LineEdit.setObjectName("WareID_LineEdit")
        self.gridLayout.addWidget(self.WareID_LineEdit, 2, 1, 1, 1)
        self.WareID_Label = QtWidgets.QLabel(self.layoutWidget)
        self.WareID_Label.setObjectName("WareID_Label")
        self.gridLayout.addWidget(self.WareID_Label, 2, 0, 1, 1)
        self.Quantity_Label = QtWidgets.QLabel(self.layoutWidget)
        self.Quantity_Label.setObjectName("Quantity_Label")
        self.gridLayout.addWidget(self.Quantity_Label, 3, 0, 1, 1)
        self.Quantity_SpinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.Quantity_SpinBox.setObjectName("Quantity_SpinBox")
        self.gridLayout.addWidget(self.Quantity_SpinBox, 3, 1, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 0, 1, 1, 1)
        PurchaseRegisterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PurchaseRegisterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        PurchaseRegisterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PurchaseRegisterWindow)
        self.statusbar.setObjectName("statusbar")
        PurchaseRegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PurchaseRegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(PurchaseRegisterWindow)

    def retranslateUi(self, PurchaseRegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        PurchaseRegisterWindow.setWindowTitle(_translate("PurchaseRegisterWindow", "商品注册"))
        self.textBrowser.setHtml(_translate("PurchaseRegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">进货登记登记界面</span></p></body></html>"))
        self.Submit_PushButton.setText(_translate("PurchaseRegisterWindow", "提交"))
        self.Clear_PushButton.setText(_translate("PurchaseRegisterWindow", "清空"))
        self.Time_Label.setText(_translate("PurchaseRegisterWindow", "进货时间"))
        self.PurchaseID_Label.setText(_translate("PurchaseRegisterWindow", "进货编号"))
        self.WareID_Label.setText(_translate("PurchaseRegisterWindow", "商品代码"))
        self.Quantity_Label.setText(_translate("PurchaseRegisterWindow", "进货数量"))
        self.dateTimeEdit.setDisplayFormat(_translate("PurchaseRegisterWindow", "yyyy-mm-dd hh-mm-ss"))

