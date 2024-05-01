class AFD:
    """Clase que representa un Autómata Finito Determinista (AFD).

    Args:
        estados (set): Conjunto de estados del AFD.
        transiciones (dict): Diccionario que contiene las transiciones del AFD.
        estado_inicial (str): Estado inicial del AFD.
        estados_finales (set): Conjunto de estados finales del AFD.

    Atributos:
        estados (set): Conjunto de estados del AFD.
        transiciones (dict): Diccionario que contiene las transiciones del AFD.
        estado_inicial (str): Estado inicial del AFD.
        estados_finales (set): Conjunto de estados finales del AFD.
    """
    def __init__(self, estados: set,transiciones: dict, estado_inicial: str, estados_finales: set):
        self.estados = estados #set
        self.transiciones = transiciones #diccionario {(estado_actual,transicion): estado a ir}
        self.estado_inicial = estado_inicial #variable
        self.estados_finales = estados_finales #set

    def validar_palabra(self, palabra:str)->bool:
        """Valida si una palabra pertenece al lenguaje definido por el AFD.

        Args:
            palabra (str): Palabra a validar.

        Returns:
            bool: True si la palabra es aceptada por el AFD, False en caso contrario.
        """
        estado_actual = self.estado_inicial
        for simbolo in palabra:
            # Verifica si hay una transición definida para el estado actual y el símbolo actual
            if (estado_actual, simbolo) in self.transiciones: #si existe la transicion leyendo el simbolo
                # Si hay una transición, actualiza el estado actual al siguiente estado
                estado_actual = self.transiciones[(estado_actual, simbolo)] # estado actual = valor en (estado_actual, simbolo)
            else:
                # Si no hay una transición definida, la palabra no es válida
                return False
        # Verifica si el estado actual después de procesar toda la palabra está en el conjunto de estados finales
        return estado_actual in self.estados_finales

    def reiniciar_afd(self):
        """Reinicia los conjuntos de datos del AFD."""
        self.estados.clear()
        self.transiciones.clear()
        self.estados_finales.clear()
