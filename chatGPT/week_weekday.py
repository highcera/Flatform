import datetime

# def get_week_of_year_and_weekday(date):
#     year, week, weekday = date.isocalendar()
#     return week, weekday

# # example usage
# date = datetime.date(2023, 2, 28)
# week, weekday = get_week_of_year_and_weekday(date)
# print(f"Week of year: {week}, Day of the week: {weekday}")

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QDate

class DotMatrix(QWidget):
    def __init__(self, param1, param2):
        self.day_week = param1
        self.week_year = param2
        print('init', self.day_week, self.week_year)
        
        super().__init__()
        self.initUI()

        
    def initUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Dot Matrix')
        
        grid = QGridLayout()
        self.setLayout(grid)
        
        # create labels for days of the week
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for i in range(7):
            grid.addWidget(QLabel(weekdays[i]), i, 0)
        
        # create labels for weeks of the year
        for i in range(52):
            grid.addWidget(QLabel(str(i+1)), 7, i+1)
        
        # create dot for today's date
        dot = QLabel()
        dot.setAutoFillBackground(True)
        p = dot.palette()
        p.setColor(dot.backgroundRole(), QColor(255, 0, 0))
        dot.setPalette(p)
        dot.setAlignment(Qt.AlignCenter)
        grid.addWidget(dot, self.day_week, self.week_year)
        
        self.show()
        
if __name__ == '__main__':
    # get current day of week and week of year
    today = datetime.datetime(2023, 3, 1)
    day_of_week = today.isoweekday()
    week_of_year = today.isocalendar()
    print(type(today), today, day_of_week, week_of_year[1])
    
    app = QApplication(sys.argv)
    dot_matrix = DotMatrix(day_of_week-1, week_of_year[1])       

    sys.exit(app.exec_())
