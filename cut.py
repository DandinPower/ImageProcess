# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cut.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.mInputX = QtWidgets.QPlainTextEdit(Form)
        self.mInputX.setGeometry(QtCore.QRect(110, 80, 71, 31))
        self.mInputX.setObjectName("mInputX")
        self.cuthint1 = QtWidgets.QLabel(Form)
        self.cuthint1.setGeometry(QtCore.QRect(50, 90, 47, 12))
        self.cuthint1.setObjectName("cuthint1")
        self.cuthint2 = QtWidgets.QLabel(Form)
        self.cuthint2.setGeometry(QtCore.QRect(50, 140, 47, 12))
        self.cuthint2.setObjectName("cuthint2")
        self.mInputY = QtWidgets.QPlainTextEdit(Form)
        self.mInputY.setGeometry(QtCore.QRect(110, 130, 71, 31))
        self.mInputY.setObjectName("mInputY")
        self.cuthint3 = QtWidgets.QLabel(Form)
        self.cuthint3.setGeometry(QtCore.QRect(210, 90, 47, 12))
        self.cuthint3.setObjectName("cuthint3")
        self.mInputWidth = QtWidgets.QPlainTextEdit(Form)
        self.mInputWidth.setGeometry(QtCore.QRect(270, 80, 71, 31))
        self.mInputWidth.setObjectName("mInputWidth")
        self.cuthint4 = QtWidgets.QLabel(Form)
        self.cuthint4.setGeometry(QtCore.QRect(210, 140, 47, 12))
        self.cuthint4.setObjectName("cuthint4")
        self.mInputHeight = QtWidgets.QPlainTextEdit(Form)
        self.mInputHeight.setGeometry(QtCore.QRect(270, 130, 71, 31))
        self.mInputHeight.setObjectName("mInputHeight")
        self.mConfirmBtn = QtWidgets.QPushButton(Form)
        self.mConfirmBtn.setGeometry(QtCore.QRect(150, 210, 101, 31))
        self.mConfirmBtn.setObjectName("mConfirmBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "設定範圍"))
        self.mInputX.setPlainText(_translate("Form", "0"))
        self.cuthint1.setText(_translate("Form", "左上角X"))
        self.cuthint2.setText(_translate("Form", "左上角Y"))
        self.mInputY.setPlainText(_translate("Form", "0"))
        self.cuthint3.setText(_translate("Form", "裁切寬度"))
        self.mInputWidth.setPlainText(_translate("Form", "0"))
        self.cuthint4.setText(_translate("Form", "裁切高度"))
        self.mInputHeight.setPlainText(_translate("Form", "0"))
        self.mConfirmBtn.setText(_translate("Form", "確認剪裁"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
