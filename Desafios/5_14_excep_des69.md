Explicación Detallada de Cada Parte
1. La Función procesar_lista(valores)
Creamos una función que toma una lista como argumento. Esta es una buena práctica porque hace que el código sea modular y reutilizable. Toda la lógica para manejar las operaciones y las excepciones se encuentra encapsulada dentro de esta función.

2. Bloque try
Este bloque contiene el código "seguro" que queremos ejecutar. Las operaciones que podrían generar un error se colocan aquí.

suma = sum(valores): La función sum() es muy útil para sumar todos los elementos de una lista. Sin embargo, si la lista contiene un valor que no es un número (como [1, '2', 3]), esta función no sabe cómo sumarlo y generará un TypeError.

primer_valor = valores[0]: Esta línea intenta obtener el primer elemento de la lista. Un IndexError ocurrirá si la lista está vacía, ya que no hay un elemento en la posición 0.

resultado_division = suma / primer_valor: Aquí intentamos realizar la división. Si el valor de primer_valor es 0, se activará un ZeroDivisionError.

3. Bloques except (Manejo de Errores)
Después del try, definimos una serie de bloques except para capturar y manejar cada tipo de error que anticipamos.

except ZeroDivisionError:: Este bloque se activa cuando el programa intenta dividir por cero. Proporciona un mensaje claro al usuario, indicando la causa del error.

except TypeError:: Este bloque captura el error si la lista contiene elementos de un tipo de dato incorrecto (por ejemplo, una cadena de texto en lugar de un número).

except IndexError:: Este bloque es específico para el error que ocurre cuando se intenta acceder a un índice de una lista que no existe (como lista[0] en una lista vacía).

except Exception as e:: Este es un bloque genérico de manejo de excepciones. Sirve como un "comodín" para cualquier otro error inesperado que no hayamos especificado. La variable e contiene los detalles del error, lo que es muy útil para la depuración. Es una buena práctica colocar los except específicos antes que el genérico.