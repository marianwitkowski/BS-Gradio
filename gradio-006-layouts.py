import gradio as  gr

def show_text(text, color):
    return f"<div style='color: {color};' >{text}</div>"

# Tworzenie głownego layoutu z zakładkami
with gr.Blocks() as app:
    gr.Markdown("# Aplikacja Layout+")

    with gr.Tab("Wprowadzanie tekstu"):
        with gr.Accordion("Zaawansowane opcje"):
            with gr.Column():
                text_input = gr.Textbox(label="Twój tekst")
                color_input = gr.Dropdown(label="wybierz kolor", choices=["black","red","blue","green"])

    with gr.Tab("Podgląd"):
        output = gr.HTML()

    with gr.Row():
        gr.Button("Pokaż tekst").click(fn=show_text, inputs=[text_input, color_input], outputs=output)

app.launch()