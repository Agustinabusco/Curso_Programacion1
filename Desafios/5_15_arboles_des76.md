Como primer paso se define la clase Nodo, de esta manera: class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
Lo que nos permite guardar en cada nodo el valor, en este caso numero; en self izquierda se referencia al hijo izquierdo (y en caso de no tener queda: None, es decir que no hay ningun vlor asignado) y en self.derecha hace referencia al hijo derecho (lo mismo pasa con None).
Posteriormente se usa una función de recorrido en preorden: def preorden(nodo):
    if nodo is not None:
        print(nodo.valor, end=" ")
        preorden(nodo.izquierda)
        preorden(nodo.derecha)
Preorden significa que primero visitamos la raiz, luego recorremos el subárbol izquierdo y finalmenterr el subárbol derecho.
- El if nodo is not None evita errores cuando llegamos a un nodo vacio.
Luego ae construye el árbol, en este caso de 3 niveles.
Luego con: preorden(raiz): se llama a la función, empieza en la raiz y recorre todo en preorden.