from typing import List
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import numpy as np
import re
import time
import Image as IMG
import window as ui
import cut as cutui
import resize as resizeui
import type as typeui
import list as listui
import imageshow as imageshowui


class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mTransBar.setRange(0, 100)
        self.mFlipBtn.clicked.connect(self.flip_item)
        self.mCutBtn.clicked.connect(self.cut_item)
        self.mResizeBtn.clicked.connect(self.resize_item)
        self.mTypeBtn.clicked.connect(self.go_type)
        self.mShowBtn.clicked.connect(self.list_show)
        self.onBeginState()

    def initialize(self):
        self.mProgressHint.setText("Success!!")
        self.mTransBar.setValue(100)

    def onBeginState(self):
        self.storetype = "Default"
        self.start = False
        self.source = []
        self.nums = 0
        self.store = "bin"
        self.cutparm = [0, 0, 0, 0]
        self.resizewh = [0, 0]
        self.resizescale = 0
        self.progress = 0
        self.mTransBar.setValue(0)
        self.setTypeText(self.storetype)
        self.setBtn(False)

    def countBarValue(self, now, end):
        return int(100 * (now/end))

    def setSource(self, list):
        self.source = list
        self.nums = len(self.source)
        if(self.nums != 0):
            self.mSystemHint.setText("已選取圖片")
            self.setBtn(True)
        else:
            self.mSystemHint.setText("尚未選取圖片")
            self.setBtn(False)

    def setTypeText(self, type):
        self.mTypeHint.setText("目前轉檔格式設定為: " + type)

    def setBtn(self, flag):
        self.mFlipBtn.setEnabled(flag)
        self.mCutBtn.setEnabled(flag)
        self.mResizeBtn.setEnabled(flag)

    def setType(self, type):
        self.storetype = type

    def setCutParm(self, input):
        self.cutparm[0] = int(input[0])
        self.cutparm[1] = int(input[1])
        self.cutparm[2] = int(input[2])
        self.cutparm[3] = int(input[3])

    def setResizeParm(self, type, input):
        # type為True為x,y
        if (type == True):
            self.resizewh = [int(input[0]), int(input[1])]
        else:
            self.resizescale = float(input)

    def getType(self):
        return self.storetype

    def go_type(self):
        editType.show()

    def flip_item(self):
        self.store = QFileDialog.getExistingDirectory(self,
                                                      "儲存位置",
                                                      "./")
        if (self.store != ""):
            self.mProgressHint.setText("Transforming")
            for i in range(self.nums):
                img = cv2.imread(self.source[i])
                img = IMG.flip(img)
                storetype = self.source[i].split('.')[1]
                if(self.storetype != "Default"):
                    storetype = self.storetype
                storename = self.store + "/" + str(i) + "." + storetype
                cv2.imwrite(storename, img)
                self.mTransBar.setValue(self.countBarValue(i, self.nums))
            self.initialize()

    def cut_item(self):
        self.store = QFileDialog.getExistingDirectory(self,
                                                      "儲存位置",
                                                      "./")
        if (self.store != ""):
            cut.show()

    def resize_item(self):
        self.store = QFileDialog.getExistingDirectory(self,
                                                      "儲存位置",
                                                      "./")
        if (self.store != ""):
            resize.show()

    def list_show(self):
        listShow.show()

    def continue_cut(self):
        self.mProgressHint.setText("Transforming")
        for i in range(self.nums):
            img = cv2.imread(self.source[i])
            img = IMG.Cutimage(
                img, self.cutparm[0], self.cutparm[1], self.cutparm[2], self.cutparm[3])
            storetype = self.source[i].split('.')[1]
            if(self.storetype != "Default"):
                storetype = self.storetype
            storename = self.store + "/" + str(i) + "." + storetype
            cv2.imwrite(storename, img)
            self.mTransBar.setValue(self.countBarValue(i, self.nums))
        self.initialize()

    def continue_resize(self, type):
        self.mProgressHint.setText("Transforming")
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
                self.mTransBar.setValue(self.countBarValue(i, self.nums))

        else:
            for i in range(self.nums):
                img = cv2.imread(self.source[i])
                img = IMG.resize(img, self.resizescale)
                storetype = self.source[i].split('.')[1]
                if(self.storetype != "Default"):
                    storetype = self.storetype
                storename = self.store + "/" + str(i) + "." + storetype
                cv2.imwrite(storename, img)
                self.mTransBar.setValue(self.countBarValue(i, self.nums))
        self.initialize()

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
        self.close()
        window.continue_cut()


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
        self.close()
        window.continue_resize(type)


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
        window.setTypeText(window.getType())
        self.close()


class Listwidget(QWidget, listui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化執行B視窗類下的 setupUi 函式
        self.mAddBtn.clicked.connect(self.image_choose)
        self.mDeleteAllBtn.clicked.connect(self.delete_all)
        self.mDeleteBtn.clicked.connect(self.delete)
        self.mShowImageBtn.clicked.connect(self.image_show)
        self.source = list()
        self.data = list()
        self.nums = 0

    def image_choose(self):
        self.source, ok1 = QFileDialog.getOpenFileNames(self,
                                                        "檔案選擇",
                                                        "./",
                                                        "Png Files (*.png);;Jpg Files (*.jpg);;Bmp Files (*.bmp)")
        self.nums = len(self.source)
        for i in range(self.nums):
            isNotCh = True
            for ch in self.source[i]:
                if re.compile(u'[\u4e00-\u9fa5]+').search(ch):
                    self.go_wrong(self.source[i])
                    isNotCh = False
                    break
            if(isNotCh):
                sourceset = set(self.data)
                if not (self.source[i] in sourceset):
                    self.data.append(self.source[i])
        self.mShowList.clear()
        for index in self.data:
            self.mShowList.addItem(index)

    def delete(self):
        self.data.remove(self.data[self.mShowList.currentRow()])
        self.mShowList.clear()
        for index in self.data:
            self.mShowList.addItem(index)

    def delete_all(self):
        self.data.clear()
        self.mShowList.clear()

    def go_wrong(self, text):
        reply = QMessageBox.critical(
            self, "錯誤訊息", text + "\n路徑或檔名含有中文無法讀取,請更改檔名或路徑")
        if(reply == QMessageBox.Yes):
            self.image_choose()

    def image_show(self):
        tempimg = cv2.imread(self.data[self.mShowList.currentRow()])
        height, width, ret = tempimg.shape
        imageshow.resize(width, height)
        imageshow.setImage(
            self.data[self.mShowList.currentRow()], width, height)
        imageshow.show()

    def closeEvent(self, event):
        window.setSource(self.data)


class ImageShowwidget(QWidget, imageshowui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化執行B視窗類下的 setupUi 函式
        self.image = ""

    def setImage(self, str, width, height):
        self.image = str
        self.mShowImage.resize(width, height)
        self.mShowImage.setPixmap(QPixmap(self.image))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    cut = Cutwidget()
    resize = Resizewidget()
    editType = Typewidget()
    listShow = Listwidget()
    imageshow = ImageShowwidget()
    window.show()
    sys.exit(app.exec_())
