from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Image as IMG
import cv2
import numpy as np
import window as ui
import cut as cutui
import resize as resizeui
import type as typeui


class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.storetype = "Default"
        self.start = False
        self.source = []
        self.nums = 0
        self.store = "bin"
        self.cutparm = [0, 0, 0, 0]
        self.resizewh = [0, 0]
        self.resizescale = 0
        self.mChooseBtn.clicked.connect(self.image_choose)
        self.mFlipBtn.clicked.connect(self.flip_item)
        self.mCutBtn.clicked.connect(self.cut_item)
        self.mResizeBtn.clicked.connect(self.resize_item)
        self.mTypeBtn.clicked.connect(self.go_type)

    def setType(self, type):
        self.storetype = type

    def go_type(self):
        editType.show()

    def image_choose(self):
        self.source, ok1 = QFileDialog.getOpenFileNames(self,
                                                        "檔案選擇",
                                                        "./",
                                                        "Png Files (*.png);;Jpg Files (*.jpg);;Bmp Files (*.bmp)")
        self.nums = len(self.source)
        showtext = ""
        for i in range(self.nums):
            showtext = showtext + self.source[i] + "\n"
        self.label.setText(showtext)

    def flip_item(self):
        self.store = QFileDialog.getExistingDirectory(self,
                                                      "儲存位置",
                                                      "./")
        for i in range(self.nums):
            img = cv2.imread(self.source[i])
            img = IMG.flip(img)
            storetype = self.source[i].split('.')[1]
            if(self.storetype != "Default"):
                storetype = self.storetype
            storename = self.store + "/" + str(i) + "." + storetype
            cv2.imwrite(storename, img)
            self.label.setText("Success")
        self.storetype = "Default"

    def setCutParm(self, input):
        self.cutparm[0] = int(input[0])
        self.cutparm[1] = int(input[1])
        self.cutparm[2] = int(input[2])
        self.cutparm[3] = int(input[3])

    def cut_item(self):
        self.store = QFileDialog.getExistingDirectory(self,
                                                      "儲存位置",
                                                      "./")
        cut.show()

    def continue_cut(self):
        for i in range(self.nums):
            img = cv2.imread(self.source[i])
            img = IMG.Cutimage(
                img, self.cutparm[0], self.cutparm[1], self.cutparm[2], self.cutparm[3])
            storetype = self.source[i].split('.')[1]
            if(self.storetype != "Default"):
                storetype = self.storetype
            storename = self.store + "/" + str(i) + "." + storetype
            cv2.imwrite(storename, img)
            self.label.setText("Success")
        self.storetype = "Default"

    def setResizeParm(self, type, input):
        # type為True為x,y
        if (type == True):
            self.resizewh = [int(input[0]), int(input[1])]
        else:
            self.resizescale = float(input)

    def resize_item(self):
        self.store = QFileDialog.getExistingDirectory(self,
                                                      "儲存位置",
                                                      "./")
        resize.show()

    def continue_resize(self, type):
        # type為True為x,y
        if (type == True):
            for i in range(self.nums):
                img = cv2.imread(self.source[i])
                img = IMG.resize_xy(
                    img, self.resizewh[0], self.resizewh[1])
                storetype = self.source[i].split('.')[1]
                if(self.storetype != "Default"):
                    storetype = self.storetype
                storename = self.store + "/" + str(i) + "." + storetype
                cv2.imwrite(storename, img)
            self.label.setText("Success")

        else:
            for i in range(self.nums):
                img = cv2.imread(self.source[i])
                img = IMG.resize(img, self.resizescale)
                storetype = self.source[i].split('.')[1]
                if(self.storetype != "Default"):
                    storetype = self.storetype
                storename = self.store + "/" + str(i) + "." + storetype
                cv2.imwrite(storename, img)
            self.label.setText("Success")
        self.storetype = "Default"

    def closeEvent(self, event):
        QApplication.closeAllWindows()


class Cutwidget(QWidget, cutui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化執行B視窗類下的 setupUi 函式
        self.mInputX.setPlainText(str(window.cutparm[0]))
        self.mInputY.setPlainText(str(window.cutparm[1]))
        self.mInputWidth.setPlainText(str(window.cutparm[2]))
        self.mInputHeight.setPlainText(str(window.cutparm[3]))
        self.mConfirmBtn.clicked.connect(self.confirm)

    def confirm(self):
        tempParm = []
        tempParm.append(self.mInputX.toPlainText())
        tempParm.append(self.mInputY.toPlainText())
        tempParm.append(self.mInputWidth.toPlainText())
        tempParm.append(self.mInputHeight.toPlainText())
        window.setCutParm(tempParm)
        window.continue_cut()
        self.close()


class Resizewidget(QWidget, resizeui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化執行B視窗類下的 setupUi 函式
        self.mInputWidth.setPlainText(str(window.resizewh[0]))
        self.mInputHeight.setPlainText(str(window.resizewh[1]))
        self.mInputScale.setPlainText(str(window.resizescale))
        self.mConfirmBtn.clicked.connect(self.confirm)

    def confirm(self):
        type = True
        if(self.mXYRadio.isChecked()):
            tempParm = []
            tempParm.append(self.mInputWidth.toPlainText())
            tempParm.append(self.mInputHeight.toPlainText())

        elif(self.mScaleRadio.isChecked()):
            type = False
            tempParm = self.mInputScale.toPlainText()
        window.setResizeParm(type, tempParm)
        window.continue_resize(type)
        self.close()


class Typewidget(QWidget, typeui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化執行B視窗類下的 setupUi 函式
        self.mConfirmBtn.clicked.connect(self.confirm)

    def confirm(self):
        if(self.mPngRadio.isChecked()):
            window.setType("png")
        elif(self.mJpgRadio.isChecked()):
            window.setType("Jpg")
        elif(self.mBmpRadio.isChecked()):
            window.setType("Bmp")
        else:
            window.setType("Default")
        self.close()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    cut = Cutwidget()
    resize = Resizewidget()
    editType = Typewidget()
    window.show()
    sys.exit(app.exec_())
