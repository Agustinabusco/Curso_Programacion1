class Autor:
    # Constructor de la clase
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []  # Nueva lista para los libros

    # Método para mostrar los detalles del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print("Libros:")
        for libro in self.libros:
            print(f"- {libro}")

    # Método para agregar un libro a la lista
    def agregar_libro(self, libro):
        self.libros.append(libro)

    # Método para eliminar un libro de la lista
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            
# Crear un autor
autor1 = Autor("Mario Benedetti", "Uruguayo" )

# Agregar libros
autor1.agregar_libro("El amor, las mujeres y la vida")
autor1.agregar_libro("La tregua")
autor1.agregar_libro("Poemas de amor")
autor1.agregar_libro("Quien de nosotros")

# Mostrar autor con libros
autor1.mostrar_autor()

# Eliminar un libro
autor1.eliminar_libro("El amor, las mujeres y la vida")

# Mostrar autor actualizado
autor1.mostrar_autor()

