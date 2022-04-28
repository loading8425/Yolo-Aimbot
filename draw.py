import win32api,win32gui,win32con

window_handler = None
Rect = win32gui.GetWindowRect(window_handler)

dcBmp = win32gui.CreateCompatibleDC(0)
dcscrn = win32gui.GetDC(0)
c_bpm = win32gui.CreateCompatibleBitmap(dcscrn, 120,230)
c_bpm_old = win32gui.SelectObject(dcBmp, c_bpm)
pen = win32gui.CreatePen(win32con.PS_GEOMETRIC, win32api.RGB(255,0,0))