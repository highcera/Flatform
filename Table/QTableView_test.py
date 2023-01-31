import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QVBoxLayout, QTableWidgetItem
from PyQt5.QtCore import Qt

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("PyQt5 QtableView")
    self.setGeometry(500, 400, 500, 300)
    self.Tables()
    self.show()

  def Tables(self):
    datas = [
            ["John", "24", "Male"],
            ["Lucy", "19", "Female"],
            ["Subaru", "18", "Male"],
            ["William", "60", "Male"],
           ]

    tW = QTableWidget()
    tW.setRowCount(4)
    tW.setColumnCount(3)
   
    tW.setHorizontalHeaderLabels(["Name", "Age", "Gender"])
 
    for r in range(tW.rowCount()):
      for c in range(tW.columnCount()):
        item = QTableWidgetItem()
        item.setText(datas[r][c])
        item.setTextAlignment(Qt.AlignCenter)
        tW.setItem(r, c, item)
  
    tW.setColumnWidth(0,100)

    self.vBox = QVBoxLayout()
    self.vBox.addWidget(tW)
    self.setLayout(self.vBox)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())



  