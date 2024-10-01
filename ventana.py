import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar(texto, marco_grafica):
    funcion_str = texto.get("1.0", "end-1c").strip()  # Obtener el texto y eliminar espacios
    if funcion_str == "":
        messagebox.showerror("Error", "Por favor, ingrese una función.")
        return

    # Preparar un rango de valores para x
    x = np.linspace(-10, 10, 400)  # 400 puntos entre -10 y 10

    try:
        # Evaluar la función usando eval()
        y = eval(funcion_str.replace("x", "x"))  # Reemplazar 'x' en la cadena de la función
    except Exception as e:
        messagebox.showerror("Error", f"Error en la función: {e}")
        return

    # Generar la gráfica
    plt.figure(figsize=(5, 4))
    plt.plot(x, y, label=f"y = {funcion_str}", color='blue')
    plt.title("Gráfica de la Función Ingresada")
    plt.xlabel("x")
    plt.ylabel("y")
    
    # Configurar límites del gráfico
    plt.xlim(-10, 10)  # Limites del eje x
    plt.ylim(-10, 10)  # Limites del eje y

    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    
    # Limpiar la ventana de gráficos anterior
    for widget in marco_grafica.winfo_children():
        widget.destroy()

    # Mostrar la gráfica en el marco de la ventana
    canvas = FigureCanvasTkAgg(plt.gcf(), master=marco_grafica)
    canvas.draw()
    canvas.get_tk_widget().pack()

def borrar(texto, marco_grafica):
    """Función para borrar el texto y los gráficos."""
    texto.delete("1.0", "end")  # Borrar el contenido del cuadro de texto
    for widget in marco_grafica.winfo_children():  # Limpiar la gráfica anterior
        widget.destroy()

def crear_ventana():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Graficador de Funciones")
    ventana.geometry("550x650")

    # Crear una etiqueta
    etiqueta = tk.Label(ventana, text="Ingrese una función (ej: y=x+2):")
    etiqueta.grid(padx=10, pady=10, row=0, column=0, columnspan=5, sticky="nsew")

    # Crear un cuadro de texto
    texto = tk.Text(ventana, height=5, width=40)
    texto.grid(padx=10, pady=10, row=1, column=0, columnspan=5, sticky="nsew")

    # Crear un marco para contener la gráfica
    marco_grafica = tk.Frame(ventana)
    marco_grafica.grid(padx=5, pady=5, row=3, column=0, columnspan=5, sticky="nsew")

    # Crear un botón para generar la gráfica
    boton_graficar = tk.Button(ventana, text="Graficar", command=lambda: graficar(texto, marco_grafica))
    boton_graficar.grid(padx=10, pady=10, row=2, column=1, sticky="nsew")

    # Crear un botón para borrar el texto y la gráfica
    boton_borrar = tk.Button(ventana, text="Borrar", command=lambda: borrar(texto, marco_grafica))
    boton_borrar.grid(padx=10, pady=10, row=2, column=3, sticky="nsew")

    # Ajustar el peso de las columnas y filas para centrar
    for i in range(5):
        ventana.grid_columnconfigure(i, weight=1)  # Distribuir espacio entre columnas
    ventana.grid_rowconfigure(3, weight=1)  # Asegurarse de que la fila de la gráfica crezca

    # Iniciar el loop principal
    ventana.mainloop()


