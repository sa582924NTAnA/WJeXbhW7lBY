# 代码生成时间: 2025-09-22 01:01:55
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout,
                                    QHBoxLayout, QPushButton, QTextEdit, QLineEdit, QMessageBox)

class InventoryManagement(QMainWindow):
    """库存管理系统的主窗口类"""
    def __init__(self):
        super().__init__()
        self.title = '库存管理系统'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.__init_ui__()

    def __init_ui__(self):
        """初始化用户界面"""
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout()

        # 显示库存信息的文本框
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        layout.addWidget(self.text_edit)

        # 操作按钮
        operation_layout = QHBoxLayout()
        self.add_button = QPushButton('添加库存', self)
        self.add_button.clicked.connect(self.add_inventory)
        operation_layout.addWidget(self.add_button)

        self.remove_button = QPushButton('移除库存', self)
        self.remove_button.clicked.connect(self.remove_inventory)
        operation_layout.addWidget(self.remove_button)

        self.update_button = QPushButton('更新库存', self)
        self.update_button.clicked.connect(self.update_inventory)
        operation_layout.addWidget(self.update_button)

        layout.addLayout(operation_layout)

        self.main_widget.setLayout(layout)

        # 初始库存数据
        self.inventory = {}

    def add_inventory(self):
        """添加库存信息"""
        item, ok = QInputDialog.getItem(self, '添加库存', '选择商品：', self.inventory.keys(), editable=True)
        if ok and item:
            try:
                quantity = int(QInputDialog.getInt(self, '添加库存', '输入数量：', value=1))
                self.inventory[item] = self.inventory.get(item, 0) + quantity
                self.update_text_edit()
            except ValueError:
                QMessageBox.warning(self, '错误', '请输入有效的数量')

    def remove_inventory(self):
        """移除库存信息"""
        item, ok = QInputDialog.getItem(self, '移除库存', '选择商品：', self.inventory.keys())
        if ok and item in self.inventory:
            try:
                quantity = int(QInputDialog.getInt(self, '移除库存', '输入数量：', value=1))
                if quantity > self.inventory[item]:
                    QMessageBox.warning(self, '错误', '移除数量不能大于库存数量')
                else:
                    self.inventory[item] -= quantity
                    self.update_text_edit()
                    if self.inventory[item] == 0:
                        del self.inventory[item]
            except ValueError:
                QMessageBox.warning(self, '错误', '请输入有效的数量')

    def update_inventory(self):
        """更新库存信息"""
        item, ok = QInputDialog.getItem(self, '更新库存', '选择商品：', self.inventory.keys())
        if ok and item in self.inventory:
            try:
                quantity = int(QInputDialog.getInt(self, '更新库存', '输入新的数量：', value=self.inventory[item]))
                self.inventory[item] = quantity
                self.update_text_edit()
            except ValueError:
                QMessageBox.warning(self, '错误', '请输入有效的数量')

    def update_text_edit(self):
        """更新文本框显示的库存信息"""
        self.text_edit.setText('')
        for item, quantity in self.inventory.items():
            self.text_edit.append(f'{item}: {quantity}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InventoryManagement()
    ex.show()
    sys.exit(app.exec_())