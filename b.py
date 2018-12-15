import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QMouseEvent
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.initUI()
    def initUI(self):
        self.resize(500,500)
        self.show()
    def paintEvent(self, e):
        if self.flag:
            self.flag = False
            self.paint = QPainter()
            self.paint.begin(self)
            self.paint.drawEllipse(self.x, self.y,10,10)
            self.paint.end()
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.flag = True
            self.x=e.pos().x()
            self.y=e.pos().y()
            self.update()

app = QApplication(sys.argv)
w = Example()
sys.exit(app.exec_())