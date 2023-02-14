import dxcam
from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import sys
import numpy

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.label = QLabel(self)
        self.central_widget = QWidget()               
        self.setCentralWidget(self.central_widget)    
        self.lay = QVBoxLayout(self.central_widget)

        # Grab screen
        self.camera = dxcam.create()
        self.camera.start()
        # set callback timer
        self.qTimer = QTimer()
        self.qTimer.setInterval(10)
        self.qTimer.timeout.connect(self.update)
        self.qTimer.start()

    def update(self):
        self.show_img(self.camera.get_latest_frame())

    def show_img(self, img:numpy.ndarray):
        qimage = QtGui.QImage(img[:], img.shape[1],img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
        qPixMap = QPixmap.fromImage(qimage).scaled(1440, 800)
        self.label.setPixmap(qPixMap)
        self.lay.addWidget(self.label)

# test run
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Window()
#     ex.show()
#     sys.exit(app.exec_())