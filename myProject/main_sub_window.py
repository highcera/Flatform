# https://eggwhite0.tistory.com/87

import sys, os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from secondwindow import secondwindow

# os.chdir("E:/Repo_Office/Flatform/myProject")
form_main = uic.loadUiType("E:/Repo_Office/Flatform/myProject/test.ui")[0]

class MainWindow(QMainWindow, QWidget, form_main):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        self.second_text = ""

    def initUI(self):
        self.setupUi(self)
        self.pushButton_1.clicked.connect(self.buttonClicked_Input)
        self.output_text.clicked.connect(self.buttonClicked_Output)
        self.SecondWindow.clicked.connect(self.buttonClicked_Second)

    def buttonClicked_Input(self):
        self.textEdit_1.append("버튼누름")
        # self.textEdit.setText("버튼누름") #한번만
        # self.textEdit.insertPlainText("버튼누름") #띄어쓰기X

    def buttonClicked_Output(self):
        self.text = self.textEdit_1.toPlainText()
        self.textEdit_2.setText(self.text)

    def buttonClicked_Second(self):
        self.hide()
        self.second = secondwindow()
        self.second.exec()
        self.textEdit_2.setText(self.second.second_text)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

