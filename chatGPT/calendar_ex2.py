import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QCalendarWidget, QMessageBox
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QDate, Qt, QRect

class LEDDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Initialize the start and end dates
        self.start_date = None
        self.end_date = None

        # Create the start date calendar widget
        self.start_calendar = QCalendarWidget(self)
        self.start_calendar.setGridVisible(True)
        self.start_calendar.clicked[QDate].connect(self.startDateChanged)

        # Create the end date calendar widget
        self.end_calendar = QCalendarWidget(self)
        self.end_calendar.setGridVisible(True)
        self.end_calendar.clicked[QDate].connect(self.endDateChanged)

        # Create the OK button
        self.ok_button = QPushButton('OK', self)
        self.ok_button.clicked.connect(self.showPeriod)

        # Create the layout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_calendar)
        hbox.addWidget(self.end_calendar)
        vbox.addLayout(hbox)
        vbox.addWidget(self.ok_button)
        self.setLayout(vbox)

        # Set the window properties
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('LED Display')
        self.show()

    def startDateChanged(self, date):
        # Update the start date when it is changed
        self.start_date = date

    def endDateChanged(self, date):
        # Update the end date when it is changed
        self.end_date = date

    def showPeriod(self):
        # Show the selected period on the LED display when the OK button is clicked
        try:
            # Get the start and end dates
            start_date = self.start_date
            end_date = self.end_date

            # Check that both dates are selected
            if not (start_date and end_date):
                raise AttributeError("Please select both start and end dates")

            # Sort the dates so that start_date <= end_date
            if start_date > end_date:
                start_date, end_date = end_date, start_date

            # Update the LED display
            self.update()

        except AttributeError as e:
            QMessageBox.warning(self, "Error", str(e))

    def paintEvent(self, event):
        # Draw the LED display
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Define the size and position of each LED
        led_width = self.width() / 1008
        led_height = self.height() / 52

        # Define the color of the LEDs
        on_color = QColor(Qt.green)
        off_color = QColor(Qt.black)

        # Draw each LED on the display
        for week in range(52):
            for minute in range(1008):
                led_x = minute * led_width
                led_y = week * led_height

                # Check if the current minute is within the selected period
                current_date = QDate.currentDate().addDays(week * 7).addDays(minute // 1440)
                if self.start_date and self.end_date and self.start_date <= current_date <= self.end_date:
                    painter.fillRect(QRect(led_x, led_y, led_width, led_height), on_color)
                else:
                    painter.fillRect(QRect(led_x, led_y, led_width, led_height), off_color)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LEDDisplay()
    sys.exit(app.exec_())