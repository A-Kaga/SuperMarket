# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\SuperMarket\QtUI\UI\RegisterErrorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegisterErrorDialog(object):
    def setupUi(self, RegisterErrorDialog):
        RegisterErrorDialog.setObjectName("RegisterErrorDialog")
        RegisterErrorDialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(RegisterErrorDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(RegisterErrorDialog)
        self.label.setGeometry(QtCore.QRect(140, 90, 131, 81))
        self.label.setObjectName("label")

        self.retranslateUi(RegisterErrorDialog)
        self.buttonBox.clicked['QAbstractButton*'].connect(RegisterErrorDialog.accept)
        self.buttonBox.clicked['QAbstractButton*'].connect(RegisterErrorDialog.close)
        QtCore.QMetaObject.connectSlotsByName(RegisterErrorDialog)

    def retranslateUi(self, RegisterErrorDialog):
        _translate = QtCore.QCoreApplication.translate
        RegisterErrorDialog.setWindowTitle(_translate("RegisterErrorDialog", "Dialog"))
        self.label.setText(_translate("RegisterErrorDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">注册失败</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">数据回滚</span></p></body></html>"))

