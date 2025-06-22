from collections import Counter
import matplotlib.pyplot as plt
import string

texto = """
Hola! Soy Agustina, y estoy aprendiendo a programar con Python.
Python es un lenguaje muy usado para análisis de datos, inteligencia artificial y desarrollo web.
Es genial ver cómo usás módulos como random, string y collections para resolver desafíos.
"""

# Paso 1: Limpiar el texto (sacar puntuación, poner en minúsculas)
texto = texto.lower()  # todo en minúsculas
for signo in string.punctuation:
    texto = texto.replace(signo, "")  # eliminamos signos

# Paso 2: Separar en palabras
palabras = texto.split()

# Paso 3: Contar las palabras
contador = Counter(palabras)

# Paso 4: Obtener las 10 más comunes
palabras_comunes = contador.most_common(10)

# Mostrar en consola
print("Top 10 palabras más comunes:")
for palabra, frecuencia in palabras_comunes:
    print(f"{palabra}: {frecuencia}")

# Paso 5: Graficar con matplotlib
# Extraemos las palabras y las frecuencias por separado
etiquetas = [item[0] for item in palabras_comunes]
frecuencias = [item[1] for item in palabras_comunes]

# Crear el gráfico
plt.figure(figsize=(10, 5))
plt.bar(etiquetas, frecuencias, color="skyblue")
plt.title("Top 10 palabras más comunes")
plt.xlabel("Palabras")
plt.ylabel("Frecuencia")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
print("\n")