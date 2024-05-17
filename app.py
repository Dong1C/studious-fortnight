import os
import gradio as gr
from utils import list_from_folder, inference_plot, get_detector

# generate the ckpt and config files
cfg_path = './configs'
ckpt_path= './checkpoints'
cfg_set = set(list_from_folder(folder_path=cfg_path, mode='d'))
ckpt_set = set(list_from_folder(folder_path=ckpt_path, mode='d'))

with gr.Blocks() as demo:

    """
        1. scan and show all the model name
        2. choose the model config and model ckpt
        3. upload the image 
        4. run the inference
    """
    with gr.Tab("Detection") as tab1:
        with gr.Row():
            model_name = gr.Dropdown(cfg_set & ckpt_set, label="Model Name", scale=2)
            cfg_file = gr.Dropdown([], label="Config Full Name", interactive=False, scale=4)
            ckpt_file = gr.Dropdown([], label="Checkpoint Full Name", interactive=False, scale=4)
            btn = gr.Button(value="Start Inference",scale=2)

        with gr.Row():
            score_thr = gr.Slider(label="Score Threshold", interactive=True, minimum=0, maximum=1.0, step=0.05, scale=2)
            use_gpu = gr.Checkbox(label="Use GPU", interactive=True, scale=1)

        with gr.Row():
            source_img = gr.Image(sources=['upload'],
                                show_download_button=False)
            plotted_img = gr.Image(label="Plotted Result Image",
                                sources=None,
                                show_download_button=True)
            
            
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
        @btn.click(inputs=[model_name, cfg_file, ckpt_file, source_img, score_thr, use_gpu], outputs=plotted_img)
        def inference(model_name, cfg_file, ckpt_file, source_img, score_thr, use_gpu):
            print("use_gpu" + "True" if use_gpu else "False")
            cfg_file = os.path.join(cfg_path, model_name, cfg_file)
            ckpt_file = os.path.join(ckpt_path, model_name, ckpt_file)
            print(cfg_file)
            print(ckpt_file)
            device = "cuda:0" if use_gpu else "cpu"
            detector = get_detector(cfg_file, ckpt_file, device)
            result_img = inference_plot(detector, source_img, score_thr)
            return result_img
    

    """
        1. Read the config file and parse it into the dict or Configdict
        2. Generate components dynamically based on all the items
        3. Offer the interface to change all these configs
    """
    with gr.Tab("Train") as tab2:

        with gr.Row() as train_config:
            model_name2 = gr.Dropdown(cfg_set & ckpt_set, label="Model Name", scale=1)
            cfg_file2 = gr.Dropdown([], label="Config Full Name", interactive=False, scale=2)

        with gr.Row():
            btn_parse = gr.Button(value="Parse Config File", scale=1)
            btn_gen = gr.Button(value="Genetate Config File", scale=1)
        
        # with gr.Row():
        #     confregis.render()

        # @btn_parse.click()
        # def gen_blocks():
        #     d = {"Name": "John", "Age": "30", "Email": "john@example.com"}
        #     for key, value in d.items():
        #         confregis.add(gr.Textbox(label=key, value=value))
        #     confregis.render()
        
            
        
demo.launch(share=False)
