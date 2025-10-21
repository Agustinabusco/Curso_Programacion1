# --- Clase base Empleado ---
class Empleado:
    def __init__(self, nombre, id_empleado):
        self.__nombre = nombre
        self.__id_empleado = id_empleado

    @property
    def nombre(self):
        return self.__nombre

    @property
    def id_empleado(self):
        return self.__id_empleado

    def mostrar_info(self):
        print(f"Empleado: {self.__nombre} (ID: {self.__id_empleado})")


# --- Subclase Gerente (hereda de Empleado) ---
class Gerente(Empleado):
    def __init__(self, nombre, id_empleado, departamento):
        super().__init__(nombre, id_empleado)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Departamento: {self.__departamento}")


# --- Subclase Tecnico (hereda de Empleado) ---
class Tecnico(Empleado):
    def __init__(self, nombre, id_empleado, especialidad):
        super().__init__(nombre, id_empleado)
        self.__especialidad = especialidad

    @property
    def especialidad(self):
        return self.__especialidad

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Especialidad: {self.__especialidad}")


# --- Clase Voluntario (independiente) ---
class Voluntario:
    def __init__(self, nombre, actividad):
        self.__nombre = nombre
        self.__actividad = actividad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def actividad(self):
        return self.__actividad

    def mostrar_info(self):
        print(f"Voluntario: {self.__nombre}, Actividad: {self.__actividad}")


# --- Roles adicionales mediante composición ---
class Administrador:
    def __init__(self, sistema):
        self.__sistema = sistema

    @property
    def sistema(self):
        return self.__sistema

    def administrar_sistema(self):
        print(f"Administrando el sistema: {self.__sistema}")


class Mantenimiento:
    def __init__(self, area):
        self.__area = area

    @property
    def area(self):
        return self.__area

    def realizar_mantenimiento(self):
        print(f"Realizando mantenimiento en: {self.__area}")


# --- Herencia múltiple: GerenteAdministrador combina Gerente + Administrador ---
class GerenteAdministrador(Gerente, Administrador):
    def __init__(self, nombre, id_empleado, departamento, sistema):
        # Inicializamos Gerente
        Gerente.__init__(self, nombre, id_empleado, departamento)
        # Inicializamos Administrador
        Administrador.__init__(self, sistema)

    # Podemos sobrescribir mostrar_info para mostrar todo
    def mostrar_info(self):
        Gerente.mostrar_info(self)
        print(f"Sistema a cargo: {self.sistema}")


# --- Herencia múltiple: TecnicoMantenimiento combina Tecnico + Mantenimiento ---
class TecnicoMantenimiento(Tecnico, Mantenimiento):
    def __init__(self, nombre, id_empleado, especialidad, area):
        Tecnico.__init__(self, nombre, id_empleado, especialidad)
        Mantenimiento.__init__(self, area)

    def mostrar_info(self):
        Tecnico.mostrar_info(self)
        print(f"Área de mantenimiento: {self.area}")


# --- Ejemplo de uso ---
gerente_admin = GerenteAdministrador("Ana Pérez", 101, "Administración", "Sistema Bibliotecario")
tecnico_mant = TecnicoMantenimiento("Juan López", 202, "Redes y computación", "Sala de servidores")
voluntario1 = Voluntario("Lucía Gómez", "Atención al público")

# Mostramos información
print("=== Gerente Administrador ===")
gerente_admin.mostrar_info()
print("\n=== Técnico de Mantenimiento ===")
tecnico_mant.mostrar_info()
print("\n=== Voluntario ===")
voluntario1.mostrar_info()

# Usando métodos de roles
print("\n=== Acciones adicionales ===")
gerente_admin.administrar_sistema()
tecnico_mant.realizar_mantenimiento()
