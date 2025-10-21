class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_isbn(self):
        return self.__isbn


class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []  # lista de objetos Libro

    # --- Propiedades con @property ---
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        self.__nacionalidad = nueva_nacionalidad

    # --- Métodos para manejar los libros ---
    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def cantidad_libros(self):
        """Devuelve la cantidad de libros escritos."""
        return len(self.__libros)

    def mostrar_libros(self):
        print(f"\nLibros escritos por {self.__nombre}:")
        if not self.__libros:
            print("  (No hay libros registrados)")
        else:
            for libro in self.__libros:
                print(f"  - {libro.get_titulo()} (ISBN: {libro.get_isbn()})")


# --- FUNCIÓN PEDIDA ---
def autor_con_mas_libros(lista_autores):
    """Recibe una lista de objetos Autor y devuelve el que tiene más libros."""
    if not lista_autores:
        return None  # si la lista está vacía

    # Comparamos usando el método cantidad_libros() (no accedemos al atributo privado)
    autor_max = lista_autores[0]
    for autor in lista_autores[1:]:
        if autor.cantidad_libros() > autor_max.cantidad_libros():
            autor_max = autor

    return autor_max


# --- Ejemplo de uso ---
autor1 = Autor("Gabriel García Márquez", "Colombiana")
autor2 = Autor("Isabel Allende", "Chilena")
autor3 = Autor("Julio Cortázar", "Argentina")

# Creamos algunos libros
libro1 = Libro("Cien años de soledad", autor1.nombre, "978-84-376-0494-7")
libro2 = Libro("El amor en los tiempos del cólera", autor1.nombre, "978-84-376-0495-4")
libro3 = Libro("La casa de los espíritus", autor2.nombre, "978-84-376-0496-1")

# Asociamos libros a los autores
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)
autor2.agregar_libro(libro3)

# Creamos la lista de autores
lista_autores = [autor1, autor2, autor3]

# Llamamos a la función
mejor_autor = autor_con_mas_libros(lista_autores)

# Mostramos resultado
print(f"El autor con más libros es: {mejor_autor.nombre} ({mejor_autor.cantidad_libros()} libros)")
