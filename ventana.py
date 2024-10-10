import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar(texto, marco_grafica):
    funciones_str = texto.get("1.0", "end-1c").strip()  # Obtener el texto y eliminar espacios
    if funciones_str == "":
        messagebox.showerror("Error", "Por favor, ingrese al menos una función.")
        return

    # Preparar un rango de valores para x
    x = np.linspace(-10, 10, 400)  # 400 puntos entre -10 y 10

    # Limpiar la figura antes de graficar
    plt.figure(figsize=(5, 4))

    colores = ['blue', 'green', 'red', 'purple', 'orange']  # Colores para las gráficas

    # Iterar sobre las funciones separadas por comas
    funciones = funciones_str.split(',')
    for i, funcion_str in enumerate(funciones):
        funcion_str = funcion_str.strip()  # Eliminar espacios en blanco
        if funcion_str == "":
            continue

        try:
            # Evaluar la función usando eval() y reemplazar 'x'
            y = eval(funcion_str.replace("x", "x"))
            plt.plot(x, y, label=f"y = {funcion_str}", color=colores[i % len(colores)])  # Graficar con colores distintos
        except Exception as e:
            messagebox.showerror("Error", f"Error en la función '{funcion_str}': {e}")
            return

    # Añadir título y etiquetas
    plt.title("Gráfica de las Funciones Ingresadas")
    plt.xlabel("x")
    plt.ylabel("y")

    # Configurar límites del gráfico
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Añadir línea central en los ejes x e y
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')

    # Estilo de la cuadrícula
    plt.grid(True, linestyle='--', alpha=0.7)
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
    etiqueta = tk.Label(ventana, text="Ingrese funciones separadas por comas (ej: y=x+2, y=x**2):")
    etiqueta.grid(padx=10, pady=10, row=0, column=0, columnspan=5, sticky="nsew")

    # Crear un cuadro de texto
    texto = tk.Text(ventana, height=5, width=40)
    texto.grid(padx=10, pady=10, row=1, column=0, columnspan=5, sticky="nsew")

    # Crear un marco para contener la gráfica con estilo personalizado
    marco_grafica = tk.Frame(ventana, bg='lightgray', bd=2, relief='solid')  # Fondo claro y borde personalizado
    marco_grafica.grid(padx=5, pady=5, row=3, column=0, columnspan=5, sticky="nsew")

    # Crear un botón para generar la gráfica
    boton_graficar = tk.Button(ventana, text="Graficar", command=lambda: graficar(texto, marco_grafica))
    boton_graficar.grid(padx=10, pady=10, row=2, column=1, sticky="nsew")

    # Crear un botón para borrar el texto y la gráfica
    boton_borrar = tk.Button(ventana, text="Borrar", command=lambda: borrar(texto, marco_grafica))
    boton_borrar.grid(padx=10, pady=10, row=2, column=3, sticky="nsew")

    # Ajustar el peso de las columnas y filas para centrar
    for i in range(5):
        ventana.grid_columnconfigure(i, weight=1)
    ventana.grid_rowconfigure(3, weight=1)

    # Iniciar el loop principal
    ventana.mainloop()
