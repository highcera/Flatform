## Ex 5-21. QTableWidget.  https://wikidocs.net/128689

import sys
import align
# from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        # self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # align = [Qt.AlignCenter
        #          , Qt.AlignVCenter
        #          , Qt.AlignHCenter
        #          , Qt.AlignRight
        #          , Qt.AlignLeft
        #          , Qt.AlignTop
        #          , Qt.AlignBottom
        #          , Qt.AlignTop | Qt.AlignRight
        #          , Qt.AlignBottom | Qt.AlignLeft
        #          , Qt.AlignBottom | Qt.AlignRight]

        for r in range(20):
            for c in range(4):
                item = QTableWidgetItem()
                item.setText(str(r+c))
                item.setTextAlignment(align.align[0])
                self.tableWidget.setItem(r, c, item)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec_()