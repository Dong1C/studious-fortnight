import os
import gradio as gr
from utils import list_from_folder

cfg_path = './configs'
ckpt_path= './checkpoints'
cfg_set = set(list_from_folder(folder_path=cfg_path, mode='d'))
ckpt_set = set(list_from_folder(folder_path=ckpt_path, mode='d'))

with gr.Blocks() as demo:
    with gr.Row():
        model_name = gr.Dropdown(cfg_set & ckpt_set, label="Model Name")
        cfg_file = gr.Dropdown([], label="Config Full Name")
        
    @model_name.change(inputs=model_name, outputs=cfg_file)
    def update_cfg_list(model_name):
        cfg_list = [cfg for cfg in 
                    list_from_folder(folder_path=os.path.join(cfg_path, model_name), mode='f')
                    if cfg.endswith('.py')]
        return gr.Dropdown(choices=cfg_list, value=cfg_list[0], interactive=True)

demo.launch(share=False)


# countries_cities_dict = {
#     "USA": ["New York", "Los Angeles", "Chicago"],
#     "Canada": ["Toronto", "Montreal", "Vancouver"],
#     "Pakistan": ["Karachi", "Lahore", "Islamabad"],
# }


# def change_textbox(choice):
#     if choice == "short":
#         return gr.Textbox(lines=2, visible=True), gr.Button(interactive=True)
#     elif choice == "long":
#         return gr.Textbox(lines=8, visible=True, value="Lorem ipsum dolor sit amet"), gr.Button(interactive=True)
#     else:
#         return gr.Textbox(visible=False), gr.Button(interactive=False)


# with gr.Blocks() as demo:
#     radio = gr.Radio(
#         ["short", "long", "none"], label="What kind of essay would you like to write?"
#     )
#     text = gr.Textbox(lines=2, interactive=True, show_copy_button=True)

#     with gr.Row():
#         num = gr.Number(minimum=0, maximum=100, label="input")
#         out = gr.Number(label="output")
#     minimum_slider = gr.Slider(0, 100, 0, label="min")
#     maximum_slider = gr.Slider(0, 100, 100, label="max")
#     submit_btn = gr.Button("Submit", variant="primary")

#     with gr.Row():
#         country = gr.Dropdown(list(countries_cities_dict.keys()), label="Country")
#         cities = gr.Dropdown([], label="Cities")
        
#     @country.change(inputs=country, outputs=cities)
#     def update_cities(country):
#         cities = list(countries_cities_dict[country])
#         return gr.Dropdown(choices=cities, value=cities[0], interactive=True)

#     def reset_bounds(minimum, maximum):
#         return gr.Number(minimum=minimum, maximum=maximum)

#     radio.change(fn=change_textbox, inputs=radio, outputs=[text, submit_btn])
#     gr.on(
#         [minimum_slider.change, maximum_slider.change],
#         reset_bounds,
#         [minimum_slider, maximum_slider],
#         outputs=num,
#     )
#     num.submit(lambda x: x, num, out)



# if __name__ == "__main__":
#     demo.launch()
