import multiprocessing
import WindowCapture
from PyQt5.QtWidgets import QApplication
import sys
import time
from multiprocessing import Queue
import pythoncom
import sharedmem
import numpy
import dxcam


def gui(message_queue, sharedMem):
    app = QApplication(sys.argv)
    ex = WindowCapture.GUI(message_queue, sharedMem)
    ex.show()
    sys.exit(app.exec_())

def screen_cap(message_queue, sharedMem):
    cam = WindowCapture.WindowCap()
    while True:
        img = cam.get_screen_shot()
        sharedMem[:] = img.copy()

if __name__ == '__main__':
    message_queue = Queue()
    gui_process = multiprocessing.Process(target=gui, args=(message_queue,))
    cam_process = multiprocessing.Process(target=screen_cap, args=(message_queue,))
    gui_process.start()
    cam_process.start()
    time.sleep(3)
    print("end")
    gui_process.join()
    cam_process.join()
    