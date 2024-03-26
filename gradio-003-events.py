import gradio as  gr

def show_text(s):
    return s

demo = gr.Blocks()

with demo:
    gr.Markdown("""
        # Tekst dla aplikacji
        Zacznij wpisywać tekst
    """)
    input = gr.Textbox(placeholder="Tu wpisz tekst...")
    output = gr.Textbox()

    input.change(fn=show_text, inputs=input, outputs=output, show_progress=False)

demo.launch()