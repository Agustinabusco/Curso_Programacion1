# Clase Libro
class Libro:
    def __init__(self, titulo, genero, isbn):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} ({self.genero}) - ISBN: {self.isbn}"


# Clase Autor
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []  # Lista de objetos Libro

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        print(f"Libros de {self.nombre}:")
        for libro in self.libros:
            print(" -", libro)

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.autores = []  # Lista de objetos Autor

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def buscar_autor(self, nombre):
        for autor in self.autores:
            if autor.nombre.lower() == nombre.lower():
                return autor
        return None

    def mostrar_biblioteca(self):
        print("Biblioteca completa:")
        for autor in self.autores:
            print(autor)
            autor.mostrar_libros()
            print()

# Crear libros
libro1 = Libro("La tregua", "Novela", "978-84-376-0494-7")
libro2 = Libro("El amor, la vida y las mujeres", "Novela", "978-84-8310-540-4")
libro3 = Libro("Quien de nosotros", "Novela", "978-9974-95-303-1")

# Crear autor
autor1 = Autor("Mario Benedetti", "Uruguayo")

# Agregar libros al autor
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)
autor1.agregar_libro(libro3)

# Crear otro autor y libros
libro4 = Libro("Cien años de soledad", "Realismo mágico", "978-84-376-0493-0")
libro5 = Libro("El coronel no tiene quien le escriba", "Novela", "978-84-8310-541-1")

autor2 = Autor("Gabriel García Márquez", "Colombiano")
autor2.agregar_libro(libro4)
autor2.agregar_libro(libro5)

# Crear biblioteca y agregar autores
biblioteca = Biblioteca()
biblioteca.agregar_autor(autor1)
biblioteca.agregar_autor(autor2)

# Mostrar toda la biblioteca
biblioteca.mostrar_biblioteca()
