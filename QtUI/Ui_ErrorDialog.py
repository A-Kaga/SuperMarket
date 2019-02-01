# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\SuperMarket\QtUI\UI\ErrorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ErrorDialog(object):
    def setupUi(self, ErrorDialog):
        ErrorDialog.setObjectName("ErrorDialog")
        ErrorDialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(ErrorDialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 230, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.ErrorMessage = QtWidgets.QLabel(ErrorDialog)
        self.ErrorMessage.setGeometry(QtCore.QRect(40, 110, 321, 61))
        self.ErrorMessage.setTextFormat(QtCore.Qt.AutoText)
        self.ErrorMessage.setScaledContents(False)
        self.ErrorMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorMessage.setWordWrap(True)
        self.ErrorMessage.setObjectName("ErrorMessage")

        self.retranslateUi(ErrorDialog)
        QtCore.QMetaObject.connectSlotsByName(ErrorDialog)

    def retranslateUi(self, ErrorDialog):
        _translate = QtCore.QCoreApplication.translate
        ErrorDialog.setWindowTitle(_translate("ErrorDialog", "错误"))
        self.pushButton.setText(_translate("ErrorDialog", "确定"))
        self.ErrorMessage.setText(_translate("ErrorDialog", "采购后库存大于上限，请修改采购量"))

