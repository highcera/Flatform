import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QGridLayout, QVBoxLayout
from PyQt5.QtGui import QFont, QIntValidator, QPalette, QColor
from PyQt5.QtCore import Qt, QRect

class EquipmentWidget(QWidget):
    def __init__(self, facility_name, unused_equipment, used_equipment):
        super().__init__()

        self.facility_name = facility_name
        self.unused_equipment = unused_equipment
        self.used_equipment = used_equipment

        self.initUI()

    def initUI(self):
        # Create a font for labels
        font = QFont()
        font.setBold(True)
        font.setPointSize(12)

        # Create a label for the facility name
        facility_label = QLabel(self.facility_name)
        facility_label.setFont(font)

        # Create a label for the unused equipment
        unused_label = QLabel("Unused Equipment")
        unused_label.setAlignment(Qt.AlignCenter)

        # Create a label for the used equipment
        used_label = QLabel("Used Equipment")
        used_label.setAlignment(Qt.AlignCenter)

        # Create a layout for the equipment widget
        layout = QGridLayout()

        # Add the facility label to the layout
        layout.addWidget(facility_label, 0, 0, 1, 2)

        # Add the unused equipment label to the layout
        layout.addWidget(unused_label, 1, 0)

        # Add the used equipment label to the layout
        layout.addWidget(used_label, 1, 1)

        # Add the unused equipment to the layout
        for i, equipment in enumerate(self.unused_equipment):
            label = QLabel(equipment)
            layout.addWidget(label, i+2, 0)

        # Add the used equipment to the layout
        for i, equipment in enumerate(self.used_equipment):
            label = QLabel(equipment)
            layout.addWidget(label, i+2, 1)

        # Set the layout for the widget
        self.setLayout(layout)

class MonthlyEquipmentStatusBoard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create the main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Create a font for labels
        font = QFont()
        font.setBold(True)
        font.setPointSize(12)

        # Create a label for the facilities
        facilities_label = QLabel("Facilities:")
        facilities_label.setFont(font)

        # Create a combobox for the facilities
        self.facilities_combobox = QComboBox()
        self.facilities_combobox.addItems(["Facility 1", "Facility 2"])

        # Create a label for the equipment
        equipment_label = QLabel("Equipment:")
        equipment_label.setFont(font)

        # Create a combobox for the equipment
        self.equipment_combobox = QComboBox()

        # Create a label for the start time
        start_time_label = QLabel("Start Time:")
        start_time_label.setFont(font)

        # Create a line edit for the start time
        self.start_time_edit = QLineEdit()
        self.start_time_edit.setValidator(QIntValidator(0, 23))

        # Create a label for the operation time
        operation_time_label = QLabel("Operation Time:")
        operation_time_label.setFont(font)

        # Create a line edit for the operation time
        self.operation_time_edit = QLineEdit()
        self.operation_time_edit.set
