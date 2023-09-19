import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_secondwindow = uic.loadUiType("E:/Repo_Office/Flatform/myProject/secondwindow.ui")[0]
class secondwindow(QDialog, QWidget, form_secondwindow):
    def __init__(self):
        super(secondwindow, self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.home.clicked.connect(self.Home)

    def Home(self):
        self.second_text = self.lineEdit.text()
        self.close()