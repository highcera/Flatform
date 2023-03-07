import sys
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QComboBox, QPushButton, QSpinBox, QGridLayout, QVBoxLayout, QHBoxLayout, QScrollArea,QCalendarWidget, QDialog, QMessageBox
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, QDate

class LEDBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create 2016 LED labels for 2 equipments (1008 for each equipment)
        self.led_labels = []
        for i in range(7*52):
            label = QLabel()
            label.setFixedSize(20, 20)
            label.setStyleSheet('background-color: gray; border: 1px solid black;')
            self.led_labels.append(label)

        # Create a scroll area for the LED labels
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Create a widget to hold the LED labels
        self.scroll_widget = QWidget()
        self.grid = QGridLayout()
        self.grid.setHorizontalSpacing(0)
        self.grid.setVerticalSpacing(0)
        self.scroll_widget.setLayout(self.grid)

        # create labels for weeks of the year
        self.week_labels = []
        for i in range(52):
            label2 = QLabel()
            label2.setFixedSize(20, 20)
            # label2.setStyleSheet('background-color: yellow; border: 1px solid black;')
            label2.setText(str(i+1))
            self.week_labels.append(label2)

        for i, label2 in enumerate(self.week_labels):
            self.scroll_widget.layout().addWidget(label2, i + 1, 0)

        # for i in range(52):
        #     self.scroll_widget.layout().addWidget(label(str(i+1)), i+1, 0)
        
        self.dow_labels = []
        weekdays = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
        for i in range(7):
            label3 = QLabel()
            label3.setFixedSize(20, 20)
            # label2.setStyleSheet('background-color: yellow; border: 1px solid black;')
            label3.setText(weekdays[i])
            self.dow_labels.append(label3)

        for i, label3 in enumerate(self.dow_labels):
            self.scroll_widget.layout().addWidget(label3, 0, i + 1)

        # create labels for days of the week
        # weekdays = ['Week', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        # for i in range(8):
        #     self.scroll_widget.layout().addWidget(QLabel(weekdays[i]), 0, i)

        self.update_led_labels()
     
        scroll_area.setWidget(self.scroll_widget)

        # Set the layout for the widget
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(scroll_area)
    
    def set_led(self, index, color):
        self.led_labels[index].setStyleSheet(f'background-color: {color}; border: 1px solid black;')
    
    def update_led_labels(self):
        for i, label in enumerate(self.led_labels):
            self.scroll_widget.layout().addWidget(label, (i // 7) + 1, (i % 7) + 1)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Create a central widget for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a LED board widget
        self.led_board = LEDBoard()
        
        # create calendar widgets for start and end dates
        self.start_cal = QCalendarWidget(self)
        self.start_cal.setGridVisible(True)
        self.start_cal.clicked[QDate].connect(self.startDateChanged)
        
        self.end_cal = QCalendarWidget(self)
        self.end_cal.setGridVisible(True)
        self.end_cal.clicked[QDate].connect(self.endDateChanged)
        
        # Create the period label
        self.period_label = QLabel(self)
        
        # create button to select dates
        self.select_btn = QPushButton('Select', self)
        self.select_btn.clicked.connect(self.select_dates)

        hbox = QHBoxLayout()    
        vbox = QVBoxLayout()
        hbox.addWidget(self.start_cal)
        hbox.addWidget(self.end_cal)
        hbox.addWidget(self.select_btn)       
        vbox.addLayout(hbox)
        vbox.addWidget(self.period_label)
        vbox.addWidget(self.led_board)

        # Set the window properties
        self.setGeometry(300, 100, 400, 800)
        self.setWindowTitle('Select 2 date - Display 7X52 matrix')

        central_widget.setLayout(vbox)

    def startDateChanged(self, date):
        # Update the start date when it is changed
        self.start_date = date

    def endDateChanged(self, date):
        # Update the end date when it is changed
        self.end_date = date   
            
    def showPeriod(self):
        # Show the selected period when the OK button is clicked
        try:
            period = f"Selected period: {self.start_date.toString('yyyy-MM-dd')} to {self.end_date.toString('yyyy-MM-dd')}"
            self.period_label.setText(period)
       
        except AttributeError:
            QMessageBox.warning(self, "Error", "Please select both start and end dates")
        
    def select_dates(self):
        # get selected start and end dates
        start_date = self.start_cal.selectedDate()
        end_date = self.end_cal.selectedDate()
        self.showPeriod()
        # get day of week and week of year for start and end dates
        # start_year = QDate.weekNumber(start_date)[1]
        start_week_of_year = QDate.weekNumber(start_date)[0]
        start_day_of_week = QDate.dayOfWeek(start_date)
        
        
        # end_year = QDate.weekNumber(end_date)[1]
        end_week_of_year = QDate.weekNumber(end_date)[0]
        end_day_of_week = QDate.dayOfWeek(end_date)

        print(start_week_of_year, start_day_of_week, end_week_of_year, end_day_of_week)
    
        # Initialize the status board to all off
        self.status_board = [0] * 7*52
        
        # create green dots for selected dates
        for week in range(start_week_of_year, end_week_of_year+1):
            if week == start_week_of_year:
                start_col = start_day_of_week # +1
            else:
                start_col = 1 #1
            if week == end_week_of_year:
                end_col = end_day_of_week
            else:
                end_col = 7
            for day in range(start_col, end_col+1):
                if self.status_board[(week-1)*7+day-1] == 0:
                    self.status_board[(week-1)*7+day-1] = 1

        # Update the status board display
        for i in range(7*52):
            if self.status_board[i] == 1:
                print('switch on :', i)
                self.led_board.set_led(i, 'red')
            else:
                print('switch off :', i)
                self.led_board.set_led(i, 'gray')

        self.led_board.update_led_labels()
        # for i, label in enumerate(self.board.led_labels):
        #     self.scroll_widget.layout().addWidget(label, (i // 7) + 1, (i % 7) + 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())