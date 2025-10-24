Explicación del código paso a paso:

Primero se crea la clase Nodo:
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
- Cada nodo guarda:
- valor → número
- izq → hijo izquierdo
- der → hijo derecho

Luego se crea la clase ArbolBB_
constructor:
self.raiz = None
- El árbol comienza vacío.

Insertar:
insertar() → si raíz es None, ese nodo pasa a ser la raíz  
sino → se llama a _insertar_recursivo()
- Regla del ABB:
- Si el valor es menor, va al subárbol izquierdo
- Si es mayor, va al subárbol derecho
- No se insertan valores repetidos

Luego la búsqueda:
buscar() → si no encuentra, devuelve False
- Se compara el número:
- Si es igual → encontrado
- Si es menor → busca en la izquierda
- Si es mayor → busca en la derecha

