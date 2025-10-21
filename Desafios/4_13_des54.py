class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []  # lista de libros del autor

    # --- Getter y Setter para 'nombre' ---
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # --- Getter y Setter para 'nacionalidad' ---
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        self.__nacionalidad = nueva_nacionalidad

    # --- Método para agregar libros ---
    def agregar_libro(self, libro):
        self.__libros.append(libro)

    # --- Método para mostrar los libros ---
    def mostrar_libros(self):
        print(f"Libros escritos por {self.__nombre}:")
        if len(self.__libros) == 0:
            print("  (No hay libros registrados)")
        else:
            for libro in self.__libros:
                print(f"  - {libro.get_titulo()} (ISBN: {libro.get_isbn()})")
