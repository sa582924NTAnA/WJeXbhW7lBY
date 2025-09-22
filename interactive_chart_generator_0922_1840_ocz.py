# 代码生成时间: 2025-09-22 18:40:01
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis

"""
Interactive Chart Generator using PyQt framework.
This program allows users to generate interactive charts.
"""

class ChartGeneratorWidget(QWidget):
    """
    Widget for chart generation.
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Initialize the user interface."""
        self.setWindowTitle('Interactive Chart Generator')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.chart = QChart()
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        layout.addWidget(self.chart_view)

        self.button = QPushButton('Generate Random Chart', self)
        self.button.clicked.connect(self.generateRandomChart)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def generateRandomChart(self):
        """Generate a random chart."""
        series = QLineSeries()
        for i in range(10):
            x = i + 1
            y = 10 * (i + 1) + (2 * (i + 1) ** 2)
            series.append(x, y)

        self.chart.addSeries(series)
        self.chart.createDefaultAxes()
        self.chart.axisX().setRange(1, 10)
        self.chart.axisY().setRange(0, 100)
        self.chart.axisX().setLabelFormat('%i')
        self.chart.axisY().setLabelFormat('%i')
        self.chart.setTitle('Random Chart')
        self.chart.legend().hide()

class MainWindow(QMainWindow):
    """Main window class."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Interactive Chart Generator')
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(ChartGeneratorWidget())

    def closeEvent(self, event):
        """Handle close event."""
        if sys.platform.startswith('darwin'):
            event.accept()
            QApplication.quit()
        else:
            event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())