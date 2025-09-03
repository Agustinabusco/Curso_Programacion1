# grafos_dirigidos.py

class NodoAdyacente:
    def __init__(self, destino):
        self.destino = destino
        self.siguiente = None  # apunta al siguiente nodo en la lista enlazada


class Grafo:
    def __init__(self, dirigido=True):
        self.dirigido = dirigido
        self.vertices = {}  # diccionario {vertice: cabeza de la lista enlazada}

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = None  # cabeza de la lista de adyacencia

    def agregar_arista(self, origen, destino):
        # aseguramos que existan los vértices
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)

        # insertamos al inicio de la lista enlazada de origen
        nuevo_nodo = NodoAdyacente(destino)
        nuevo_nodo.siguiente = self.vertices[origen]
        self.vertices[origen] = nuevo_nodo

        # si es no dirigido, agregamos también la inversa
        if not self.dirigido:
            nuevo_nodo = NodoAdyacente(origen)
            nuevo_nodo.siguiente = self.vertices[destino]
            self.vertices[destino] = nuevo_nodo

    def mostrar(self):
        for v in self.vertices:
            print(f"{v} -> ", end="")
            actual = self.vertices[v]
            while actual:
                print(f"{actual.destino} -> ", end="")
                actual = actual.siguiente
            print("None")
