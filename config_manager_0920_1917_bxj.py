# 代码生成时间: 2025-09-20 19:17:26
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import QIODevice, QTextStream
from PyQt5.QtGui import QTextCharFormat

"""
ConfigManager is a PyQt5 application for managing configuration files.
It allows users to load, edit, and save configuration files.
"""

class ConfigManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Initialize the user interface."""
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Config Manager')

        layout = QVBoxLayout()

        self.textEdit = QTextEdit()
        layout.addWidget(self.textEdit)

        self.loadButton = QPushButton('Load')
        self.loadButton.clicked.connect(self.loadConfig)
        layout.addWidget(self.loadButton)

        self.saveButton = QPushButton('Save')
        self.saveButton.clicked.connect(self.saveConfig)
        layout.addWidget(self.saveButton)

        self.setLayout(layout)

    def loadConfig(self):
        """Load configuration file into the text editor."""
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', '.', 'JSON Files (*.json);;All Files (*)')
        if fileName:
            try:
                with open(fileName, 'r') as config_file:
                    config_data = config_file.read()
                    self.textEdit.setText(config_data)
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to load configuration file: {e}')

    def saveConfig(self):
        """Save the configuration file from the text editor."""
        fileName, _ = QFileDialog.getSaveFileName(self, 'Save File', '.', 'JSON Files (*.json);;All Files (*)')
        if fileName:
            try:
                with open(fileName, 'w') as config_file:
                    config_data = self.textEdit.toPlainText()
                    config_file.write(config_data)
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to save configuration file: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ConfigManager()
    ex.show()
    sys.exit(app.exec_())