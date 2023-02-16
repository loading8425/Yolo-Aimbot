import numpy as np
import cv2
import multiprocessing
import sharedmem
import dxcam
import time
def screen_cap(sharedMem):
    cam = dxcam.create()
    cam.start()
    while True:
        img = cam.get_latest_frame()
        sharedMem[:]
        print(sharedMem)
        time.sleep(1)


if __name__ == '__main__':
    shape = (2160, 3840, 3)
    dtype = "uint8"
    sharedImg = sharedmem.empty(shape, dtype)

    p1 = multiprocessing.Process(target=screen_cap, args=(sharedImg,))
    p1.start()

    while True:
        time.sleep(3)
        #print(sharedImg)