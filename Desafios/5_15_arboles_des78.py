# Definimos la clase Nodo para construir el árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para recorrer en postorden y devolver el valor máximo
def max_postorden(nodo):
    if nodo is None:
        return float('-inf')  # Si no hay nodo, devolvemos -infinito para no afectar el máximo

    # 1. Recorremos el subárbol izquierdo
    max_izquierda = max_postorden(nodo.izquierda)
    # 2. Recorremos el subárbol derecho
    max_derecha = max_postorden(nodo.derecha)
    # 3. Visitamos el nodo actual
    actual = nodo.valor

    # Devolvemos el mayor entre los tres valores
    return max(max_izquierda, max_derecha, actual)

# Construimos un árbol de ejemplo
raiz = Nodo(8)
raiz.izquierda = Nodo(3)
raiz.derecha = Nodo(10)
raiz.izquierda.izquierda = Nodo(1)
raiz.izquierda.derecha = Nodo(6)
raiz.derecha.derecha = Nodo(14)
raiz.derecha.derecha.izquierda = Nodo(13)

# Llamamos a la función para obtener el valor máximo
resultado = max_postorden(raiz)
print("El valor máximo en el árbol es:", resultado)
