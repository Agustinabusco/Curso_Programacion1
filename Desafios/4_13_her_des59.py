# --- Clase base ---
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    # --- Getters ---
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_isbn(self):
        return self.__isbn

    # --- Método para mostrar info ---
    def mostrar_info(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"ISBN: {self.__isbn}")


# --- Subclase: LibroDigital ---
class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo):
        super().__init__(titulo, autor, isbn)  # inicializamos atributos de Libro
        self.__formato = formato
        self.__tamaño_archivo = tamaño_archivo  # en MB

    # --- Getters y Setters ---
    @property
    def formato(self):
        return self.__formato

    @formato.setter
    def formato(self, nuevo_formato):
        self.__formato = nuevo_formato

    @property
    def tamaño_archivo(self):
        return self.__tamaño_archivo

    @tamaño_archivo.setter
    def tamaño_archivo(self, nuevo_tamaño):
        self.__tamaño_archivo = nuevo_tamaño

    # --- Método sobrescrito para mostrar info adicional ---
    def mostrar_info(self):
        super().mostrar_info()  # llamamos al método de la clase base
        print(f"Formato: {self.__formato}")
        print(f"Tamaño del archivo: {self.__tamaño_archivo} MB")


# --- Subclase: EBook ---
class EBook(LibroDigital):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo, enlace_descarga):
        super().__init__(titulo, autor, isbn, formato, tamaño_archivo)
        self.__enlace_descarga = enlace_descarga

    @property
    def enlace_descarga(self):
        return self.__enlace_descarga

    @enlace_descarga.setter
    def enlace_descarga(self, nuevo_enlace):
        self.__enlace_descarga = nuevo_enlace

    # --- Sobrescribimos mostrar_info para incluir enlace de descarga ---
    def mostrar_info(self):
        super().mostrar_info()  # mostramos información de LibroDigital
        print(f"Enlace de descarga: {self.__enlace_descarga}")


# --- Ejemplo de uso ---
ebook1 = EBook(
    "Aprendiendo Python",
    "Agustina Giménez",
    "978-84-123456-7-8",
    "PDF",
    5.6,
    "https://descargas.ejemplo.com/aprendiendo-python"
)

ebook1.mostrar_info()
