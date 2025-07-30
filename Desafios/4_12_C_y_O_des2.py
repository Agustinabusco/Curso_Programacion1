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


# -------------------
# Ejemplo de uso real
# -------------------

# Crear libros
libro1 = Libro("La tregua", "Novela", "978-84-376-0494-7")
libro2 = Libro("El amor, la vida y las mujeres", "Novela", "978-84-8310-540-4")
libro3 = Libro("Quien de nosotros", "Novela", "978-9974-95-303-1")

# Crear autor
autor = Autor("Mario Benedetti", "Uruguayo")

# Relacionar libros con el autor
autor.agregar_libro(libro1)
autor.agregar_libro(libro2)
autor.agregar_libro(libro3)

# Mostrar información
print(autor)
autor.mostrar_libros()
