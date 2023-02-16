"""
@Author：  Fabreel
@Time：  2023/1/29/029 19:18:29

鼠标、键盘 控制和监听

https://www.johngo689.com/226869/
https://pan.baidu.com/s/1VkE2FQrNEOOkW6tCOLZ-kw?pwd=yh3s
https://pypi.org/project/pynput/
"""
import os
from pynput import mouse
from pynput import keyboard
from game_plug_in.function.logitech import Logitech
from game_plug_in.function import config

is_mouse_left = False  # 鼠标左键按下
is_mouse_right = False  # 鼠标右键按下
flag_lock_obj = True  # 是否开启锁定的功能
mouse_offset_ratio = config.mouse_offset_ratio


def on_press(key):
    global flag_lock_obj
    if key == keyboard.Key.home:
        flag_lock_obj = not flag_lock_obj
        print(f'锁定功能：{"开" if flag_lock_obj else "关"}')
    print(key)


def on_click(x, y, button, pressed):
    global is_mouse_left, is_mouse_right, mouse_offset_ratio
    if pressed:
        if button == mouse.Button.left:
            is_mouse_left = True
        elif button == mouse.Button.right:
            is_mouse_right = True
        # elif button == mouse.Button.x1:  # 这个地方是不需要停止运行程序就能实时调整 mouse_offset_ratio 的，但是被我屏蔽了。因为和有的游戏按键设置有冲突
        #     mouse_offset_ratio += 0.01
        #     print(f'mouse_offset_ratio: {mouse_offset_ratio}')
        # elif button == mouse.Button.x2:  # 这个地方是不需要停止运行程序就能实时调整 mouse_offset_ratio 的，但是被我屏蔽了。因为和有的游戏按键设置有冲突
        #     mouse_offset_ratio -= 0.01
        #     print(f'mouse_offset_ratio: {mouse_offset_ratio}')
    else:
        if button == mouse.Button.left:
            is_mouse_left = False
        elif button == mouse.Button.right:
            is_mouse_right = False
    # print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    print(f'is_mouse_left:{is_mouse_left}  is_mouse_right:{is_mouse_right}')


def mouse_ctrl_func(queue):
    global mouse_offset_ratio, is_mouse_right, is_mouse_left, flag_lock_obj

    print('mouse_ctrl_func:', os.getpid())

    listener_mouse = mouse.Listener(on_click=on_click)
    listener_mouse.start()

    listener_keyboard = keyboard.Listener(on_press=on_press)
    listener_keyboard.start()

    while True:
        if queue.empty() is True:
            continue
        pos_min = queue.get()

        if is_mouse_right:
            Logitech.mouse.move(int(pos_min[0] * mouse_offset_ratio), int(pos_min[1] * mouse_offset_ratio))
