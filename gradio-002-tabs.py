import gradio as gr

def func1(name):
    return f"Siemka, {name}"

def func2(word):
    return word[::-1]

app1 = gr.Interface(fn=func1, inputs="text", outputs="text" )
app2 = gr.Interface(fn=func2, inputs="text", outputs="text" )

demo = gr.TabbedInterface([app1, app2], ["Zakładka 1", "Zakładka 2"], title="Tabs")
demo.launch()