### Desafío 5

Utiliza el módulo `os` para interactuar con el sistema operativo y añade características como guardar un archivo o leer un archivo existente en nuestro procesador de texto.

Solución del código: 

el objetivo de este desafío es usar el módulo os para:
- verificar si un archivo existe
leer un archivo existente
guardar texto en un archivo nuevo

Primero también dar un concepto de que es el módulo os: este es un módulo nativo de Python que permite trabajar con archivos, carpetas, rutas, variables del sistma y más.

Como vamos a probar este programa? 
1- correr el programa
2- elegis opcion 2, escribis texto y guardas en algo como texto1.text
3- después vas a opción 1 y lo lees y así quedaría un mini procesador de texto interactuando con el sistema operativo.

explicación en líneas: primero importamos el módulo os: import os, este módulo permite trabajr con archivos y rutas, por ejemplo, para ver si un archivo existe (os.path.exists), como paso dos, con: def mostrar_menu():
    print("\n=== Procesador de Texto ===")
    print("1. Leer archivo")
    print("2. Guardar nuevo archivo")
    print("3. Salir"), mostramos el menú, esta función lo que hace es imprimir en el menú cada vez que el programa empieza un ciclo.
    el paso3 utilizamos la funcion:  def leer_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print("\nContenido del archivo:")
            print(contenido)
    else:
        print("El archivo no existe."), esta es la función para leer un archivo, y que hace?: 

os.path.exists(nombre_archivo) verifica si el archivo existe, luego: with open(nombre_archivo, "r", encoding="utf-8") as archivo: abre el archivo en modo lectura (r = read)
despues, utilizamos: enconding="utf-8: asegura que los acentos y símbolos se lean correctamente, luego usamos: archivo.read(): esto lee todo el contenido y lo guarda en la avriable contenido y finalmente usamos los prints para que nos muestre el resultado en pantalla, y si no exise, nos muestra un mensaje de error.

en el paso 4: función para guardar un nuevo archivo: def guardar_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
    print("Archivo guardado correctamente."): lo que hacemos acá es con open(...,"w") abrimos el archivo en modo escritura (w = write), si el archivo existe, lo sobreescribe, si no existe, lo crea, y con: archivo.write(contenido) escribe el texto que pusimos en contenido.

luego en el paso 5: bucle principal del programa: while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-3): "), con while true: lo que hacemos es un bucle infinito que sigue mostrandoel menú hasat que elijas salis (opción 3)

Luego en el paso 6: opción 1: leer archivo 
utilizamos:     if opcion == "1":
        nombre = input("Nombre del archivo a leer (con .txt): ")
        leer_archivo(nombre), con esto se pide el nombre de un archivo (por ejemplo texto1.text) y llama a la función leer_archvo.

en el paso 7: opción 2: guardar archivo, utilizamos:     elif opcion == "2":
        nombre = input("Nombre del archivo a guardar (con .txt): ")
        texto = input("Escribí el contenido del archivo:\n")
        guardar_archivo(nombre, texto), con esto basicamente lo que se pide es: el nombre del archvo a guardar y el texto que querés guardar y lo pasa a la función guardar_archivo.

        luego en el paso 8: opcion 3: salir del programa, utilizamos:     elif opcion == "3":
        print("Saliendo del procesador... ¡Chau!")
        break, con esto se sale del bucle while usando break y termina el programa.

        finalmente ne el paso 9 basicamente refeire a que cualquier otra opción da error, esto lo hacemos con:     else:
        print("Opción inválida. Intentá de nuevo."), por si el usuarioescribe algo como "8" o "hola", muestra un mensaje de error. 

