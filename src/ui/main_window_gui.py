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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

from view import GraphicsView
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(656, 434)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.add_vertex_btn = QPushButton(self.widget_2)
        self.add_vertex_btn.setObjectName(u"add_vertex_btn")
        self.add_vertex_btn.setEnabled(True)
        self.add_vertex_btn.setMinimumSize(QSize(85, 34))
        icon = QIcon()
        icon.addFile(u":/ico/img/dobavit_vershinu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_vertex_btn.setIcon(icon)
        self.add_vertex_btn.setIconSize(QSize(20, 20))
        self.add_vertex_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.add_vertex_btn)

        self.add_edge_btn = QPushButton(self.widget_2)
        self.add_edge_btn.setObjectName(u"add_edge_btn")
        self.add_edge_btn.setMinimumSize(QSize(85, 34))
        icon1 = QIcon()
        icon1.addFile(u":/ico/img/dobavit_rebro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_edge_btn.setIcon(icon1)
        self.add_edge_btn.setIconSize(QSize(20, 20))
        self.add_edge_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.add_edge_btn)

        self.del_vertex_btn = QPushButton(self.widget_2)
        self.del_vertex_btn.setObjectName(u"del_vertex_btn")
        self.del_vertex_btn.setMinimumSize(QSize(85, 34))
        icon2 = QIcon()
        icon2.addFile(u":/ico/img/udalit_vershinu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.del_vertex_btn.setIcon(icon2)
        self.del_vertex_btn.setIconSize(QSize(20, 20))
        self.del_vertex_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.del_vertex_btn)

        self.del_edge_btn = QPushButton(self.widget_2)
        self.del_edge_btn.setObjectName(u"del_edge_btn")
        self.del_edge_btn.setMinimumSize(QSize(85, 34))
        icon3 = QIcon()
        icon3.addFile(u":/ico/img/udalit_rebro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.del_edge_btn.setIcon(icon3)
        self.del_edge_btn.setIconSize(QSize(20, 20))
        self.del_edge_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.del_edge_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.checkBox = QCheckBox(self.widget_2)
        self.checkBox.setObjectName(u"checkBox")
        font = QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(False)
        font1 = QFont()
        font1.setPointSize(14)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox = QSpinBox(self.widget_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setEnabled(False)
        self.spinBox.setFont(font1)

        self.horizontalLayout_2.addWidget(self.spinBox)


        self.verticalLayout.addWidget(self.widget_2)

        self.graphicsView = GraphicsView(self.widget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(200, 200))

        self.verticalLayout.addWidget(self.graphicsView)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setTextFormat(Qt.AutoText)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.run_btn = QPushButton(self.widget_4)
        self.run_btn.setObjectName(u"run_btn")
        self.run_btn.setMinimumSize(QSize(2, 32))
        font3 = QFont()
        font3.setFamilies([u"Courier New"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.run_btn.setFont(font3)

        self.horizontalLayout_3.addWidget(self.run_btn)


        self.verticalLayout.addWidget(self.widget_4)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.checkBox.clicked["bool"].connect(self.spinBox.setEnabled)
        self.checkBox.clicked["bool"].connect(self.label_2.setEnabled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_vertex_btn.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \n"
"\u0432\u0435\u0440\u0448\u0438\u043d\u0443", None))
#if QT_CONFIG(shortcut)
        self.add_vertex_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.add_edge_btn.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \n"
"\u0440\u0435\u0431\u0440\u043e", None))
#if QT_CONFIG(shortcut)
        self.add_edge_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.del_vertex_btn.setText(QCoreApplication.translate("MainWindow", u"\u0443\u0434\u0430\u043b\u0438\u0442\u044c \n"
"\u0432\u0435\u0440\u0448\u0438\u043d\u0443", None))
#if QT_CONFIG(shortcut)
        self.del_vertex_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.del_edge_btn.setText(QCoreApplication.translate("MainWindow", u"\u0443\u0434\u0430\u043b\u0438\u0442\u044c \n"
"\u0440\u0435\u0431\u0440\u043e", None))
#if QT_CONFIG(shortcut)
        self.del_edge_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u042d\u0432\u043e\u043b\u044e\u0446\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043e\u043d\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0446\u0432\u0435\u0442\u043e\u0432: ", None))
        self.run_btn.setText(QCoreApplication.translate("MainWindow", u"run", None))
    # retranslateUi

