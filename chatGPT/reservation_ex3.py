import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDateTime, QDate, QTime
from ReserveDia import *

class ReservationSystem(QMainWindow):
    def __init__(self):
        super().__init__()

        # 예약 정보를 저장할 리스트를 생성합니다.
        self.reservations = []

        # 현재 선택된 예약 날짜를 저장할 변수를 생성합니다.
        self.current_start_time = QDateTime.currentDateTime().addDays(-1).date()
        self.current_end_time = QDateTime.currentDateTime().date()

        # 메뉴바를 생성합니다.
        menu_bar = self.menuBar()

        # 일간, 주간, 월간 메뉴를 생성합니다.
        daily_menu = menu_bar.addMenu('일간')
        weekly_menu = menu_bar.addMenu('주간')
        monthly_menu = menu_bar.addMenu('월간')

        # 일간 메뉴에 액션을 추가합니다.
        daily_action = daily_menu.addAction('보기')
        daily_action.triggered.connect(self.show_daily_reservations)

        # 주간 메뉴에 액션을 추가합니다.
        weekly_action = weekly_menu.addAction('보기')
        weekly_action.triggered.connect(self.show_weekly_reservations)

        # 월간 메뉴에 액션을 추가합니다.
        monthly_action = monthly_menu.addAction('보기')
        monthly_action.triggered.connect(self.show_monthly_reservations)

        # GUI 화면을 생성합니다.
        self.init_ui()

    def init_ui(self):
        # 윈도우 타이틀을 설정합니다.
        self.setWindowTitle('설비 예약 시스템')

        # 일간 예약 상황을 보여줄 그룹박스를 생성합니다.
        daily_group_box = QGroupBox('일간 예약 현황', self)
        daily_layout = QVBoxLayout(daily_group_box)

        # 일간 예약 상황을 보여줄 달력 위젯을 생성합니다.
        daily_calendar = QCalendarWidget(daily_group_box)
        daily_calendar.setGridVisible(True)
        daily_calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        daily_calendar.setMinimumDate(QDate.currentDate().addDays(-365))
        daily_calendar.setMaximumDate(QDate.currentDate().addDays(365))
        daily_calendar.clicked.connect(self.select_daily_date)
        daily_layout.addWidget(daily_calendar)

        # 주간 예약 상황을 보여줄 그룹박스를 생성합니다.
        weekly_group_box = QGroupBox('주간 예약 현황', self)
        weekly_layout = QVBoxLayout(weekly_group_box)

        # 주간 예약 상황을 보여줄 달력 위젯을 생성합니다.
        weekly_calendar = QCalendarWidget(weekly_group_box)
        weekly_calendar.setGridVisible(True)
        weekly_calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        weekly_calendar.setMinimumDate(QDate.currentDate().addDays(-365))
        weekly_calendar.setMaximumDate(QDate.currentDate().addDays(365))
        weekly_calendar.clicked.connect(self.select_weekly_date)
        weekly_layout.addWidget(weekly_calendar)

        # 월간 예약 상황을 보여줄 그룹박스를 생성합니다.
        monthly_group_box = QGroupBox('월간 예약 현황', self)
        monthly_layout = QVBoxLayout(monthly_group_box)

        # 월간 예약 상황을 보여줄 달력 위젯을 생성합니다.
        monthly_calendar = QCalendarWidget(monthly_group_box)
        monthly_calendar.setGridVisible(True)
        monthly_calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        monthly_calendar.setMinimumDate(QDate.currentDate().addDays(-365))
        monthly_calendar.setMaximumDate(QDate.currentDate().addDays(365))
        monthly_calendar.clicked.connect(self.select_monthly_date)
        monthly_layout.addWidget(monthly_calendar)

        # 설비 예약 버튼들을 생성합니다.
        button_1 = QPushButton('1번 설비')
        button_2 = QPushButton('2번 설비')
        button_3 = QPushButton('3번 설비')
        button_4 = QPushButton('4번 설비')
        button_5 = QPushButton('5번 설비')
        button_6 = QPushButton('6번 설비')

        # 설비 예약 버튼들을 그리드 레이아웃에 추가합니다.
        grid_layout = QGridLayout()
        grid_layout.addWidget(button_1, 0, 0)
        grid_layout.addWidget(button_2, 0, 1)
        grid_layout.addWidget(button_3, 1, 0)
        grid_layout.addWidget(button_4, 1, 1)
        grid_layout.addWidget(button_5, 2, 0)
        grid_layout.addWidget(button_6, 2, 1)

        # 설비 예약 버튼들의 크기를 조절합니다.
        for button in [button_1, button_2, button_3, button_4, button_5, button_6]:
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 설비 예약 버튼들에 대한 예약 시간을 보여줄 그룹박스를 생성합니다.
        reservation_group_box = QGroupBox('설비 예약 현황', self)
        reservation_layout = QHBoxLayout(reservation_group_box)
        reservation_layout.addLayout(grid_layout)

        # 예약 정보를 보여줄 레이블을 생성합니다.
        reservation_info_label = QLabel('', self)
        reservation_info_label.setAlignment(Qt.AlignCenter)
        reservation_layout.addWidget(reservation_info_label)

        # 예약 정보를 입력할 다이얼로그를 생성합니다.
        self.reservation_dialog = ReservationDialog(self)

        # 설비 예약 버튼들에 대한 클릭 이벤트를 설정합니다.
        button_1.clicked.connect(lambda: self.reserve_equipment(1))
        button_2.clicked.connect(lambda: self.reserve_equipment(2))
        button_3.clicked.connect(lambda: self.reserve_equipment(3))
        button_4.clicked.connect(lambda: self.reserve_equipment(4))
        button_5.clicked.connect(lambda: self.reserve_equipment(5))
        button_6.clicked.connect(lambda: self.reserve_equipment(6))

        # 메인 윈도우 레이아웃을 설정합니다.
        main_layout = QHBoxLayout()
        main_layout.addWidget(daily_group_box)
        main_layout.addWidget(weekly_group_box)
        main_layout.addWidget(monthly_group_box)
        main_layout.addWidget(reservation_group_box)
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # 윈도우 크기와 위치를 설정합니다.
        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle('설비 예약 시스템')

    def reserve_equipment(self, equipment_number):
        """설비를 예약합니다."""
        # 예약 정보를 입력할 다이얼로그를 실행합니다.
        if self.reservation_dialog.exec():
            start_time = self.reservation_dialog.get_start_time.time()
            end_time = self.reservation_dialog.get_end_time.time()

            # 예약 정보에 따라 예약 현황을 갱신합니다.
            for time_slot in self.time_slots:
                if time_slot.start_time <= start_time and time_slot.end_time > start_time:
                    if time_slot.equipment_number == equipment_number:
                        QMessageBox.warning(self, '예약 오류', '이미 해당 시간에 해당 설비가 예약되어 있습니다.')
                        return
                    else:
                        QMessageBox.warning(self, '예약 오류', '해당 시간에 다른 설비가 이미 예약되어 있습니다.')
                        return
                elif time_slot.start_time < end_time and time_slot.end_time >= end_time:
                    if time_slot.equipment_number == equipment_number:
                        QMessageBox.warning(self, '예약 오류', '이미 해당 시간에 해당 설비가 예약되어 있습니다.')
                        return
                    else:
                        QMessageBox.warning(self, '예약 오류', '해당 시간에 다른 설비가 이미 예약되어 있습니다.')
                        return

            # 예약 정보에 따라 예약 현황을 갱신합니다.
            for time_slot in self.time_slots:
                if time_slot.equipment_number == equipment_number and time_slot.start_time == start_time and time_slot.end_time == end_time:
                    QMessageBox.warning(self, '예약 오류', '이미 해당 시간에 해당 설비가 예약되어 있습니다.')
                    return

            time_slot = TimeSlot(equipment_number, start_time, end_time)
            self.time_slots.append(time_slot)

            # 예약 현황 레이블을 갱신합니다.
            self.update_reservation_info_label()

    def select_daily_date(self, date):
        """일간 예약 상황을 선택한 날짜에 맞게 갱신합니다."""
        self.selected_date = date
        self.update_reservation_info_label()

    def select_weekly_date(self, date):
        """주간 예약 상황을 선택한 날짜에 맞게 갱신합니다."""
        self.selected_date = date
        self.update_reservation_info_label()

    def select_monthly_date(self, date):
        """월간 예약 상황을 선택한 날짜에 맞게 갱신합니다."""
        self.selected_date = date
        self.update_reservation_info_label()

    def update_reservation_info_label(self):
        """예약 현황 레이블을 갱신합니다."""
        if isinstance(self.selected_date, QDate):
            # 일간 예약 상황을 선택한 경우
            reservation_info = f'{self.selected_date.toString("yyyy년 MM월 dd일")} 일간 예약 상황\n\n'
            for time_slot in self.time_slots:
                if time_slot.start_time.date() == self.selected_date and time_slot.equipment_number not in self.reserved_equipment_numbers:
                    reservation_info += f'{time_slot.equipment_number}번 설비: {time_slot.start_time.toString("hh:mm")} ~ {time_slot.end_time.toString("hh:mm")}\n'
                self.reservation_info_label.setText(reservation_info)

        elif isinstance(self.selected_date, tuple):
            # 주간 예약 상황을 선택한 경우
            start_date, end_date = self.selected_date
            reservation_info = f'{start_date.toString("yyyy년 MM월 dd일")} ~ {end_date.toString("yyyy년 MM월 dd일")} 주간 예약 상황\n\n'
            for time_slot in self.time_slots:
                if start_date <= time_slot.start_time.date() <= end_date and time_slot.equipment_number not in self.reserved_equipment_numbers:
                    reservation_info += f'{time_slot.equipment_number}번 설비: {time_slot.start_time.toString("yyyy년 MM월 dd일 hh:mm")} ~ {time_slot.end_time.toString("yyyy년 MM월 dd일 hh:mm")}\n'

            self.reservation_info_label.setText(reservation_info)

        elif isinstance(self.selected_date, QDate):
            # 월간 예약 상황을 선택한 경우
            year = self.selected_date.year()
            month = self.selected_date.month()
            reservation_info = f'{year}년 {month}월 월간 예약 상황\n\n'
            for time_slot in self.time_slots:
                if time_slot.start_time.year() == year and time_slot.start_time.month() == month and time_slot.equipment_number not in self.reserved_equipment_numbers:
                    reservation_info += f'{time_slot.start_time.toString("dd일 hh:mm")} ~ {time_slot.end_time.toString("dd일 hh:mm")}: {time_slot.equipment_number}번 설비\n'

            self.reservation_info_label.setText(reservation_info)

    def clear_reservation_info(self):
        """예약 현황을 초기화합니다."""
        self.time_slots.clear()
        self.update_reservation_info_label()

    def show_daily_reservations(self):
        """일간 예약 상황을 보여줍니다."""
        selected_date, ok = QInputDialog.getDate(self, '일간 예약 상황', '날짜를 선택하세요.', QDate.currentDate())
        if ok:
            self.select_daily_date(selected_date)

    def show_weekly_reservations(self):
        """주간 예약 상황을 보여줍니다."""
        today = QDate.currentDate()
        start_of_week = today.addDays(-today.dayOfWeek() + 1)
        end_of_week = start_of_week.addDays(6)
        selected_date_range, ok = QInputDialog.getItem(self, '주간 예약 상황', '주를 선택하세요.',
                                                        [f'{start_of_week.toString("yyyy년 MM월 dd일")} ~ {end_of_week.toString("yyyy년 MM월 dd일")}',
                                                        f'{start_of_week.addDays(7).toString("yyyy년 MM월 dd일")} ~ {end_of_week.addDays(7).toString("yyyy년 MM월 dd일")}',
                                                        f'{start_of_week.addDays(14).toString("yyyy년 MM월 dd일")} ~ {end_of_week.addDays(14).toString("yyyy년 MM월 dd일")}'])
        if ok:
            if selected_date_range == f'{start_of_week.toString("yyyy년 MM월 dd일")} ~ {end_of_week.toString("yyyy년 MM월 dd일")}':
                self.select_weekly_date((start_of_week, end_of_week))

            elif selected_date_range == f'{start_of_week.addDays(7).toString("yyyy년 MM월 dd일")} ~ {end_of_week.addDays(7).toString("yyyy년 MM월 dd일")}':
                self.select_weekly_date((start_of_week.addDays(7), end_of_week.addDays(7)))
            elif selected_date_range == f'{start_of_week.addDays(14).toString("yyyy년 MM월 dd일")} ~ {end_of_week.addDays(14).toString("yyyy년 MM월 dd일")}':
                self.select_weekly_date((start_of_week.addDays(14), end_of_week.addDays(14)))

    def show_monthly_reservations(self):
        """월간 예약 상황을 보여줍니다."""
        selected_date, ok = QInputDialog.getDate(self, '월간 예약 상황', '날짜를 선택하세요.', QDate.currentDate())
        if ok:
            self.select_monthly_date(selected_date)

    def show_reservation_dialog(self):
        """예약 다이얼로그를 보여줍니다."""
        reservation_dialog = ReservationDialog(self)
        if reservation_dialog.exec_():
            self.time_slots.append(reservation_dialog.time_slot)
            self.update_reservation_info_label()

    def cancel_reservation(self):
        """예약을 취소합니다."""
        selected_indexes = self.reservation_table.selectedIndexes()
        if selected_indexes:
            selected_time_slot_index = selected_indexes[0].row()
            self.time_slots.pop(selected_time_slot_index)
            self.update_reservation_info_label()

    def update_reservation_info_label(self):
        """예약 현황 레이블을 업데이트합니다."""
        self.reserved_equipment_numbers = [time_slot.equipment_number for time_slot in self.time_slots]
        self.update_reservation_info()

    def closeEvent(self, event):
        """프로그램을 종료할 때 예약 정보를 저장합니다."""
        with open('reservation_data.json', 'w') as f:
            time_slot_dicts = [time_slot.__dict__ for time_slot in self.time_slots]
            json.dump(time_slot_dicts, f)

        super().closeEvent(event)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReservationSystem()
    window.show()
    sys.exit(app.exec_())