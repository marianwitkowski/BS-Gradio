import gradio as  gr

def show_messages(message, history):
    output = {
        "current" : message,
        "prev" : history[::-1]
    }
    history.append(message)
    return output, history


app = gr.Interface(
    fn=show_messages,
    inputs=["textbox", gr.State(value=[])],
    outputs= ["json", gr.State()]
)
app.launch()