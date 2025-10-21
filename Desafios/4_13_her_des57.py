class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []  # lista privada de libros

    # --- Propiedades ---
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

    # --- Métodos ---
    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def cantidad_libros(self):
        return len(self.__libros)

    def mostrar_libros(self):
        print(f"\nLibros escritos por {self.__nombre}:")
        if not self.__libros:
            print("  (No hay libros registrados)")
        else:
            for libro in self.__libros:
                print(f"  - {libro.get_titulo()} (ISBN: {libro.get_isbn()})")


# --- CLASE HIJA: Poeta ---
class Poeta(Autor):
    def __init__(self, nombre, nacionalidad, tipo_poesia):
        # Llamamos al constructor de la clase padre (Autor)
        super().__init__(nombre, nacionalidad)
        # Agregamos el nuevo atributo propio de Poeta
        self.__tipo_poesia = tipo_poesia

    # --- Getter y Setter con @property ---
    @property
    def tipo_poesia(self):
        return self.__tipo_poesia

    @tipo_poesia.setter
    def tipo_poesia(self, nuevo_tipo):
        self.__tipo_poesia = nuevo_tipo

    # --- Método adicional ---
    def mostrar_info(self):
        print(f"Poeta: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Tipo de poesía: {self.__tipo_poesia}")
        print(f"Libros publicados: {self.cantidad_libros()}")


# --- Clase Libro para completar el ejemplo ---
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


# --- Ejemplo de uso ---
poeta1 = Poeta("Pablo Neruda", "Chilena", "Poesía lírica")

libro1 = Libro("Veinte poemas de amor", poeta1.nombre, "978-84-376-1234-5")
libro2 = Libro("Cien sonetos de amor", poeta1.nombre, "978-84-376-5678-9")

poeta1.agregar_libro(libro1)
poeta1.agregar_libro(libro2)

poeta1.mostrar_info()
poeta1.mostrar_libros()
