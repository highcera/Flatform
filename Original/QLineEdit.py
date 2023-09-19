import sys
from PyQt5.QtWidgets import *
 
class MyApp(QWidget):
 
    def __init__(self):
 
        super().__init__()
        self.initUI()
 
 
    def initUI(self):
 
        # QLabel 인스턴스인 lbl을 생성하고 문자열을 "NULL"로 초기화한다.
        self.lbl = QLabel("NULL", self)
        # 위치를 x = 60, y = 40으로 지정
        self.lbl.move(60, 40)
 
        # QLineEdit 인스턴스인 qle를 생성한다.
        self.qle = QLineEdit(self)
        # 위치를 x = 60, y = 70으로 지정
        self.qle.move(60, 70)
 
        # QPushButton 인스턴스인 btn을 생성하고 문자열을 "Change Label Text"로 초기화한다.
        btn = QPushButton("Change Label Text", self)
        # 위치를 x = 200, y = 70으로 지정
        btn.move(200, 70)
        btn.setCheckable(True)
 
        # 버튼 btn을 클릭하는 시그널이 발생하면 changeLabelText() 슬롯을 호출한다.
        btn.clicked.connect(self.changeLabelText)
        # qle의 입력 과정에서 엔터 입력 시그널이 발생하면 changeLabelText() 슬롯을 호출한다.
        self.qle.returnPressed.connect(self.changeLabelText)
 
        self.setWindowTitle("QLineEdit")
        self.setGeometry(300, 300, 400, 150)
 
    # 사용자 지정 함수
    def changeLabelText(self):
 
        # 라벨 lbl의 문자열을 qle의 입력값으로 설정한다.
        self.lbl.setText(self.qle.text())
        # 입력 길이에 맞추어 라벨 lbl의 길이를 조절한다.
        self.lbl.adjustSize()
        # qle 입력을 비운다.
        self.qle.setText("")
 
 
if __name__ == __name__:
 
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())