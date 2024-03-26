import gradio as gr
import matplotlib.pyplot as plt
import numpy as np


def solve_quadratic_equation(a, b, c):
    # Obliczanie delty
    delta = b ** 2 - 4 * a * c

    # Sprawdzanie ilości miejsc zerowych
    if delta > 0:
        x1 = (-b - np.sqrt(delta)) / (2 * a)
        x2 = (-b + np.sqrt(delta)) / (2 * a)
        roots = f"Miejsca zerowe: x1 = {x1:.2f}, x2 = {x2:.2f}"
    elif delta == 0:
        x = -b / (2 * a)
        roots = f"Jedno miejsce zerowe: x = {x:.2f}"
    else:
        roots = "Brak miejsc zerowych w zbiorze liczb rzeczywistych."

    # Tworzenie wykresu
    x_values = np.linspace(-10, 10, 400)
    y_values = a * (x_values ** 2) + b * x_values + c
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label=f'y = {a}x² + {b}x + {c}')
    plt.title("Wykres funkcji kwadratowej")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axhline(0, color='black', lw=2)
    plt.axvline(0, color='black', lw=2)
    plt.legend()

    # Zapisywanie wykresu do pliku
    plt.savefig("quadratic_function_plot.png")
    plt.close()

    return roots, "quadratic_function_plot.png"


app = gr.Interface(
    fn=solve_quadratic_equation,
    inputs=[gr.Number(label="a"), gr.Number(label="b"), gr.Number(label="c")],
    outputs=[gr.Textbox(label="Miejsce zerowe"), gr.Image(label="Wykres funkcji")],
    title="Rozwiązywanie równania kwadratowego",
    description="Podaj współczynniki a, b, i c równania kwadratowego, a aplikacja obliczy miejsca zerowe i wygeneruje wykres funkcji."
)

app.launch()