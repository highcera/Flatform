# https://studyingrabbit.tistory.com/28

import sys
import PyQt5
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class QPushButtonOperation(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QFont("Helvetia", 13)
        font.setBold(True)
        self.setFont(font)

class QPushButtonNumber(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QFont("Helvetia", 13)
        font.setBold(True)
        self.setFont(font)

class QLineEditCustom(QLineEdit):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QFont("Helvetia", 13)
        self.setFont(font)

class QLabelCustom(QLabel):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QFont("Helvetia", 13)
        font.setBold(True)
        self.setFont(font)

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.set_style()
        self.init_ui()

    def set_style(self):
        with open("E:/Repo_Office/Flatform/Basic/update_style", 'r') as f:
            self.setStyleSheet(f.read())

    def init_ui(self):
        main_layout = QVBoxLayout()

        layout_operation = QHBoxLayout()
        layout_clear_equal = QHBoxLayout()
        layout_number = QGridLayout()
        layout_equation_solution = QFormLayout()

        label_equation = QLabelCustom("Equation: ")
        label_solution = QLabelCustom("Solution: ")
        self.equation = QLineEditCustom("")
        self.solution = QLineEditCustom("")

        layout_equation_solution.addRow(label_equation, self.equation)
        layout_equation_solution.addRow(label_solution, self.solution)
        group_equation_solution = QGroupBox()
        group_equation_solution.setLayout(layout_equation_solution)

        button_plus = QPushButtonOperation("+")
        button_minus = QPushButtonOperation("-")
        button_product = QPushButtonOperation("x")
        button_division = QPushButtonOperation("/")

        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        layout_operation.addWidget(button_plus)
        layout_operation.addWidget(button_minus)
        layout_operation.addWidget(button_product)
        layout_operation.addWidget(button_division)

        button_equal = QPushButtonNumber("=")
        button_clear = QPushButtonNumber("Clear")
        button_backspace = QPushButtonNumber("Backspace")

        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        layout_clear_equal.addWidget(button_clear)
        layout_clear_equal.addWidget(button_backspace)
        layout_clear_equal.addWidget(button_equal)

        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButtonNumber(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], x, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        button_dot = QPushButtonNumber(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        button_double_zero = QPushButtonNumber("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_number.addWidget(button_double_zero, 3, 0)

        main_layout.addWidget(group_equation_solution, stretch=2)
        main_layout.addLayout(layout_operation, stretch=1)
        main_layout.addLayout(layout_clear_equal, stretch=1)
        main_layout.addLayout(layout_number, stretch=3)

        self.setLayout(main_layout)
        self.setWindowTitle("CALCULATOR")
        self.setWindowIcon(QIcon("./icon.png"))
        self.resize(500, 500)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.solution.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())