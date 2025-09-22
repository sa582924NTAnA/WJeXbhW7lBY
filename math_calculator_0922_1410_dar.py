# 代码生成时间: 2025-09-22 14:10:28
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt

"""
A simple PyQT application that serves as a math calculator.
"""

class MathCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window's title and size
        self.setWindowTitle('Math Calculator')
        self.setGeometry(100, 100, 300, 200)

        # Create layout and widgets
        self.layout = QVBoxLayout()
        self.result_display = QLineEdit(self)
        self.result_display.setReadOnly(True)
        self.result_display.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.result_display)

        # Define buttons and their actions
        self.buttons = {}
        self.buttons['7'] = QPushButton('7', self)
        self.buttons['7'].clicked.connect(lambda: self.append_to_display('7'))
        self.layout.addWidget(self.buttons['7'])

        # Add more buttons and their actions following the above pattern
        self.buttons['8'] = QPushButton('8', self)
        self.buttons['8'].clicked.connect(lambda: self.append_to_display('8'))
        self.layout.addWidget(self.buttons['8'])

        # ... Add other buttons (9, 4, 5, 6, 1, 2, 3, 0, +, -, *, /)

        self.buttons['+'] = QPushButton('+', self)
        self.buttons['+'].clicked.connect(lambda: self.set_operation('+'))
        self.layout.addWidget(self.buttons['+'])

        # Include error handling for invalid operations
        self.buttons['='] = QPushButton('=', self)
        self.buttons['='].clicked.connect(self.calculate_result)
        self.layout.addWidget(self.buttons['='])

        # Set the layout for the main window
        self.setLayout(self.layout)

    def append_to_display(self, value):
        # Append the value to the result display
        self.result_display.setText(self.result_display.text() + value)

    def set_operation(self, operation):
        # Store the current result and set a new operation
        self.current_result = float(self.result_display.text())
        self.current_operation = operation
        self.result_display.setText('')

    def calculate_result(self):
        # Perform the operation and display the result
        try:
            if self.current_operation == '+':
                self.result_display.setText(str(self.current_result + float(self.result_display.text())))
            elif self.current_operation == '-':
                self.result_display.setText(str(self.current_result - float(self.result_display.text())))
            elif self.current_operation == '*':
                self.result_display.setText(str(self.current_result * float(self.result_display.text())))
            elif self.current_operation == '/':
                if float(self.result_display.text()) != 0:
                    self.result_display.setText(str(self.current_result / float(self.result_display.text())))
                else:
                    self.result_display.setText('Error: Division by zero')
        except ValueError:
            # Handle the case where the input is not a number
            self.result_display.setText('Error: Invalid input')

    def run(self):
        # Run the application
        self.show()
        sys.exit(QApplication.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = MathCalculator()
    calc.run()