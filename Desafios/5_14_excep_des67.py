try:
    # Solicitamos los números al usuario y los convertimos a enteros
    dividendo = int(input("Por favor, ingresa el dividendo: "))
    divisor = int(input("Ahora, ingresa el divisor: "))

    # Realizamos la división
    resultado = dividendo / divisor

    # Mostramos el resultado de la operación
    print(f"El resultado de la división de {dividendo} entre {divisor} es: {resultado}")

# 'except' para un error específico
except ZeroDivisionError:
    # Este bloque se ejecuta si el usuario intenta dividir por cero
    print("Error: No puedes dividir un número entre cero. Por favor, intenta de nuevo.")

# 'except' para otro tipo de error
except ValueError:
    # Este bloque se ejecuta si el usuario ingresa un valor que no es un número entero
    print("Error: Los valores ingresados deben ser números enteros. Por favor, intenta de nuevo.")