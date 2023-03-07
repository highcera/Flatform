import sys
from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class TabDemo(QTabWidget):
    def __init__(self):
        super().__init__()

        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")

        self.tab1UI()
        self.tab2UI()

        self.setWindowTitle("Tab Demo")

    def tab1UI(self):
        layout = QVBoxLayout()
        table_view = QTableView()
        table_model = QStandardItemModel()

        # Set table header
        table_model.setHorizontalHeaderLabels(['Value 1', 'Value 2', 'Value 3', 'Value 4'])

        # Set table data
        for row in range(4):
            for col in range(4):
                item = QStandardItem(str((row+1)*(col+1)*10))
                table_model.setItem(row, col, item)

        table_view.setModel(table_model)

        layout.addWidget(table_view)
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
        table_view = QTableView()
        table_model = QStandardItemModel()

        # Set table header
        table_model.setHorizontalHeaderLabels(['Fruit 1', 'Fruit 2', 'Fruit 3', 'Fruit 4'])

        # Set table data
        fruits = ['Apple', 'Banana', 'Cherry', 'Durian']
        for row, fruit in enumerate(fruits):
            for col in range(4):
                item = QStandardItem(fruit)
                table_model.setItem(row, col, item)

        table_view.setModel(table_model)

        layout.addWidget(table_view)
        self.tab2.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TabDemo()
    demo.show()
    sys.exit(app.exec_())
