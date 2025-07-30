Como estrategia: creamos una clase Libro con los atributos titulo, genero e ISNB, creamos una clase Autor con nombre, nacionalidad y una lista de libros que ha escrito, asi, un autor puede tener muchos libros, lo cual representa una relación de uno a muchos entre Autor y Libro.
Explicación del códiggo:
# Clase Libro
class Libro:
    def __init__(self, titulo, genero, isbn):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} ({self.genero}) - ISBN: {self.isbn}"
Esta parte del codigo lo que hace es crear un objeto Libro con: titulo: nombre del libro, genero: por ejemplo "novela", isbn: numero unico de identificacion y el metodo __str__() sirve para mostrar el libro como un texto amigable.
Continuando con:
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
Acá crea un objeto Autor con: nombre ("Mario Benedetti), nacionalidad: ("Uruguayo") una lista vacia de libros que se irá llenando, el metodo: agregar_libro(libro) agrega un objeto Libro a la lista del autor. mostrar_libros() imprime todos los libros que ese autor ha escrito.

¿Cual es la relacion entre autor y libro? que es una relación "uno a muchos", un autor puede escribir varios libros pero cada libro pertenece a un solo autor (en este caso) 