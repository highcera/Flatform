import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget, QDateTimeEdit, QCalendarWidget
from PyQt5.QtCore import Qt, QDateTime, QTimeLine

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

        # 시작시간 입력 위젯 생성
        self.start_time_edit = QDateTimeEdit()
        self.start_time_edit.setDisplayFormat('yyyy-MM-dd hh:mm:ss')

        # 완료시간 입력 위젯 생성
        self.end_time_edit = QDateTimeEdit()
        self.end_time_edit.setDisplayFormat('yyyy-MM-dd hh:mm:ss')

        # 탭 위젯 생성
        self.tab_widget = QTabWidget()

        # 일간 예약 상황 탭 생성
        self.daily_calendar = QCalendarWidget()
        self.daily_timeline = QTimeLine(24 * 60 * 60 * 1000, self)
        self.daily_timeline.setFrameRange(0, 23)
        self.daily_timeline.frameChanged.connect(self.daily_timeline_frame_changed)
        self.tab_widget.addTab(self.daily_calendar, 'Daily')

        # 주간 예약 상황 탭 생성
        self.weekly_calendar = QCalendarWidget()
        self.weekly_timeline = QTimeLine(7 * 24 * 60 * 60 * 1000, self)
        self.weekly_timeline.setFrameRange(0, 6)
        self.weekly_timeline.frameChanged.connect(self.weekly_timeline_frame_changed)
        self.tab_widget.addTab(self.weekly_calendar, 'Weekly')

        # 월간 예약 상황 탭 생성
        self.monthly_calendar = QCalendarWidget()
        self.monthly_timeline = QTimeLine(30 * 24 * 60 * 60 * 1000, self)
        self.monthly_timeline.setFrameRange(0, 29)

    def show_daily_reservations(self, start_time, end_time):
        # 일간 예약 상황 탭을 업데이트합니다.
        self.daily_timeline.stop()
        self.daily_calendar.setSelectedDate(start_time.date())

        # 예약된 시간대를 하이라이트로 표시합니다.
        self.daily_timeline.setCurrentTime(0)
        for i in range(24):
            self.daily_calendar.setDateTextFormat(start_time.date().addDays(i), self.default_format)
        for start, end in self.reservations:
            if start.date() == start_time.date():
                start_frame = start.time().hour()
                end_frame = end.time().hour()
                if end.time().minute() > 0:
                    end_frame += 1
                for i in range(start_frame, end_frame):
                    self.daily_calendar.setDateTextFormat(start_time.date().addDays(start.daysTo(start_time.date()) + i), self.reservation_format)
                    self.daily_timeline.setFrameRange(start_frame, end_frame - 1)
                    self.daily_timeline.start()

    def show_weekly_reservations(self, start_time, end_time):
        # 주간 예약 상황 탭을 업데이트합니다.
        self.weekly_timeline.stop()
        self.weekly_calendar.setSelectedDate(start_time.date())

        # 예약된 시간대를 하이라이트로 표시합니다.
        self.weekly_timeline.setCurrentTime(0)
        for i in range(7):
            self.weekly_calendar.setDateTextFormat(start_time.date().addDays(i), self.default_format)
        for start, end in self.reservations:
            if start.date() >= start_time.date() and start.date() <= end_time.date():
                start_frame = start.date().daysTo(start_time.date()) * 24 + start.time().hour()
                end_frame = end.date().daysTo(start_time.date()) * 24 + end.time().hour()
                if end.time().minute() > 0:
                    end_frame += 1
                for i in range(start_frame, end_frame):
                    self.weekly_calendar.setDateTextFormat(start_time.date().addDays(i // 24), self.reservation_format)
                    self.weekly_timeline.setFrameRange(start_frame // 24, end_frame // 24 - 1)
                    self.weekly_timeline.start()

    def show_monthly_reservations(self, start_time, end_time):
        # 월간 예약 상황 탭을 업데이트합니다.
        self.monthly_timeline.stop()
        self.monthly_calendar.setSelectedDate(start_time.date())

        # 예약된 시간대를 하이라이트로 표시합니다.
        self.monthly_timeline.setCurrentTime(0)
        for i in range(start_time.date().daysInMonth()):
            self.monthly_calendar.setDateTextFormat(start_time.date().addDays(i), self.default_format)
        for start, end in self.reservations:
            if start.date() >= start_time.date() and start.date() <= end_time.date():
                start_frame = start.date().daysTo(start

                class ReservationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 시작시간 위젯을 만듭니다.
        self.start_label = QLabel('시작시간:')
        self.start_edit = QDateTimeEdit()
        self.start_edit.setDisplayFormat('yyyy-MM-dd HH:mm')
        self.start_edit.setMinimumDateTime(QDateTime.currentDateTime())

        # 완료시간 위젯을 만듭니다.
        self.end_label = QLabel('완료시간:')
        self.end_edit = QDateTimeEdit()
        self.end_edit.setDisplayFormat('yyyy-MM-dd HH:mm')
        self.end_edit.setMinimumDateTime(self.start_edit.dateTime())

        # 예약 버튼과 취소 버튼을 만듭니다.
        self.ok_button = QPushButton('예약')
        self.cancel_button = QPushButton('취소')
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        # 레이아웃을 만들고 위젯을 추가합니다.
        layout = QGridLayout()
        layout.addWidget(self.start_label, 0, 0)
        layout.addWidget(self.start_edit, 0, 1)
        layout.addWidget(self.end_label, 1, 0)
        layout.addWidget(self.end_edit, 1, 1)
        layout.addWidget(self.ok_button, 2, 0)
        layout.addWidget(self.cancel_button, 2, 1)
        self.setLayout(layout)

    def get_reservation(self):
        # 대화상자에서 시작시간과 완료시간을 입력받습니다.
        if self.exec_() == QDialog.Accepted:
            return self.start_edit.dateTime(), self.end_edit.dateTime()
        else:
            return None, None

    def reserve(self):
        # 선택된 설비가 없으면 메시지 박스를 엽니다.
        if self.selected_machine is None:
            QMessageBox.warning(self, '경고', '설비를 선택해주세요.')
            return

        # 예약 대화상자를 엽니다.
        dialog = ReservationDialog(self)
        start_time, end_time = dialog.get_reservation()
        if start_time and end_time:
            # 예약 리스트에 추가합니다.
            self.reservations.append((start_time, end_time))

            # 선택된 설비를 하이라이트로 표시합니다.
            self.machine_buttons[self.selected_machine].setStyleSheet('background-color: yellow')

            # 예약 상황을 업데이트합니다.
            self.update_reservations()
