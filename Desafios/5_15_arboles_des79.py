# Nodo del Árbol Binario de Búsqueda
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

# Clase ABB con métodos insertar y buscar
class ArbolBB:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.der, valor)
        # Si el valor es igual, no se inserta porque la consigna dice "enteros únicos"

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izq, valor)
        else:
            return self._buscar_recursivo(nodo.der, valor)


#Demostración

# Conjunto de valores únicos
valores = [8, 3, 10, 1, 6, 14, 4, 7]

arbol = ArbolBB()

# Insertar valores en el árbol
for num in valores:
    arbol.insertar(num)

# Buscar un valor ingresado por el usuario
numero = int(input("Número a buscar: "))

if arbol.buscar(numero):
    print(f"El número {numero} SÍ está en el árbol.")
else:
    print(f"El número {numero} NO se encuentra en el árbol.")
