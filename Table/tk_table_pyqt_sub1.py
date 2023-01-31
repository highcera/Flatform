# https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/

import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import pandas as pd

class Test:
    def __init__(self):
        self.data = self.read_data()
        print(self.data)
       
    def read_data(self):
        self.df=pd.read_csv("E:/Repo_Office/Flatform/Table/tips.csv")
        # print(self.df)
        return self.df

a=Test()
a.read_data()