import gradio as gr
import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
cap = None


# 推理函数
def inference(camera_idx):
    global cap
    if cap is not None:
        cap.release()
    cap = cv2.VideoCapture(camera_idx)
    while True:


    return model(frame)[0].plot()


def get_camera_list():
    devices = []
    for i in range(10):
        try:
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                devices.append(i)
                cap.release()
                # 捕获所有其他类型的异常
        except Exception as e:
            print("发生了一个未知的异常:", e)
        finally:
            continue

    camera_choices = {f"Camera {i}": i for i in devices}
    return camera_choices


with gr.Blocks() as demo:
    # 创建 Gradio 输入组件
    camera_input = gr.Radio(choices=[0, 1, 2], label="Select Camera Device")

    # 创建 Gradio 输出组件
    output_image = gr.Image(type="numpy")

    # 创建 Gradio UI
    gr.Interface(
        inference,
        inputs=camera_input,
        outputs=output_image,
        title="Camera Stream with YOLOv8 Inference",
        live=True
    )

demo.launch()
