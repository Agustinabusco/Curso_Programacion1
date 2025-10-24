Explicación del código paso a paso:

Primero creamos la excepción personalizada:
class NegativeNumberError(Exception):
- Hereda de Exception, lo que la convierte en una excepción propia.
- Sirve para controlar un error específico: números negativos.

    def __init__(self, mensaje=...):
        super().__init__(mensaje)
- Le pasamos un mensaje de error personalizado que se mostrará cuando ocurra la excepción.

Luego le pedimos un número al usuario:
numero = float(input("Ingresa un número..."))
- float() convierte el texto ingresado en un número decimal.
- Esto puede fallar si el usuario escribe letras → por eso tenemos un except ValueError.

Luego verificamos si el número es negativo:
if numero < 0:
    raise NegativeNumberError()
- raise dispara (lanza) la excepción personalizada.
- El programa saltará automáticamente al bloque except.

Si es válido calculamos la raíz cuadrada:
resultado = math.sqrt(numero)
print(...)
- math.sqrt() solo funciona con números ≥ 0.

Luego hacemos manejo de excepciones:
except NegativeNumberError as e:
    print(f"Error: {e}")
- Captura solo cuando el número es negativo.

except ValueError:
    print("Error: Debes ingresar un número válido.")
- Captura cuando el usuario ingresa algo que no es un número.