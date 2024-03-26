import gradio as  gr
import numpy as np

def flip(im):
    return np.flipud(im)

app = gr.Interface(
    fn=flip,
    inputs=gr.Image(sources="webcam", streaming=True),
    outputs="image",
    live=True
)
app.launch()