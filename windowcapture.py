import win32gui, win32ui, win32con, win32api
import numpy as np

class WindowCapture():

    w = 0 # set this
    h = 0 # set this
    hwnd = None

    def __init__(self, window_name):
        self.hwnd  = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception("Window not found")
        if window_name == '':
            self.hwnd = None
        moniter = win32api.EnumDisplayMonitors(None,None)
        self.w=moniter[0][2][2]
        self.h=moniter[0][2][3]

    def list_window_names(self):
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)


    def get_screenshot(self):
        #hwnd = win32gui.FindWindow(None, 'Counter-Strike: Global Offensive - Direct3D 9')

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (0,0), win32con.SRCCOPY)

        #save file
        #dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img = img[...,:3]
        img = np.ascontiguousarray(img)

        return img

