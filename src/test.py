import multiprocessing
import WindowCapture
from PyQt5.QtWidgets import QApplication
import sys
import time
from multiprocessing import Queue


def gui(message_queue):
    app = QApplication(sys.argv)
    ex = WindowCapture.GUI(message_queue)
    ex.show()
    sys.exit(app.exec_())

def screen_cap(message_queue):
    cam = WindowCapture.WindowCap()
    while True:
        message_queue.put(cam.get_screen_shot())

if __name__ == '__main__':
    message_queue = Queue()
    gui_process = multiprocessing.Process(target=gui, args=(message_queue,))
    cam_process = multiprocessing.Process(target=screen_cap, args=(message_queue,))
    gui_process.start()
    cam_process.start()
    time.sleep(3)
    print("end")
    