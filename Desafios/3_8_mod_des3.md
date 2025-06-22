### Desafío 3

Crea un módulo personalizado que contenga funciones para cambiar el formato del texto (por ejemplo, a negrita, itálica, etc.) e impórtalo en un nuevo programa.

Expliación del código:

El priemr paso es crear el modulo, lo vamos a hacer con primero con el archivo: formato_texto.py, estre archivo tendrá funciones de formato, vamos a simular: negrita, itálica y subrayado, usando código estilo markdown. este  va a ser nueystro módulo personalizado y lo vamos a guardar en un archivo .py

# Formato_texto.py

def en_negrita(texto):
    return f"**{texto}**"  # estilo Markdown

def en_italica(texto):
    return f"*{texto}*"

def subrayado(texto):
    return f"__{texto}__"


el paso 2 es usar el módulo desde otro archivo, archivo: main.py, este archivo será el programa principal que importa el módulo.

# main.py

import formato_texto  # Importamos nuestro propio módulo

texto = "Hola Agustina"

# Usamos las funciones del módulo
print("Negrita:", Formato_texto.en_negrita(texto))
print("Itálica:", Formato_texto.en_italica(texto))
print("Subrayado:", Formato_texto.subrayado(texto))

¿Cómo se concectan? Formato_texto.py y main.py:
- ambos archivos tienen que estar en la misma carpeta
- Python va a buscar: formato_texto.py como si feura un módulo más.
