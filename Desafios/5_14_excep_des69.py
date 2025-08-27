def procesar_lista(valores):
    """
    Procesa una lista de valores, calcula la suma y realiza una división.
    Maneja excepciones para errores comunes.
    """
    try:
        # Bloque 1: 'try' - Se intenta realizar las operaciones
        print(f"La lista de valores es: {valores}")

        # Intentamos sumar todos los elementos de la lista
        # Si la lista contiene elementos no numéricos, 'sum()' lanzará un TypeError
        suma = sum(valores)
        print(f"La suma de los valores es: {suma}")

        # Intentamos dividir la suma por el primer elemento de la lista
        # Si el primer elemento es 0, se lanzará un ZeroDivisionError
        # Si la lista está vacía, se lanzará un IndexError
        primer_valor = valores[0]
        resultado_division = suma / primer_valor
        print(f"El resultado de la división (suma / primer valor) es: {resultado_division}")
        
    # Bloque 2: 'except' - Manejamos errores específicos
    except ZeroDivisionError:
        print("\n¡Error de división por cero! El primer valor de la lista es cero.")
    except TypeError:
        print("\n¡Error de tipo de dato! La lista contiene un valor que no es un número.")
    except IndexError:
        print("\n¡Error de índice! La lista está vacía.")
    except Exception as e:
        # Bloque para capturar cualquier otra excepción inesperada
        print(f"\n¡Ocurrió un error inesperado! Detalle del error: {e}")

# --- Ejemplos de uso ---
print("--- Caso 1: Todo correcto ---")
lista_correcta = [10, 20, 30]
procesar_lista(lista_correcta)

print("\n--- Caso 2: División por cero ---")
lista_cero = [0, 2, 4]
procesar_lista(lista_cero)

print("\n--- Caso 3: Error de tipo de dato ---")
lista_con_texto = [1, '2', 3]
procesar_lista(lista_con_texto)

print("\n--- Caso 4: Lista vacía ---")
lista_vacia = []
procesar_lista(lista_vacia)