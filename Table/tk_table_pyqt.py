# https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
import pandas as pd
from pandasModel2 import pandasModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tableLib = QTableView()
        self.setCentralWidget(self.tableLib)

        self.tableLib.setGeometry(QtCore.QRect(30, 140, 831, 331))
      
        data = self.read_data()
        # print(data)
        show = data.round(2)

        self.make_tableLib(show)       

    def read_data(self):
        self.df=pd.read_csv("C:/Flatform/Table/tips.csv")
   
        return self.df

    def make_tableLib(self, df):
        model = pandasModel(df)
        self.tableLib.setModel(model)
        self.tableLib.resizeColumnsToContents()
        self.tableLib.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableLib.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()