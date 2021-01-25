import random
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor


class BaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout(self)

        self.button = QPushButton("Случайная окружность", self)
        main_layout.addWidget(self.button)
        main_layout.setAlignment(Qt.AlignBottom)


class MyWidget(BaseWindow):
    def __init__(self):
        super().__init__()
        self.button.clicked.connect(self.clicked)
        self.do_paint = False

    def clicked(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter()
            painter.begin(self)
            self.draw_circle(painter)
            painter.end()

    def draw_circle(self, painter):
        painter.setPen(QPen(self.get_random_color(), 8))
        painter.drawEllipse(*self.get_random_pos())

    def get_random_color(self):
        return QColor(*[random.randint(0, 255) for _ in range(3)])

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
