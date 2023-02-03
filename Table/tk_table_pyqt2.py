from PyQt5.QtWidgets import *
import pandas as pd
from pandasModel2 import pandasModel

class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=None)
        vLayout = QVBoxLayout(self)
        hLayout = QHBoxLayout()
        self.pathLE = QLineEdit(self)
        hLayout.addWidget(self.pathLE)
        self.loadBtn = QPushButton("Select File", self)
        hLayout.addWidget(self.loadBtn)
        vLayout.addLayout(hLayout)
        self.pandasTv = QTableView(self)
        vLayout.addWidget(self.pandasTv)
        self.loadBtn.clicked.connect(self.loadFile)
        self.pandasTv.setSortingEnabled(True)

    def loadFile(self):
        fileName, _ =  QFileDialog.getOpenFileName(self, "Open File", "", "CSV Files (*.csv)")
        self.pathLE.setText('팁 $6 이상 고객')
        df = pd.read_csv(fileName)
        df2 = df[df.tip>=6]
        show = df2.round(2)
        model = pandasModel(show)
        self.pandasTv.setModel(model)

if __name__ == "__main__":
    import sys
    app =  QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())