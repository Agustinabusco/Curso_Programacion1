class Libro:
    # Constructor: inicializa los atributos privados
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo    # atributo privado
        self.__autor = autor      # atributo privado
        self.__isbn = isbn        # atributo privado

    # --- Getters (obtener el valor de un atributo) ---
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_isbn(self):
        return self.__isbn

    # --- Setters (modificar el valor de un atributo) ---
    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    def set_isbn(self, nuevo_isbn):
        self.__isbn = nuevo_isbn

    # Método opcional para mostrar la información
    def mostrar_info(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"ISBN: {self.__isbn}")

# --- Ejemplo de uso ---
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-84-376-0494-7")

libro1.mostrar_info()  # muestra los datos originales

libro1.set_titulo("El amor en los tiempos del cólera")  # modificamos el título

print("\nDespués de modificar:")
libro1.mostrar_info()
