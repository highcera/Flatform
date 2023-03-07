import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QComboBox, QPushButton, QSpinBox, QGridLayout, QVBoxLayout, QHBoxLayout, QScrollArea
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

class LEDBoard(QWidget):
    def __init__(self):
        super().__init__()

        # Create 2016 LED labels for 2 equipments (1008 for each equipment)
        self.led_labels = []
        for i in range(2016):
            label = QLabel()
            label.setFixedSize(10, 10)
            label.setStyleSheet('background-color: gray; border: 1px solid black;')
            self.led_labels.append(label)

        # Create a scroll area for the LED labels
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Create a widget to hold the LED labels
        scroll_widget = QWidget()
        scroll_widget.setLayout(QGridLayout())

        for i, label in enumerate(self.led_labels):
            scroll_widget.layout().addWidget(label, i // 144, i % 144)
            # if col % 12 == 0:
            #     col += 1

        scroll_area.setWidget(scroll_widget)

        # Set the layout for the widget
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(scroll_area)

    def set_led(self, index, color):
        self.led_labels[index].setStyleSheet(f'background-color: {color}; border: 1px solid black;')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a LED board widget
        self.led_board = LEDBoard()

        # Create a combo box to select the equipment
        self.equipment_combo = QComboBox()
        self.equipment_combo.addItems(['Equipment 1', 'Equipment 2'])

        # Create spin boxes to enter the start time and operation time
        self.start_time_spin = QSpinBox()
        self.start_time_spin.setRange(0, 1008)
        self.start_time_spin.setValue(0)

        self.operation_time_spin = QSpinBox()
        self.operation_time_spin.setRange(1, 1008)
        self.operation_time_spin.setValue(1)

        # Create a push button to start the operation
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_operation)

        # Create a layout for the central widget
        vbox = QVBoxLayout()
        vbox.addWidget(self.led_board)

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel('Equipment:'))
        hbox.addWidget(self.equipment_combo)
        hbox.addWidget(QLabel('Start time:'))
        hbox.addWidget(self.start_time_spin)
        hbox.addWidget(QLabel('Operation time:'))
        hbox.addWidget(self.operation_time_spin)
        hbox.addWidget(self.start_button)

        vbox.addLayout(hbox)
        central_widget.setLayout(vbox)

    
    def start_operation(self):
        # Initialize the status board to all off
        self.status_board = [0] * 2016

        # Get the selected equipment and operation time
        equipment = self.equipment_combo.currentIndex()
        start_time = self.start_time_spin.value()
        operation_time = self.operation_time_spin.value()

        
        # Turn on the LEDs corresponding to the operation time for the selected equipment
        for i in range(operation_time):
            index = start_time + i
            if self.status_board[(equipment * 1008) + index] == 0:
                self.status_board[(equipment * 1008) + index] = 1

        # Update the status board display
        for i in range(1008):
            if self.status_board[(equipment * 1008) + i] == 1:
                if equipment == 0:
                    self.led_board.set_led((equipment * 1008) + i, 'green')
                else:
                    self.led_board.set_led((equipment * 1008) + i, 'red')
            else:
                self.led_board.set_led((equipment * 1008) + i, 'gray')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())