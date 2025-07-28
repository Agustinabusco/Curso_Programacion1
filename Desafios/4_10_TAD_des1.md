### Desafío 1: Sistemas con Múltiples Entidades Interconectadas
Imagina un sistema de gestión de biblioteca que maneja libros, usuarios, préstamos y multas. Usar TADs separados para cada uno de estos elementos podría complicar la interacción y gestión de relaciones entre ellos.

Primeor que nada, ¿Qué estamos simulando?
Estamos representando una situación básica en una biblioteca: Un usario (agustina ej) toma prestado un libro (El principito) y luego lo devuelve. Este ejemplo usa lo mínimo necesario para que se entienda cómo interactúan los elementos más importantes: el libro, el usuario y el registro de préstamo.
En el paso 1: Crear los datos del sistema, cuando escribímos en el código: libro = {"titulo": "El Principito", "disponible": True}
usuario = {"nombre": "Agustina", "prestamos": []}
Lo que hacemos en esta parte es que se crea un diccionario llamado libro, tiene dos datos: título, que es el nombre del libro y disponible que indica si el libro está libre para ser prestado (Es True al principio) Luego se crea un diccionario llamado: usuario,también tiene dos datos: nombre: es el nombre de la persona que va a tomar prestado el libro y prestamom: es una lista vacía, donde se van a guardar los libros que tiene el préstamo.
Este es un modelo siempre pero muy útil para ver cómo se pueden conectar datos usando estructuras básicas de Python.
En el paso 2: Prestar el libro, en esta parte del código: if libro["disponible"]:
    libro["disponible"] = False
    usuario["prestamos"].append(libro["titulo"])
    print("Libro prestado.")
Primero se pregunta: ¿el libro está disponible? con if libro ["disponible"]: evalúa si el valor es True. 
Si está disponible: se marca como no disponible: libro["disponible"] = False se agrega el nombre del libro a la lista de préstamos del usuario: usuario["prestamos"].append(libro["titulo"]). Y se muestra un mensaje: "Libro prestado".
Este paso muestra cómo dos entidades separadas (el libro y el usuario) se conectan a través de una acción (el prestamo).
En el paso 3: Devolver el libro, en esta parte del código: libro["disponible"] = True
usuario["prestamos"].remove(libro["titulo"])
print("Libro devuelto.")
Al devolver el libro: se marca como disponible otra vez, se elimina el título del libro de la lista de préstamos del usuario y se muestra un mensaje: "Libro devuelto". 
Este paso revierte el préstamo y deja el distema como al inicio.

Que aprendemos con este ejemplo? 
1- Uso de diccionarios para presentar objetos simples como libros y usuarios
2- Listas para guardar préstamos (más adelante podrían ser varios) 
3- Condicionales (if) para decidir si una acción se puede hacer o no
4- Simulación de una relación entre objetos: el libro se conecta con el usuaio a través del préstamo.
¿Y si éste ´codigo quiere amplearse? Este mismo código podría crecer facilmente para: manejar varios libros, tener mñas suuarios, agregar fechas y multas, o separar todo en funciones o clases.
Pero para empezar, este ejemplo es ideal porque: es corto y fácil de leer, tiene todas las ideas importantes: objetos, estados relaciones y acciones, y te permite explicarlo paso por paso sin confundirte.