# Programa para leer un archivo de texto con manejo de excepciones

archivo = None  # Declaramos la variable antes del try por seguridad

try:
    nombre_archivo = input("Ingresa el nombre del archivo a leer: ")

    # Intentamos abrir el archivo
    archivo = open(nombre_archivo, "r")

    # Leemos y mostramos el contenido
    contenido = archivo.read()
    print("\nContenido del archivo:")
    print(contenido)

except FileNotFoundError:
    print("Error: El archivo no existe o el nombre es incorrecto.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

finally:
    # Se ejecuta siempre, haya o no errores
    if archivo:
        archivo.close()
        print("\nEl archivo ha sido cerrado correctamente.")
