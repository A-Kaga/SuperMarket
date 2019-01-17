# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\SuperMarket\QtUI\UI\SaleSearchWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SaleSearchWindow(object):
    def setupUi(self, SaleSearchWindow):
        SaleSearchWindow.setObjectName("SaleSearchWindow")
        SaleSearchWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SaleSearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 801, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(160, 190, 511, 351))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 110, 247, 23))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.StartTime_Label = QtWidgets.QLabel(self.layoutWidget)
        self.StartTime_Label.setObjectName("StartTime_Label")
        self.horizontalLayout.addWidget(self.StartTime_Label)
        self.StartTime_DateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.StartTime_DateEdit.setObjectName("StartTime_DateEdit")
        self.horizontalLayout.addWidget(self.StartTime_DateEdit)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(460, 110, 232, 23))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.EndTime_Label = QtWidgets.QLabel(self.layoutWidget1)
        self.EndTime_Label.setObjectName("EndTime_Label")
        self.horizontalLayout_2.addWidget(self.EndTime_Label)
        self.EndTime_DateEdit = QtWidgets.QDateEdit(self.layoutWidget1)
        self.EndTime_DateEdit.setObjectName("EndTime_DateEdit")
        self.horizontalLayout_2.addWidget(self.EndTime_DateEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 160, 93, 28))
        self.pushButton.setObjectName("pushButton")
        SaleSearchWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SaleSearchWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        SaleSearchWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SaleSearchWindow)
        self.statusbar.setObjectName("statusbar")
        SaleSearchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SaleSearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SaleSearchWindow)

    def retranslateUi(self, SaleSearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SaleSearchWindow.setWindowTitle(_translate("SaleSearchWindow", "销售查询"))
        self.textBrowser.setHtml(_translate("SaleSearchWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">销货查询界面</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SaleSearchWindow", "销售代码"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SaleSearchWindow", "售出时间"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SaleSearchWindow", "商品代码"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SaleSearchWindow", "售出数量"))
        self.StartTime_Label.setText(_translate("SaleSearchWindow", "起始时间"))
        self.StartTime_DateEdit.setDisplayFormat(_translate("SaleSearchWindow", "yyyy/MM/dd dddd"))
        self.EndTime_Label.setText(_translate("SaleSearchWindow", "结束时间"))
        self.EndTime_DateEdit.setDisplayFormat(_translate("SaleSearchWindow", "yyyy/MM/dd dddd"))
        self.pushButton.setText(_translate("SaleSearchWindow", "查询"))

