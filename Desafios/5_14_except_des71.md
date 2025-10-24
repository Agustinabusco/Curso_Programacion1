Explicación del código paso a paso_

Primero declaramos una avriable para el archivo:
archivo = None
- Así podemos verificar luego si se llegó a abrir realmente.

Luego usamos un bloque: Try:
nombre_archivo = input("Ingresa el nombre del archivo a leer: ")
archivo = open(nombre_archivo, "r")
contenido = archivo.read()
- Pedimos al usuario el nombre del archivo.
- open(..., "r") lo abre en modo lectura.
- read() obtiene todo el contenido del archivo.

Excepción: archivo inexistente:
except FileNotFoundError:
    print("Error: El archivo no existe o el nombre es incorrecto.")
- Se ejecuta cuando el nombre del archivo está mal o no está en la carpeta.

Excepción genérica (cualquier otro error):
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

Bloque finally:
finally:
    if archivo:
        archivo.close()
        print("\nEl archivo ha sido cerrado correctamente.")
- Se ejecuta siempre
- Garantiza que el archivo se cierre aunque haya error