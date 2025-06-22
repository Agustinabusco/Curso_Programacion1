import string
import random

caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits

contraseña = ''.join(random.choices(caracteres, k=8))

print("Tu contraseña aleatoria es:", contraseña)
print("\n")