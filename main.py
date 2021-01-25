import random
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter()
            painter.begin(self)
            self.draw_circle(painter)
            painter.end()

    def draw_circle(self, painter):
        painter.setPen(QPen(self.get_random_color(),  8))
        painter.drawEllipse(*self.get_random_pos())

    def get_random_color(self):
        return QColor(255, 204, 0)

    def get_random_pos(self):
        s = random.randint(50, 100)
        x = random.randint(0, self.width() - s)
        y = random.randint(0, self.height() - s)
        return (x, y, s, s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
