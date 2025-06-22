### Desafío 1

Investiga y utiliza al menos tres funciones del módulo `string` que puedan ser útiles para mejorar nuestro procesador de texto.

Explicación del código:

Primero que nada saber ques es un módulo string, éste, e sun módulo de Python que contiene funciones y constantes útiles para trabajar con texto: letras, números, símbolos, etc.
No se usa para remplazar funciones como .upper() o .lower(), sino que te da herramientas extra para manipular texto.

En este caso estas son las funciones/constantes que vamos a utilizar.
1- string.ascii_letters: esta contiene todas las letras del alfabeto (mayúsculas + minúsculas), y es útil para validar si un carácter es una letra.
2- string.punctuation: contiene todos los signos de puntuacion: (!"#$%&'()*+,-./:;<=>?@[\]^_{|}~), y es útil para eliminar o contar signos.
3- string.whitespace: contiene todos los espacios en blanco (espacio; tab; salto de línea) y es útil para limpiar texto.

Ahora para comenzar a explicar nuestro código, primero importamos el módulo string.
Luego en la siguiente línea simulamos un texto que escribimos en un procesador de texto, entonces: texto = "¡Hola! Bienvenidos a nuestro procesador de texto 2025.\n¿Están listos?   "

El siguiente paso, el 1, utilizando string.ascii_letters, lo que hacemos es contar cuántas letras hay, entonces: letras = [c for c in texto if c in string.ascii_letters] y luego su print para que nos muestre el resultado en pantalla más tade: print("Cantidad de letras:", len (letras)).

El paso 2, donde utilizamos: string.punctuación, lo vamos a utilizar para eliminar los signos de puntuación, entonces: texto_sin_puntuacion = .join([c for c in texto if c not in string.punctuation]) y finalmente su print("Texto sin puntuación:", texto_sin_puntuacion)

Luego en el paso 3 utulizamos: string.whitespace, entonces, acá vamos a remplazar espacios en blanco por un único espacio, comenzamos con: import re, en la siguiete línea: texto_sin_espacios_extra = re.sub(f"[{string.whitespace}]+", " ", texto_sin_puntuacion) y finalmente el print("Texto con espacios normalizados:", texto_sin_espacios_extra.strip())

Para redondear, utilizamos:
1- ascii_letters: para recorrer el texto y contar cuántos caracteres son letras del alfabeto (A-Z,a-z)

2- punctuation: eliminamos todos los signos (como ¡, ., ?, etc.) comparando carácter por carácter.

3- whitespace + módulo re: con ayuda del módulo re (expreciones regulares), remplazamos cualquier espacio en blanco (salto de línea, tabulación, espacios dobles) por un solo espaci0 (" ").