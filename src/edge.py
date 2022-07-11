from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from typing import Optional
from typing import Union
from math import sqrt, pow


class Edge(QGraphicsLineItem):
    count = 0

    def __init__(self, left_vertex=None, right_vertex=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Edge.count += 1
        self.e_number = int(Edge.count)
        self.setZValue(-99)
        self.m_left_vertex = left_vertex
        self.m_right_vertex = right_vertex
        pen = QPen()
        pen.setWidth(2)
        self.setPen(pen)
        self.checked = False
        self.pressed = False
        self.setFlag(QGraphicsItem.ItemIsSelectable, False)
        self.setFlag(QGraphicsItem.ItemIsMovable, False)

        self.m_left_vertex.m_edge_list[self.e_number] = self
        self.m_right_vertex.m_edge_list[self.e_number] = self

    def cood_recalc(self, left_x, left_y, right_x, right_y):
        left_x += 10
        left_y += 10
        right_x += 10
        right_y += 10

        length = sqrt((right_x - left_x) ** 2 + (right_y - left_y) ** 2)
        ratio = (length - 10) / 10

        right_x = (left_x + ratio * right_x) / (1 + ratio)
        right_y = (left_y + ratio * right_y) / (1 + ratio)
        ratio = (length - 20) / 10
        left_x = (right_x + ratio * left_x) / (1 + ratio)
        left_y = (right_y + ratio * left_y) / (1 + ratio)
        return [left_x, left_y, right_x, right_y]

    def my_update(self):
        coord_list = self.cood_recalc(self.m_left_vertex.sceneBoundingRect().x(),
                                      self.m_left_vertex.sceneBoundingRect().y(),
                                      self.m_right_vertex.sceneBoundingRect().x(),
                                      self.m_right_vertex.sceneBoundingRect().y())

        self.setLine(coord_list[0], coord_list[1], coord_list[2], coord_list[3])
        # self.setPos(QPointF(rect.x(), rect.y()), rect.width(), rect.height())
        # self.setPos(self.m_left_vertex.sceneBoundingRect().x(), self.m_left_vertex.sceneBoundingRect().y(), self.m_right_vertex.sceneBoundingRect().x(), self.m_right_vertex.sceneBoundingRect().y())
        print("09098")
