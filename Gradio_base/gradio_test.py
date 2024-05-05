import gradio as gr


def greet(name, intensity, blast):
    print(blast)
    return "Hello, " + name + "!" * int(intensity)


demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider", "slider"],
    outputs=["text"],
)

if __name__ == '__main__':
    demo.launch()
