### Desafío 4

Utiliza el módulo `collections` para analizar un texto y generar estadísticas avanzadas, 
como las 10 palabras más comunes y su frecuencia. 
Extiende esto creando un gráfico de barras con matplotlib para visualizar la frecuencia de las palabras.

Solución del ejercicio: 

Para este desafío voy a utilizar: 
-collection.Counter, que cuenta fácilmente elementos repetidos es una lista (en este caso, palabras)
-matplotlib.pyplot, este sirve para hacer gráficos, como de barras o líenas.

lo primero qvamos a hacer es importar los tres módulos que vamos a utilizar para este desafío, entonces, from collections importCounter: 
- collections es un módulo de Python que tiene estructurasde datos más avanzadas
- counter es una de esas estructuras y sirve para contar cuántas veces aparece cada elemento en una lista.

Luego con import matplotlib.pyplot as plt
- matplolib.pyplot es un submódulo de la biblioteca matplotlib
- lo estamos importando con el alias plt, que e sla forma mas comun de hacerlo
- se usa para crear gráficos y visualizaciones (como gráficos de barras, líneas,tortas, etc).

Import string
este módlo tiene constantes útiles de texto, como:
- string.punctuation: todos los signos de puntuación (!?,.:;)
- string.ascii_lowercase: todas las letras minúsculas ( a a z)
- string.whitespace: todos los espacios (\n, \t, etc)
Lo usamos para limpiar y analizar texto de froma mas controlada.

Luego utilizamos un texto de ejemplo para contar las palabras en el gráfico posteriormente también, luego en el paso 1 limpiamos el texto (sacar puntuación, poner minúsculas): esto lo hacemos con text.lower(), lo que hace esto es convertr todo el texto a minúsculas para que "Python" y "python" sean iguales, dentro de la línea, o mejor dicho el bloque, introducimos un bucle for con string.punctuation, este lo vamosa a usar para eliminar los signos como: ".", ",",, etc.
luego en el paso 2 utilizamos texto split() para separar el texto en palabras (por espacios) 
en el paso 3, con counter(palabras) lo utilizamos para que cuente cuantas veces aparececada palabra, en el paso 4, obtendremos las palabras mas comunes declarando la variable; palabras_comunes = contador.most_common(10), a su vez utilizamos most_common(10) para que nos saque las 10 palabras más frecuentes, luego utilizamos los prints para que nos muestre el resultado en pantalla: print("Top 10 palabras más comunes:")
for palabra, frecuencia in palabras_comunes:
    print(f"{palabra}: {frecuencia}")
    y finalmente en el paso 5 graficamos con matplotlib, con el que extraeremos las palabras y las ferecuencias por separado con: etiquetas = [item[0] for item in palabras_comunes]
frecuencias = [item[1] for item in palabras_comunes]
y finalmente usamos matpotlib.pyplot.bar() que nos muestra un gráfico de barras con las plabras y sus frecuencias. el paso final es crear el gráfico así: plt.figure(figsize=(10, 5))
plt.bar(etiquetas, frecuencias, color="skyblue")
plt.title("Top 10 palabras más comunes")
plt.xlabel("Palabras")
plt.ylabel("Frecuencia")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show().