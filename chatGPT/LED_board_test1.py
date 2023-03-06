import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit


class LEDBoard(QWidget):
    def __init__(self, parent=None):
        super(LEDBoard, self).__init__(parent)
        self.status = [0] * 1008  # 7 days x 24 hours x 6 10-minute blocks
        self.setMinimumSize(500, 100)

    def setStatus(self, start_time, duration):
        # Clear the status board
        self.status = [0] * 1008

        # Calculate the start and end blocks
        start_block = int(start_time / 10)
        end_block = int((start_time + duration) / 10)

        # Set the status for the corresponding blocks
        for block in range(start_block, end_block + 1):
            self.status[block] = 1

        # Update the display
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        block_size = min(self.width() / 1008, self.height())
        for i in range(1008):
            if self.status[i] == 1:
                painter.fillRect(i * block_size, 0, block_size, self.height(), QColor(255, 0, 0))
            else:
                painter.fillRect(i * block_size, 0, block_size, self.height(), QColor(255, 255, 255))


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create the combo box to select the equipment
        self.equipmentComboBox = QComboBox(self)
        self.equipmentComboBox.setGeometry(10, 10, 150, 30)
        self.equipmentComboBox.addItems(['Equipment 1', 'Equipment 2'])

        # Create the start time input field
        self.startTimeLabel = QLabel('Start time:', self)
        self.startTimeLabel.setGeometry(10, 50, 80, 30)
        self.startTimeInput = QLineEdit(self)
        self.startTimeInput.setGeometry(100, 50, 80, 30)

        # Create the operation time input field
        self.operationTimeLabel = QLabel('Operation time:', self)
        self.operationTimeLabel.setGeometry(200, 50, 100, 30)
        self.operationTimeInput = QLineEdit(self)
        self.operationTimeInput.setGeometry(310, 50, 80, 30)

        # Create the LED status board
        self.ledBoard = LEDBoard(self)
        self.ledBoard.setGeometry(10, 100, 480, 30)

        # Create the update button
        self.updateButton = QLabel('Update', self)
        self.updateButton.setGeometry(400, 50, 80, 30)
        self.updateButton.setAlignment(Qt.AlignCenter)
        self.updateButton.setStyleSheet('background-color: yellow;')
        self.updateButton.mousePressEvent = self.updateStatus

        self.setGeometry(100, 100, 500, 150)
        self.setWindowTitle('Equipment Status Board')
        self.show()

    def updateStatus(self, event):
        start_time = int(self.startTimeInput.text())
        operation_time = int(self.operationTimeInput.text())
        self.ledBoard.setStatus(start_time, operation_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())