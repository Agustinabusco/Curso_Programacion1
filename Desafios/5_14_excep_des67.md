Egxplicación del Código
1. try: "Intentar" una Operación
El bloque try es el corazón de nuestro manejo de excepciones. Contiene el código que podría fallar durante su ejecución.

dividendo = int(input("...")): Esta línea le pide al usuario que ingrese un valor y luego intenta convertirlo a un número entero usando la función int(). Si el usuario, en lugar de un número, ingresa una letra o una palabra (por ejemplo, "hola"), la conversión falla y Python lanza una excepción del tipo ValueError.

divisor = int(input("...")): Es la misma lógica que la línea anterior, pero para el divisor.

resultado = dividendo / divisor: Aquí es donde ocurre la división. Si el valor de la variable divisor es 0, Python no puede realizar la operación matemáticamente y, en ese momento, lanza una excepción del tipo ZeroDivisionError.

print(...): Si todo el código dentro del bloque try se ejecuta sin ningún problema, esta línea mostrará el resultado al usuario.

2. except ZeroDivisionError: Manejando la División por Cero
Este bloque solo se activa si la excepción específica ZeroDivisionError ocurre en el bloque try.

except ZeroDivisionError:: Esta línea actúa como un "filtro". Si el error es una división por cero, el programa salta inmediatamente a este bloque, ignorando el resto del código en el try.

print("Error: No puedes dividir un número entre cero..."): Dentro de este bloque, le proporcionamos un mensaje claro al usuario, explicándole qué salió mal. En lugar de que el programa termine abruptamente con un error, le damos una respuesta útil.

3. except ValueError: Manejando Datos No Numéricos
Similar al anterior, este bloque se activa si la excepción es de tipo ValueError.

except ValueError:: Este "filtro" captura el error que ocurre cuando la función int() no puede convertir la entrada del usuario a un número.

print("Error: Los valores ingresados deben ser números enteros..."): Aquí le informamos al usuario que su entrada no era válida y que debe ingresar solo números.

El uso de múltiples bloques except te permite manejar diferentes tipos de errores de manera individual, lo que hace que tu código sea más preciso y que los mensajes para el usuario sean más específicos y útiles.