import tkinter as tk

def confirmar():
    # Obtener valores de los campos de entrada
    estados_str = entry_estados.get().strip()
    alfabeto_str = entry_alfabeto.get().strip()

    # Verificar que no haya elementos vacíos
    
    estados = set(estados_str.split(','))
    alfabeto = set(alfabeto_str.split(','))

    # Verificar que no haya elementos vacíos en los conjuntos
    if "" not in estados and "" not in alfabeto:
        # Actualizar las etiquetas con los conjuntos ingresados
        label_estados.config(text="Estados: " + ", ".join(estados))
        label_alfabeto.config(text="Alfabeto: " + ", ".join(alfabeto))
    else:
        error_label.config(text="ERROR: No ingrese elementos vacíos (',,' o terminado en coma)")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ingreso de Estados y Alfabetos")
ventana.geometry("400x300")

# Etiquetas y campos de entrada para estados y alfabeto
tk.Label(ventana, text="Ingresar estados (separados por comas):").pack()
entry_estados = tk.Entry(ventana)
entry_estados.pack()

tk.Label(ventana, text="Ingresar alfabeto (separado por comas):").pack()
entry_alfabeto = tk.Entry(ventana)
entry_alfabeto.pack()

# Botón para confirmar y cerrar la ventana
tk.Button(ventana, text="Confirmar", command=confirmar).pack()

# Etiqueta para mostrar conjuntos ingresados
label_estados = tk.Label(ventana, text="")
label_estados.pack()

label_alfabeto = tk.Label(ventana, text="")
label_alfabeto.pack()

# Etiqueta para mostrar errores
error_label = tk.Label(ventana, text="", fg="red")
error_label.pack()

# Bucle principal de la ventana
ventana.mainloop()
