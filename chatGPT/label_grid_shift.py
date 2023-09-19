import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton

class LabelGrid(QWidget):
    def __init__(self):
        super().__init__()
        
        # Initialize the label grid
        self.labels = [QLabel(str(i+1)) for i in range(100)]

        self.grid_layout = QHBoxLayout()
        self.startP = 0
        self.update_show_labels()

        # self.setLayout(self.grid_layout)
        
        # Initialize the buttons
        self.left_button = QPushButton('<')
        self.left_button.clicked.connect(lambda: self.shift_labels(-1))
        self.double_left_button = QPushButton('<<')
        self.double_left_button.clicked.connect(lambda: self.shift_labels(-10))
        self.right_button = QPushButton('>')
        self.right_button.clicked.connect(lambda: self.shift_labels(1))
        self.double_right_button = QPushButton('>>')
        self.double_right_button.clicked.connect(lambda: self.shift_labels(10))
        
        # Create the button layout
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.double_left_button)
        self.button_layout.addWidget(self.left_button)
        self.button_layout.addWidget(self.right_button)
        self.button_layout.addWidget(self.double_right_button)
        
        # Create the main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.grid_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)
        
    def shift_labels(self, shift):
        # Move the labels by the specified shift amount
        self.startP += shift
        if self.startP < 0: 
            self.startP = 0
        elif self.startP > 75: 
            self.startP = 75  
        
        self.update_show_labels()  
       
        # self.labels = show_labels
        # self.grid_layout = QHBoxLayout()
        # for label in self.labels:
        #     self.grid_layout.addWidget(label)
        # self.setLayout(self.grid_layout)

    def update_show_labels(self):
        self.show_label=[]
        for i, label in enumerate(self.labels[self.startP:self.startP+25]):
            self.show_label.append(label)

        self.grid_layout.addWidget(self.show_label)
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    grid = LabelGrid()
    grid.show()
    sys.exit(app.exec_())
