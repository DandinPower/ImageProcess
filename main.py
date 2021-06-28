from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Image as IMG
import cv2
import numpy as np
import window as ui
import cut as cutui


class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.source = []
        self.nums = 0
        self.store = "bin"
        self.cutparm = [0, 0, 0, 0]
        self.mChooseBtn.clicked.connect(self.image_choose)
        self.mFlipBtn.clicked.connect(self.flip_item)
        self.mCutBtn.clicked.connect(self.cut_item)

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
            storename = self.store + "/" + str(i) + "." + storetype
            cv2.imwrite(storename, img)
            self.label.setText("Success")

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
            storename = self.store + "/" + str(i) + "." + storetype
            cv2.imwrite(storename, img)
            self.label.setText("Success")

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


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    cut = Cutwidget()
    window.show()
    sys.exit(app.exec_())
