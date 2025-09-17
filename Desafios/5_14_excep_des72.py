# Lista de códigos de los productos 
inventario = ["A1", "B2", "C3", "D4"]

# Pedimos al usuario que ingrese un código
codigo = input("Ingresa el código de producto que buscas: ")

# Verificamos si el código está en la lista
if codigo in inventario:
    posicion = inventario.index(codigo)
    print(f"El código {codigo} está en la posición {posicion}.")
else:
    print("El código no se encontró en el inventario.")
