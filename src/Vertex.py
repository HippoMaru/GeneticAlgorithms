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
        self.m_edge_list = {}
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        super(Vertex, self).mousePressEvent(event)
        # self.setSelected(not self.isSelected())
        self.pressed = True
        print(self.isSelected())
        print(self.pos())
        self.v_point = self

        pen = QPen()
        self.isActive()
        if self.isActive():
            pen.setWidth(1)
            self.setPen(pen)
        else:
            pen.setWidth(1)
            self.setPen(pen)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        super(Vertex, self).mouseMoveEvent(event)

        for edge in self.m_edge_list.values():
            left_x = edge.m_left_vertex.sceneBoundingRect().x()
            left_y = edge.m_left_vertex.sceneBoundingRect().y()
            right_x = edge.m_left_vertex.sceneBoundingRect().x()
            right_y = edge.m_left_vertex.sceneBoundingRect().x()
            print(left_x, left_y, right_x, right_y)
            edge.my_update()

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

    def set_color(self, brush):
        pass