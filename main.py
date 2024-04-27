import tkinter as tk


def main():
    # Crear una instancia de la clase Tk, que representa la ventana principal de la aplicación
    ventana = tk.Tk()

    # Opcional: configurar propiedades de la ventana, como su tamaño y título
    ventana.geometry("900x600")  # Establece el tamaño de la ventana a 400x300 píxeles
    ventana.title("AFD")  # Establece el título de la ventana

    # Bucle principal de la aplicación para que la ventana permanezca abierta
    entrada = tk.Entry(ventana)
    entrada.pack()
    ventana.mainloop()


def ventana_ingresos():
    pass






if __name__ == "__main__":
    main()
