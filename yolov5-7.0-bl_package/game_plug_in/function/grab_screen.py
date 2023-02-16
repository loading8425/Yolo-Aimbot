"""
@Author：  Fabreel
@Time：  2023/1/12/012 20:11:37

grab_screen_win32_v2    640: 348        2560: 72
grab_screen_pyqt_v2     640: 175        2560: 42
g.cap()                 640: 77         2560: 34
win32_cls.capture()     640: 312        2560: 35
dxgi.cap()              640: 312        2560: 52
mss.mss().grab()        640: 74         2560: 36
"""
import numpy as np
import win32ui, win32con, win32api
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage
import win32gui
import sys
import cv2

hwnd_title = dict()

is_show_not_find_window = True


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


# win32gui.EnumWindows(get_all_hwnd, 0)
# for h, t in hwnd_title.items():
#     if t is not "":
#         print(h, t)


def update_hwnd_title():
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t != "":
            print(h, t)


def qImage2array(img):
    assert isinstance(img, QImage), "img must be a QtGui.QImage object"
    assert img.format() == QImage.Format.Format_RGB32, \
        "img format must be QImage.Format.Format_RGB32, got: {}".format(img.format())
    img_size = img.size()
    buffer: sip.voidptr = img.constBits()
    depth = (img.depth() // 8)
    buffer.setsize(img.width() * img.height() * depth)
    arr = np.ndarray(shape=(img_size.height(), img_size.width(), depth), buffer=buffer, dtype=np.uint8)
    return arr


def grab_screen_pyqt_v2(window_title, grab_rect=None):
    hwnd = win32gui.FindWindow(None, window_title)
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    if grab_rect is None:
        img = screen.grabWindow(hwnd).toImage()
    else:
        x, y, w, h = grab_rect
        img = screen.grabWindow(hwnd, x, y, w, h).toImage()
    img = qImage2array(img)
    return img


def grab_screen_win32_v2(window_title, grab_rect=None):
    global is_show_not_find_window
    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    hwnd = win32gui.FindWindow(None, window_title)
    # print(hwnd)
    if hwnd == 0 and is_show_not_find_window:
        print(f'{window_title} 窗口没有找到，请检查窗口名字是否正确！')
        is_show_not_find_window = False
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    x, y, w, h = (0, 0, 100, 100)
    if grab_rect is None:
        # 获取监控器信息
        MoniterDev = win32api.EnumDisplayMonitors(None, None)
        w = MoniterDev[0][2][2]
        h = MoniterDev[0][2][3]
        # 为bitmap开辟空间
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        # 高度saveDC，将截图保存到saveBitmap中
        saveDC.SelectObject(saveBitMap)
    else:
        x, y, w, h = grab_rect
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)

    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (x, y), win32con.SRCCOPY)
    signed_ints_array = saveBitMap.GetBitmapBits(True)
    img = np.frombuffer(signed_ints_array, dtype="uint8")
    img.shape = (h, w, 4)
    img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    mfcDC.DeleteDC()
    saveDC.DeleteDC()
    # saveBitMap.SaveBitmapFile(saveDC, 'grab_win32.jpg')

    return img
