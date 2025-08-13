Explicación del código: 
1) class Usuario:
    def __init__(self, nombre, apellido, id_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = id_usuario
      self.id_usuario = id_usuario
-class Usuario:
Declara una clase llamada Usuario.
¿Por qué así? Es la clase base: representa cualquier usuario, no solo bibliotecarios.
-def __init__
Es el constructor. Se ejecuta automáticamente cuando creo un nuevo Usuario.
Recibe nombre, apellido e id_usuario y los guarda en self (atributos del objeto).
¿Por qué usar self? Es la forma en Python de decir “este atributo pertenece a este objeto en particular”.

2)     def presentarse(self):
        return f"Soy {self.nombre} {self.apellido} (ID: {self.id_usuario})."
-def presentarse(self):
Método para mostrar una presentación del usuario.
¿Por qué? Tener este método facilita mostrar la info sin repetir print() con concatenaciones largas.
-return f"...
Uso un f-string para insertar variables dentro del texto.
¿Por qué f-strings? Son más claros y rápidos que usar + para unir cadenas.

3) class Bibliotecario(Usuario):
-(Usuario)
Significa que hereda de Usuario.
¿Por qué herencia? Así aprovecho lo que ya tiene Usuario (nombre, apellido, id) sin repetir código.

4)     def __init__(self, nombre, apellido, id_usuario, seccion, anios_experiencia):
        # Reutiliza el constructor de Usuario
        super().__init__(nombre, apellido, id_usuario)
        self.seccion = seccion
        self.anios_experiencia = anios_experiencia
-super().__init__()
Llama al constructor de la clase padre (Usuario) para evitar duplicar la asignación de nombre, apellido e id_usuario.
¿Por qué super()? Es la forma limpia y clara de reutilizar el constructor de la clase base.
-self.seccion y self.anios_experiencia
Son atributos propios de Bibliotecario.
¿Por qué agregarlos aquí? Porque no todos los Usuario tienen sección o experiencia; solo los bibliotecarios.

5)     def presentarse(self):
        # Sobrescribe el método para agregar la info del bibliotecario
        return (f"Soy {self.nombre} {self.apellido} (ID: {self.id_usuario}), "
                f"bibliotecario/a de la sección '{self.seccion}' con "
                f"{self.anios_experiencia} año(s) de experiencia.")
-Sobrescritura de método: Este presentarse reemplaza al de Usuario cuando el objeto es un Bibliotecario.
¿Por qué sobrescribir? Para agregar la información extra (sección y experiencia) sin modificar el comportamiento de los Usuario comunes.
-F-strings con varias líneas
¿Por qué así? Para que el texto sea más fácil de leer y mantener, en lugar de escribirlo todo en una sola línea gigante.

6) u = Usuario("Ana", "Pérez", 101)
print(u.presentarse())

b = Bibliotecario("Luis", "Gómez", 102, "Historia", 3)
print(b.presentarse())
-u = Usuario(...)
Creo un objeto Usuario con nombre, apellido e ID.
-print(u.presentarse())
Llama al método presentarse de Usuario.
-b = Bibliotecario(...)
Creo un Bibliotecario con los datos de usuario más sección y experiencia.
-print(b.presentarse())
Llama al método sobrescrito de Bibliotecario

Por qué elegí esta forma:
-Simpleza: eliminé métodos extra del ejemplo anterior para que el código sea más corto y fácil de leer.
-Eficiencia: la herencia evita duplicar código, y super() es más limpio que volver a escribir asignaciones.
-Claridad: los nombres de métodos y variables describen lo que hacen (presentarse, anios_experiencia).
-F-strings: facilitan la lectura del código y la construcción de textos.


