import gradio as  gr


def calculate_bmr_and_bmi(sex, weight, height, age):
    # Obliczenie BMR (Basal Metabolic Rate) według wzoru Harrisa-Benedicta
    if sex == "Mężczyzna":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    # Obliczenie BMI (Body Mass Index)
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)

    return f"Zapotrzebowanie kaloryczne (BMR): {bmr:.2f} kcal/dzień", f"BMI: {bmi:.2f}"

app = gr.Interface(
    fn=calculate_bmr_and_bmi,
    inputs=[
        gr.Radio(choices=["Mężczyzna","Kobieta"], label="Płeć"),
        gr.Number(label="Waga (kg)"),
        gr.Slider(minimum=140, maximum=220, step=1, label="Wzrost (cm)"),
        gr.Slider(minimum=18, maximum=100, step=1, label="Wiek")
    ],
    outputs=[
        gr.Textbox(label="Zapotrzebowanie kaloryczne"),
        gr.Textbox(label="BMI")
    ],
    title="Kalkulator BMI i BMR",
    description="Oblicz wartości",
    allow_flagging="never"
)

app.launch()