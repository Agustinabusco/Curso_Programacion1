#definimos la clase Nodo para construir el árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

#función para recorrer el árbol inorden y sumar los valores
def sumainorden(Nodo):
    if Nodo is None:
        return 0
    #recorrer subárbol izquierdo
    izquierda = sumainorden(Nodo.izquierda)
    #se procesa el nodo actual
    actual = Nodo.valor
    #recorrer el subárbol derecho
    derecha = sumainorden(Nodo.derecha)
    #devolver la suma total
    return izquierda + actual + derecha

#construir un árbol binario
raiz = Nodo(10)
raiz.izquierda = Nodo(5)
raiz.derecha = Nodo(15)
raiz.izquierda.izquierda = Nodo(2)
raiz.izquierda.derecha = Nodo(7)
raiz.derecha.izquierda = Nodo(12)
raiz.derecha.derecha = Nodo(20)

#llamamos a la función para realizar la suma
resultado = sumainorden(raiz)
print("La suma de todos los valores es:", resultado)