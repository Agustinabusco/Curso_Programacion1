### Desafío 2

Utiliza el módulo `random` de Python para crear un programa que genere una contraseña aleatoria de 8 caracteres que incluya letras minúsculas, letras mayúsculas y números.

Explicación del código:

Prime que nada unos conceptos claves de lo que vamos a utilziar: 
Módulo string: Nos da listas de caracteres útiles:
- string.ascii_lowecase: todas las letras minúsculas(abcdefghijklmnopqrstuvwxyz)
-string.ascii_uppercase: todas las mayúsculas (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
- string.digits: todos los números del o al 0 (0123456789)

Módulo random: 
- random.choice(lista): elige 1 elemento al azar
- random.choices(lista, k=n): elige n elementos al azar
- random.shuffle(lista): mezcla una lista

A continuación vamos con el paso a paso de nuestro código:

En la primer línea: import string y import random, lo que hacemos es importar lso dos módulos necesarios, en el siguiente paso, juntamos todos los caracteres posibles: caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits, con caracteres = ..., lo que hacemos es crear un conjunto de todos los carácteres válidos (letras y números),
en el paso 2 elegimos 8 caracteres al azar, para esto, utilizamos: random.choices: contraseña = ''.join(random.choices(caracteres, k=8)), con random. choices lo que hcemos es elegir 8 caracters al azar de la lista y con .join lo que hacems es unir los 8 caracteres en una sola cadena (string) y finalmente utilizamos el proint para mostrar la contraseña aleatoria wue nos genere el programa. 