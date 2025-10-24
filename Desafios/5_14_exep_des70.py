import math

# Excepción personalizada
class NegativeNumberError(Exception):
    def __init__(self, mensaje="No se permiten números negativos para calcular raíces cuadradas."):
        super().__init__(mensaje)

# Programa que maneja la excepción
try:
    numero = float(input("Ingresa un número para calcular su raíz cuadrada: "))

    if numero < 0:
        raise NegativeNumberError()

    resultado = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {resultado:.2f}")

except NegativeNumberError as e:
    print(f"Error: {e}")

except ValueError:
    print("Error: Debes ingresar un número válido.")
