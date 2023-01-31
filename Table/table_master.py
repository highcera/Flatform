import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QGridLayout, QTableWidgetItem

class MainScreen(QMainWindow):
    def __init__(self, wid, hei):
        super().__init__()

        self.setWindowTitle("TEST SCREEN")  # 프로젝트 타이틀 설정
        self.setGeometry(0, 0, int(wid * .5), int(hei * .5))  # 화면 사이즈 설정

        self.mainWidget = QWidget()                     # 메인 위젯 생성
        self.mainLayout = QGridLayout(self.mainWidget)  # 메인 레이아웃 생성 및 메인 위젯 연결
        self.setCentralWidget(self.mainWidget)          # 메인윈도우 센트럴위젯에 메인 위젯 연결

        # column 4, row 10
        self.sample1(0, 0)

        # column 4, row 10, 항목명 설정
        self.sample2(0, 1)

        # column 4, row 10, 항목명 설정, 데이터 세팅
        self.sample3(0, 2)

        # column 4, row 10, 항목명 설정, 데이터 동적 추가
        self.sample4(1, 0)

        # # column 4, row 10, 항목명 설정, 데이터 세팅, row 자동 간격 조정
        # self.sample5(1, 1)

        # # column 4, row 10, 항목명 설정, 데이터 세팅, column 자동 간격 조정
        # self.sample6(1, 2)

        # # column 4, row 10, 항목명 설정, 데이터 세팅, 삭제
        # self.sample7(2, 0)

        # column 4, row 10, 항목명 설정, 데이터 세팅, 정렬
        self.sample8(2, 1)

        self.showMaximized()


    def sample1(self, row, col):
        table = QTableWidget()  # 테이블 위젯 생성
        table.setColumnCount(4)  # 테이블 column 개수 세팅
        table.setRowCount(10)  # 테이블 row 개수 세팅

        self.mainLayout.addWidget(table, row, col)  # 메인 레이아웃에 테이블 위젯 추가

    def sample2(self, row, col):
        table = QTableWidget()  # 테이블 위젯 생성
        table.setColumnCount(4)  # 테이블 column 개수 세팅
        table.setRowCount(10)  # 테이블 row 개수 세팅
        table.setHorizontalHeaderLabels(["국어", "영어", "수학", "과학"])           # col 항목명 세팅
        table.setVerticalHeaderLabels(["김치국", "박자반", "오영수", "이영어", "신과학", "콩국수", "기러기", "김철수", "배수칠", "김작별"])   # row 항목명 세팅

        self.mainLayout.addWidget(table, row, col)  # 메인 레이아웃에 테이블 위젯 추가

    def sample3(self, row, col):
        table = QTableWidget()  # 테이블 위젯 생성
        table.setColumnCount(4)  # 테이블 column 개수 세팅
        table.setRowCount(10)  # 테이블 row 개수 세팅
        table.setHorizontalHeaderLabels(["국어", "영어", "수학", "과학"])           # col 항목명 세팅
        table.setVerticalHeaderLabels(["김치국", "박자반", "오영수", "이영어", "신과학", "콩국수", "기러기", "김철수", "배수칠", "김작별"])   # row 항목명 세팅

        # table.rowCount() : row 개수 리턴
        for r in range(table.rowCount()):
            # table.columnCount() : column 개수 리턴
            for c in range(table.columnCount()):
                # 테이블위젯아이템 생성
                item = QTableWidgetItem()
                # 데이터 삽입
                item.setText(str(r+c))
                # 아이템을 테이블에 세팅
                table.setItem(r, c, item)

        self.mainLayout.addWidget(table, row, col)  # 메인 레이아웃에 테이블 위젯 추가

    def sample4(self, row, col):
        table = QTableWidget()  # 테이블 위젯 생성
        table.setColumnCount(4)  # 테이블 column 개수 세팅

        table.setHorizontalHeaderLabels(["국어", "영어", "수학", "과학"])           # col 항목명 세팅


        # 추가할 로우 개수
        for r in range(5):
            # 동적 row 생성
            table.insertRow(r)
            # table.columnCount() : column 개수 리턴
            for c in range(table.columnCount()):
                # 테이블위젯아이템 생성
                item = QTableWidgetItem()
                # 데이터 삽입
                item.setText(str(r+c))
                # 아이템을 테이블에 세팅
                table.setItem(r, c, item)

        table.setVerticalHeaderLabels(["김치국", "박자반", "오영수", "이영어", "신과학"])  # row 항목명 세팅

        self.mainLayout.addWidget(table, row, col)  # 메인 레이아웃에 테이블 위젯 추가

    # def sample5(self, row, col):
    #     table = QTableWidget()  # 테이블 위젯 생성
    #     table.setColumnCount(4)  # 테이블 column 개수 세팅
    #     table.setRowCount(10)  # 테이블 row 개수 세팅
    #     table.setHorizontalHeaderLabels(["국어", "영어", "수학", "과학"])  # col 항목명 세팅
    #     table.setVerticalHeaderLabels(
    #         ["김치국", "박자반", "오영수", "이영어", "신과학", "콩국수", "기러기", "김철수", "배수칠", "김작별"])  # row 항목명 세팅

    #     # table.rowCount() : row 개수 리턴
    #     for r in range(table.rowCount()):
    #         # table.columnCount() : column 개수 리턴
    #         for c in range(table.columnCount()):
    #             # 테이블위젯아이템 생성
    #             item = QTableWidgetItem()
    #             # 데이터 삽입
    #             item.setText(str(r + c))
    #             # 아이템을 테이블에 세팅
    #             table.setItem(r, c, item)

    #     # 줄과 줄 사이 간격 자동 조정
    #     table.resizeRowsToContents()
    #     self.mainLayout.addWidget(table, row, col)  # 메인 레이아웃에 테이블 위젯 추가

    # def sample6(self, row, col):
    #     table = QTableWidget()  # 테이블 위젯 생성
    #     table.setColumnCount(4)  # 테이블 column 개수 세팅
    #     table.setRowCount(10)  # 테이블 row 개수 세팅
    #     table.setHorizontalHeaderLabels(["국어", "영어", "수학", "과학"])  # col 항목명 세팅
    #     table.setVerticalHeaderLabels(
    #         ["김치국", "박자반", "오영수", "이영어", "신과학", "콩국수", "기러기", "김철수", "배수칠", "김작별"])  # row 항목명 세팅

    #     # table.rowCount() : row 개수 리턴
    #     for r in range(table.rowCount()):
    #         # table.columnCount() : column 개수 리턴
    #         for c in range(table.columnCount()):
    #             t = str(r+c)
    #             if c % 2 == 0:
    #                 t = "Loooooooooooooooooooooooooooooong : " + t
    #             # 테이블위젯아이템 생성
    #             item = QTableWidgetItem()
    #             # 데이터 삽입
    #             item.setText(t)
    #             # 아이템을 테이블에 세팅
    #             table.setItem(r, c, item)

    #     # 항목과 항목 사이 간격 자동 조정
    #     table.resizeColumnsToContents()
    #     self.mainLayout.addWidget(table, row, col)  # 메인 레이아웃에 테이블 위젯 추가


    # def sample7(self, row, col):
    #     table = QTableWidget()  # 테이블 위젯 생성
    #     table.setColumnCount(4)  # 테이블 column 개수 세팅
    #     table.setRowCount(10)  # 테이블 row 개수 세팅
    #     table.setHorizontalHeaderLabels(["국어", "영어", "수학", "과학"])           # col 항목명 세팅
    #     table.setVerticalHeaderLabels(["김치국", "박자반", "오영수", "이영어", "신과학", "콩국수", "기러기", "김철수", "배수칠", "김작별"])   # row 항목명 세팅

    #     # table.rowCount() : row 개수 리턴
    #     for r in range(table.rowCount()):
    #         # table.columnCount() : column 개수 리턴
    #         for c in range(table.columnCount()):
    #             # 테이블위젯아이템 생성
    #             item = QTableWidgetItem()
    #             # 데이터 삽입
    #             item.setText(str(r+c))
    #             # 아이템을 테이블에 세팅
    #             table.setItem(r, c, item)

    #     # 6번째 row 삭제 (시작 인덱스는 0부터 입니다.)
    #     table.removeRow(5)
    #     # 2번째 column 삭제 (시작 인덱스는 0부터 입니다.)
    #     table.removeColumn(1)

    #     self.mainLayout.addWidget(table, row, col)  # 메인 레이아웃에 테이블 위젯 추가

    def sample8(self, row, col):
        table = QTableWidget()  # 테이블 위젯 생성
        table.setColumnCount(4)  # 테이블 column 개수 세팅
        table.setRowCount(10)  # 테이블 row 개수 세팅
        table.setHorizontalHeaderLabels(["align", "국어", "영어", "수학", "과학"])           # col 항목명 세팅
        table.setVerticalHeaderLabels(["김치국", "박자반", "오영수", "이영어", "신과학", "콩국수", "기러기", "김철수", "배수칠", "김작별"])   # row 항목명 세팅

        align = [Qt.AlignCenter
                 , Qt.AlignVCenter
                 , Qt.AlignHCenter
                 , Qt.AlignRight
                 , Qt.AlignLeft
                 , Qt.AlignTop
                 , Qt.AlignBottom
                 , Qt.AlignTop | Qt.AlignRight
                 , Qt.AlignBottom | Qt.AlignLeft
                 , Qt.AlignBottom | Qt.AlignRight]

        align_name = ["Qt.AlignCenter : 가운데정렬"
                 , "Qt.AlignVCenter : 세로정렬"
                 , "Qt.AlignHCenter : 가로정렬"
                 , "Qt.AlignRight : 오른쪽정렬"
                 , "Qt.AlignLeft : 왼쪽정렬"
                 , "Qt.AlignTop : 위쪽정렬"
                 , "Qt.AlignBottom : 아래쪽 정렬"
                 , "Qt.AlignTop | Qt.AlignRight : 위, 오른쪽 정렬"
                 , "Qt.AlignBottom | Qt.AlignLeft : 아래 왼쪽 정렬"
                 , "Qt.AlignBottom | Qt.AlignRight : 아래 오른쪽 정렬"]

        # table.rowCount() : row 개수 리턴
        for r in range(table.rowCount()):
            # table.columnCount() : column 개수 리턴
            for c in range(table.columnCount()):
                # 테이블위젯아이템 생성
                item = QTableWidgetItem()

                if c == 0:
                    item.setText(align_name[r])

                else:
                    # 데이터 삽입
                    item.setText(str(r+c))
                    # 정렬
                    item.setTextAlignment(align[r])

                # 아이템을 테이블에 세팅
                table.setItem(r, c, item)

        self.mainLayout.addWidget(table, row, col)  # 메인 레이아웃에 테이블 위젯 추가

if __name__ == '__main__':
    app = QApplication(sys.argv)
    size: QSize = app.primaryScreen().size()    # 모니터 사이즈

    main = MainScreen(size.width()/2, size.height())
    app.exec_()