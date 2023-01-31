import sys
from PyQt5.QtWidgets import *
from form_code import Ui_Form

class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.resize(400, 220)

        self.spAge.valueChanged[int].connect(self.chk_age)
        self.btnFindId.clicked.connect(self.chk_id)
        self.btnOk.clicked.connect(self.chk_ok)

    def chk_age(self, v):
        if v < 20:
            self.InPNum2.setEnabled(True)
        else:
            self.InPNum2.setEnabled(False)  
 
    def chk_id(self):
        if len(self.InId.text()) < 2:
            self.lblChkId.setText("2글자 이상 입력하세요")
        else:
            if ids.count(self.InId.text()) == 1: # class 밖의 리스트 ids를 참조할 수 있음.
                self.lblChkId.setText("중복되는 ID가 존재합니다")
            else:
                self.lblChkId.setText("멋진 ID네요!")   
 
    def chk_ok(self):
        str = ""
        if self.InName.text() == "":
            str += "이름 "
        if self.lblChkId.text() != "멋진 ID네요!":
            str += "ID "
        if len(self.InPNum.text()) < 13:
            str += "연락처 "
        if str != "":
            self.btnOk.setText(str+"을(를) 확인하세요")
        else:
            self.btnOk.setText("처리되었습니다")
    

if __name__ == '__main__':
    ids = ["return", "zero", "abc", "python", "class"]
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec_()
