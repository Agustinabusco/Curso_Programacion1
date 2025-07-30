# TAD: Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Stock: {self.stock}"


# TAD: Empleado
class Empleado:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def __str__(self):
        return f"{self.nombre} ({self.rol})"


# TAD: Tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []    # Lista de objetos Producto
        self.empleados = []    # Lista de objetos Empleado

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_inventario(self):
        print(f"Inventario de {self.nombre}:")
        for producto in self.productos:
            print(" -", producto)

    def mostrar_empleados(self):
        print(f"Empleados en {self.nombre}:")
        for empleado in self.empleados:
            print(" -", empleado)


# TAD: Cadena de tiendas
class CadenaTiendas:
    def __init__(self):
        self.tiendas = []  # Lista de objetos Tienda

    def agregar_tienda(self, tienda):
        self.tiendas.append(tienda)

    def mostrar_tiendas(self):
        for tienda in self.tiendas:
            print(f"Tienda: {tienda.nombre}")
            tienda.mostrar_inventario()
            tienda.mostrar_empleados()
            print()

# Crear productos
p1 = Producto("Pan", 40, 100)
p2 = Producto("Leche", 60, 50)

# Crear empleados
e1 = Empleado("Lucía", "Cajera")
e2 = Empleado("Carlos", "Repositor")

# Crear una tienda y agregar productos y empleados
tienda1 = Tienda("Tienda Centro")
tienda1.agregar_producto(p1)
tienda1.agregar_producto(p2)
tienda1.agregar_empleado(e1)
tienda1.agregar_empleado(e2)

# Crear otra tienda
tienda2 = Tienda("Tienda Barrio")
tienda2.agregar_producto(Producto("Queso", 120, 20))
tienda2.agregar_empleado(Empleado("María", "Encargada"))

# Crear la cadena de tiendas
cadena = CadenaTiendas()
cadena.agregar_tienda(tienda1)
cadena.agregar_tienda(tienda2)

# Mostrar toda la información
cadena.mostrar_tiendas()
