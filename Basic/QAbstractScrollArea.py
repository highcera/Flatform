# https://wikidocs.net/163407

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5 import uic

# import pandas as pd
# from pandasModel import pandasModel

form_class = uic.loadUiType("C:/Flatform/Basic/main.ui")[0]

class WindowClass(QMainWindow, form_class):
    one, two, three = range(3)

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.table_1.setRowCount(7)
        self.table_1.setColumnCount(3)
        self.table_1.setItem(0, 0, QTableWidgetItem("Table_1"))

        self.table_2.setRowCount(7)
        self.table_2.setColumnCount(3)
        self.table_2.setItem(0, 0, QTableWidgetItem("Table_2"))
        # self.table_2.setColumnWidth(0, 200)
        self.table_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) 
    
        # addScrollBarWidget [스크롤바에 위젯 추가] / setCornerWidget [코너에 위젯추가]
        self.table_3.setRowCount(7)
        self.table_3.setColumnCount(3)
        self.table_3.setItem(0, 0, QTableWidgetItem("Table_3"))
        self.btn_1 = QPushButton()          # 버튼 생성(btn_1)
        self.btn_1.setText('btn_1')             # 버튼 텍스트 btn_1로
        self.table_3.addScrollBarWidget(self.btn_1,Qt.AlignLeft)# 스크롤바 왼쪽에 btn_1 추가
        self.btn_2 = QPushButton()          # 버튼 생성(btn_2)
        self.btn_2.setText('2')             # 버튼 텍스트 2로
        self.table_3.setCornerWidget(self.btn_2)        # 모서리에 btn_2 추가

        # setVerticalScrollBar / setHorizontalScrollBa [스크롤바 적용]
        self.table_4.setRowCount(7)
        self.table_4.setColumnCount(3)
        self.table_4.setItem(0, 0, QTableWidgetItem("Table_4"))
        self.scroll_bar=QScrollBar(self) # 스크롤바 객체 scroll_bar생성
        self.scroll_bar.setStyleSheet("background : black;") # 스타일로 배경색:검정 을 적용
        self.table_4.setVerticalScrollBar(self.scroll_bar) # table_4의 수직 스크롤바에 scroll_bar 적용

        self.table_5.setRowCount(7)
        self.table_5.setColumnCount(3)
        self.table_5.setItem(0, 0, QTableWidgetItem("Table_5"))
        # setSizeAdjustPolicy [사이즈 조정 정책]
        self.table_5.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) # 내용물 기준으로 조정
        self.table_5.resizeColumnsToContents() # 열을 컨텐츠에 맞게 리사이즈

        # setViewport [뷰포트에 위젯 삽입]
        self.scrollarea_1 = QAbstractScrollArea(self)       # QAbstractScrollArea객체 생성
        self.scrollarea_1.setGeometry(10,410,250,174)   # 위치 지정
        self.scrollarea_1.setFrameShape(QFrame.Box) # 테두리 설정(보기 쉽게)
        self.scrollarea_1.setViewport(self.tree_7)      # scrollarea_1객체의 뷰포트에 tree_7 삽입
        model = self.create_model()
        self.tree_7.setModel(model)           # 내용물 삽입.
        
        # QAbstractScrollArea.AdjustIgnored : 스크롤 영역 조정하지 않음
        # QAbstractScrollArea.AdjustToContent : 스크롤 영역을 내용물 기준 조정
        # QAbstractScrollArea.AdjustToContentsOnFirstShow : 처음에만 내용물 기준 조정


        # setVerticalScrollBarPolicy / setHorizontalScrollBarPolicy [스크롤 표시정책]
        # self.table_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #table_2의 수평 스크롤바 안보이게
        # ↓
        # self.table_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded) #: 컨텐츠가 뷰포트보다 클때 스크롤바 생성(기본)
        # Qt.ScrollBarAlwaysOff : 스크롤바 항상 표시안함
        # Qt.ScrollBarAlwaysOn : 스크롤바 항상 표시
    
        # setViewportMargins [뷰포트 여백]
        self.scrollarea_2 = QAbstractScrollArea(self)       # QAbstractScrollAea 객체 생성
        self.scrollarea_2.setGeometry(265,410,260,174)  # 위치 지정
        self.scrollarea_2.setFrameShape(QFrame.Box) # 테두리 설정(보기쉽게)
        self.scrollarea_2.setViewportMargins(30, 0, 0, 0)   # 뷰포트 왼쪽에 30의 영역을 줌
        self.tree_8.setParent(self.scrollarea_2.viewport()) # tree_8의 부모를 scrollarea_2로 설정
        self.tree_8.setGeometry(0,0,217,174)        # scrollarea_2내 tree_8위치 지정
        # model = self.create_model()
        self.tree_8.setModel(model) 

        # scrollContentsBy [뷰포트 내용 스크롤] / viewportSizeHint [권장 뷰포트 크기]
        # model = self.create_model()
        self.layout = QVBoxLayout()
        self.btn_9 = QPushButton() 
        self.tree_9.setModel(model)      # 내용 삽입
        self.btn_9.clicked.connect(self.fnc_btn_9)  # btn_9누르면 fnc_btn_9로

        self.layout.addLayout(self.tree_9)
        self.layout.addLayout(self.btn_9)
        self.setLayout(self.layout)
       
    def fnc_btn_9(self):
        self.tree_9.scrollContentsBy(100, 0)        # 내용을 100,0 만큼 이동
        print(self.tree_9.viewportSizeHint())       # 권장 뷰포트 크기 출력
       
    def create_model(self):
        model = QStandardItemModel(3, 3)
        model.setHeaderData(self.one, Qt.Vertical, "Name")
        model.setHeaderData(self.two, Qt.Vertical, "Age")
        model.setHeaderData(self.three, Qt.Vertical, "Sex")
     
        return model

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 