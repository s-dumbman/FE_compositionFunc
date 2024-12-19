import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import math as mt

def plot_function(type, expression, x_range=(-10, 10), n_points=1000):
    x = np.linspace(x_range[0], x_range[1], n_points)
    try:
        y = eval(expression, {"x": x, "np": np, "mt": mt})
        
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f"y = {expression}")
        plt.title(f"{type}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")

def plot_generate(f_ex, p_ex, x_range=(-10, 10), n_points=1000):
    x = np.linspace(x_range[0], x_range[1], n_points)
    try:
        p = eval(p_ex, {"x": x, "np": np, "mt": mt})
        y = eval(f_ex, {"x": p, "np": np, "mt": mt})

        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f"y = f(p(x)), f(x) = {f_ex}, p(x) = {p_ex}")
        plt.title("f(p(x))")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")

def launch():
    def selected_plot_generate():
        f_ex = f_entry.get()
        p_ex = p_entry.get()
        selection = combo_box.get()

        if selection == "f(x)":
            plot_function("f(x)", f_ex)
        elif selection == "p(x)":
            plot_function("p(x)", p_ex)
        elif selection == "f(p(x))":
            plot_generate(f_ex, p_ex)

    root = tk.Tk()
    root.title("HAP-SEONG Func Generator")

    ttk.Label(root, text="f(x):").grid(row=0, column=0, padx=10, pady=10)
    f_entry = ttk.Entry(root, width=30)
    f_entry.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(root, text="p(x):").grid(row=1, column=0, padx=10, pady=10)
    p_entry = ttk.Entry(root, width=30)
    p_entry.grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(root, text="Plot?:").grid(row=2, column=0, padx=10, pady=10)
    combo_box = ttk.Combobox(root, values=["f(x)", "p(x)", "f(p(x))"])
    combo_box.grid(row=2, column=1, padx=10, pady=10)
    combo_box.set("f(x)")

    plot_button = ttk.Button(root, text="Plot", command=selected_plot_generate)
    plot_button.grid(row=3, column=0, columnspan=2, pady=20)

    root.mainloop()

if __name__ == "__main__":
    launch()
