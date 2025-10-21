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

    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    def set_isbn(self, nuevo_isbn):
        self.__isbn = nuevo_isbn

    def mostrar_info(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"ISBN: {self.__isbn}")


# --- NUEVA CLASE: Autor ---
class Autor:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = []  # lista vacía para guardar objetos Libro

    # Getter y setter del nombre
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Método para agregar un libro a la lista
    def agregar_libro(self, libro):
        self.__libros.append(libro)

    # Mostrar todos los libros del autor
    def mostrar_libros(self):
        print(f"Libros escritos por {self.__nombre}:")
        if len(self.__libros) == 0:
            print("  (No hay libros registrados)")
        else:
            for libro in self.__libros:
                print(f"  - {libro.get_titulo()} (ISBN: {libro.get_isbn()})")


# --- Ejemplo de uso ---
autor1 = Autor("Gabriel García Márquez")

libro1 = Libro("Cien años de soledad", autor1.get_nombre(), "978-84-376-0494-7")
libro2 = Libro("El amor en los tiempos del cólera", autor1.get_nombre(), "978-84-376-0495-4")

# Agregamos los libros al autor
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)

# Mostramos los libros del autor
autor1.mostrar_libros()
