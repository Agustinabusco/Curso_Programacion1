def operaciones_lista(valores):
    try:
        # Intentamos convertir todo a números
        numeros = [float(x) for x in valores]

        # Suma
        suma = sum(numeros)

        # Promedio (puede dar ZeroDivisionError si la lista está vacía)
        promedio = suma / len(numeros)

        # División de los dos primeros (puede dar ZeroDivisionError)
        division = numeros[0] / numeros[1]

        print("Lista convertida:", numeros)
        print("Suma:", suma)
        print("Promedio:", promedio)
        print("División primer/par segundo:", division)

    except ZeroDivisionError:
        print("Error: Intentaste dividir entre cero.")
    except TypeError:
        print("Error: Algún valor no es del tipo correcto (ej. no se puede operar con cadenas).")
    except ValueError:
        print("Error: No se pudo convertir algún valor a número.")