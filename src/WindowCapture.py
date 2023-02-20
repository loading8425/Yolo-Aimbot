import time
import dxcam
from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import sys
import numpy
from multiprocessing import Queue

class WindowCap():
    def __init__(self):
        self.camera = dxcam.create()
        self.camera.start(target_fps=140)

    def get_screen_shot(self):
        return self.camera.get_latest_frame()

class GUI(QMainWindow):
    def __init__(self, message_queue:Queue, sharedMemImg):
        super().__init__()
        self.message_queue = message_queue
        self.sharedMemImg = sharedMemImg
        self.setWindowTitle("Title")
        self.label = QLabel(self)
        self.central_widget = QWidget()               
        self.setCentralWidget(self.central_widget)    
        self.lay = QVBoxLayout(self.central_widget)

        # set callback timer
        self.qTimer = QTimer()
        self.qTimer.setInterval(100)
        self.qTimer.timeout.connect(self.update)
        self.qTimer.start()

    def update(self):
        self.show_img(self.sharedMemImg)

    def show_img(self, img):
        qimage = QtGui.QImage(img[:], img.shape[1],img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
        qPixMap = QPixmap.fromImage(qimage).scaled(1440, 800)
        self.label.setPixmap(qPixMap)
        self.lay.addWidget(self.label)

# test run
if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ex = Window()
    # ex.show()
    # sys.exit(app.exec_())
    cam = dxcam.create()
    while True:
        t1 = time.time()
        img = cam.grab()
        print(img)
        t2 = time.time() - t1
        print(1/t2)