import os
import gradio as gr
from utils import list_from_folder, inference_plot, get_detector

# generate the ckpt and config files
cfg_path = './configs'
ckpt_path= './checkpoints'
cfg_set = set(list_from_folder(folder_path=cfg_path, mode='d'))
ckpt_set = set(list_from_folder(folder_path=ckpt_path, mode='d'))

# build detector and inference to get the plotted_image
def inference_pipeline(cfg, ckpt, img):
    print(cfg, ckpt)
    detector = get_detector(cfg, ckpt)
    result_img = inference_plot(detector, img)
    return result_img

with gr.Blocks() as demo:
    with gr.Tab("Detection") as tab1:
        with gr.Row():
            model_name = gr.Dropdown(cfg_set & ckpt_set, label="Model Name", scale=1)
            cfg_file = gr.Dropdown([], label="Config Full Name", interactive=False, scale=2)
            ckpt_file = gr.Dropdown([], label="Checkpoint Full Name", interactive=False, scale=2)
            btn = gr.Button(value="Start Inference",scale=1)
        with gr.Row():
            source_img = gr.Image(sources=['upload'],
                                show_download_button=False)
        with gr.Row():
            plotted_img = gr.Image(label="Plotted Result Image",
                                sources=None,
                                show_download_button=True)
            
    with gr.Tab("Train") as tab2:
        with gr.Row():
            gr.Textbox()
    
    # update the list of files from the model_name
    @model_name.change(inputs=model_name, outputs=[cfg_file, ckpt_file])
    def update_file_list(model_name):
        cfg_list = [cfg for cfg in 
                    list_from_folder(folder_path=os.path.join(cfg_path, model_name), mode='f')
                    if cfg.endswith('.py')]
        ckpt_list = [ckpt for ckpt in
                     list_from_folder(os.path.join(ckpt_path, model_name), mode='f')
                     if ckpt.endswith('.pth')]
        return (gr.Dropdown(choices=cfg_list, value=cfg_list[0], interactive=True), 
                gr.Dropdown(choices=ckpt_list, value=ckpt_list[0], interactive=True))
    
    # do inference when clicking the button
    @btn.click(inputs=[model_name, cfg_file, ckpt_file, source_img], outputs=plotted_img)
    def inference(model_name, cfg_file, ckpt_file, source_img):
        cfg_file = os.path.join(cfg_path, model_name, cfg_file)
        ckpt_file = os.path.join(ckpt_path, model_name, ckpt_file)
        print(cfg_file)
        print(ckpt_file)
        detector = get_detector(cfg_file, ckpt_file)
        result_img = inference_plot(detector, source_img)
        return result_img

demo.launch(share=False)
