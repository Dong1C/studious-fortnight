import gradio as gr
from gradio_test import greet

with gr.Blocks() as demo:
    gr.Markdown("# Greetings from Gradio!")
    inp = gr.Textbox(placeholder="What is your name?")
    inIntensity = gr.Slider(0, 100, label="intensity")
    out = gr.Textbox()

    inp.change(fn=lambda x: f"Welcome, {x}!",
               inputs=inp,
               outputs=out)

if __name__ == "__main__":
    demo.launch()
