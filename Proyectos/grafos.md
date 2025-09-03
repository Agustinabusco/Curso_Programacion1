Ejercicio grafos:

- Usar clases (con constructor __init__, atributos y métodos).
- Representar grafos dirigidos y no dirigidos.
- Puede ser con una sola clase (y usar un flag para diferenciar)
- O con dos clases: GrafoDirigido y GrafoNoDirigido.
- Usar listas enlazadas para representar las aristas.
- Cada nodo tendrá su lista de adyacencia.
- Separar archivos en:
grafos_dirigidos.py → definición de las clases.
appmain.py → donde se importa, instancia y se prueba la clase.
- Diseño con listas enlazadas
- Para cumplir con la idea de listas linkeadas, lo más simple es tener dos clases:
NodoAdyacente: representa un nodo de la lista enlazada de adyacencia.
Grafo: contiene los vértices y la lista enlazada de cada vértice.

Explicación del código parte por parte:

Como primer paso,en el archivo: grafos_dirigidos.py y luego de definir la clase grafos, en esta parte del codigo: class NodoAdyacente:
    def __init__(self, destino):
        self.destino = destino
        self.siguiente = None  # apunta al siguiente nodo en la lista enlazada
Un grafo se puede guardar con una lista de adyacencia: cada vértice tiene una lista con sus vecinos.

Como se pidió usar listas enlazadas, cada elemento de la lista es un nodo y este NodoAdyacente guarda:
- destino: el nombre del vértice al que apunta la arista.
- siguiente: referencia al próximo nodo en la lista (o None si es el último).

Luego, en la clase grafo:
class Grafo:
    def __init__(self, dirigido=True):
        self.dirigido = dirigido
        self.vertices = {}  # diccionario {vertice: cabeza de la lista enlazada}
- dirigido: guarda si el grafo es dirigido o no dirigido.
- vertices: es un diccionario (tipo mapa) donde:
La clave es el nombre del vértice (ej: "A", "B"). y el valor es la cabeza de la lista enlazada de adyacencia.
Así cada vértice tiene su propia lista de vecinos.

Luego utilizamos el método agregar_vertice:
def agregar_vertice(self, v):
    if v not in self.vertices:
        self.vertices[v] = None
Acá lo que hace es crear un vértice nuevo si no existe todavía; Y lo inicializa con None porque todavía no tiene vecinos (su lista enlazada está vacía).

Luego, usamos el método agregar_arista:
def agregar_arista(self, origen, destino):
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
Primero se asegura de que existan los vértices (origen y destino).
- Crea un nuevo nodo de adyacencia con el destino.
- Lo engancha al principio de la lista del origen (esto es típico en listas enlazadas: se inserta adelante).
Si el grafo es no dirigido, también mete la arista inversa (ej: si agrego A-B, también agrega B-A).

Luego con el método mostrar lo que hace es:
def mostrar(self):
    for v in self.vertices:
        print(f"{v} -> ", end="")
        actual = self.vertices[v]
        while actual:
            print(f"{actual.destino} -> ", end="")
            actual = actual.siguiente
        print("None")
- Recorre cada vértice.
- Empieza en la cabeza de la lista enlazada.
- Va imprimiendo todos los destinos hasta llegar a None.
 Es como decir: "A -> B -> C -> None".

 Luego vamos al archivo appmain.py:
from grafos_dirigidos import Grafo
- Acá llamamos a la clase Grafo para poder usarla.

Luego en esta parte:
g_dir = Grafo(dirigido=True)  # grafo dirigido
g_no_dir = Grafo(dirigido=False)  # grafo no dirigido
Creamos dos grafos distintos, uno dirigido y otro no dirigido.

Luego se agregan las aristas asi:
g_dir.agregar_arista("A", "B")
g_dir.agregar_arista("A", "C")
g_dir.agregar_arista("B", "C")
Cada vez que agregamos una arista:
- Si es dirigido, va en una sola dirección.
- Si es no dirigido, la agrega en los dos sentidos.

Finalmente lo msotramos:
g_dir.mostrar()
g_no_dir.mostrar()
Esto imprime la lista enlazada de cada vértice para que veas cómo quedó guardado el grafo.