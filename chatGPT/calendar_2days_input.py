import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QDate

class CalendarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Cselfreate the start date calendar widget
        self.start_cal = QCalendarWidget(self)
        # self.start_cal.setVerticalHeaderFormat(0)  # vertical header 숨기기
        self.start_cal.setGridVisible(True)
        self.start_cal.clicked[QDate].connect(self.startDateChanged)

        # Create the end date calendar widget
        self.end_cal = QCalendarWidget(self)
        self.end_cal.setGridVisible(True)
        self.end_cal.clicked[QDate].connect(self.endDateChanged)

        # Create the period label
        self.period_label = QLabel(self)

        # Create the OK button
        self.ok_button = QPushButton('OK', self)
        preiod = self.ok_button.clicked.connect(self.showPeriod)

        # Create the layout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_cal)
        hbox.addWidget(self.end_cal)
        vbox.addLayout(hbox)
        vbox.addWidget(self.period_label)
        vbox.addWidget(self.ok_button)
        self.setLayout(vbox)

        # Set the window properties
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Select Period')
        # self.show()

    def startDateChanged(self, date):
        # Update the start date when it is changed
        # self.display_sel(1, date)
        self.start_date = date

    def endDateChanged(self, date):
        # Update the end date when it is changed
        # self.display_sel(2, date)
        self.end_date = date

    def display_sel(self, cal, date):  
        fm = QTextCharFormat()
        fm.setForeground(Qt.blue)
        fm.setBackground(Qt.yellow)

        if cal == 1:
            self.start_cal.setDateTextFormat(date, fm)
        else:            
            self.end_cal.setDateTextFormat(date, fm)

    def showPeriod(self):
        # Show the selected period when the OK button is clicked
        try:
            self.display_sel(1, self.start_date)
            self.display_sel(2, self.end_date)
            period = f"Selected period: {self.start_date.toString('yyyy-MM-dd')} to {self.end_date.toString('yyyy-MM-dd')}"
            self.period_label.setText(period)
            return(period)
        except AttributeError:
            QMessageBox.warning(self, "Error", "Please select both start and end dates")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalendarWidget()
    ex.show()
    sys.exit(app.exec_())
