# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

from view import GraphicsView
#import test_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(501, 338)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_vertex_btn = QPushButton(self.widget_2)
        self.add_vertex_btn.setObjectName(u"add_vertex_btn")
        self.add_vertex_btn.setEnabled(True)
        icon = QIcon()
        icon.addFile(u":/ico/img/dobavit_vershinu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_vertex_btn.setIcon(icon)
        self.add_vertex_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.add_vertex_btn)

        self.add_edge_btn = QPushButton(self.widget_2)
        self.add_edge_btn.setObjectName(u"add_edge_btn")
        icon1 = QIcon()
        icon1.addFile(u":/ico/img/dobavit_rebro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_edge_btn.setIcon(icon1)
        self.add_edge_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.add_edge_btn)

        self.del_vertex_btn = QPushButton(self.widget_2)
        self.del_vertex_btn.setObjectName(u"del_vertex_btn")
        icon2 = QIcon()
        icon2.addFile(u":/ico/img/udalit_vershinu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.del_vertex_btn.setIcon(icon2)
        self.del_vertex_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.del_vertex_btn)

        self.del_edge_btn = QPushButton(self.widget_2)
        self.del_edge_btn.setObjectName(u"del_edge_btn")
        icon3 = QIcon()
        icon3.addFile(u":/ico/img/udalit_rebro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.del_edge_btn.setIcon(icon3)
        self.del_edge_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.del_edge_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.widget_2)

        self.graphicsView = GraphicsView(self.widget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(200, 200))

        self.verticalLayout.addWidget(self.graphicsView)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout.addWidget(self.widget)

        self.run_btn = QPushButton(self.centralwidget)
        self.run_btn.setObjectName(u"run_btn")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.run_btn.setFont(font)

        self.horizontalLayout.addWidget(self.run_btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 501, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_vertex_btn.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432\u0435\u0440\u0448\u0438\u043d\u0443", None))
        self.add_edge_btn.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0435\u0431\u0440\u043e", None))
        self.del_vertex_btn.setText(QCoreApplication.translate("MainWindow", u"\u0443\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u0435\u0440\u0448\u0438\u043d\u0443", None))
        self.del_edge_btn.setText(QCoreApplication.translate("MainWindow", u"\u0443\u0434\u0430\u043b\u0438\u0442\u044c \u0440\u0435\u0431\u0440\u043e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0446\u0432\u0435\u0442\u043e\u0432:</span></p></body></html>", None))
        self.run_btn.setText(QCoreApplication.translate("MainWindow", u"run", None))
    # retranslateUi

