import sys
from PyQt5.QtCore import Qt, QTime, QDate, QDateTime
from PyQt5.QtWidgets import (QDialog, QDialogButtonBox, QFormLayout, QComboBox, QDateTimeEdit, QApplication)

class ReservationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Reservation")
        self.resize(300, 150)

        layout = QFormLayout(self)

        # Add combo box for facility selection
        self.facility_combo_box = QComboBox(self)
        layout.addRow("Facility:", self.facility_combo_box)

        # Add start time and end time date time edits
        now = QDateTime.currentDateTime()
        self.start_time_edit = QDateTimeEdit(self)
        self.start_time_edit.setDisplayFormat("yyyy-MM-dd hh:mm")
        self.start_time_edit.setDateTime(now)
        self.start_time_edit.setCalendarPopup(True)
        layout.addRow("Start time:", self.start_time_edit)

        self.end_time_edit = QDateTimeEdit(self)
        self.end_time_edit.setDisplayFormat("yyyy-MM-dd hh:mm")
        self.end_time_edit.setDateTime(now)
        self.end_time_edit.setCalendarPopup(True)
        layout.addRow("End time:", self.end_time_edit)

        # Add buttons
        button_box = QDialogButtonBox(self)
        button_box.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(button_box)

        # Connect signals to slots
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

    def set_facilities(self, facilities):
        self.facility_combo_box.clear()
        self.facility_combo_box.addItems(facilities)

    def get_facility(self):
        return self.facility_combo_box.currentText()

    def get_start_time(self):
        return self.start_time_edit.dateTime()

    def get_end_time(self):
        return self.end_time_edit.dateTime()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReservationDialog()
    window.show()
    
    # Create reservation dialog and set available facilities
    reservation_dialog = ReservationDialog()
    reservation_dialog.set_facilities(["Facility 1", "Facility 2", "Facility 3"])

    # Show dialog and get user input
    if reservation_dialog.exec() == QDialog.Accepted:
        facility = reservation_dialog.get_facility()
        start_time = reservation_dialog.get_start_time()
        end_time = reservation_dialog.get_end_time()
        
        print(f"Facility: {facility}")
        print(f"Start time: {start_time.toString('yyyy-MM-dd hh:mm')}")
        print(f"End time: {end_time.toString('yyyy-MM-dd hh:mm')}")

    sys.exit(app.exec_())