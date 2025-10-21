Clase base Libro

Atributos privados: __titulo, __autor, __isbn.

Método mostrar_info() muestra los datos básicos.

Subclase LibroDigital

Hereda de Libro.

Añade atributos privados: __formato (PDF, EPUB, etc.) y __tamaño_archivo (MB).

Usa @property para getters y setters.

Sobrescribe mostrar_info() para añadir la información digital, pero llama a super().mostrar_info() para no repetir el código de Libro.

Subclase EBook

Hereda de LibroDigital.

Añade atributo privado __enlace_descarga.

Sobrescribe mostrar_info() para incluir enlace de descarga junto con toda la info heredada.

Encapsulamiento

Todos los atributos siguen privados (__atributo) y solo se acceden mediante getters/setters.

Esto mantiene seguridad y coherencia del diseño.

Herencia de niveles

EBook → LibroDigital → Libro.

Cada nivel añade información específica y puede sobrescribir métodos.