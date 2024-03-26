import gradio as gr

def hello(name):
    return f"Siemka, {name}"

app = gr.Interface(fn=hello, inputs="text", outputs="text")
app.launch(share=True)