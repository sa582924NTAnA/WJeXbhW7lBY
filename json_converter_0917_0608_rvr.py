# 代码生成时间: 2025-09-17 06:08:51
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtCore import Qt

"""
JSON数据格式转换器
使用Python和PyQt框架创建一个GUI应用程序，用于转换JSON数据格式。
"""

class JsonConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题
        self.setWindowTitle('JSON数据格式转换器')
        # 设置窗口大小
        self.resize(600, 400)

        # 创建垂直布局
        layout = QVBoxLayout()

        # 创建文本编辑框，用于显示和编辑JSON数据
        self.json_text = QTextEdit()
        self.json_text.setPlaceholderText('在这里输入或粘贴JSON数据')
        layout.addWidget(self.json_text)

        # 创建按钮，用于执行JSON数据格式转换
        self.convert_button = QPushButton('转换JSON格式')
        self.convert_button.clicked.connect(self.convert_json)
        layout.addWidget(self.convert_button)

        # 创建文本编辑框，用于显示转换后的JSON数据
        self.formatted_json_text = QTextEdit()
        self.formatted_json_text.setReadOnly(True)
        layout.addWidget(self.formatted_json_text)

        # 设置布局
        self.setLayout(layout)

    def convert_json(self):
        # 从文本编辑框获取JSON数据
        json_data = self.json_text.toPlainText()

        try:
            # 尝试将JSON数据解析为Python对象
            data = json.loads(json_data)

            # 将Python对象格式化为JSON字符串
            formatted_json = json.dumps(data, indent=4)

            # 将格式化后的JSON数据显示在文本编辑框中
            self.formatted_json_text.setText(formatted_json)

        except json.JSONDecodeError as e:
            # 如果解析JSON数据失败，显示错误信息
            self.formatted_json_text.setText(f'JSON解析错误：{e}')

    def open_json_file(self):
        # 打开文件对话框，选择JSON文件
        file_name, _ = QFileDialog.getOpenFileName(self, '打开JSON文件', '', 'JSON文件 (*.json)')

        if file_name:
            # 读取JSON文件内容
            with open(file_name, 'r', encoding='utf-8') as file:
                json_data = file.read()

            # 将JSON文件内容显示在文本编辑框中
            self.json_text.setText(json_data)

    def save_json_file(self):
        # 打开文件对话框，保存JSON文件
        file_name, _ = QFileDialog.getSaveFileName(self, '保存JSON文件', '', 'JSON文件 (*.json)')

        if file_name:
            # 从文本编辑框获取JSON数据
            json_data = self.formatted_json_text.toPlainText()

            # 保存JSON数据到文件
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(json_data)

if __name__ == '__main__':
    # 创建应用程序实例
    app = QApplication(sys.argv)

    # 创建JSON数据格式转换器窗口实例
    converter = JsonConverter()

    # 显示窗口
    converter.show()

    # 运行应用程序
    sys.exit(app.exec_())