from PyQt5.QtWidgets import QApplication
import sys
from ReserveDia import *

app = QApplication(sys.argv)

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

sys.exit(app.exec())
