# 代码生成时间: 2025-09-22 09:55:30
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout, QLabel, QLineEdit, QComboBox, QFileDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
Interactive Chart Generator
This program creates a PyQt5 application that allows users to generate charts interactively.
"""

class ChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # Set window properties
        self.setWindowTitle('Interactive Chart Generator')
        self.setGeometry(100, 100, 800, 600)

        # Create main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        # Add input fields and buttons
        self.add_input_fields()

        # Display window
        self.show()

    def add_input_fields(self):
        # Add file selection button
        self.file_button = QPushButton('Select File')
        self.file_button.clicked.connect(self.select_file)
        self.main_layout.addWidget(self.file_button, 0, 0)

        # Add chart type selection combo box
        self.chart_type_combo = QComboBox()
        self.chart_type_combo.addItems(['Line', 'Bar', 'Scatter'])
        self.main_layout.addWidget(self.chart_type_combo, 0, 1)

        # Add X-axis and Y-axis labels
        self.x_label = QLabel('X-axis Label:')
        self.main_layout.addWidget(self.x_label, 1, 0)
        self.x_axis_input = QLineEdit()
        self.main_layout.addWidget(self.x_axis_input, 1, 1)

        self.y_label = QLabel('Y-axis Label:')
        self.main_layout.addWidget(self.y_label, 2, 0)
        self.y_axis_input = QLineEdit()
        self.main_layout.addWidget(self.y_axis_input, 2, 1)

        # Add chart generation button
        self.generate_button = QPushButton('Generate Chart')
        self.generate_button.clicked.connect(self.generate_chart)
        self.main_layout.addWidget(self.generate_button, 3, 0, 1, 2)

    def select_file(self):
        # Open file dialog to select CSV file
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, 'Select File', '', 'CSV Files (*.csv)', options=options)
        if file:
            self.file_path = file
            print(f'Selected file: {self.file_path}')
        else:
            print('No file selected')

    def generate_chart(self):
        # Read CSV file into pandas DataFrame
        try:
            data = pd.read_csv(self.file_path)
        except Exception as e:
            print(f'Error reading file: {e}')
            return

        # Get chart type and axis labels from input fields
        chart_type = self.chart_type_combo.currentText()
        x_axis_label = self.x_axis_input.text()
        y_axis_label = self.y_axis_input.text()

        # Generate chart based on chart type
        if chart_type == 'Line':
            data.plot.line(x=x_axis_label, y=y_axis_label)
        elif chart_type == 'Bar':
            data.plot.bar(x=x_axis_label, y=y_axis_label)
        elif chart_type == 'Scatter':
            data.plot.scatter(x=x_axis_label, y=y_axis_label)
        else:
            print('Invalid chart type')
            return

        # Display chart
        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chart_window = ChartWindow()
    sys.exit(app.exec_())