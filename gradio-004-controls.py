import gradio as  gr
import json

def process_inputs(text, number, slider, checkbox1, checkbox2, radio, dropdown, colorpicker):
    data = {
        "textbox": text,
        "number": number,
        "slider": slider,
        "checkbox1": checkbox1,
        "checkbox2": checkbox2,
        "radio": radio,
        "dropdown": dropdown,
        "colorpicker" : colorpicker
    }
    return json.dumps(data, indent=4)

app = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Textbox(label="pole tekstowe", placeholder="wprowadz teskt", text_align="left"),
        gr.Number(label="pole numeryczne", minimum=-10, maximum=10, step=0.5),
        gr.Slider(minimum=0, maximum=100, label="suwak"),
        gr.Checkbox(label="checbox"),
        gr.Checkboxgroup(["wariant A","wariant B","wariant C"]),
        gr.Radio(["opcja1","opcja2","opcja3"]),
        gr.Dropdown(["X","Y","Z"], multiselect=True),
        gr.ColorPicker(label="Wybór koloru")
    ],
    outputs="json",
    title="Tytuł aplikacji",
    description="Opis aplikacji"
)
app.launch()