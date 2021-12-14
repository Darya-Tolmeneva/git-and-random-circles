import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt
from random import randint
import design


class Main(QWidget, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.paint_circle = False
        self.setupUi(self)
        self.pushButton.clicked.connect(self.circle)

    def paintEvent(self, event):
        if self.paint_circle:
            painter = QPainter(self)
            r = randint(0, 256)
            g = randint(0, 256)
            b = randint(0, 256)
            color = QColor(r, g, b)
            painter.setBrush(QBrush(color, Qt.SolidPattern))
            x = randint(0, 400)
            y = randint(0, 400)
            w = h = randint(1, 400)
            painter.drawEllipse(x, y, w, h)

    def circle(self):
        self.paint_circle = True
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())