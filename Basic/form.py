import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QFormLayout()

        name_widget = QLineEdit()
        birthday_layout = QHBoxLayout()
        year_widget = QComboBox()
        month_widget = QComboBox()
        date_widget = QComboBox()

        birthday_layout.addWidget(year_widget)
        birthday_layout.addWidget(month_widget)
        birthday_layout.addWidget(date_widget)

        for year in range(1900, 2021):
            year_widget.addItem(str(year))
        for month in range(1, 13):
            month_widget.addItem(str(month))
        for date in range(1, 32):
            date_widget.addItem(str(date))

        address_layout = QVBoxLayout()
        address_1 = QComboBox()
        address_1.addItems(["Seoul", "Daejeon", "Daegu", "Busan"])
        address_2 = QLineEdit()
        address_layout.addWidget(address_1)
        address_layout.addWidget(address_2)

        email_layout = QHBoxLayout()
        email_id = QLineEdit()
        email_company = QLineEdit()
        email_combobox = QComboBox()
        email_combobox.addItems(["google.com", "naver.com", "daum.net"])
        email_layout.addWidget(email_id)
        email_layout.addWidget(QLabel("@"))
        email_layout.addWidget(email_company)
        email_layout.addWidget(email_combobox)

        phone_number_layout = QHBoxLayout()
        phone_number_layout.addWidget(QLineEdit())
        phone_number_layout.addWidget(QLabel("-"))
        phone_number_layout.addWidget(QLineEdit())
        phone_number_layout.addWidget(QLabel("-"))
        phone_number_layout.addWidget(QLineEdit())

        height_widget = QSpinBox()
        height_widget.setMaximum(250)

        personal_info = QCheckBox("Agree?")

        self_intro = QPlainTextEdit()

        save_cancel_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        cancel_button = QPushButton("Cancel")
        save_cancel_layout.addWidget(save_button)
        save_cancel_layout.addWidget(cancel_button)

        main_layout.addRow("Name: ", name_widget)
        main_layout.addRow("Birthday: ", birthday_layout)
        main_layout.addRow("Address: ", address_layout)
        main_layout.addRow("E-mail: ", email_layout)
        main_layout.addRow("Phone Number: ", phone_number_layout)
        main_layout.addRow("Height(cm): ", height_widget)
        main_layout.addRow("Personal Information Share: ", personal_info)
        main_layout.addRow("Self Introduction: ", self_intro)
        main_layout.addRow("", save_cancel_layout)

        self.setLayout(main_layout)
        self.resize(500, 500)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
