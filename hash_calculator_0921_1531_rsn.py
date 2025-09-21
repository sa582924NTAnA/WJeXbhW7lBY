# 代码生成时间: 2025-09-21 15:31:19
import sys
import hashlib
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QComboBox
from PyQt5.QtCore import Qt

"""
哈希值计算工具
"""

class HashCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口属性
        self.setWindowTitle('Hash Calculator')
        self.setGeometry(100, 100, 400, 200)

        # 创建布局
        layout = QVBoxLayout()

        # 文本框，用于输入待哈希的字符串
        self.textEdit = QTextEdit()
        layout.addWidget(self.textEdit)

        # 哈希算法下拉菜单
        self.comboBox = QComboBox()
        self.comboBox.addItems(['MD5', 'SHA1', 'SHA256', 'SHA512'])
        layout.addWidget(self.comboBox)

        # 按钮，点击计算哈希值
        self.calcButton = QPushButton('Calculate')
        self.calcButton.clicked.connect(self.calculateHash)
        layout.addWidget(self.calcButton)

        # 文本框，显示哈希结果
        self.resultTextEdit = QTextEdit()
        self.resultTextEdit.setReadOnly(True)
        layout.addWidget(self.resultTextEdit)

        # 设置布局
        self.setLayout(layout)

    def calculateHash(self):
        # 获取输入文本和选择的哈希算法
        text = self.textEdit.toPlainText()
        hash_type = self.comboBox.currentText()

        try:
            # 计算哈希值
            hash_value = self.calculate(text, hash_type)
            self.resultTextEdit.setText(hash_value)
        except Exception as e:
            # 错误处理
            self.resultTextEdit.setText(f'Error: {str(e)}')

    def calculate(self, text, hash_type):
        # 根据选择的哈希算法生成哈希值
        if hash_type == 'MD5':
            hash_obj = hashlib.md5()
        elif hash_type == 'SHA1':
            hash_obj = hashlib.sha1()
        elif hash_type == 'SHA256':
            hash_obj = hashlib.sha256()
        elif hash_type == 'SHA512':
            hash_obj = hashlib.sha512()
        else:
            raise ValueError('Invalid hash type')

        # 更新哈希对象
        hash_obj.update(text.encode('utf-8'))
        return hash_obj.hexdigest()

def main():
    app = QApplication(sys.argv)
    ex = HashCalculator()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()