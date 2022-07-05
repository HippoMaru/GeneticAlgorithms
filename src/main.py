import sys  # sys нужен для передачи argv в QApplication
from PySide6 import QtWidgets, QtCore, QtGui
from ui.main_window_gui import Ui_MainWindow   # Это наш конвертированный файл дизайна


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__(*args, **kwargs)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.scene = QtWidgets.QGraphicsScene(0, 0, 300, 300, self)

        qp = QtGui.QPainter()
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setBrush(QtGui.QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)
        qp.drawRect(10, 15, 90, 60)

        self.scene.addLine(80, 55, 180, 55)
        self.scene.addLine(55, 80, 55, 180)
        self.scene.addLine(205, 80, 205, 180)
        self.scene.addLine(80, 205, 180, 205)

        self.scene.addEllipse(30, 30, 50, 50)
        self.scene.addEllipse(180, 30, 50, 50)
        self.scene.addEllipse(30, 180, 50, 50)
        self.scene.addEllipse(180, 180, 50, 50)

        self.graphicsView.setScene(self.scene)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
