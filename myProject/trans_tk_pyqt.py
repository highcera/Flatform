import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import pandas as pd

os.chdir('myProject')

GUI_FILE_NAME = 'telephone'
# C:\Flatform\myProject\telephone.ui
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from telephone import Ui_MainWindow
from mypandasModel import pandasModel

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)

        df = self.loadFile()
        # print(df)
        model = pandasModel(df)
        self.tableView.setModel(model)

        tel_lists = df.values.tolist()
        # print(tel_lists)
        # members = ['banana', 'apple', 'orange']
        
        model2 = QStandardItemModel()
        for x in tel_lists:
            model2.appendRow(QStandardItem(x))
        self.listView.setModel(model2)

        # df2 = df.describe()
        # model2 = pandasModel(df2)
        # self.label_2.setText("데이터 description")
        # self.tableView_2.setModel(model2)
        
        # df3 = df.round(1)
        # model3 = pandasModel(df3)
        # self.label_3.setText("소수점 1자리 반올림")
        # self.tableView_3.setModel(model3)

        # df4 = df[df.tip>=6]
        # model4 = pandasModel(df4)
        # self.label_4.setText("Tip $6 이상")
        # self.tableView_4.setModel(model4)
        
    def loadFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All File(*);; CSV Files (*.csv);; Text File(*.txt)", "CSV Files (*.csv)")
        df = pd.read_csv(fileName)
        # read_file.to_csv (r'Path where the CSV will be saved\File name.csv', index=None)

        return df
# import pandas as pd
# file = pd.read_csv('Boston_Housing.txt', delimiter = '\t')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    app.exec_()