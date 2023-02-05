from PyQt5.QtCore import *
import pandas as pd

class pandasModel(QAbstractTableModel):
    def __init__(self, df=pd.DataFrame()):
        super().__init__()
        self.df = df

    def rowCount(self, parent=None):
        return self.df.shape[0]

    def columnCount(self, index=None):
        return self.df.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return QVariant()
        else: 
            # Get the raw value
            value = self._data[index.row()][index.column()]
            if isinstance(value, float):
                # Render float to 2 dp
                return "%.2f" % value

            if isinstance(value, str):
                # Render strings with quotes
                return '"%s"' % value
            return value

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def setData(self, index, value, role):
        if not index.isValid():
            return QVariant()
        if role == Qt.DisplayRole or role == Qt.EditRole:
            self.df.iloc[index.row(), index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()

        if orientation == Qt.Horizontal:

            return self.df.columns[section]
        elif orientation == Qt.Vertical:
            return str(self.df.index[section])