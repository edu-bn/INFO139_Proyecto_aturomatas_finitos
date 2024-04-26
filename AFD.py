class AFD:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_finales):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estados_finales = estados_finales

    def validar_palabra(self, palabra):
        estado_actual = self.estado_inicial
        for simbolo in palabra:
            if (estado_actual, simbolo) in self.transiciones:
                estado_actual = self.transiciones[(estado_actual, simbolo)]
            else:
                return False
        return estado_actual in self.estados_finales


# Solicitar al usuario los estados y el alfabeto
estados = set(input("Ingrese los estados separados por comas: ").split(','))
alfabeto = set(input("Ingrese el alfabeto separado por comas: ").split(','))

# Solicitar al usuario las transiciones
transiciones = {}
while True:
    lista = input("Ingrese una transición en el formato 'estado, símbolo, nuevo estado' (o 'fin' para terminar): ")
    if lista.lower() == 'fin':
        break
    lista = lista.strip().split(',')
    estado = lista[0]
    simbolo = lista[1]
    nuevo_estado = lista[2]
    transiciones[(estado, simbolo)] = nuevo_estado

# Solicitar al usuario el estado inicial y los estados finales
estado_inicial = input("Ingrese el estado inicial: ")
estados_finales = set(input("Ingrese los estados finales separados por comas: ").split(','))

# Crear el AFD
AFD = AFD(estados, alfabeto, transiciones, estado_inicial, estados_finales)

# Probar algunas palabras
while True:
    palabra = input("Ingrese una palabra para validar (o 'fin' para terminar): ")
    if palabra.lower() == 'fin':
        break
    print("¿La palabra '{}' es aceptada? {}".format(palabra, AFD.validar_palabra(palabra)))
