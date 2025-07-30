En la primer parte del código:
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre        # Nombre del producto (Ej: "Pan")
        self.precio = precio        # Precio del producto (Ej: 40)
        self.stock = stock          # Cantidad en stock (Ej: 100)

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Stock: {self.stock}"
__init__(): es el constructor, se usa cuando creamos un producto: recibe nombre, precio y stock y los guarda como atributos del objeto. y __str__(): sirve para mostrar el producto de forma legible cuando se imprime, ej: pan - $40 - Stock: 100.
Luego en clase Empleado:
class Empleado:
    def __init__(self, nombre, rol):
        self.nombre = nombre        # Nombre del empleado
        self.rol = rol              # Rol que cumple (Ej: "Cajera")

    def __str__(self):
        return f"{self.nombre} ({self.rol})"
Lo que hace es representar a un trabajador de la tienda, tiene: un nombre, ej: Lucia y un rol, ej: cajera y con __str__(): lo muestra asi: Lucia (Cajera).
En clase Tienda:
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []         # Lista que guarda objetos Producto
        self.empleados = []         # Lista que guarda objetos Empleado
Lo que hace esta parte del código es representar una tienda individual, tiene: un nombre (ej: "Tienda Centro"). una lista de productos (producto) y una lista de empleados (empleados), usamos listas vacias para empezar. Luego con métodos vamos agregando objetos.
luego con Métodos de Tienda:
    def agregar_producto(self, producto):
        self.productos.append(producto)
Agrega un producto a la lista, el producto debe ser un objeto de la clase Producto.
Con:     def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
Agrega un empleado a la tienda, debe ser un objeto de la clase Empleado.
luego:     def mostrar_inventario(self):
        print(f"Inventario de {self.nombre}:")
        for producto in self.productos:
            print(" -", producto)
Imprime el nombre de la tienda y todos sus productos.
continuando con:     def mostrar_empleados(self):
        print(f"Empleados en {self.nombre}:")
        for empleado in self.empleados:
            print(" -", empleado)
Imprime el nombre de la tienda y todos los empleados que tiene.
Luego en: Clase CadenaTiendas: class CadenaTiendas:
    def __init__(self):
        self.tiendas = []       # Lista de objetos Tienda
Representa la cadena completa de tiendas, contiene una lista de objetos Tienda, por ejemplo: [tienda1, tienda2, tienda3].
Continuando con Métodos de CadenaTiendas:     def agregar_tienda(self, tienda):
        self.tiendas.append(tienda)
Agrega una tienda a la cadena, la tienda debe ser un objeto de la clase Tienda.
Continuando:     def mostrar_tiendas(self):
        for tienda in self.tiendas:
            print(f"Tienda: {tienda.nombre}")
            tienda.mostrar_inventario()
            tienda.mostrar_empleados()
            print()
Recorre todas las listas y llama a sus métodos para mostrar su inventario y empleados, es decir, muestra toda la red de tiendas.
Continuando con la ejecución del programa: # Crear productos
p1 = Producto("Pan", 40, 100)
p2 = Producto("Leche", 60, 50)
Creamos dos productos usando la clase Producto.
Con: # Crear empleados
e1 = Empleado("Lucía", "Cajera")
e2 = Empleado("Carlos", "Repositor")
Creamos empleados con nombre y rol.
Continuando: # Crear una tienda y agregar productos y empleados
tienda1 = Tienda("Tienda Centro")
tienda1.agregar_producto(p1)
tienda1.agregar_producto(p2)
tienda1.agregar_empleado(e1)
tienda1.agregar_empleado(e2)
Creamos la tienda principal y le agregamos: dos productos y dos empleados.
Luego en esta parte: # Crear otra tienda
tienda2 = Tienda("Tienda Barrio")
tienda2.agregar_producto(Producto("Queso", 120, 20))
tienda2.agregar_empleado(Empleado("María", "Encargada"))
Creamos otra tienda con un producto y un empleado.
Continuando: # Crear la cadena de tiendas
cadena = CadenaTiendas()
cadena.agregar_tienda(tienda1)
cadena.agregar_tienda(tienda2)
Creamos una cadena de tiendas que contiene a tienda1 y tienda2.
Finalmente con: # Mostrar toda la información
cadena.mostrar_tiendas()
Mostramos toda la información almacenada: cada tienda, su inventario y sus empleados.

CONCEPTOS IMPORTANTES
- TAD (Tipo Abstracto de Dato): cada clase (Producto, Empleado, Tienda, CadenaTiendas) representa un tipo abstracto con su comportamiento.
- Encapsulamiento: cada TAD tiene sus datos protegidos en una estructura clara.
- Estructuras anidadas: listas de objetos dentro de objetos. Por ejemplo: una Tienda contiene una lista de Producto y una CadenaTiendas contiene una lista de Tienda.