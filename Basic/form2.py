import sys
from PyQt5.QtWidgets import *
from form_widget import Ui_Form

class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
     
        for year in range(1900, 2021):
            self.year_widget.addItem(str(year))
        for month in range(1, 13):
            self.month_widget.addItem(str(month))
        for date in range(1, 32):
            self.date_widget.addItem(str(date))
  
        self.address_1.addItems(["Seoul", "Daejeon", "Daegu", "Busan"])
        self.email_combobox.addItems(["google.com", "naver.com", "daum.net"])
        
        # self.label_5.setText("@")
        # self.label_7.setText("-")
        # self.label_8.setText("-")
        # self.checkBox.setText("Agree?")

        # self.resize(500, 500)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec_()
