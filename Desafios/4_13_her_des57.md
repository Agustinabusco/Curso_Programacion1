Explicación paso a paso

Herencia (class Poeta(Autor):)

Esto significa que Poeta hereda todos los atributos y métodos de la clase Autor.

No hace falta volver a definir nombre, nacionalidad o agregar_libro(), ya vienen incluidos.

super().__init__(...)

Llama al constructor de la clase padre (Autor) para inicializar correctamente nombre, nacionalidad y la lista de libros.

Así evitamos repetir código.

Nuevo atributo privado __tipo_poesia

Es propio de Poeta y no existe en Autor.

Lo manejamos también con @property y su setter.

Método mostrar_info()

Muestra toda la información del poeta, incluyendo el nuevo atributo y la cantidad de libros.

Herencia práctica

Un objeto Poeta puede usar todos los métodos del Autor: agregar_libro(), mostrar_libros(), etc.