#Definimos la clase Nodo para construir el árbol
class Nodo:
   def __init__(self, valor):
       self.valor = valor 
       self.izquierda = None
       self.derecha = None

#función para recorrer el árbol 
def preorden(nodo):
    if nodo is not None:
#visitar la raiz
     print(nodo.valor, end=" ")
#recorrer el subárbol izquierdo
    preorden(nodo.izquierda)
#recorremos el subárbol derecho
    preorden(nodo.derecho)

#construir árbol binario de 3 niveles
raiz = Nodo(1) #nivel 1(raíz)

raiz.izquierda = Nodo(2) #nivel 2(hijo izquierdo)
raiz.derecha = Nodo(3) #nivel 2(hijo derecho)

raiz.izquierda.izquierda = Nodo(4) #nivel 3(hijo izquierdo de 2)
raiz.izquierda.derecha = Nodo(5) #nivel 3(hijo derecho de 2)
raiz.derecha.izquierda = Nodo(6) #nivel 3(hijo de 3)
raiz.derecha.derecha = Nodo(7) #nivel 3(hijo de 3)
#llamar a la función de recorrido preorden
print("Recorrido en preorden:")
preorden(raiz)