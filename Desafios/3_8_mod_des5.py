import os

def mostrar_menu():
    print("\n=== Procesador de Texto ===")
    print("1. Leer archivo")
    print("2. Guardar nuevo archivo")
    print("3. Salir")

def leer_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print("\nContenido del archivo:")
            print(contenido)
    else:
        print("El archivo no existe.")

def guardar_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
    print("Archivo guardado correctamente.")

# --- PROGRAMA PRINCIPAL ---
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        nombre = input("Nombre del archivo a leer (con .txt): ")
        leer_archivo(nombre)

    elif opcion == "2":
        nombre = input("Nombre del archivo a guardar (con .txt): ")
        texto = input("Escribí el contenido del archivo:\n")
        guardar_archivo(nombre, texto)

    elif opcion == "3":
        print("Saliendo del procesador... ¡Chau!")
        break

    else:
        print("Opción inválida. Intentá de nuevo.")
print("\n")