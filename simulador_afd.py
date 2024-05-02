import tkinter as tk
from clase_afd import AFD

def ventana_estados(ventana):
    """Crea y muestra la ventana para el ingreso de estado inicial y estados finales de un AFD.

    Args:
        ventana (tk.Tk): Ventana principal de la aplicación.
    """
    limpiar_ventana(ventana)

    tk.Label(ventana, text="Ingresar estado inicial:").pack()
    entry_estado_inicial = tk.Entry(ventana)
    entry_estado_inicial.pack()

    tk.Label(ventana, text="Ingresar estados finales separados por comas:").pack()
    entry_estados_finales = tk.Entry(ventana)
    entry_estados_finales.pack()

    def validar_estados():
        global estado_inicial
        global estados_finales
        estado_inicial = entry_estado_inicial.get().strip()
        estados_finales = set(entry_estados_finales.get().strip().split(','))

        if estado_inicial == "":
            error_label_estado.config(text="ERROR: el estado inicial no puede ser vacio")
        elif "," in estado_inicial:
             error_label_estado.config(text="ERROR: solo puede haber un estado inicial")
        elif "" in estados_finales:
            error_label_estado.config(text="ERROR: el campo 'estados finales' no puede ser vacio")            
        else:
            estados.add(estado_inicial)
            for f in estados_finales:
                estados.add(f)
            
            ventana_transiciones(ventana)


    tk.Button(ventana, text="Confirmar", command=validar_estados).pack()

    error_label_estado = tk.Label(ventana, text="", fg="red")
    error_label_estado.pack()



def ventana_transiciones(ventana):
    """Crea y muestra la ventana para el ingreso de transiciones de un AFD.

    Args:
        ventana (tk.Tk): Ventana principal de la aplicación.
    """
    limpiar_ventana(ventana)

    

    tk.Label(ventana, text='Transición "estado, símbolo, nuevo estado":').pack()
   
    entry_transicion = tk.Entry(ventana)
    entry_transicion.pack()

    def agregar_transicion():
        transicion_str = entry_transicion.get().strip()
        transicion = transicion_str.split(',')
        if len(transicion) == 3:
            estado = transicion[0].strip()
            simbolo = transicion[1].strip()
            nuevo_estado = transicion[2].strip()
            if estado == "" or nuevo_estado == "":
                error_label_transiciones.config(text=f"ERROR: no se acepta estado ni alfabeto vacio")
            elif( len(simbolo) != 1):
                error_label_transiciones.config(text=f"ERROR: el simbolo tiene que tener un carácter")
            elif  (estado, simbolo) in transiciones:
                error_label_transiciones.config(text=f"Simbolo ya utilizado en el estado: {estado}")
            else:
                transiciones[(estado, simbolo)] = nuevo_estado
                if(estado not in estados):
                    estados.add(estado)
                if(nuevo_estado not in estados):
                    estados.add(estado)
                
                label_transiciones.config(text=label_transiciones.cget("text") + "\n" + ", ".join(transicion))
                entry_transicion.delete(0, tk.END)
                error_label_transiciones.config(text="")
                
        else:
            error_label_transiciones.config(text="ERROR: Formato incorrecto")

    tk.Button(ventana, text="Agregar Transición", command=agregar_transicion).pack()
    
    estado_inicial_label = tk.Label(ventana, text="Estado inicial:\n" + estado_inicial)
    estado_inicial_label.pack()
    estados_finales_label = tk.Label(ventana, text="Estados finales:\n" )
    for ef in estados_finales:
        estados_finales_label.config(text=estados_finales_label.cget("text") + "  " + ef)
    estados_finales_label.pack()

    label_transiciones = tk.Label(ventana, text="Transiciones:")
    label_transiciones.pack()

    error_label_transiciones = tk.Label(ventana, text="", fg="red")
    error_label_transiciones.pack()

    mi_AFD = AFD(estados,transiciones,estado_inicial,estados_finales)
    
    tk.Button(ventana, text="Continuar", command=lambda: ventana_palabras(ventana, mi_AFD)).pack()


def ventana_palabras(ventana, mi_AFD: AFD):
    """Crea y muestra la ventana para el ingreso de palabras a evaluar en un AFD.

    Args:
        ventana (tk.Tk): Ventana principal de la aplicación.
        mi_AFD (AFD): Instancia del AFD sobre el cual se evaluarán las palabras.
    """
    limpiar_ventana(ventana)


    tk.Label(ventana, text="Ingresar una palabra:").pack()
    entry_palabra = tk.Entry(ventana)
    entry_palabra.pack()

    def validar_palabras():
        palabra = str(entry_palabra.get())
        if mi_AFD.validar_palabra(palabra):
            palabra_label.config(text="La palabra pertenece al AFD", fg='green')
        else:
            palabra_label.config(text="La palabra no pertenece al AFD", fg='red')
            
    estado_inicial_label = tk.Label(ventana, text="Estado inicial:\n" + estado_inicial)
    estado_inicial_label.pack()
    
    estados_finales_label = tk.Label(ventana, text="Estados finales:\n" )
    for ef in estados_finales:
        estados_finales_label.config(text=estados_finales_label.cget("text") + "  " + ef)
    estados_finales_label.pack()

    tk.Label(ventana, text="Transiciones:").pack()
    for (estado, simbolo), nuevo_estado in transiciones.items():
        tk.Label(ventana, text=f"{estado}, {simbolo} -> {nuevo_estado}").pack()

    tk.Button(ventana, text="Confirmar", command=validar_palabras).pack()


    palabra_label = tk.Label(ventana, text="", fg="red")
    palabra_label.pack()
     
    tk.Button(ventana, text="Volver a Ingresar AFD", command=lambda:( mi_AFD.reiniciar_afd(),ventana_estados(ventana))).pack()


def limpiar_ventana(ventana):
    """Elimina todos los widgets de la ventana.

    Args:
        ventana (tk.Tk): Ventana de la cual se eliminarán los widgets.
    """
    for widget in ventana.winfo_children():
        widget.destroy()



ventana = tk.Tk()
ventana.title("Simulador AFD")
ventana.geometry("854x480")


estados = set()
transiciones = {}
estados_finales = set()

ventana_estados(ventana)

ventana.mainloop()
