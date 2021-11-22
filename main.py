import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi("UI.ui", self)
        qp = QPainter()
        qp.begin(self)
        self.btn.clicked.connect(self.draw)
        self.flag = False

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.flag:
            self.flag = False
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))
            qp.drawEllipse(randint(5, 200), randint(5, 200), randint(5, 200), randint(5, 200))
            qp.end()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
