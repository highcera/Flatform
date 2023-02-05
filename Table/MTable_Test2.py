## https://wikidocs.net/33707

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QTableView, QMainWindow

import pandas as pd
from mypandasModel import pandasModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        tabs = QTabWidget()
        tabs.setMovable(True)

        tab1 = QTableView()
        tab2 = QTableView()
        tab3 = QTableView()
        tab4 = QTableView()
                
        tabs.addTab(tab1, '전체 데이터')
        tabs.addTab(tab2, '데이터 description')
        tabs.addTab(tab3, '소수점 1자리 반올림')
        tabs.addTab(tab4, 'Tip $6 이상')

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 800, 600)

        df = self.read_data()

        model1 = pandasModel(df)
        tab1.setModel(model1)
        # tabs.tabl.setText("전체 데이터")

        df2 = df.describe()
        model2 = pandasModel(df2)
        tab2.setModel(model2)
        # tabs.tab2.setText("데이터 description")

        df3 = df.round(1)
        model3 = pandasModel(df3)
        tab3.setModel(model3)
        # tabs.tab3.setText("소수점 1자리 반올림")

        df4 = df[df.tip>=6]
        model4 = pandasModel(df4)
        tab4.setModel(model4)
        # tab4.setText("Tip $6 이상")
       
        self.setCentralWidget(tabs)

    def read_data(self):
        self.df=pd.read_csv("Table/tips.csv")           
        return self.df

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    app.exec_()