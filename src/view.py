from PySide6.QtWidgets import QGraphicsView, QSizePolicy
from PySide6.QtCore import Signal
from PySide6.QtGui import QMouseEvent


class GraphicsView(QGraphicsView):
    signal_pressed = Signal(QMouseEvent)
    signal_released = Signal(QMouseEvent)

    def __init__(self, *args, **kwargs):
        super(GraphicsView, self).__init__(*args, **kwargs)
        self.start = None
        self.end = None
        self.box_list = list()
        self.__zoom = 0
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            factor = 1.25
            self.__zoom += 1
        else:
            factor = 0.8
        if self.__zoom > 0:
            self.scale(factor, factor)
        elif self.__zoom == 0:
            pass
        else:
            self.__zoom = 0

    def mousePressEvent(self, event: QMouseEvent) -> None:
        super(GraphicsView, self).mousePressEvent(event)
        self.signal_pressed[QMouseEvent].emit(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        super(GraphicsView, self).mouseReleaseEvent(event)
        self.signal_released[QMouseEvent].emit(event)