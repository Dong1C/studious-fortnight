import gradio as gr


class ConfRegis:
    def __init__(self, *args):
        self.max_textboxes = 10
        self.conf_list = [
            gr.Textbox(value="", interactive=True) for _ in range(self.max_textboxes)
        ]

    def add(self, conf_block):
        self.conf_list.append(conf_block)

    def clear(self):
        self.conf_list.clear()

    def render(self, num: int):
        k = int(num)
        self.conf_list = [gr.Textbox(visible=True)] * k + [
            gr.Textbox(visible=False)
        ] * (max_textboxes - k)

    def gen(self):
        pass


max_textboxes = 10
with gr.Blocks() as demo:
    s = gr.Slider(
        1,
        max_textboxes,
        value=max_textboxes,
        step=1,
        label="How many textboxes to show:",
    )
    with gr.Row():
        # textBoxes = [gr.Textbox(value="") for _ in range(max_textboxes)]
        confregis = ConfRegis()

    @s.change(inputs=s, outputs=confregis.conf_list)
    def activate(num):
        k = int(num)
        return [gr.Textbox(visible=True)] * k + [gr.Textbox(visible=False)] * (
            max_textboxes - k
        )


demo.launch(share=False)
