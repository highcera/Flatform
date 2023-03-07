import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton

class EquipmentReservationSystem(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 설비 예약 버튼 생성
        self.reservation_buttons = []
        for i in range(6):
            button = QPushButton('Equipment {}'.format(i+1))
            button.clicked.connect(lambda checked, index=i: self.reserve(index))
            self.reservation_buttons.append(button)

        # 예약 현황 레이블 생성
        self.reservation_status = QLabel('')

        # 레이아웃 생성
        vbox = QVBoxLayout()
        for button in self.reservation_buttons:
            vbox.addWidget(button)
        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addWidget(self.reservation_status)
        self.setLayout(hbox)

        # 창 설정
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Equipment Reservation System')
        self.show()

    def reserve(self, index):
        self.reservation_status.setText('Equipment {} is reserved.'.format(index+1))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EquipmentReservationSystem()
    sys.exit(app.exec_())
