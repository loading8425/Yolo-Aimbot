import cv2 as cv
import numpy as np
import os
import time
import matplotlib.pyplot as plt
from windowcapture import WindowCapture
import torch
import matplotlib.pyplot as plt

wincap = WindowCapture('')
wincap.list_window_names()

# initialize model
model = torch.hub.load('ultralytics/yolov5',  'custom', path='csgoLarge.pt')
model.conf = 0.52  # confidence threshold (0-1)
model.iou = 0.45  # NMS IoU threshold (0-1)

while(True):
    # get image
    img = wincap.get_screenshot()
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

    # show image
    # plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    # plt.show()

    # apply model
    results = model(img)
    print(results.xyxy[0])
    print(results.pandas().xyxy[0])
    
    time.sleep(5)
