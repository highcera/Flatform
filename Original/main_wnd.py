# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_wnd.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 711)
        MainWindow.setMinimumSize(QtCore.QSize(897, 711))
        MainWindow.setMaximumSize(QtCore.QSize(897, 711))
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableLib = QtWidgets.QTableView(self.centralwidget)
        self.tableLib.setGeometry(QtCore.QRect(30, 140, 831, 331))
        self.tableLib.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableLib.setProperty("showDropIndicator", False)
        self.tableLib.setDragEnabled(True)
        self.tableLib.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tableLib.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.tableLib.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableLib.setObjectName("tableLib")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableConst = QtWidgets.QTableView(self.centralwidget)
        self.tableConst.setGeometry(QtCore.QRect(30, 480, 451, 91))
        self.tableConst.setObjectName("tableConst")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(310, 90, 410, 47))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnApply = QtWidgets.QPushButton(self.layoutWidget)
        self.btnApply.setObjectName("btnApply")
        self.gridLayout.addWidget(self.btnApply, 1, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.cboFreq = QtWidgets.QComboBox(self.layoutWidget)
        self.cboFreq.setObjectName("cboFreq")
        self.gridLayout.addWidget(self.cboFreq, 1, 1, 1, 1)
        self.cboDiel = QtWidgets.QComboBox(self.layoutWidget)
        self.cboDiel.setObjectName("cboDiel")
        self.gridLayout.addWidget(self.cboDiel, 1, 0, 1, 1)
        self.STlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.STlineEdit.setObjectName("STlineEdit")
        self.gridLayout.addWidget(self.STlineEdit, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.CaplineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.CaplineEdit.setText("")
        self.CaplineEdit.setObjectName("CaplineEdit")
        self.gridLayout.addWidget(self.CaplineEdit, 1, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(620, 40, 241, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblratio_name = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblratio_name.setFont(font)
        self.lblratio_name.setObjectName("lblratio_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblratio_name)
        self.lblratio = QtWidgets.QLabel(self.layoutWidget1)
        self.lblratio.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblratio.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblratio.setText("")
        self.lblratio.setObjectName("lblratio")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lblratio)
        self.lblvdc_name = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblvdc_name.setFont(font)
        self.lblvdc_name.setObjectName("lblvdc_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblvdc_name)
        self.lblvdc = QtWidgets.QLabel(self.layoutWidget1)
        self.lblvdc.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblvdc.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblvdc.setText("")
        self.lblvdc.setObjectName("lblvdc")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lblvdc)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 90, 271, 44))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.cboPow = QtWidgets.QComboBox(self.layoutWidget2)
        self.cboPow.setObjectName("cboPow")
        self.gridLayout_2.addWidget(self.cboPow, 1, 0, 1, 1)
        self.btnGraph = QtWidgets.QPushButton(self.centralwidget)
        self.btnGraph.setGeometry(QtCore.QRect(760, 490, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnGraph.setFont(font)
        self.btnGraph.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.btnGraph.setObjectName("btnGraph")
        self.btnExcel = QtWidgets.QPushButton(self.centralwidget)
        self.btnExcel.setGeometry(QtCore.QRect(760, 530, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnExcel.setFont(font)
        self.btnExcel.setStyleSheet("\n"
"background-color: rgb(198, 180, 255);")
        self.btnExcel.setObjectName("btnExcel")
        self.fileLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.fileLineEdit.setGeometry(QtCore.QRect(600, 540, 151, 21))
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 40, 131, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblfreq = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblfreq.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblfreq.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblfreq.setText("")
        self.lblfreq.setObjectName("lblfreq")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lblfreq)
        self.lblac = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblac.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblac.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblac.setText("")
        self.lblac.setObjectName("lblac")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lblac)
        self.lblfreq_name = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblfreq_name.setFont(font)
        self.lblfreq_name.setObjectName("lblfreq_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblfreq_name)
        self.lblac_name = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblac_name.setFont(font)
        self.lblac_name.setObjectName("lblac_name")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblac_name)
        self.lblratio_name_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblratio_name_3.setGeometry(QtCore.QRect(30, 20, 77, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblratio_name_3.setFont(font)
        self.lblratio_name_3.setObjectName("lblratio_name_3")
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(290, 60, 71, 18))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.lblvdc_name_3 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblvdc_name_3.setFont(font)
        self.lblvdc_name_3.setObjectName("lblvdc_name_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblvdc_name_3)
        self.lbldf = QtWidgets.QLabel(self.layoutWidget3)
        self.lbldf.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbldf.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbldf.setText("")
        self.lbldf.setObjectName("lbldf")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lbldf)
        self.lbleqn = QtWidgets.QLabel(self.centralwidget)
        self.lbleqn.setGeometry(QtCore.QRect(30, 590, 601, 91))
        self.lbleqn.setObjectName("lbleqn")
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(160, 40, 131, 41))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.layoutWidget_3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.lbltime = QtWidgets.QLabel(self.layoutWidget_3)
        self.lbltime.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbltime.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbltime.setText("")
        self.lbltime.setObjectName("lbltime")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lbltime)
        self.lblaging = QtWidgets.QLabel(self.layoutWidget_3)
        self.lblaging.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblaging.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblaging.setText("")
        self.lblaging.setObjectName("lblaging")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lblaging)
        self.lbltime_name = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbltime_name.setFont(font)
        self.lbltime_name.setObjectName("lbltime_name")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbltime_name)
        self.lbaging_name = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbaging_name.setFont(font)
        self.lbaging_name.setObjectName("lbaging_name")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbaging_name)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 897, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu_F = QtWidgets.QMenu(self.menuBar)
        self.menu_F.setObjectName("menu_F")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.menu_F.addAction(self.actionOpen_2)
        self.menuBar.addAction(self.menu_F.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "DC-bias library"))
        self.btnApply.setText(_translate("MainWindow", "적용"))
        self.label_6.setText(_translate("MainWindow", "측정 조건"))
        self.STlineEdit.setPlaceholderText(_translate("MainWindow", "S/T 입력"))
        self.label_3.setText(_translate("MainWindow", "유전율"))
        self.CaplineEdit.setPlaceholderText(_translate("MainWindow", "용량 입력"))
        self.label_5.setText(_translate("MainWindow", "필요용량"))
        self.label_4.setText(_translate("MainWindow", "Sheet 두께 (um)"))
        self.lblratio_name.setText(_translate("MainWindow", "0Vdc 저주파/고주파 변화율 %"))
        self.lblvdc_name.setText(_translate("MainWindow", "고주파 0Vdc"))
        self.label_2.setText(_translate("MainWindow", "조성"))
        self.btnGraph.setText(_translate("MainWindow", "그래프"))
        self.btnExcel.setText(_translate("MainWindow", "엑셀 추출"))
        self.fileLineEdit.setPlaceholderText(_translate("MainWindow", "저장할 파일명 입력"))
        self.lblfreq_name.setText(_translate("MainWindow", "주파수 (kHz)"))
        self.lblac_name.setText(_translate("MainWindow", "AC (V)"))
        self.lblratio_name_3.setText(_translate("MainWindow", "측정 조건"))
        self.lblvdc_name_3.setText(_translate("MainWindow", "DF"))
        self.lbleqn.setText(_translate("MainWindow", "TextLabel"))
        self.lbltime_name.setText(_translate("MainWindow", "전압유지시간"))
        self.lbaging_name.setText(_translate("MainWindow", "Aging 시간"))
        self.menu_F.setTitle(_translate("MainWindow", "파일 (F)"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

