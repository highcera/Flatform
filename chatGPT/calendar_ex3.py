from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QDate


class MyMain(QWidget):
    def __init__(self):
        super().__init__()

        holidays = ['20231003', '20231004', '20231005', '20231006', '20231009']

        vbox = QVBoxLayout()

        self.cal = QCalendarWidget()
        self.cal.setVerticalHeaderFormat(0)  # vertical header 숨기기

        fm = QTextCharFormat()
        fm.setForeground(Qt.red)
        fm.setBackground(Qt.yellow)

        for dday in holidays:
            dday2 = QDate.fromString(dday, "yyyyMMdd")
            self.cal.setDateTextFormat(dday2, fm)

        vbox.addWidget(self.cal)
        self.setLayout(vbox)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    myWindow = MyMain()

    myWindow.show()
    app.exec_()