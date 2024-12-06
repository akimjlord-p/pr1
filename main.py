import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QPoint
from PyQt6 import uic
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        f = open('ui.ui', 'r')
        uic.loadUi(f, self)
        self.initUI()
        self.do_paint = False
        self.pos = QPoint(200, 200)
        self.draw.clicked.connect(self.paint)

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Рисование')

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        if self.do_paint:
            self.do_paint = False
        else:
            self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        qp.setBrush(QColor('yellow'))
        r = randint(1, 150)
        qp.drawEllipse(self.pos, r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
