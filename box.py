from PyQt5.QtGui import QPolygonF, QPainter, QPen
from PyQt5.QtCore import QPointF, Qt
import numpy as np
import math

class Point(object):
    def __init__(self, x, y, yaw, t) -> None:
        self.x = x
        self.y = y
        self.yaw = yaw
        self.t = t

class OBB(object):
    def __init__(self, point, length, width):
        self.updated = False
        self.point = point
        self.length = length
        self.width = width
        self.color = Qt.green
        self.corners = np.ndarray(4, QPointF)

    def update_internal(self):
        if self.updated == False:
            dx1 = math.cos(self.point.yaw) * self.length * 0.5;
            dy1 = math.sin(self.point.yaw) * self.length * 0.5;
            dx2 = math.sin(self.point.yaw) * self.width * 0.5;
            dy2 = -math.cos(self.point.yaw) * self.width * 0.5;
            self.corners[0] = QPointF(self.point.x + dx1 + dx2, self.point.y + dy1 + dy2);
            self.corners[1] = QPointF(self.point.x + dx1 - dx2, self.point.y + dy1 - dy2);
            self.corners[2] = QPointF(self.point.x - dx1 - dx2, self.point.y - dy1 - dy2);
            self.corners[3] = QPointF(self.point.x - dx1 + dx2, self.point.y - dy1 + dy2);
            self.updated = True

    def set_center(self, point):
        self.point = point
        self.updated = False

    def set_color(self, color):
        self.color = color

    def draw(self, painter:QPainter):
        self.update_internal()
        o_pen = painter.pen()
        poly = QPolygonF(self.corners)
        painter.setPen(QPen(Qt.green,  1, Qt.SolidLine))
        painter.drawPolygon(poly)
        painter.setPen(QPen(Qt.red,  2, Qt.SolidLine))
        painter.drawPoint(QPointF(self.point.x, self.point.y))
        painter.setPen(o_pen)
