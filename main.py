import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic

SIZE_X, SIZE_Y = 300, 300


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.do_paint = False
        self.fig = 0
        self.x, self.y = random.randint(10, SIZE_X - 10), random.randint(10, SIZE_Y - 10)
        self.setMouseTracking(True)
        self.paint()

    def mouseMoveEvent(self, event):
        self.x, self.y = event.x(), event.y()

    def circle(self, qp):
        x, y = self.x, self.y
        d = min(x, y, SIZE_X - x, SIZE_Y - y)
        d = random.randint(10, d) // 2
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x - d, y - d, 2 * d, 2 * d)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            if self.fig == 0:
                self.circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def mousePressEvent(self, event):
        self.x, self.y = event.x(), event.y()
        if (event.button() == Qt.LeftButton):
            self.fig = 0
            self.paint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
