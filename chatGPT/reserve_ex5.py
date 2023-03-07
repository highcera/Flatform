import sys
from PyQt5.QtWidgets import QApplication
from monthly_equipment_status_board import MonthlyEquipmentStatusBoard

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the monthly equipment status board
    monthly_equipment_status_board = MonthlyEquipmentStatusBoard()

    # Set the window properties
    monthly_equipment_status_board.setGeometry(100, 100, 600, 400)
    monthly_equipment_status_board.setWindowTitle("Monthly Equipment Status Board")
    monthly_equipment_status_board.show()

    sys.exit(app.exec_())
