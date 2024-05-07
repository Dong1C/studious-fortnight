import gradio as gr
from utils import get_detector, inference


# 定义主函数，该函数将由 Gradio 界面调用
def main_pipe(cfg, ckpt, img):
    detector = get_detector(cfg, ckpt)  # 加载模型
    # 使用模型进行推理
    result_img = inference(detector, img)
    return result_img


# 创建 Gradio 界面
iface = gr.Interface(fn=main_pipe, inputs=["text", "text", "text"], outputs="image")

# 启动界面
iface.launch(share=False)
