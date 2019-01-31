import random
import os, shutil
from PIL import Image

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# Скрипт виджетов

class Window_(object):
    def ui_for_project(self, Window):
        self.centralWidget = QtWidgets.QWidget(Window)

        SizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                           QtWidgets.QSizePolicy.Maximum)
        SizePolicy.setHorizontalStretch(0)
        SizePolicy.setVerticalStretch(0)
        SizePolicy.setHeightForWidth(
            self.centralWidget.sizePolicy().hasHeightForWidth())

        self.centralWidget.setSizePolicy(SizePolicy)
        self.centralWidget.setObjectName("Центральный виджет")

        self.VerticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.VerticalLayout.setContentsMargins(11, 11, 11, 11)
        self.VerticalLayout.setSpacing(6)
        self.VerticalLayout.setObjectName("Вертикальное расположение")

        self.HorizontalLayout = QtWidgets.QHBoxLayout()
        self.HorizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.HorizontalLayout.setSpacing(6)
        self.HorizontalLayout.setObjectName("Горизонтальное расположение")

        self.VerticalLayout_2 = QtWidgets.QVBoxLayout()
        self.VerticalLayout_2.setSpacing(6)
        self.VerticalLayout_2.setObjectName("Вертикальное расположение 2")

        self.Widget = QtWidgets.QWidget(self.centralWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                           QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Widget.sizePolicy().hasHeightForWidth())

        self.Widget.setSizePolicy(sizePolicy)
        self.Widget.setObjectName("Виджет")

        self.gridLayout = QtWidgets.QGridLayout(self.Widget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName("Макет сетки")

        self.rectButton = QtWidgets.QPushButton(self.Widget)
        self.rectButton.setMinimumSize(QtCore.QSize(30, 30))
        self.rectButton.setMaximumSize(QtCore.QSize(30, 30))
        self.rectButton.setText("")

        QuadrilateralIcon = QtGui.QIcon()
        QuadrilateralIcon.addPixmap(QtGui.QPixmap(
            "icons/четырёхугольник.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.rectButton.setIcon(QuadrilateralIcon)
        self.rectButton.setCheckable(True)
        self.rectButton.setObjectName("Кнопка для четырёхугольника")

        self.gridLayout.addWidget(self.rectButton, 6, 0, 1, 1)

        self.eraserButton = QtWidgets.QPushButton(self.Widget)

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.eraserButton.sizePolicy().hasHeightForWidth())

        self.eraserButton.setSizePolicy(sizePolicy)
        self.eraserButton.setMinimumSize(QtCore.QSize(30, 30))
        self.eraserButton.setMaximumSize(QtCore.QSize(30, 30))
        self.eraserButton.setText("")

        Erasericon = QtGui.QIcon()
        Erasericon.addPixmap(QtGui.QPixmap("icons/Ластик.png"),
                             QtGui.QIcon.Normal,
                             QtGui.QIcon.Off)

        self.eraserButton.setIcon(Erasericon)
        self.eraserButton.setCheckable(True)
        self.eraserButton.setObjectName("Кнопка для ластика")

        self.gridLayout.addWidget(self.eraserButton, 1, 0, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.
                                           QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.brushButton = QtWidgets.QPushButton(self.Widget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.brushButton.sizePolicy().hasHeightForWidth())

        self.brushButton.setSizePolicy(sizePolicy)
        self.brushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.brushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.brushButton.setText("")

        BrushIcon = QtGui.QIcon()
        BrushIcon.addPixmap(QtGui.QPixmap("icons/Кисточка.png"),
                            QtGui.QIcon.Normal,
                            QtGui.QIcon.Off)

        self.brushButton.setIcon(BrushIcon)
        self.brushButton.setCheckable(True)
        self.brushButton.setObjectName("Кнопка для кисточки")

        self.gridLayout.addWidget(self.brushButton, 3, 1, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.fillButton = QtWidgets.QPushButton(self.Widget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fillButton.sizePolicy().hasHeightForWidth())

        self.fillButton.setSizePolicy(sizePolicy)
        self.fillButton.setMinimumSize(QtCore.QSize(30, 30))
        self.fillButton.setMaximumSize(QtCore.QSize(30, 30))
        self.fillButton.setText("")

        Fillicon = QtGui.QIcon()
        Fillicon.addPixmap(QtGui.QPixmap("icons/Заливка.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)

        self.fillButton.setIcon(Fillicon)
        self.fillButton.setCheckable(True)
        self.fillButton.setObjectName("Кнопка для заливки")
        self.gridLayout.addWidget(self.fillButton, 1, 1, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.polygonButton = QtWidgets.QPushButton(self.Widget)
        self.polygonButton.setMinimumSize(QtCore.QSize(30, 30))
        self.polygonButton.setMaximumSize(QtCore.QSize(30, 30))
        self.polygonButton.setText("")

        Polygonicon = QtGui.QIcon()
        Polygonicon.addPixmap(QtGui.QPixmap("icons/Многоугольник.png"),
                              QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)

        self.polygonButton.setIcon(Polygonicon)
        self.polygonButton.setCheckable(True)
        self.polygonButton.setObjectName("Кнопка для многоугольника")

        self.gridLayout.addWidget(self.polygonButton, 6, 1, 1, 1)

        self.ellipseButton = QtWidgets.QPushButton(self.Widget)
        self.ellipseButton.setMinimumSize(QtCore.QSize(30, 30))
        self.ellipseButton.setMaximumSize(QtCore.QSize(30, 30))
        self.ellipseButton.setText("")

        EllipseIcon = QtGui.QIcon()
        EllipseIcon.addPixmap(QtGui.QPixmap("icons/Эллипс.png"),
                              QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)

        self.ellipseButton.setIcon(EllipseIcon)
        self.ellipseButton.setCheckable(True)
        self.ellipseButton.setObjectName("Кнопка для эллипса")

        self.gridLayout.addWidget(self.ellipseButton, 7, 0, 1, 1)

        self.sprayButton = QtWidgets.QPushButton(self.Widget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sprayButton.sizePolicy().hasHeightForWidth())

        self.sprayButton.setSizePolicy(sizePolicy)
        self.sprayButton.setMinimumSize(QtCore.QSize(30, 30))
        self.sprayButton.setMaximumSize(QtCore.QSize(30, 30))
        self.sprayButton.setText("")

        SprayIcon = QtGui.QIcon()
        SprayIcon.addPixmap(QtGui.QPixmap("icons/Баллончик.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sprayButton.setIcon(SprayIcon)
        self.sprayButton.setCheckable(True)
        self.sprayButton.setFlat(False)
        self.sprayButton.setObjectName("Кнопка для баллончика")
        self.gridLayout.addWidget(self.sprayButton, 3, 0, 1, 1)

        self.VerticalLayout_2.addWidget(self.Widget)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)

        self.VerticalLayout_2.addItem(spacerItem)
        self.HorizontalLayout.addLayout(self.VerticalLayout_2)
        self.canvas = QtWidgets.QLabel(self.centralWidget)

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())

        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setText("")
        self.canvas.setObjectName("Холст")

        self.HorizontalLayout.addWidget(self.canvas)

        self.VerticalLayout.addLayout(self.HorizontalLayout)

        self.Widget_2 = QtWidgets.QWidget(self.centralWidget)
        self.Widget_2.setMinimumSize(QtCore.QSize(78, 50))
        self.Widget_2.setMaximumSize(QtCore.QSize(78, 50))
        self.Widget_2.setObjectName("Виджет 2")
        # Сначала идет побочная, т.к. главная должна перекрывать её

        # Побочная кнопка цвета
        self.SideButton = QtWidgets.QPushButton(self.Widget_2)
        self.SideButton.setGeometry(QtCore.QRect(30, 10, 40, 40))
        self.SideButton.setMinimumSize(QtCore.QSize(40, 40))
        self.SideButton.setMaximumSize(QtCore.QSize(40, 40))
        self.SideButton.setText("")
        self.SideButton.setObjectName("Побочная кнопка цвета")

        # Главная кнопка цвета
        self.MainButton = QtWidgets.QPushButton(self.Widget_2)
        self.MainButton.setGeometry(QtCore.QRect(10, 0, 40, 40))
        self.MainButton.setMinimumSize(QtCore.QSize(40, 40))
        self.MainButton.setMaximumSize(QtCore.QSize(40, 40))
        self.MainButton.setText("")
        self.MainButton.setObjectName("Главная кнопка цвета")

        self.VerticalLayout_2.addWidget(self.Widget_2)

        self.VerticalLayout_2.addItem(
            QtWidgets.QSpacerItem(40, 20,
                                  QtWidgets.QSizePolicy.Expanding,
                                  QtWidgets.QSizePolicy.Minimum))

        self.VerticalLayout.addLayout(self.VerticalLayout_2)

        Window.setCentralWidget(self.centralWidget)

        # Меню бар

        self.menuBar = QtWidgets.QMenuBar(Window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 549, 22))
        self.menuBar.setObjectName("MENU BAR")

        # Меню файла
        self.menuFIle = QtWidgets.QMenu(self.menuBar)
        self.menuFIle.setObjectName("Меню файла")

        # Меню редакции
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("Меню редакции")

        # Меню помощь
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("Меню помощь")

        Window.setMenuBar(self.menuBar)

        self.actionClearImage = QtWidgets.QAction(Window)
        self.actionClearImage.setObjectName("Очистка")

        self.actioneBackStep = QtWidgets.QAction(Window)
        self.actioneBackStep.setObjectName("Undo")

        self.actionHelpToUse = QtWidgets.QAction(Window)
        self.actionHelpToUse.setObjectName("Помощь")

        self.actionSaveImage = QtWidgets.QAction(Window)

        SaveIcon = QtGui.QIcon()
        SaveIcon.addPixmap(QtGui.QPixmap("icons/Сохранение.png"),
                           QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)

        self.actionSaveImage.setIcon(SaveIcon)
        self.actionSaveImage.setObjectName("Сохранение")

        self.actionNewImage = QtWidgets.QAction(Window)

        self.menuFIle.addAction(self.actionSaveImage)
        self.menuFIle.addAction(self.actioneBackStep)

        self.menuHelp.addAction(self.actionHelpToUse)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionClearImage)

        self.menuBar.addAction(self.menuFIle.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.drawingToolbar = QtWidgets.QToolBar(Window)
        self.drawingToolbar.setIconSize(QtCore.QSize(16, 16))
        Window.addToolBar(QtCore.Qt.TopToolBarArea, self.drawingToolbar)

        Window.setWindowTitle(QtCore.QCoreApplication.translate(
            "Window", "Pint-Point"))
        self.menuFIle.setTitle(QtCore.QCoreApplication.translate(
            "Window", "Файл"))
        self.menuEdit.setTitle(QtCore.QCoreApplication.translate(
            "Window", "Редактировать"))
        self.menuHelp.setTitle(QtCore.QCoreApplication.translate(
            "Window", "Помощь"))
        self.actionClearImage.setText(QtCore.QCoreApplication.translate(
            "Window", "Очистить"))
        self.actionClearImage.setShortcut(QtCore.QCoreApplication.translate(
            "Window", "Ctrl+D"))
        self.actionHelpToUse.setText(QtCore.QCoreApplication.translate(
            "Window", "Помощь"))
        self.actionHelpToUse.setShortcut(QtCore.QCoreApplication.translate(
            "Window", "Ctrl+H"))
        self.actioneBackStep.setText(QtCore.QCoreApplication.translate(
            "Window", "Undo"))
        self.actioneBackStep.setShortcut(QtCore.QCoreApplication.translate(
            "Window", "Ctrl+Z"))
        self.actionSaveImage.setText(QtCore.QCoreApplication.translate(
            "Window", "Сохранить изображение как"))
        self.actionSaveImage.setShortcut(QtCore.QCoreApplication.translate(
            "Window", "Ctrl+S"))
        QtCore.QMetaObject.connectSlotsByName(Window)


# Скрипт холста

# Режимы

regimes = [
    'eraser', 'fill',
    'brush', 'spray',
    'rect', 'polygon',
    'ellipse'
]


# Класс холста

class Canvas(QLabel):
    regime = 'rectangle'
    numkat = 0

    MainColor = QColor(Qt.black)  # Основной цвет
    SideColor = None  # Второй цвет

    config = {
        # Опции рисования
        'size': 1,
        'fill': True,
    }

    def set_config(self, key, value):
        self.config[key] = value

    active_color = None
    timer_event = None

    active_color = None
    timer_event = None

    def initialize(self):
        if self.SideColor:
            self.background_color = QColor(self.SideColor)
        else:
            self.background_color = QColor(Qt.white)
        if self.SideColor:
            self.Eraser_color = QColor(self.SideColor)
        else:
            self.Eraser_color = QColor(Qt.white)
        self.Eraser_color.setAlpha(100)
        self.reset()

    def reset(self):
        # Создадим растровое изображение для отображения
        self.setPixmap(QPixmap(600, 400))

        # Очистим холст
        self.pixmap().fill(self.background_color)

    # Установка главного цвета

    def install_maincolor(self, e):
        self.MainColor = QColor(e)

    # Установка второго цвета

    def install_sidecolor(self, hex):
        self.SideColor = QColor(hex)

    # Установка режима по умолчанию

    def installation_mode(self, regime):
        # Очистить активную анимацию таймера
        self.timer_cleanup()
        # Сбросить зависящие от режима переменные
        self.active_shape_function = None
        self.active_shape_args = ()

        self.origin_pos = None

        self.current_position = None
        self.last_pos = None

        self.position_change_history = None
        self.last_history = []

        self.dash_offset = 0
        self.locked = False

        self.regime = regime

    # Функция сброса

    def reset_mode(self):
        self.installation_mode(self.regime)

    # Функция включения таймера (т.к. все действия временные)

    def timer_on(self):
        if self.timer_event:
            self.timer_event()

    # Очистим таймер нового действия

    def timer_cleanup(self):
        if self.timer_event:
            # Остановим таймер, затем запустите очистку.
            timer_event = self.timer_event
            self.timer_event = None
            timer_event(final=True)

    # События мыши.

    def mousePressEvent(self, mouse):
        if getattr(self, "%s_mousePressEvent" % self.regime, None):
            return getattr(self, "%s_mousePressEvent" % self.regime,
                           None)(mouse)

    def mouseMoveEvent(self, mouse):
        if getattr(self, "%s_mouseMoveEvent" % self.regime, None):
            return getattr(self, "%s_mouseMoveEvent" % self.regime,
                           None)(mouse)

    def mouseReleaseEvent(self, mouse):
        if getattr(self, "%s_mouseReleaseEvent" % self.regime, None):
            self.numkat += 1
            pixmap = self.pixmap()
            pixmap.save('screens\picture' + str(self.numkat), "PNG")
            return getattr(self, "%s_mouseReleaseEvent" % self.regime,
                           None)(mouse)

    def mouseDoubleClickEvent(self, mouse):
        if getattr(self, "%s_mouseDoubleClickEvent" % self.regime, None):
            return getattr(self, "%s_mouseDoubleClickEvent" % self.regime,
                           None)(mouse)

    """ Общие события (общие для инструментов, похожих на кисть 
    (т.е кисточка, ластик, баллончик(распылитель)))"""

    def generic_mousePressEvent(self, mouse):
        self.last_pos = mouse.pos()

        if mouse.button() == Qt.LeftButton:
            self.active_color = self.MainColor
        else:
            self.active_color = self.SideColor

    def generic_mouseReleaseEvent(self, e):
        self.last_pos = None

    # Кисточка

    def brush_mousePressEvent(self, e):
        self.generic_mousePressEvent(e)

    def brush_mouseMoveEvent(self, e):
        if self.last_pos:
            p = QPainter(self.pixmap())
            p.setPen(QPen(self.active_color, self.config['size'] * 3,
                          Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            p.drawLine(self.last_pos, e.pos())

            self.last_pos = e.pos()
            self.update()

    def brush_mouseReleaseEvent(self, e):
        self.generic_mouseReleaseEvent(e)

    # События четырехугольника

    def selectrect_mousePressEvent(self, e):
        self.active_shape_function = 'drawRect'
        self.preview_pen = QPen(QColor(0xff, 0xff, 0xff), 1, Qt.DashLine)
        self.generic_shape_mousePressEvent(e)

    def selectrect_timerEvent(self, final=False):
        self.generic_shape_timerEvent(final)

    def selectrect_mouseMoveEvent(self, e):
        if not self.locked:
            self.current_position = e.pos()

    def selectrect_mouseReleaseEvent(self, e):
        self.current_position = e.pos()
        self.locked = True

    # События ластика

    def eraser_mousePressEvent(self, e):
        self.generic_mousePressEvent(e)

    def eraser_mouseMoveEvent(self, e):
        if self.last_pos:
            p = QPainter(self.pixmap())
            p.setPen(QPen(self.Eraser_color, 30,
                          Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            p.drawLine(self.last_pos, e.pos())

            self.last_pos = e.pos()
            self.update()

    def eraser_mouseReleaseEvent(self, e):
        self.generic_mouseReleaseEvent(e)

    # События баллончика (распылителя)

    def spray_mousePressEvent(self, e):
        self.generic_mousePressEvent(e)

    def spray_mouseMoveEvent(self, e):
        if self.last_pos:
            p = QPainter(self.pixmap())
            p.setPen(QPen(self.active_color, 1))

            for n in range(self.config['size'] * 100):  # Можно изменить умножатель(по умолчанию стоит 100)
                xo = random.gauss(0, self.config['size'] * 5)  # чем он больше, тем "жирнее" будет рисовать
                yo = random.gauss(0, self.config['size'] * 5)  # распылитель
                p.drawPoint(e.x() + xo, e.y() + yo)

        self.update()

    def spray_mouseReleaseEvent(self, e):
        self.generic_mouseReleaseEvent(e)

    # Событие заливки

    def fill_mousePressEvent(self, e):

        if e.button() == Qt.LeftButton:
            self.active_color = self.MainColor
        else:
            self.active_color = self.SideColor

        # Преобразуем в изображение для попиксельного чтения
        image = self.pixmap().toImage()
        w, h = image.width(), image.height()
        s = image.bits().asstring(w * h * 4)
        x, y = e.x(), e.y()
        # Найдём 3-байтовое значение в нашем текущем местоположении.
        i = (x + (y * w)) * 4
        target_color = s[i:i + 3]

        # Конвертирование байтовой строки в 1 байт. True - 255, False - 0
        s = b''.join(b'\xff' if s[n:n + 3] == target_color else b'\x00' for n in range(
            0, len(s), 4))

        def get_pixel(x, y):
            return s[x + (y * w)]

        have_seen = set()
        to_fill = []
        xy = [(x, y)]

        def get_points(have_seen, center_pos):
            points = []
            cx, cy = center_pos
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                xx, yy = cx + x, cy + y
                if (xx >= 0 and xx < w and yy >= 0 and yy < h
                        and ((xx, yy) not in have_seen)):
                    points.append((xx, yy))
                    have_seen.add((xx, yy))
            return points

        while xy:
            x, y = xy.pop()
            if get_pixel(x, y):
                to_fill.append((x, y))
                xy.extend(get_points(have_seen, (x, y)))

        if to_fill:
            # Теперь у нас есть точки для заливки
            p = QPainter(self.pixmap())
            p.setPen(QPen(self.active_color))
            p.drawPoints(*[QPoint(*xy) for xy in to_fill])
            self.update()
            self.numkat += 1
            pixmap = self.pixmap()
            pixmap.save('screens\picture' + str(self.numkat), "PNG")
    # Общие события для фигур как многоугольник (Четырехугольник, многоугольник, эллипс)

    def generic_shape_mousePressEvent(self, e):
        self.origin_pos = e.pos()
        self.current_position = e.pos()
        self.timer_event = self.generic_shape_timerEvent

    def generic_shape_timerEvent(self, final=False):
        p = QPainter(self.pixmap())
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen = self.preview_pen
        pen.setDashOffset(self.dash_offset)
        p.setPen(pen)
        if self.last_pos:
            getattr(p, self.active_shape_function)(QRect(
                self.origin_pos, self.last_pos), *self.active_shape_args)

        if not final:
            self.dash_offset -= 1
            pen.setDashOffset(self.dash_offset)
            p.setPen(pen)
            getattr(p, self.active_shape_function)(QRect(
                self.origin_pos, self.current_position), *self.active_shape_args)

        self.update()
        self.last_pos = self.current_position

    def generic_shape_mouseMoveEvent(self, e):
        self.current_position = e.pos()

    def generic_shape_mouseReleaseEvent(self, e):
        if self.last_pos:
            # Индикатор очистки
            self.timer_cleanup()

            p = QPainter(self.pixmap())
            p.setPen(QPen(self.MainColor, self.config['size'],
                          Qt.SolidLine, Qt.SquareCap, Qt.MiterJoin))

            if self.config['fill']:
                p.setBrush(QBrush(self.SideColor))
            getattr(p, self.active_shape_function)(QRect(
                self.origin_pos, e.pos()), *self.active_shape_args)
            self.update()

        self.reset_mode()

    # Четырехугольник

    def rect_mousePressEvent(self, e):
        self.active_shape_function = 'drawRect'
        self.active_shape_args = ()
        self.preview_pen = QPen(QColor(0xff, 0xff, 0xff), 1, Qt.SolidLine)
        self.generic_shape_mousePressEvent(e)

    def rect_timerEvent(self, final=False):
        self.generic_shape_timerEvent(final)

    def rect_mouseMoveEvent(self, e):
        self.generic_shape_mouseMoveEvent(e)

    def rect_mouseReleaseEvent(self, e):
        self.generic_shape_mouseReleaseEvent(e)

    # Многоугольник

    def Polygon_mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            if self.position_change_history:
                self.position_change_history.append(e.pos())
            else:
                self.position_change_history = [e.pos()]
                self.current_position = e.pos()
                self.timer_event = self.Polygon_timerEvent
            self.numkat += 1
            pixmap = self.pixmap()
            pixmap.save('screens\picture' + str(self.numkat), "PNG")
        elif e.button() == Qt.RightButton and self.position_change_history:
            # Убираем, мы не рисуем
            self.timer_cleanup()
            self.reset_mode()

    def Polygon_timerEvent(self, final=False):
        p = QPainter(self.pixmap())
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen = self.preview_pen
        pen.setDashOffset(self.dash_offset)
        p.setPen(pen)
        if self.last_history:
            getattr(p, self.active_shape_function)(*self.last_history)

        if not final:
            self.dash_offset -= 1
            pen.setDashOffset(self.dash_offset)
            p.setPen(pen)
            getattr(p, self.active_shape_function)(
                *self.position_change_history + [self.current_position])

        self.update()
        self.last_pos = self.current_position
        self.last_history = self.position_change_history + [self.current_position]

    def generic_poly_mouseMoveEvent(self, e):
        self.current_position = e.pos()

    def generic_poly_mouseDoubleClickEvent(self, e):
        self.timer_cleanup()
        p = QPainter(self.pixmap())
        p.setPen(QPen(self.MainColor,
                      self.config['size'], Qt.SolidLine, Qt.RoundCap,
                      Qt.RoundJoin))

        getattr(p, self.active_shape_function)(*self.position_change_history + [e.pos()])
        self.update()
        self.reset_mode()

    def polygon_mousePressEvent(self, e):
        self.active_shape_function = 'drawPolygon'
        self.preview_pen = QPen(QColor(0xff, 0xff, 0xff), 1, Qt.SolidLine)
        self.Polygon_mousePressEvent(e)

    def polygon_timerEvent(self, final=False):
        self.Polygon_timerEvent(final)

    def polygon_mouseMoveEvent(self, e):
        self.current_position = e.pos()

    def polygon_mouseDoubleClickEvent(self, e):
        self.generic_poly_mouseDoubleClickEvent(e)

    # Эллипс

    def ellipse_mousePressEvent(self, e):
        self.active_shape_function = 'drawEllipse'
        self.active_shape_args = ()
        self.preview_pen = QPen(QColor(0xff, 0xff, 0xff), 1, Qt.SolidLine)
        self.generic_shape_mousePressEvent(e)

    def ellipse_timerEvent(self, final=False):
        self.generic_shape_timerEvent(final)

    def ellipse_mouseMoveEvent(self, e):
        self.generic_shape_mouseMoveEvent(e)

    def ellipse_mouseReleaseEvent(self, e):
        self.generic_shape_mouseReleaseEvent(e)


# Главный собирающий класс включающий в себя классы canvas и window_,
# а также реализирующий их

class MainWindow(QMainWindow, Window_, ):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui_for_project(self)
        self.setWindowIcon(QIcon('icons/paint.png'))

        self.HorizontalLayout.removeWidget(self.canvas)
        self.canvas = Canvas()
        self.canvas.initialize()
        '''Нам нужно включить отслеживание мыши, 
        чтобы следовать за мышью без нажатия кнопки.'''
        self.canvas.setMouseTracking(True)
        # Включить фокус для захвата ключевых входов.
        self.canvas.setFocusPolicy(Qt.StrongFocus)
        self.HorizontalLayout.addWidget(self.canvas)

        # Настроим кнопки режима
        regime_group = QButtonGroup(self)
        regime_group.setExclusive(True)
        folder = 'screens'

        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)

        im = Image.new("RGB", (600, 400))
        pix = im.load()
        for x in range(600):
            for y in range(400):
                pix[x, y] = (255, 255, 255)

        im.save('screens/picture0.png')

        for regime in regimes:
            btn = getattr(self, '%sButton' % regime)
            btn.pressed.connect(
                lambda regime=regime: self.canvas.installation_mode(regime))
            regime_group.addButton(btn)

        # Настроим кнопки выбора цвета.
        self.MainButton.pressed.connect(
            lambda: self.Choose_a_color(self.install_maincolor))
        self.SideButton.pressed.connect(
            lambda: self.Choose_a_color(self.install_sidecolor))

        #  Инициализируем таймер

        self.timer = QTimer()
        self.timer.timeout.connect(self.canvas.timer_on)
        self.timer.setInterval(100)
        self.timer.start()

        # Установим цвета по умолчанию

        self.install_maincolor('#000000')  # Основной цвет - Черный
        self.install_sidecolor('#ffffff')  # Второй цвет - Белый

        # Меню опций

        self.actionNewImage.triggered.connect(self.canvas.initialize)
        self.actionHelpToUse.triggered.connect(self.help)
        self.actionSaveImage.triggered.connect(self.save)
        self.actioneBackStep.triggered.connect(self.UnDo)
        self.actionClearImage.triggered.connect(self.canvas.reset)

        # Размер для кисточки, контура фигур, ластика и баллончика (расспылителя)

        self.sizeselect = QSlider()
        self.sizeselect.setRange(1, 20)
        self.sizeselect.setOrientation(Qt.Horizontal)
        self.sizeselect.valueChanged.connect(lambda s: self.canvas.set_config('size', s))
        self.drawingToolbar.addWidget(self.sizeselect)

        self.show()

    # Функция для выбора цвета

    def Choose_a_color(self, e):
        colordialog = QColorDialog()
        if colordialog.exec():
            e(colordialog.selectedColor().name())

    # Функция для установки выбранного цвета на главный

    def install_maincolor(self, e):
        self.canvas.install_maincolor(e)
        self.MainButton.setStyleSheet('QPushButton { background-color: %s; }' % e)

    # Функция для установки выбранного цвета на второй

    def install_sidecolor(self, e):
        self.canvas.install_sidecolor(e)
        self.SideButton.setStyleSheet('QPushButton { background-color: %s; }' % e)

    # функция Помощи

    def help(self):
        system('start ПрочтиМеня.txt')

    # Функция Back_Step

    def UnDo(self):
        try:
            if self.canvas.numkat > 0:
                self.canvas.numkat -= 1
                pixmap = QPixmap()
                pixmap.load('screens\picture' + str(self.canvas.numkat))
                self.canvas.setPixmap(pixmap)
                os.remove("screens\picture" + str(self.canvas.numkat + 1))
            else:
                pass
        except:
            pass

    # Функция сохранения

    def save(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Save file", "",
            "PNG Image file (*.png);; JPEG Image file (*.jpg);;All Files (*.*)")

        if path:
            pixmap = self.canvas.pixmap()
            pixmap.save(path, "PNG")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
