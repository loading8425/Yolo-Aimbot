import sys
import win32com.client
from ctypes import *

# Key map
KEY = {
    'page_up':33,
    'page_down':34,
    'end':35,
    'home':36,
    'left_arrow':37,
    'up_arrow':38,
    'right_arrow':39,
    'down_arrow':40,
    'insert':45,
    'delete':46,
    '0':48,
    '1':49,
    '2':50,
    '3':51,
    '4':52,
    '5':53,
    '6':54,
    '7':55,
    '8':56,
    '9':57,
    'numpad_0':96,
    'numpad_1':97,
    'numpad_2':98,
    'numpad_3':99,
    'numpad_4':100,
    'numpad_5':101,
    'numpad_6':102,
    'numpad_7':103,
    'numpad_8':104,
    'numpad_9':105,
    'F1':112,
    'F2':113,
    'F3':114,
    'F4':115,
    'F5':116,
    'F6':117,
    'F7':118,
    'F8':119,
    'F9':120,
    'F10':121,
    'F11':122,
    'F12':123,
}

class HKM_Mouse:
    wyhkm = None
    
    def __init__(self, VID, PID):
        """
        Args:
            VID (int32): Mouse Box VID
            PID (int32): Mouse Box PID
        """
        hkmdll = windll.LoadLibrary(r".\3rd-requirements\wyhkm\x64\wyhkm.dll")
        hkmdll.DllInstall.argtypes=(c_long,c_longlong)
        if hkmdll.DllInstall(1,2)<0:
            print("Fail to register!")
            sys.exit(0)
        try:
            self.wyhkm=win32com.client.Dispatch("wyp.hkm")
        except:
            print("class initiate fail!")
            sys.exit(0)
        #wyhkm.SearchDevice(0x1E71, 0x2022, 0) current vid pid
        DevId = self.wyhkm.SearchDevice(VID, PID, 0)
        if DevId == -1:
            print("mouse box not found")
            sys.exit(0)
            
        if not self.wyhkm.Open(DevId,0):
            print("fail to call mouse box")
            sys.exit(0)

    def __del__(self):
        self.wyhkm.Close()
    
    def get_version(self):
        return hex(self.wyhkm.GetVersion())

    def press_key(self, button):
        return self.wyhkm.KeyPress(button)

    def key_down(self, button):
        return self.wyhkm.KeyDown(button)

    def key_up(self, button):
        return self.wyhkm.KeyUp(button)
        
    def random_delay(self, time1, time2):
        """ Delay random time(ms), value chose from time1~time2"""
        return self.wyhkm.DelayRnd(time1,time2)
    
    def get_cursor_pos(self):
        a,x,y = self.wyhkm.GetCursorPos(0,0)
        return x,y
    
    def check_pressed_keys(self, para = 0):
        return self.wyhkm.CheckPressedKeys(para)
    
    def leftClick(self):
        return self.wyhkm.LeftClick()
    
    def rightClick(self):
        return self.wyhkm.RightClick()
    
    def leftDown(self):
        return self.wyhkm.LeftDown()
    
    def rightDown(self):
        return self.wyhkm.RightDown()
    
    def rightUp(self):
        return self.wyhkm.RightUp()
    
    def leftUp(self):
        return self.wyhkm.LeftUp()
    
    def release_Mouse(self):
        return self.wyhkm.ReleaseMouse()
    
    def move_To(self, x:int, y:int):
        return self.wyhkm.MoveTo(x,y)
    
    def move_Reletive(self, x:int, y:int):
        return self.wyhkm.MoveR(x,y)
    
    def move_Reletive_No_Acceleration(self, x:int, y:int):
        return self.wyhkm.MoveR2(x,y)
    
    def moveRP(self, x:int, y:int):
        return self.wyhkm.MoveRP(x,y)
    
    def set_mouse_click_interval(self, time:int):
        return self.wyhkm.SetMouseInterval(time)
    
    # -1 is cancel timeout
    def set_mouse_move_timeout(self, time:int):
        return self.wyhkm.SetMouseMoveTimeout(time)
    
    #
    def set_mouse_speed(self, speed:int):
        """ Set mouse speed from 5 to 100, default is 45 """
        return self.wyhkm.SetMouseSpeed(speed)


#test
# mouse = HKM_Mouse(0x1E71,0x2022)
# mouse.set_mouse_speed(5)
# mouse.move_To(1000,1000)