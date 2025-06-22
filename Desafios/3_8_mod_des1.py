import string  

texto = "¡Hola! Bienvenidos a nuestro procesador de texto 2025.\n¿Están listos?   "

letras = [c for c in texto if c in string.ascii_letters]
print("Cantidad de letras:", len(letras))

texto_sin_puntuacion = ''.join([c for c in texto if c not in string.punctuation])
print("Texto sin puntuación:", texto_sin_puntuacion)

import re
texto_sin_espacios_extra = re.sub(f"[{string.whitespace}]+", " ", texto_sin_puntuacion)
print("Texto con espacios normalizados:", texto_sin_espacios_extra.strip())
print("\n")