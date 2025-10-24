# Clase base Libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"


# Subclase LibroEspecializado que hereda de Libro
class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel):
        # Llamamos al constructor de la clase padre
        super().__init__(titulo, autor)
        # Atributos adicionales
        self.campo_estudio = campo_estudio
        self.nivel = nivel

    # Método que sobrescribe el de la clase padre
    def mostrar_informacion(self):
        # Usamos super() para incluir la información básica del libro
        info_base = super().mostrar_informacion()
        return f"{info_base}, Campo de estudio: {self.campo_estudio}, Nivel: {self.nivel}"


# Instanciamos un objeto de LibroEspecializado
libro_esp = LibroEspecializado("Introducción a la Programación", "Ana Pérez", "Informática", "Básico")

# Mostramos la información completa
print(libro_esp.mostrar_informacion())
