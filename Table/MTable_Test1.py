import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import pandas as pd

os.chdir('Table')

GUI_FILE_NAME = 'MTable_dsn1'

os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from MTable_dsn1 import Ui_MainWindow
from mypandasModel import pandasModel

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)

        df = self.loadFile()

        model1 = pandasModel(df)
        self.label_1.setText("전체 데이터")
        self.tableView_1.setModel(model1)

        df2 = df.describe()
        model2 = pandasModel(df2)
        self.label_2.setText("데이터 description")
        self.tableView_2.setModel(model2)
        
        df3 = df.round(1)
        model3 = pandasModel(df3)
        self.label_3.setText("소수점 1자리 반올림")
        self.tableView_3.setModel(model3)

        df4 = df[df.tip>=6]
        model4 = pandasModel(df4)
        self.label_4.setText("Tip $6 이상")
        self.tableView_4.setModel(model4)
        
    def loadFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "CSV Files (*.csv)")
        df = pd.read_csv(fileName)
        return df

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    app.exec_()