from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PAINT v.2")
        self.setGeometry(400, 400, 800, 600)

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 3
        self.brushColor = Qt.black

        self.lastPoint = QPoint()

        MainMenu = self.menuBar()

        # Первая менюшка Файл - Сохранить
        FileMenu = MainMenu.addMenu("Файл")

        # Сохранить --> Сохранение

        FileSaveAction = QAction("Сохранить", self)
        FileSaveAction.setShortcut("Ctrl+S")
        FileMenu.addAction(FileSaveAction)
        FileSaveAction.triggered.connect(self.save)

        # Вторая менюшка Редакция --> и там мнго разного

        RevisionMenu = MainMenu.addMenu("Редактировать")
        """Дальше пошел код для редакции файла: Очистка, Кисточка (её размеры и цвета), 
        Ластик, Фигуры (Прямоугольник, Треугольник, Круг), Заливка"""

        # Редакция --> Очистка

        clearAction = QAction("Очистка", self)
        clearAction.setShortcut("Ctrl+C")
        RevisionMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        # Редакция --> Кисточка

        BrashMenu = RevisionMenu.addMenu("Кисточка")

        # Редакция --> Кисточка --> Размеры кисточки

        BrashSizeMenu = BrashMenu.addMenu("Размер кисточки")

        thereepxAction = QAction("3px", self)
        thereepxAction.setShortcut("Ctrl+T")
        BrashSizeMenu.addAction(thereepxAction)
        thereepxAction.triggered.connect(self.threePx)

        fivepxAction = QAction("5px", self)
        fivepxAction.setShortcut("Ctrl+F")
        BrashSizeMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePx)

        sevenpxAction = QAction("7px", self)
        sevenpxAction.setShortcut("Ctrl+S")
        BrashSizeMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPx)

        ninepxAction = QAction("9px", self)
        ninepxAction.setShortcut("Ctrl+N")
        BrashSizeMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePx)

        # Редакция --> Кисточка --> Цвет кисточки

        BrashColorMenu = BrashMenu.addMenu("Цвет кисточки")

        BrashColorAction = QAction("Поменять цвет", self)
        BrashColorAction.setShortcut("Ctrl+B")
        BrashColorMenu.addAction(BrashColorAction)
        BrashColorAction.triggered.connect(self.color)

        # Редакция --> Ластик

        EraserMenu = RevisionMenu.addMenu("Ластик")

        # Размер ластика

        # -//- что и для кисточки

        # Цвет ластика (по умолчанию должен стоять белый цвет)

        # -//- что и для кисточки

        # Редакция --> Фигуры

        ShapesMenu = RevisionMenu.addMenu("Фигуры")

        # Прямоугольник

        RectangleAction = QAction("Прямоугольник", self)
        # RectangleAction.setShortcut("Ctrl+B") !!!! Поменять комбинацию
        ShapesMenu.addAction(RectangleAction)
        RectangleAction.triggered.connect(self.color)  # !!!! Поменять функцию

        # Треугольник

        TriangleAction = QAction("Треугольник", self)
        # TriangleAction.setShortcut("Ctrl+B") !!!! Поменять комбинацию
        ShapesMenu.addAction(TriangleAction)
        TriangleAction.triggered.connect(self.color)  # !!!! Поменять функцию

        # Круг

        CircleleAction = QAction("Круг", self)
        # CircleleAction.setShortcut("Ctrl+B") !!!! Поменять комбинацию
        ShapesMenu.addAction(CircleleAction)
        CircleleAction.triggered.connect(self.color)  # !!!! Поменять функцию

        # Редакция --> Заливка

        FillMenu = RevisionMenu.addMenu("Заливка")

        # Заливка

        FillAction = QAction("Заливка", self)
        # FillAction.setShortcut("Ctrl+B") !!!! Поменять комбинацию
        FillMenu.addAction(FillAction)
        FillAction.triggered.connect(self.color)  # !!!! Поменять функцию

        # Третия менюшка - Помощь

        HelpMenu = MainMenu.addMenu("Помощь")

        # Помощь - Помощь

        HelpAction = QAction("Помощь", self)
        # HelpAction.setShortcut("Ctrl+B") !!!! Поменять комбинацию
        HelpMenu.addAction(HelpAction)
        HelpAction.triggered.connect(self.color)  # !!!! Поменять функцию

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def threePx(self):
        self.brushSize = 3

    def fivePx(self):
        self.brushSize = 5

    def sevenPx(self):
        self.brushSize = 7

    def ninePx(self):
        self.brushSize = 9

    def color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.brushColor = color


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
