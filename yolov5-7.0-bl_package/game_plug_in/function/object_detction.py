"""
@Author：  Fabreel
@Time：  2023/1/15/015 10:26:29

"""
import torch

from models.common import DetectMultiBackend
from utils.general import (Profile, non_max_suppression, scale_boxes, xyxy2xywh)
from utils.torch_utils import select_device
from utils.augmentations import letterbox
import numpy as np

from game_plug_in.function.config import *


def load_model():
    # --- --- --- --- --- --- --- ---  --- --- --- --- --- --- --- --- #
    # 加载模型
    # --- --- --- --- --- --- --- ---  --- --- --- --- --- --- --- --- #
    device = select_device('')
    model = DetectMultiBackend(weights, device=device, dnn=False, data=data, fp16=False)
    model.warmup(imgsz=(1, 3, *imgsz))  # warmup
    return model


def interface_img(img, model):
    stride, names = model.stride, model.names
    # --- --- --- --- --- --- --- ---  --- --- --- --- --- --- --- --- #
    # 加载图片
    # --- --- --- --- --- --- --- ---  --- --- --- --- --- --- --- --- #
    im = letterbox(img, imgsz[0], stride=stride, auto=True)[0]  # padded resize
    im = im.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
    im = np.ascontiguousarray(im)  # contiguous

    # --- --- --- --- --- --- --- ---  --- --- --- --- --- --- --- --- #
    # 运行推断
    # --- --- --- --- --- --- --- ---  --- --- --- --- --- --- --- --- #
    dt = (Profile(), Profile(), Profile())
    with dt[0]:
        im = torch.from_numpy(im).to(model.device)
        im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
        im /= 255  # 0 - 255 to 0.0 - 1.0
        if len(im.shape) == 3:
            im = im[None]  # expand for batch dim

    # Inference  推断
    with dt[1]:
        pred = model(im, augment=False, visualize=False)
    
    # NMS  非极大值抑制
    with dt[2]:
        pred = non_max_suppression(pred, conf_thres, iou_thres, max_det=1000)
    print(pred)
    box_list = []
    for i, det in enumerate(pred):  # per image
        gn = torch.tensor(img.shape)[[1, 0, 1, 0]]  # normalization gain whwh
        if len(det):
            # Rescale boxes from img_size to im0 size
            det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], img.shape).round()

            # Write results
            for *xyxy, conf, cls in reversed(det):
                xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                line = (names[int(cls)], *xywh, int(100 * float(conf)))  # label format
                box_list.append(line)
    return box_list
