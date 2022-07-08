from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from typing import Optional

class Vertex(QGraphicsEllipseItem):
    count = 0
    v_point = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Vertex.count += 1
        self.v_number = int(Vertex.count)
        self.setBrush(QBrush(QColor(255, 255, 255)))
        self.checked = False
        self.pressed = False
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        super(Vertex, self).mousePressEvent(event)
        # self.setSelected(not self.isSelected())
        self.pressed = True
        print(self.isSelected())
        print(self.pos())
        self.v_point = self

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[QWidget] = ...) -> None:
        if self.isSelected():
            pen = painter.pen()
            pen.setWidth(50)
            painter.setPen(pen)
        super(Vertex, self).paint(painter, option, widget)

        # def focusInEvent(self, event):
        # print("+")

        # def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:

        '''super(Vertex, self).mouseReleaseEvent(event)
        self.setSelected(not self.isSelected())
        self.pressed = False
        print(self.isSelected())'''
