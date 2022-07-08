from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from typing import Optional


class Edge(QGraphicsLineItem):
    count = 0

    def __init__(self, left_vertex=None, right_vertex=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Edge.count += 1
        self.e_number = int(Edge.count)
        self.m_left_vertex = left_vertex
        self.m_right_vertex = right_vertex
        self.checked = False
        self.pressed = False
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
