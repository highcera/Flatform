# https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/

import sys
from PyQt5 import QtWidgets
import pandas as pd
from pandasModel2 import pandasModel

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        data = self.read_data()
        print(data)

        self.table = QtWidgets.QTableView()
        self.model = pandasModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

    def read_data(self):
        self.df=pd.read_csv("C:/Flatform/Table/tips.csv")
        self.df2 = self.df.round(2)
   
        return self.df2

app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()