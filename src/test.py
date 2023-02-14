import multiprocessing
import WindowCapture
from PyQt5.QtWidgets import QApplication
import sys
import time
from multiprocessing import Queue


def window_cap():
    app = QApplication(sys.argv)
    ex = WindowCapture.Window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    message_queue = Queue()
    window_process = multiprocessing.Process(target=window_cap, args=(message_queue,))
    window_process.start()
    time.sleep(3)
    print("end")
