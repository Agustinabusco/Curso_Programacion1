Explicación del código paso a paso:

Primero creamos la clase abase libro:
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
- El método __init__ es el constructor, se ejecuta al crear el objeto.
- Guarda los atributos titulo y autor dentro del objeto (self).

    def mostrar_informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
- Este método devuelve un texto con los datos básicos del libro.

Creamos la subclase LibroEspecializado
class LibroEspecializado(Libro):
- Hereda de Libro, por eso tiene todos sus atributos y métodos.

    def __init__(self, titulo, autor, campo_estudio, nivel):
        super().__init__(titulo, autor)
        self.campo_estudio = campo_estudio
        self.nivel = nivel
- Agrega dos atributos nuevos:
- campo_estudio → por ejemplo, “Informática”, “Biología”.
- nivel → puede ser “Básico”, “Intermedio” o “Avanzado”.
- super().__init__(titulo, autor) llama al constructor de la clase padre para no repetir código.

Sobreescrimos el método mostrar_informacion:
def mostrar_informacion(self):
    info_base = super().mostrar_informacion()
    return f"{info_base}, Campo de estudio: {self.campo_estudio}, Nivel: {self.nivel}"
- Usamos super() para reutilizar el texto de Libro.
- Luego le agregamos los nuevos datos del LibroEspecializado.

Creamos e imprimimos un objeto:
libro_esp = LibroEspecializado("Introducción a la Programación", "Ana Pérez", "Informática", "Básico")
print(libro_esp.mostrar_informacion())
