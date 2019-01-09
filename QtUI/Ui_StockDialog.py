# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\SuperMarket\QtUI\UI\StockDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StockDialog(object):
    def setupUi(self, StockDialog):
        StockDialog.setObjectName("StockDialog")
        StockDialog.resize(400, 300)
        self.dialogButtonBox = QtWidgets.QDialogButtonBox(StockDialog)
        self.dialogButtonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialogButtonBox.setObjectName("dialogButtonBox")
        self.widget = QtWidgets.QWidget(StockDialog)
        self.widget.setGeometry(QtCore.QRect(40, 50, 331, 121))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.WareID_Label = QtWidgets.QLabel(self.widget)
        self.WareID_Label.setObjectName("WareID_Label")
        self.gridLayout.addWidget(self.WareID_Label, 0, 0, 1, 1)
        self.WareID = QtWidgets.QLabel(self.widget)
        self.WareID.setObjectName("WareID")
        self.gridLayout.addWidget(self.WareID, 0, 1, 1, 1)
        self.WareName_Label = QtWidgets.QLabel(self.widget)
        self.WareName_Label.setObjectName("WareName_Label")
        self.gridLayout.addWidget(self.WareName_Label, 1, 0, 1, 1)
        self.WareName = QtWidgets.QLabel(self.widget)
        self.WareName.setObjectName("WareName")
        self.gridLayout.addWidget(self.WareName, 1, 1, 1, 1)
        self.Stock_Label = QtWidgets.QLabel(self.widget)
        self.Stock_Label.setObjectName("Stock_Label")
        self.gridLayout.addWidget(self.Stock_Label, 2, 0, 1, 1)
        self.Stock = QtWidgets.QLabel(self.widget)
        self.Stock.setObjectName("Stock")
        self.gridLayout.addWidget(self.Stock, 2, 1, 1, 1)

        self.retranslateUi(StockDialog)
        self.dialogButtonBox.clicked['QAbstractButton*'].connect(StockDialog.close)
        self.dialogButtonBox.clicked['QAbstractButton*'].connect(StockDialog.close)
        QtCore.QMetaObject.connectSlotsByName(StockDialog)

    def retranslateUi(self, StockDialog):
        _translate = QtCore.QCoreApplication.translate
        StockDialog.setWindowTitle(_translate("StockDialog", "Dialog"))
        self.WareID_Label.setText(_translate("StockDialog", "商品编号"))
        self.WareID.setText(_translate("StockDialog", "TextLabel"))
        self.WareName_Label.setText(_translate("StockDialog", "商品名称"))
        self.WareName.setText(_translate("StockDialog", "TextLabel"))
        self.Stock_Label.setText(_translate("StockDialog", "当前库存"))
        self.Stock.setText(_translate("StockDialog", "TextLabel"))

