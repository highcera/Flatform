# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(724, 691)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 711, 611))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.dateyear_widgetsetWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.year_widget = QtWidgets.QComboBox(self.formLayoutWidget)
        self.year_widget.setObjectName("year_widget1")
        self.horizontalLayout.addWidget(self.year_widget)
        self.month_widget = QtWidgets.QComboBox(self.formLayoutWidget)
        self.month_widget.setObjectName("month_widget1")
        self.horizontalLayout.addWidget(self.month_widget)
        self.date_widget = QtWidgets.QComboBox(self.formLayoutWidget)
        self.date_widget.setObjectName("date_widget1")
        self.horizontalLayout.addWidget(self.date_widget)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.address_1 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.address_1.setObjectName("address_1")
        self.verticalLayout.addWidget(self.address_1)
        self.address_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.address_2.setObjectName("address_2")
        self.verticalLayout.addWidget(self.address_2)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.email_id = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.email_id.setObjectName("email_id")
        self.horizontalLayout_2.addWidget(self.email_id)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.email_company = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.email_company.setObjectName("email_company")
        self.horizontalLayout_2.addWidget(self.email_company)
        self.email_combobox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.email_combobox.setObjectName("email_combobox")
        self.horizontalLayout_2.addWidget(self.email_combobox)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_3.addWidget(self.lineEdit_4)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_3.addWidget(self.lineEdit_5)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.checkBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.label_31 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.save_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_10.addWidget(self.save_button)
        self.cancel_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_10.addWidget(self.cancel_button)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 724, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Name : "))
        self.label_2.setText(_translate("MainWindow", "Birthday : "))
        self.label_3.setText(_translate("MainWindow", "Address : "))
        self.label_4.setText(_translate("MainWindow", "E-mail :"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Phone Number : "))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "Height(cm) : "))
        self.label_18.setText(_translate("MainWindow", "Personal InformationShare : "))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.label_19.setText(_translate("MainWindow", "Self Introduction : "))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
