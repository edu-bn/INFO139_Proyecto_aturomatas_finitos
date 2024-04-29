import tkinter as tk
from Clase_AFD import AFD

def crear_ventana(ventana):
    #ventana = tk.Toplevel(ventana)
    LimpiarVentana(ventana)
    ventana.title("Ingreso de Transiciones")
    
    # Etiqueta y campo de entrada para la transición
    tk.Label(ventana, text="Transición (estado, símbolo, nuevo estado):").pack()
    entry_transicion = tk.Entry(ventana)
    entry_transicion.pack()

    def agregar_transicion():
        transicion_str = entry_transicion.get().strip()
        transicion = transicion_str.split(',')
        if len(transicion) == 3:
            estado = transicion[0]
            simbolo = transicion[1]
            print(estado)
            print(simbolo)
            nuevo_estado = transicion[2]
            if simbolo not in alfabeto or estado not in estados or nuevo_estado not in estados:
                error_label_transiciones.config(text="ERROR: Transición no válida")
            elif  (estado, simbolo) in transiciones:
                error_label_transiciones.config(text=f"Simbolo ya utilizado en el estado: {estado}")

            else:
                transiciones[(estado, simbolo)] = nuevo_estado
                label_transiciones.config(text=label_transiciones.cget("text") + "\n" + ", ".join(transicion))
                entry_transicion.delete(0, tk.END)     
                print(transiciones)

        else:
            error_label_transiciones.config(text="ERROR: Formato incorrecto")

    # Botón para agregar la transición
    tk.Button(ventana, text="Agregar Transición", command=agregar_transicion).pack()

    # Etiqueta para mostrar transiciones ingresadas
    label_transiciones = tk.Label(ventana, text="Transiciones:")
    label_transiciones.pack()

    # Etiqueta para mostrar errores
    error_label_transiciones = tk.Label(ventana, text="", fg="red")
    error_label_transiciones.pack()

    # Botones para continuar o agregar más transiciones
    tk.Button(ventana, text="Continuar", command=lambda:continuar(ventana)).pack()
    #FIN crear ventana
    
    
def continuar(ventana):
    LimpiarVentana(ventana)

    tk.Label(ventana, text="Ingresar estado inicial:").pack()
    entry_estado_inicial = tk.Entry(ventana)
    entry_estado_inicial.pack()

    tk.Label(ventana, text="Ingresar estados finales separados por comas:").pack()
    entry_estados_finales =  tk.Entry(ventana)
    entry_estados_finales.pack()
    
    def seguir():
        estado_inicial = entry_estado_inicial.get().strip()
        estados_finales = set(entry_estados_finales.get().strip().split(','))
        
        
        if (estado_inicial not in estados):
            error_label_estado.config(text="ERROR: el estado inicial ingresado no pertenece a los estados")
        elif (not estados_finales.issubset(estados)):
            error_label_estado.config(text="ERROR: algun estado final no pertenece a los estados")
        else:
            mi_AFD = AFD(estados,alfabeto,transiciones,estado_inicial,estados_finales)
            ventana_palabras(ventana,mi_AFD)
            
    tk.Button(ventana, text="confirmar", command=seguir).pack()    
    # Etiqueta para mostrar errores
    error_label_estado = tk.Label(ventana, text="", fg="red")
    error_label_estado.pack()

    
def ventana_palabras(ventana,mi_AFD: AFD):
    LimpiarVentana(ventana)
    ventana.title("ingresar palabras")
    tk.Label(ventana, text="ingresar una palabra:").pack()

    entry_palabra = tk.Entry(ventana)
    entry_palabra.pack()
    
    def confirmar_palabras():
        palabra = str(entry_palabra.get())
        if(mi_AFD.validar_palabra(palabra)):
            palabra_label.config(text="la palabra pertenece al AFD", fg='green')
        else:
            palabra_label.config(text="la palabra no pertenece al AFD")


    tk.Button(ventana, text="confirmar", command=confirmar_palabras).pack()    
    palabra_label = tk.Label(ventana, text="", fg="red")
    palabra_label.pack()
    



def confirmar_estados_alfabeto(ventana):
    # Obtener valores de los campos de entrada
    estados_str = entry_estados.get().strip()
    alfabeto_str = entry_alfabeto.get().strip()

    # Verificar que no haya elementos vacíos
   
    global estados, alfabeto
    estados = set(estados_str.split(','))
    alfabeto = set(alfabeto_str.split(','))

    # Verificar que no haya elementos vacíos en los conjuntos
    if "" not in estados and "" not in alfabeto:
        crear_ventana(ventana)
    else:
        error_label.config(text="ERROR: No ingrese elementos vacíos (',,' o terminado en coma)")
    

def LimpiarVentana(ventana):
    """Elimina todos los widgets de la ventana"""
    for widget in ventana.winfo_children():
       widget.destroy()


# Crear ventana principal

ventana = tk.Tk()
ventana.title("Ingreso de Estados y Alfabetos")
ventana.geometry("400x400")

# Etiquetas y campos de entrada para estados y alfabeto
tk.Label(ventana, text="Estados separados por comas:").pack()
entry_estados = tk.Entry(ventana)
entry_estados.pack()

tk.Label(ventana, text="Alfabeto separado por comas:").pack()
entry_alfabeto = tk.Entry(ventana)
entry_alfabeto.pack()

# Botón para confirmar y cerrar la ventana
tk.Button(ventana, text="Confirmar", command=lambda:confirmar_estados_alfabeto(ventana)).pack()

# Etiqueta para mostrar errores
error_label = tk.Label(ventana, text="", fg="red")
error_label.pack()

# Conjuntos para almacenar estados, alfabeto y transiciones
estados = set()
alfabeto = set()
transiciones = {}
estados_finales = set()
estado_inicial = str()


# Bucle principal de la ventana
ventana.mainloop()
