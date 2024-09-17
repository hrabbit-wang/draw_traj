from PyQt5.QtGui import QPainter
import numpy as np
import box

class Trajectory(object):
    def __init__(self, length, width) -> None:
        self.points = []
        self.length = length
        self.width = width

    def add_point(self, x, y, yaw, t):
        p = box.Point(x, y, yaw, t)
        self.points.append(p)

    def draw_to_time(self, t, painter:QPainter):
        print(f"size: {len(self.points)}")
        for point in self.points:
            if point.t <= t:
                print(f"p: {point.x}, {point.y}")
                obb = box.OBB(point, self.length, self.width)
                obb.draw(painter)