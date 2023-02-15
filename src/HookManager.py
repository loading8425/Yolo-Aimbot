import pythoncom
import PyHook3
import win32api

class EventListener:

    def __init__(self) -> None:
        self.hm = PyHook3.HookManager()
        #绑定事件处理函数
        self.hm.MouseAllButtonsDown = self.OnMouseEvent #将OnMouseEvent函数绑定到MouseAllButtonsDown事件上
        self.hm.KeyDown = self.OnKeyboardEvent     
        self.hm.HookMouse()        #设置鼠标钩子
        self.hm.HookKeyboard()   #设置键盘钩子

    # 鼠标事件处理函数
    def OnMouseEvent(self, event):
        print('MessageName:',event.MessageName)  #事件名称
        print('Message:',event.Message)          #windows消息常量 
        print('Time:',event.Time)                #事件发生的时间戳        
        print('Window:',event.Window)            #窗口句柄         
        print('WindowName:',event.WindowName)    #窗口标题
        print('Position:',event.Position)        #事件发生时相对于整个屏幕的坐标
        print('Wheel:',event.Wheel)              #鼠标滚轮
        print('Injected:',event.Injected)        #判断这个事件是否由程序方式生成，而不是正常的人为触发。
        print('---')
        # 返回True代表将事件继续传给其他句柄，为False则停止传递，即被拦截
        return True
    
    #键盘事件处理函数
    def OnKeyboardEvent(self, event):
        print('MessageName:',event.MessageName)          #同上，共同属性不再赘述
        print('Message:',event.Message)
        print('Time:',event.Time)
        print('Window:',event.Window)
        print('WindowName:',event.WindowName)
        print('Ascii:', event.Ascii, chr(event.Ascii))   #按键的ASCII码
        print('Key:', event.Key, type(event.Key))                         #按键的名称
        print('KeyID:', event.KeyID)                     #按键的虚拟键值
        print('ScanCode:', event.ScanCode)               #按键扫描码
        print('Extended:', event.Extended)               #判断是否为增强键盘的扩展键
        print('Injected:', event.Injected)
        print('Alt', event.Alt)                          #是某同时按下Alt
        print('Transition', event.Transition)            #判断转换状态
        print('---')
        
        if event.Key == "Home":
            win32api.PostQuitMessage()
        # 同上
        return True
 

# test run
# listener = EventListener()
# pythoncom.PumpMessages()
