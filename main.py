from concurrent.futures import thread
from pickle import FALSE
import win32api
import win32con
import win32gui
from ctypes import *
import time
import pyautogui
import threading
import sys
import queue
import PyHook3 as pyHook
import pythoncom
import pydirectinput
import tkinter

# mouse down queue front=1
def on_left_down_event(event):
    if script_ON:
        print(event.MessageName)
        global_queue.put(1)
    return True

# mouse up queue front=0
def on_left_up_event(event):
    if script_ON:
        print(event.MessageName)
        global_queue.get()
    return True
    
def onKeyboardEvent(event):
    global script_ON
    global recoil_process
    pid = c_ulong(0)
    windowTitle = create_string_buffer(512)
    windll.user32.GetWindowTextA(event.Window, byref(windowTitle), 512)
    windll.user32.GetWindowThreadProcessId(event.Window, byref(pid))
    windowName = windowTitle.value.decode('gbk')
    # print("当前您处于%s窗口" % windowName)
    # print("当前窗口所属进程id %d" % pid.value)
    
    # quit program when click Page Up
    if event.Key == "Prior":
        win32api.PostQuitMessage()
        print("Script terminated")
    elif event.Key == "F1" and script_ON:
        script_ON = False
    elif event.Key == "F1" and  not script_ON:
        script_ON = True
    return True

def AK47():
    # speed range from 0.1 ~ 1
    spraySpeed = 0.3
    
    start = time.time()
    timelimit = 0.1
    while (time.time()-start)<=timelimit and global_queue.queue[global_queue.qsize()-1] == 1:
        pydirectinput.move(0, int(10*spraySpeed),relative=True, duration=0.1, _pause=False)
        time.sleep(0.01)
    
def Script_Start():
    while True:
        if script_ON:
            if global_queue.queue[global_queue.qsize()-1] == 1:
                AK47()
        time.sleep(0.01)

def debug():
    return
    #time.sleep(1)

# global variables
global_queue = queue.LifoQueue()
global_queue.put(100)
script_threads = []
script_ON = False

recoil_process = threading.Thread(target=Script_Start, daemon=True)
recoil_process.start()

debug_p = threading.Thread(target=debug, daemon=True)
debug_p.start()

# mouse and keyboard hooks
hm = pyHook.HookManager()
hm.KeyDown = onKeyboardEvent
hm.HookKeyboard()
#hm.MouseAll = onMouseEvent
hm.MouseLeftDown = on_left_down_event
hm.MouseLeftUp = on_left_up_event
hm.HookMouse()
pythoncom.PumpMessages()