import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QCalendarWidget, QPushButton, QDialog, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QDate

class DotMatrix(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Dot Matrix')
        
        self.grid = QGridLayout()
        self.grid.setHorizontalSpacing(1)
        self.setLayout(self.grid)
        
        # create labels for weeks of the year
        for i in range(52):
            self.grid.addWidget(QLabel(str(i+1)), i+1, 0)
        
        # create labels for days of the week
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for i in range(7):
            self.grid.addWidget(QLabel(weekdays[i]), 0, i+1)
        
        self.show()
        
    def update_dates(self, start_date, end_date):
        # get day of week and week of year for start and end dates
        start_day_of_week = start_date.dayOfWeek() - 1
        end_day_of_week = end_date.dayOfWeek() - 1
        start_week_of_year = start_date.weekNumber()[0] - 1
        end_week_of_year = end_date.weekNumber()[0] - 1
        
        # create green dots for selected dates
        for week in range(start_week_of_year, end_week_of_year+1):
            if week == start_week_of_year:
                start_row = start_day_of_week  # +1
            else:
                start_row = 0 #1
            if week == end_week_of_year:
                end_row = end_day_of_week + 1
            else:
                end_row = 7
            for day in range(start_row, end_row):
                dot = QLabel()
                dot.setAutoFillBackground(True)
                p = dot.palette()
                p.setColor(dot.backgroundRole(), QColor(0, 255, 0))
                dot.setPalette(p)
                dot.setAlignment(Qt.AlignCenter)
                self.grid.addWidget(dot, week+1, day+1)

class DateInput(QDialog):
    def __init__(self, dot_matrix):
        super().__init__()
        self.dot_matrix = dot_matrix
        self.initUI()
        
    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        
        # create calendar widgets for start and end dates
        self.start_calendar = QCalendarWidget(self)
        self.start_calendar.setGridVisible(True)
        vbox.addWidget(self.start_calendar)
        
        self.end_calendar = QCalendarWidget(self)
        self.end_calendar.setGridVisible(True)
        vbox.addWidget(self.end_calendar)
        
        # create button to select dates
        self.select_btn = QPushButton('Select', self)
        self.select_btn.clicked.connect(self.select_dates)
        vbox.addWidget(self.select_btn)
        
        self.show()
        
    def select_dates(self):
        # get selected start and end dates
        start_date = self.start_calendar.selectedDate()
        end_date = self.end_calendar.selectedDate()
        self.dot_matrix.update_dates(start_date, end_date)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dot_matrix = DotMatrix()
    date_input = DateInput(dot_matrix)
    sys.exit(app.exec_())