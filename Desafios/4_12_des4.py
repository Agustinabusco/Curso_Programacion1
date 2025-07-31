# Clase Libro
class Libro:
    def __init__(self, titulo, genero, isbn):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} ({self.genero}) - ISBN: {self.isbn}"


# Clase Autor mejorada
class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento="", biografia=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento  # Nuevo atributo
        self.biografia = biografia                # Nuevo atributo
        self.premios = []                         # Nuevo atributo
        self.libros = []                          # Ya existente

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_premio(self, premio):
        self.premios.append(premio)

    def mostrar_libros(self):
        print(f"Libros de {self.nombre}:")
        for libro in self.libros:
            print(" -", libro)

    def mostrar_premios(self):
        if self.premios:
            print(f"Premios de {self.nombre}:")
            for premio in self.premios:
                print(" -", premio)
        else:
            print(f"{self.nombre} no tiene premios registrados.")

    def cantidad_libros(self):
        return len(self.libros)

    def editar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad}) - Nacido: {self.fecha_nacimiento}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.autores = []

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
            print("Biografía:", autor.biografia)
            autor.mostrar_libros()
            autor.mostrar_premios()
            print(f"Total de libros: {autor.cantidad_libros()}")
            print()

# Crear libros
libro1 = Libro("La tregua", "Novela", "978-84-376-0494-7")
libro2 = Libro("El amor, la vida y las mujeres", "Novela", "978-84-8310-540-4")
libro3 = Libro("Quien de nosotros", "Novela", "978-9974-95-303-1")

# Crear autor con más información
autor1 = Autor("Mario Benedetti", "Uruguayo", "1920", "Fue un poeta, novelista y cuentista uruguayo.")
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)
autor1.agregar_libro(libro3)
autor1.agregar_premio("Premio Reina Sofía de Poesía Iberoamericana")
autor1.agregar_premio("Doctor Honoris Causa por la Universidad de Valladolid")

# Crear otro autor
libro4 = Libro("Cien años de soledad", "Realismo mágico", "978-84-376-0493-0")
libro5 = Libro("El coronel no tiene quien le escriba", "Novela", "978-84-8310-541-1")
autor2 = Autor("Gabriel García Márquez", "Colombiano", "1927", "Fue un escritor, periodista y premio Nobel.")
autor2.agregar_libro(libro4)
autor2.agregar_libro(libro5)
autor2.agregar_premio("Premio Nobel de Literatura")

# Crear biblioteca y agregar autores
biblioteca = Biblioteca()
biblioteca.agregar_autor(autor1)
biblioteca.agregar_autor(autor2)

# Mostrar toda la biblioteca
biblioteca.mostrar_biblioteca()
