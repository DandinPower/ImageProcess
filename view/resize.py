# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resize.ui'
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
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        self.mConfirmBtn = QtWidgets.QPushButton(Form)
        self.mConfirmBtn.setGeometry(QtCore.QRect(150, 220, 91, 31))
        self.mConfirmBtn.setObjectName("mConfirmBtn")
        self.mXYRadio = QtWidgets.QRadioButton(Form)
        self.mXYRadio.setGeometry(QtCore.QRect(70, 160, 83, 31))
        self.mXYRadio.setObjectName("mXYRadio")
        self.mScaleRadio = QtWidgets.QRadioButton(Form)
        self.mScaleRadio.setGeometry(QtCore.QRect(240, 160, 83, 31))
        self.mScaleRadio.setObjectName("mScaleRadio")
        self.mWidthHint = QtWidgets.QLabel(Form)
        self.mWidthHint.setGeometry(QtCore.QRect(30, 90, 51, 16))
        self.mWidthHint.setObjectName("mWidthHint")
        self.mHeightHint = QtWidgets.QLabel(Form)
        self.mHeightHint.setGeometry(QtCore.QRect(30, 130, 61, 20))
        self.mHeightHint.setObjectName("mHeightHint")
        self.mScaleHint = QtWidgets.QLabel(Form)
        self.mScaleHint.setGeometry(QtCore.QRect(210, 100, 51, 20))
        self.mScaleHint.setObjectName("mScaleHint")
        self.mInputWidth = QtWidgets.QPlainTextEdit(Form)
        self.mInputWidth.setGeometry(QtCore.QRect(90, 80, 104, 31))
        self.mInputWidth.setObjectName("mInputWidth")
        self.mInputHeight = QtWidgets.QPlainTextEdit(Form)
        self.mInputHeight.setGeometry(QtCore.QRect(90, 120, 104, 31))
        self.mInputHeight.setObjectName("mInputHeight")
        self.mInputScale = QtWidgets.QPlainTextEdit(Form)
        self.mInputScale.setGeometry(QtCore.QRect(270, 100, 104, 31))
        self.mInputScale.setObjectName("mInputScale")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "設定大小"))
        self.mConfirmBtn.setText(_translate("Form", "確認變更"))
        self.mXYRadio.setText(_translate("Form", "依據長寬"))
        self.mScaleRadio.setText(_translate("Form", "依據比例"))
        self.mWidthHint.setText(_translate("Form", "輸入寬度:"))
        self.mHeightHint.setText(_translate("Form", "輸入高度:"))
        self.mScaleHint.setText(_translate("Form", "輸入比例:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
