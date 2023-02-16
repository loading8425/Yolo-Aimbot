"""
@Author：  Fabreel
@Time：  2023/2/4/004 12:32:15

文件夹结构

yolov5-7.0
	--.....
	--game-plug-in
		--dataset  			# 以后存放自己的数据集
		--function			# 用来调用的方法  （截图、鼠标移动等）
		--model				# 模型
		--utils				# 自己开发的小工具  （视频提取图片、自动标注图片、调整图片分辨率）
		game-plug-in.py		# 主程序
"""
import os
import cv2
import win32con
import win32gui
import time
import numpy as np
from multiprocessing import set_start_method, Queue, Process

from game_plug_in.function.object_detction import load_model, interface_img
from game_plug_in.function.grab_screen import grab_screen_win32_v2, update_hwnd_title, grab_screen_pyqt_v2
from game_plug_in.function.mouse_controller import mouse_ctrl_func
from game_plug_in.function.config import *


def send_nearest_pos_to_mouse_ctrl(box_list, queue):
    if len(box_list) == 0:
        return None
    dis_min = (grab_width / 2) ** 2 + (grab_height / 2) ** 2
    pos_min = (0, 0)
    for _box in box_list:
        if _box[0] not in show_list:
            continue
        x_center = _box[1] * grab_width
        y_center = _box[2] * grab_height
        if (x_center - grab_width / 2) ** 2 + (y_center - grab_height / 2) ** 2 < dis_min:
            dis_min = (x_center - grab_width / 2) ** 2 + (y_center - grab_height / 2) ** 2
            pos_min = ((x_center - grab_width / 2), (y_center - grab_height / 2))
    if pos_min == (0, 0):
        return None
    queue.put(pos_min)


def draw_box(img, box_list):
    if len(box_list) == 0:
        return img
    for _box in box_list:
        if _box[0] not in show_list:
            continue
        x_center = _box[1] * grab_width
        y_center = _box[2] * grab_height
        w = _box[3] * grab_width
        h = _box[4] * grab_height
        x1, y1 = int(x_center - w / 2), int(y_center - h / 2)
        x2, y2 = int(x_center + w / 2), int(y_center + h / 2)
        cv2.rectangle(img, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=4)
        cv2.putText(img, f'{_box[0]}_{_box[5]}%', (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
    return img


def draw_fps(img, fps_tag, fps_list):
    timer = time.time() - fps_tag
    if len(fps_list) > 10:
        fps_list.pop(0)
        fps_list.append(timer)
    else:
        fps_list.append(timer)
    cv2.putText(img, str(int(1 / np.mean(fps_list))), (20, 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
    return img


def detect_img(queue):
    # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
    # 0. 初始化
    # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
    print('detect_img:', os.getpid())
    fps_list = []  # 记录每帧运行的时间

    # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
    # 1. 加载模型
    # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
    model = load_model()

    while True:
        fps_tag = time.time()
        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
        # 2. 截图
        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
        img = grab_screen_win32_v2(window_title=grab_window_title, grab_rect=grab_rectangle)
        # img = grab_screen_pyqt_v2(window_title=grab_window_title, grab_rect=grab_rectangle)

        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
        # 3. 物体检测
        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
        box_list = interface_img(img, model)

        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
        # 4. 发送最近坐标
        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
        send_nearest_pos_to_mouse_ctrl(box_list, queue)

        if is_show_top_window:
            # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
            # 5. 画框
            # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
            img = draw_box(img, box_list)

            # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
            # 6. FPS
            # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
            img = draw_fps(img, fps_tag, fps_list)

            # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
            # 7. 窗口显示
            # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
            cv2.namedWindow(top_window_name, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(top_window_name, top_window_width, int(top_window_width * grab_height / grab_width))  # 重置窗口大小
            hwnd = win32gui.FindWindow(None, top_window_name)
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)  # 窗口置顶
            cv2.imshow(top_window_name, img)
        cv2.waitKey(cv2_wait_ms)


def main():
    set_start_method('spawn')
    q = Queue()
    p_d = Process(target=detect_img, args=(q,))
    p_m = Process(target=mouse_ctrl_func, args=(q,))
    p_d.start()
    p_m.start()


if __name__ == '__main__':
    update_hwnd_title()
    main()
