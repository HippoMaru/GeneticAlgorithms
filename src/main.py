import sys
from typing import Optional
from math import sqrt, pow
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import PySide6.Qt3DInput
from ui.main_window_gui import Ui_MainWindow   # Это наш конвертированный файл дизайна
from Vertex import Vertex
from edge import Edge

number_of_vertices = 0


class ExampleApp(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.scene = QGraphicsScene(0, 0, 300, 300, self)

        '''self.scene.addLine(80, 55, 180, 55)
        self.scene.addLine(55, 80, 55, 180)
        self.scene.addLine(205, 80, 205, 180)
        self.scene.addLine(80, 205, 180, 205)

        self.scene.addEllipse(30, 30, 50, 50)
        self.scene.addEllipse(180, 30, 50, 50)
        self.scene.addEllipse(30, 180, 50, 50)
        ellips2 = self.scene.addEllipse(180, 180, 50, 50)'''
        self.brush = QBrush(QColor(0, 255, 255))

        self.graphicsView.setScene(self.scene)

        self.vertex_list = {}
        self.edge_list = {}

        self.left_vertex = None

        self.transform = QTransform

        self.add_vertex_btn_is_pressed = False
        self.add_edge_btn_is_pressed = False
        self.del_vertex_btn_is_pressed = False
        self.del_edge_btn_is_pressed = False

        # self.add_vertex_btn.clicked.connect(self.create_vertex)
        # self.add_edge_btn.clicked.connect(self.create_edge)
        # self.del_vertex_btn.clicked.connect(self.delete_vertex)
        # self.del_edge_btn.clicked.connect(self.delete_edge)
        self.run_btn.clicked.connect(self.color_the_graph)
        self.graphicsView.signal_pressed.connect(self.on_press)
        self.graphicsView.signal_released.connect(self.on_released)

        '''v1 = Vertex(30, 30, 20, 20)
        v2 = Vertex(100, 100, 20, 20)
        print(f"{v1.sceneBoundingRect().x(), v1.sceneBoundingRect().y(), v2.sceneBoundingRect().x(), v2.sceneBoundingRect().y()}")
        line = Edge(v1, v2, v1.sceneBoundingRect().x(), v1.sceneBoundingRect().y(), v2.sceneBoundingRect().x(), v2.sceneBoundingRect().y())
        self.scene.addItem(v1)
        self.scene.addItem(v2)
        self.scene.addItem(line)'''

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


    @Slot(QMouseEvent)
    def on_press(self, event: QMouseEvent):
        point = self.graphicsView.mapToScene(event.pos())

        if self.add_vertex_btn.isChecked():
            self.create_vertex(point.x(), point.y())

        elif self.del_vertex_btn_is_pressed:
            pass

        elif self.add_edge_btn.isChecked():
            if self.left_vertex is None:
                temp_vertex = self.scene.itemAt(point.x(), point.y(), QTransform())
                if isinstance(temp_vertex, Vertex):
                    self.left_vertex = temp_vertex
                    print("!")
                else:
                    print("Eror")
            else:
                right_vertex = self.scene.itemAt(point.x(), point.y(), QTransform())
                if isinstance(right_vertex, Vertex) and right_vertex != self.left_vertex:
                    self.create_edge(self.left_vertex, right_vertex)
                    self.left_vertex = None
                    print("@")

        elif self.del_vertex_btn.isChecked():
            vertex = self.scene.itemAt(point.x(), point.y(), QTransform())
            if isinstance(vertex, Vertex):
                self.delete_vertex(vertex)

        elif self.del_edge_btn.isChecked():
            edge = self.scene.itemAt(point.x(), point.y(), QTransform())
            if isinstance(edge, Edge):
                self.delete_edge(edge)

            # point = event.
        # print(f"{event.pos()}")

    @Slot(QMouseEvent)
    def on_released(self, event: QMouseEvent):
        pass

    def create_vertex(self, x, y):
        new_vertex = Vertex(x, y, 20, 20)
        self.scene.addItem(new_vertex)
        # new_vertex.setFlag(QGraphicsItem.ItemIsMovable)
        self.vertex_list[new_vertex.v_number] = new_vertex

    def create_edge(self, left_vertex=None, right_vertex=None):

        left_x = left_vertex.sceneBoundingRect().x()
        left_y = left_vertex.sceneBoundingRect().y()
        right_x = right_vertex.sceneBoundingRect().x()
        right_y = right_vertex.sceneBoundingRect().y()
        '''k = (abc(right_x - left_x))/(abc(right_y - left_y))
        b = 10
        x = sqtr(b)'''
        coord_list = self.cood_recalc(left_x, left_y, right_x, right_y)

        new_edge = Edge(left_vertex, right_vertex, coord_list[0], coord_list[1], coord_list[2], coord_list[3])

        self.scene.addItem(new_edge)
        self.edge_list[new_edge.e_number] = new_edge
        print("$")

    def delete_vertex(self, vertex):
        print(vertex.m_edge_list)

        for k_edge in vertex.m_edge_list:
            if vertex.m_edge_list[k_edge].m_left_vertex == vertex:
                vertex.m_edge_list[k_edge].m_right_vertex.m_edge_list.pop(k_edge)
            else:
                vertex.m_edge_list[k_edge].m_left_vertex.m_edge_list.pop(k_edge)

        size = len(vertex.m_edge_list)
        for i in range(size):
            temp = vertex.m_edge_list.popitem()
            self.edge_list.pop(temp[0])
            self.scene.removeItem(temp[1])

        self.vertex_list.pop(vertex.v_number)
        self.scene.removeItem(vertex)

        print("2")

    def delete_edge(self, edge):
        edge.m_right_vertex.m_edge_list.pop(edge.e_number)
        edge.m_left_vertex.m_edge_list.pop(edge.e_number)
        self.edge_list.pop(edge.e_number)
        self.scene.removeItem(edge)


        print("3")

    def color_the_graph(self):

        pass






def main():
    colors = [QBrush(QColor(0,255,255)), QBrush(QColor(0, 0, 255)), QBrush(QColor(255, 0, 255)),
            QBrush(QColor(128, 128, 128)), QBrush(QColor(0, 128, 0)), QBrush(QColor(128, 128, 0)),
              QBrush(QColor(128, 0, 128)), QBrush(QColor(255, 0, 0)), QBrush(QColor(192, 192, 192)),
              QBrush(QColor(0, 128, 128)), QBrush(QColor(0, 0, 128)), QBrush(QColor(255, 255, 0)),
              QBrush(QColor(0, 255, 0)), QBrush(QColor(200, 20, 100)), QBrush(QColor(128, 0, 0)), QBrush(QColor(128, 233, 50))]
    #==============
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    #window.create_vertex()
    #window.create_vertex()
    # window.create_edge()

    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
