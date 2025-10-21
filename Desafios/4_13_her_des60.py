# --- Clase base Escritor ---
class Escritor:
    def __init__(self, nombre, genero):
        self.__nombre = nombre
        self.__genero = genero
        self.__libros = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def genero(self):
        return self.__genero

    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def mostrar_libros(self):
        if not self.__libros:
            print(f"{self.__nombre} no tiene libros publicados.")
        else:
            print(f"Libros de {self.__nombre}:")
            for libro in self.__libros:
                print(f" - {libro}")


# --- Clase base Academico ---
class Academico:
    def __init__(self, universidad, especialidad):
        self.__universidad = universidad
        self.__especialidad = especialidad
        self.__articulos = []

    @property
    def universidad(self):
        return self.__universidad

    @property
    def especialidad(self):
        return self.__especialidad

    def agregar_articulo(self, articulo):
        self.__articulos.append(articulo)

    def mostrar_articulos(self):
        if not self.__articulos:
            print("No hay artículos académicos publicados.")
        else:
            print(f"Artículos en {self.__especialidad} de {self.__universidad}:")
            for art in self.__articulos:
                print(f" - {art}")


# --- Subclase EscritorAcademico ---
class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero, universidad, especialidad):
        # Inicializamos las clases base usando super() y la resolución de método (MRO)
        Escritor.__init__(self, nombre, genero)
        Academico.__init__(self, universidad, especialidad)

    # Método adicional
    def publicar_articulo_academico(self, titulo_articulo):
        self.agregar_articulo(titulo_articulo)
        print(f"Artículo académico '{titulo_articulo}' publicado por {self.nombre}.")


# --- Ejemplo de uso ---
escritor_acad = EscritorAcademico(
    "Ana Pérez",
    "Narrativa",
    "Universidad de Montevideo",
    "Literatura Comparada"
)

# Agregamos libros
escritor_acad.agregar_libro("Teoría de la narrativa moderna")
escritor_acad.agregar_libro("Estudios literarios avanzados")

# Publicamos artículos académicos
escritor_acad.publicar_articulo_academico("Análisis del realismo mágico")
escritor_acad.publicar_articulo_academico("Comparación de poéticas latinoamericanas")

# Mostramos información
escritor_acad.mostrar_libros()
escritor_acad.mostrar_articulos()
