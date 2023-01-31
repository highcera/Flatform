from PyQt5.QtCore import Qt

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
