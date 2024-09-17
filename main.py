from PyQt5 import QtGui
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys
import box
import trajectory

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Tutorial"
        self.top= 150
        self.left= 150
        self.width = 500
        self.height = 500
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        traj = trajectory.Trajectory(40.0, 20.0)
        traj.add_point(250.0, 250.0, 0, 0)
        traj.add_point(280.0, 250.0, -0.1, 1)
        traj.draw_to_time(1, painter)

# main entry
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
