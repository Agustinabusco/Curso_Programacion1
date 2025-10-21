Explicación paso a paso

Herencia múltiple

EscritorAcademico(Escritor, Academico) hereda atributos y métodos de dos clases base.

La resolución de métodos (MRO) en Python determina qué super() llamar si se usa.

En este caso usamos Escritor.__init__() y Academico.__init__() explícitamente para inicializar ambas clases.

Encapsulamiento

Los atributos de cada clase siguen privados (__nombre, __universidad, etc.).

Se accede a ellos mediante getters y métodos de la clase.

Método adicional publicar_articulo_academico()

Agrega un artículo académico a la lista de artículos del académico.

Usa el método de la clase base agregar_articulo() para mantener encapsulamiento.

Uso práctico

El objeto escritor_acad puede gestionar libros como Escritor y artículos académicos como Academico.

Todo queda centralizado en una sola instancia.