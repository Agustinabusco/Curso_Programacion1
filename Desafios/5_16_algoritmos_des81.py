from collections import deque

# Clase que representa un nodo del árbol
class Nodo:
    def __init__(self, grado, estudiantes):
        self.grado = grado
        self.estudiantes = estudiantes
        self.hijos = []  # lista de grados inferiores (subniveles)

# Función para recorrer el árbol por niveles
def recorrido_por_niveles(raiz):
    if not raiz:
        return

    cola = deque([raiz])  # usamos una cola para recorrer nivel por nivel

    while cola:
        nodo_actual = cola.popleft()  # sacamos el primer elemento
        print(f"Grado {nodo_actual.grado}: {', '.join(nodo_actual.estudiantes)}")

        # agregamos los hijos del nodo actual a la cola
        for hijo in nodo_actual.hijos:
            cola.append(hijo)


# Ejemplo de uso

# Creamos los nodos (grados con sus estudiantes)
grado12 = Nodo(12, ["Ana", "Bruno"])
grado11 = Nodo(11, ["Carla", "Diego"])
grado10 = Nodo(10, ["Eva", "Facundo"])
grado9 = Nodo(9, ["Gina", "Hugo"])

# Conectamos los grados (12 -> 11 -> 10 -> 9)
grado12.hijos.append(grado11)
grado11.hijos.append(grado10)
grado10.hijos.append(grado9)

# Llamamos a la función
print("Recorrido de estudiantes por niveles:\n")
recorrido_por_niveles(grado12)
