import os
import gradio as gr

def list_from_folder(folder_path='../configs', mode='d'):
    assert mode in ('d', 'a', 'f')
    if mode == 'd':
        return [f.path for f in os.scandir(folder_path) if f.is_dir()]
    elif mode == 'f':
        return [f.name for f in os.scandir(folder_path) if f.is_file()]
    elif mode == 'a':
        return [f.name for f in os.scandir(folder_path)]

def update(dropdown):
    print("change done!")
    dropdown.choices = list_from_folder()
    

with gr.Blocks() as app:
    with gr.Row():
        dd_configs = gr.Dropdown(choices=list_from_folder())
        with gr.Row():
            update_btn = gr.Button("Update Dropdown")

    update_btn.click(lambda : update(dd_configs))

app.launch(share=False)
