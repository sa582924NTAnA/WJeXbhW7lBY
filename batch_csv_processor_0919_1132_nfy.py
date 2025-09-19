# 代码生成时间: 2025-09-19 11:32:56
import csv
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtCore import Qt

"""
CSV文件批量处理器
这个程序允许用户选择一个文件夹，然后批量处理该文件夹中的所有CSV文件。
"""

class CSVBatchProcessor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('CSV Batch Processor')
        self.setGeometry(100, 100, 800, 600)

        # 设置布局
        layout = QVBoxLayout()

        # 添加按钮用于选择文件夹
        self.btn_select_folder = QPushButton('Select Folder')
        self.btn_select_folder.clicked.connect(self.select_folder)
        layout.addWidget(self.btn_select_folder)

        # 添加表格用于显示文件信息
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['File Name', 'Status'])
        layout.addWidget(self.table)

        # 添加按钮用于开始处理
        self.btn_process = QPushButton('Start Processing')
        self.btn_process.clicked.connect(self.process_files)
        layout.addWidget(self.btn_process)

        self.setLayout(layout)

    def select_folder(self):
        # 选择文件夹
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder_path:
            self.folder_path = folder_path
            self.update_table()

    def update_table(self):
        # 清空表格
        self.table.setRowCount(0)

        # 获取文件夹中的所有CSV文件
        for file in os.listdir(self.folder_path):
            if file.endswith('.csv'):
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                self.table.setItem(row_position, 0, QTableWidgetItem(file))
                self.table.setItem(row_position, 1, QTableWidgetItem('Pending'))

    def process_files(self):
        # 处理所有CSV文件
        for row in range(self.table.rowCount()):
            file_name = self.table.item(row, 0).text()
            file_path = os.path.join(self.folder_path, file_name)
            try:
                # 假设处理CSV文件的代码在这里
                with open(file_path, 'r') as file:
                    reader = csv.reader(file)
                    for index, row in enumerate(reader):
                        # 这里可以添加具体的处理逻辑
                        pass
                self.table.setItem(row, 1, QTableWidgetItem('Processed'))
            except Exception as e:
                self.table.setItem(row, 1, QTableWidgetItem(f'Error: {str(e)}'))

if __name__ == '__main__':
    app = QApplication([])
    ex = CSVBatchProcessor()
    ex.show()
    app.exec_()