Primero pasamos la lista de productos: inventario = ["A101", "B202", "C303", "D404", "E505"]
Luego utilizamos un input para que el usuario pueda ingresar a buscar la posición del producto que esté buscando en esa lista y lo guardamos en la variable codigo: codigo = input("Ingresa el código de producto que deseas buscar: ")
Como tercer paso usamos el condicional if payra verificar si el código que se busca se encuentra en el inventario (lista), se usa if para que si la condicion es verdadera, es decir, que se encuentrav el codigo del producto en la lista se va a poder ejecutar el bloque de abajo.
El cuarto paso es obtener la posición, esto lo hacemos con:posicion = inventario.index(codigo)
el .index(codigo) busca en que posición está ese elemento en la lista.
En el quinto paso usamos print para mostrar el resultado: print(f"El código {codigo} se encuentra en la posición {posicion}.")
Nos va  aostrar el mensaje usando un f-string, qu elo usamos justamente para poder combinar texto y variables.
Finalmente en el paso 6 usamos un else para que si la ondición del if no se cumple, es decir, no se encuentra un elemento en la lista se muestre el mensaje de que no se encuentra lo que busca en esa lista: else:
    print("El código no se ha encontrado en el inventario.")
Fin del código.