# 代码生成时间: 2025-09-18 14:58:30
import sys
import logging
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLineEdit
from PyQt5.QtCore import pyqtSlot

"""
安全审计日志系统 - PyQt5 GUI 应用程序
实现基本的日志记录和显示功能。
"""

# 配置日志记录器
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)

class LogWidget(QWidget):
    """
    PyQt5 应用程序的主窗口类，用于显示和记录安全审计日志。
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        初始化用户界面组件。
        """
        self.layout = QVBoxLayout()

        # 日志显示文本框
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        self.layout.addWidget(self.log_display)

        # 日志输入框
        self.log_input = QLineEdit()
        self.layout.addWidget(self.log_input)

        # 日志记录按钮
        self.log_button = QPushButton('Record Log')
        self.log_button.clicked.connect(self.record_log)
        self.layout.addWidget(self.log_button)

        self.setLayout(self.layout)
        self.setWindowTitle('Security Audit Log System')
        self.resize(400, 300)

    @pyqtSlot()
    def record_log(self):
        """
        记录安全审计日志到文本框和文件。
        """
        log_message = self.log_input.text()
        if log_message:
            # 将日志信息写入到文本框
            self.log_display.append(log_message)
            # 使用日志记录器记录信息
            logger.info(log_message)
        else:
            self.log_input.setFocus()

class LogHandler(logging.FileHandler):
    """
    Custom LogHandler 用于将日志写入到文件。
    """
    def __init__(self, filename):
        super().__init__(filename)
        self.setFormatter(logging.Formatter(LOG_FORMAT))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 添加日志文件处理器
    handler = LogHandler('security_audit.log')
    logger.addHandler(handler)

    main_window = LogWidget()
    main_window.show()
    sys.exit(app.exec_())