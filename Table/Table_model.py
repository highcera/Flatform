# https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/

import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
        #     # See below for the nested-list data structure.
        #     # .row() indexes into the outer list,
        #     # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

        if role == Qt.TextAlignmentRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, int) or isinstance(value, float):
                # Align right, vertical middle.
                return Qt.AlignCenter
     
        if role == Qt.ForegroundRole:
            value = self._data[index.row()][index.column()]

            if (
                (isinstance(value, int) or isinstance(value, float))
                and value < 0
            ):
                return QtGui.QColor('red')

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = [
            [4, 9, 2],
            [1, -1, 'hello'],
            [3.023, 5, -5],
            [3, 3, datetime(2017,10,1)],
            [7.555, 8, 9],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()