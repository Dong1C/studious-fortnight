"""
1. build the detector and inference : done
2. scan and get the configs : 
3. parse the configs into several params : 
4. integrate the config files
"""
import torch
import numpy as np

import mmcv
from mmcv.runner import load_checkpoint
from mmdet.apis import inference_detector, show_result_pyplot
from mmrotate.models import build_detector
from mmrotate.core import imshow_det_rbboxes 


import os.path as osp

device = 'cuda:0' if torch.cuda.is_available() else 'cpu'

def get_detector(config : str, checkpoint : str, device: str = 'cpu', *args, **kwargs):
    # all assertion
    assert device == 'cpu' or device.split(':')[0] == 'cuda'
    assert osp.exists(config) 
    assert osp.exists(checkpoint)
    
    # load the config -> model build -> load checkpoint
    config = mmcv.Config.fromfile(config)
    print("================config load done================\n", config)
    model = build_detector(config.model)
    checkpoint = load_checkpoint(model, checkpoint, map_location=device)

    # set config(classes, regis, map_location, status)
    model.CLASSES = checkpoint['meta']['CLASSES']
    model.cfg = config
    model.to(device)
    model.eval()

    return model


def inference(model, img, score_thr=0.3, palette='dota', text_color=(200,200,200),):
    
    # inference 
    result = inference_detector(model, img)

    if hasattr(model, 'module'):
        model = model.module
    plotted_img = model.show_result(img, 
                                    result, 
                                    score_thr=score_thr, 
                                    bbox_color=palette,
                                    text_color=(200,200,200),
                                    mask_color=palette,
                                    thickness=2,
                                    font_size=13,
                                    show=False)
    
    return mmcv.bgr2rgb(plotted_img)








if __name__ == "__main__":
    checkpoint = './checkpoints/oriented_rcnn_r50_fpn_1x_dota_le90-6d2b2ce0.pth'
    config = './configs/oriented_rcnn/oriented_rcnn_r50_fpn_1x_dota_le90.py'
    demo_img = './dota_demo.jpg'
    # test 1 - get detector
    model = get_detector(config, checkpoint)
    # test 2 - inference 
    img = inference(model, demo_img)
    print(img)