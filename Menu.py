from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def UI_FOR_PROJECT(self, Window):
        self.centralWidget = QtWidgets.QWidget(Window)

        SizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        SizePolicy.setHorizontalStretch(0)
        SizePolicy.setVerticalStretch(0)
        SizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())

        self.centralWidget.setSizePolicy(SizePolicy)
        self.centralWidget.setObjectName("Центральный виджет")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("Вертикальное расположение")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("Горизонтальное расположение")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("Вертикальное расположение 2")

        self.widget = QtWidgets.QWidget(self.centralWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())

        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("Виджет")

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName("Макет сетки")

        self.rectButton = QtWidgets.QPushButton(self.widget)
        self.rectButton.setMinimumSize(QtCore.QSize(30, 30))
        self.rectButton.setMaximumSize(QtCore.QSize(30, 30))
        self.rectButton.setText("")

        quadrilateralicon = QtGui.QIcon()
        quadrilateralicon.addPixmap(QtGui.QPixmap("icons/четырёхугольник.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.rectButton.setIcon(quadrilateralicon)
        self.rectButton.setCheckable(True)
        self.rectButton.setObjectName("Кнопка для четырёхугольника")

        self.gridLayout.addWidget(self.rectButton, 6, 0, 1, 1)

        self.eraserButton = QtWidgets.QPushButton(self.widget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eraserButton.sizePolicy().hasHeightForWidth())

        self.eraserButton.setSizePolicy(sizePolicy)
        self.eraserButton.setMinimumSize(QtCore.QSize(30, 30))
        self.eraserButton.setMaximumSize(QtCore.QSize(30, 30))
        self.eraserButton.setText("")

        Erasericon = QtGui.QIcon()
        Erasericon.addPixmap(QtGui.QPixmap("icons/Ластик.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.eraserButton.setIcon(Erasericon)
        self.eraserButton.setCheckable(True)
        self.eraserButton.setObjectName("Кнопка для ластика")

        self.gridLayout.addWidget(self.eraserButton, 1, 0, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.brushButton = QtWidgets.QPushButton(self.widget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brushButton.sizePolicy().hasHeightForWidth())

        self.brushButton.setSizePolicy(sizePolicy)
        self.brushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.brushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.brushButton.setText("")

        Brushicon = QtGui.QIcon()
        Brushicon.addPixmap(QtGui.QPixmap("icons/Кисточка.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.brushButton.setIcon(Brushicon)
        self.brushButton.setCheckable(True)
        self.brushButton.setObjectName("Кнопка для кисточки")

        self.gridLayout.addWidget(self.brushButton, 3, 1, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.fillButton = QtWidgets.QPushButton(self.widget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillButton.sizePolicy().hasHeightForWidth())

        self.fillButton.setSizePolicy(sizePolicy)
        self.fillButton.setMinimumSize(QtCore.QSize(30, 30))
        self.fillButton.setMaximumSize(QtCore.QSize(30, 30))
        self.fillButton.setText("")

        Fillicon = QtGui.QIcon()
        Fillicon.addPixmap(QtGui.QPixmap("icons/Заливка.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.fillButton.setIcon(Fillicon)
        self.fillButton.setCheckable(True)
        self.fillButton.setObjectName("Кнопка для заливки")
        self.gridLayout.addWidget(self.fillButton, 1, 1, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.polygonButton = QtWidgets.QPushButton(self.widget)
        self.polygonButton.setMinimumSize(QtCore.QSize(30, 30))
        self.polygonButton.setMaximumSize(QtCore.QSize(30, 30))
        self.polygonButton.setText("")

        Polygonicon = QtGui.QIcon()
        Polygonicon.addPixmap(QtGui.QPixmap("icons/Многоугольник.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.polygonButton.setIcon(Polygonicon)
        self.polygonButton.setCheckable(True)
        self.polygonButton.setObjectName("Кнопка для многоугольника")

        self.gridLayout.addWidget(self.polygonButton, 6, 1, 1, 1)

        self.ellipseButton = QtWidgets.QPushButton(self.widget)
        self.ellipseButton.setMinimumSize(QtCore.QSize(30, 30))
        self.ellipseButton.setMaximumSize(QtCore.QSize(30, 30))
        self.ellipseButton.setText("")

        Ellipseicon = QtGui.QIcon()
        Ellipseicon.addPixmap(QtGui.QPixmap("icons/Эллипс.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.ellipseButton.setIcon(Ellipseicon)
        self.ellipseButton.setCheckable(True)
        self.ellipseButton.setObjectName("Кнопка для эллипса")

        self.gridLayout.addWidget(self.ellipseButton, 7, 0, 1, 1)

        self.sprayButton = QtWidgets.QPushButton(self.widget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sprayButton.sizePolicy().hasHeightForWidth())

        self.sprayButton.setSizePolicy(sizePolicy)
        self.sprayButton.setMinimumSize(QtCore.QSize(30, 30))
        self.sprayButton.setMaximumSize(QtCore.QSize(30, 30))
        self.sprayButton.setText("")

        Sprayicon = QtGui.QIcon()
        Sprayicon.addPixmap(QtGui.QPixmap("icons/Баллончик.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sprayButton.setIcon(Sprayicon)
        self.sprayButton.setCheckable(True)
        self.sprayButton.setFlat(False)
        self.sprayButton.setObjectName("Кнопка для баллончика")
        self.gridLayout.addWidget(self.sprayButton, 3, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.widget)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.canvas = QtWidgets.QLabel(self.centralWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())

        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setText("")
        self.canvas.setObjectName("Холст")

        self.horizontalLayout.addWidget(self.canvas)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widget_2 = QtWidgets.QWidget(self.centralWidget)
        self.widget_2.setMinimumSize(QtCore.QSize(78, 50))
        self.widget_2.setMaximumSize(QtCore.QSize(78, 50))
        self.widget_2.setObjectName("Виджет 2")
        # Сначала идет побочная, т.к. главная должна перекрывать её

        # Побочная кнопка цвета
        self.SideButton = QtWidgets.QPushButton(self.widget_2)
        self.SideButton.setGeometry(QtCore.QRect(30, 10, 40, 40))
        self.SideButton.setMinimumSize(QtCore.QSize(40, 40))
        self.SideButton.setMaximumSize(QtCore.QSize(40, 40))
        self.SideButton.setText("")
        self.SideButton.setObjectName("Побочная кнопка цвета")

        # Главная кнопка цвета
        self.MainButton = QtWidgets.QPushButton(self.widget_2)
        self.MainButton.setGeometry(QtCore.QRect(10, 0, 40, 40))
        self.MainButton.setMinimumSize(QtCore.QSize(40, 40))
        self.MainButton.setMaximumSize(QtCore.QSize(40, 40))
        self.MainButton.setText("")
        self.MainButton.setObjectName("Главная кнопка цвета")

        self.verticalLayout_2.addWidget(self.widget_2)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(spacerItem1)

        self.verticalLayout.addLayout(self.verticalLayout_2)

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

        # Меню помощи
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("Меню Помощи")

        Window.setMenuBar(self.menuBar)

        self.actionCopy = QtWidgets.QAction(Window)
        self.actionCopy.setObjectName("Копия")

        self.actionClearImage = QtWidgets.QAction(Window)
        self.actionClearImage.setObjectName("Очистка")

        self.actionSaveImage = QtWidgets.QAction(Window)

        Saveicon = QtGui.QIcon()
        Saveicon.addPixmap(QtGui.QPixmap("icons/Сохранение.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionSaveImage.setIcon(Saveicon)
        self.actionSaveImage.setObjectName("Сохранение")

        self.actionNewImage = QtWidgets.QAction(Window)

        self.menuFIle.addAction(self.actionSaveImage)

        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionClearImage)

        self.menuHelp.addSeparator()

        self.menuBar.addAction(self.menuFIle.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.drawingToolbar = QtWidgets.QToolBar(Window)
        self.drawingToolbar.setIconSize(QtCore.QSize(16, 16))
        Window.addToolBar(QtCore.Qt.TopToolBarArea, self.drawingToolbar)

        Window.setWindowTitle(QtCore.QCoreApplication.translate("Window", "Pint-Point"))
        self.menuFIle.setTitle(QtCore.QCoreApplication.translate("Window", "Файл"))
        self.menuEdit.setTitle(QtCore.QCoreApplication.translate("Window", "Редактировать"))
        self.menuHelp.setTitle(QtCore.QCoreApplication.translate("Window", "Помощь"))
        self.actionCopy.setText(QtCore.QCoreApplication.translate("Window", "Скопировать"))
        self.actionCopy.setShortcut(QtCore.QCoreApplication.translate("Window", "Ctrl+C"))
        self.actionClearImage.setText(QtCore.QCoreApplication.translate("Window", "Очистить"))
        self.actionClearImage.setShortcut(QtCore.QCoreApplication.translate("Window", "Ctrl+D"))
        self.actionSaveImage.setText(QtCore.QCoreApplication.translate("Window", "Сохранить изображение как"))
        self.actionSaveImage.setShortcut(QtCore.QCoreApplication.translate("Window", "Ctrl+S"))
        QtCore.QMetaObject.connectSlotsByName(Window)
