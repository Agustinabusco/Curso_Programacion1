class Usuario:
    def __init__(self, nombre, apellido, id_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = id_usuario

    def presentarse(self):
        return f"Soy {self.nombre} {self.apellido} (ID: {self.id_usuario})."


class Bibliotecario(Usuario):
    def __init__(self, nombre, apellido, id_usuario, seccion, anios_experiencia):
        # Reutiliza el constructor de Usuario
        super().__init__(nombre, apellido, id_usuario)
        self.seccion = seccion
        self.anios_experiencia = anios_experiencia

    def presentarse(self):
        # Sobrescribe el método para agregar la información del bibliotecario
        return (f"Soy {self.nombre} {self.apellido} (ID: {self.id_usuario}), "
                f"bibliotecario/a de la sección '{self.seccion}' con "
                f"{self.anios_experiencia} año(s) de experiencia.")


u = Usuario("Agustina", "Busco", 101)
print(u.presentarse())

b = Bibliotecario("Jorge", "el curioso", 102, "Historia", 3)
print(b.presentarse())
