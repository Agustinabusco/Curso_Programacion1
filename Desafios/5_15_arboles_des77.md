Primeor se define la clase Nodo, igual que antes cada nodo guarda: 
- un valor (numero entero),
- referencia a su izquierda,
- referencia a su derecha 

Luego pasamos a la función: suma_inorden:
def suma_inorden(nodo):
    if nodo is None:
        return 0
    izquierda = suma_inorden(nodo.izquierda)
    actual = nodo.valor
    derecha = suma_inorden(nodo.derecha)
    return izquierda + actual + derecha
se usa caso base: donde si el nodo es None (árbol vacio), devolvemos 0 porque no hay nada que sumar.
luego recorremos en inorden:
1- llamamos recursivamente al subárbol izquierdo
2- tommamos el valor del nodo actual
3- llamamos recursivamente al subárbol derecho
Finalmente, sumamos todo: izquierda + actual + derecha

En el paso 3 se implementa la construcción del árbol de ejemplo
raiz = 10
hijo izquierdo = 5, hijo derecho = 15
y cada uno de ellos tiene dos hijos mas (para darle 3 niveles)

Como cuarto paso esta el resultado, donde los valores son: 2 + 5 + 7 + 10 + 12 + 15 + 20 = 71
y el programa nos va a mostrar: la suma de todos los valores es: 71.

·se usa recursión porque simplifica mucho recorrido y evita que tengamos que manejar estructuras adicionales como pilas.