Explicación paso a paso

Clase base Empleado

Atributos privados: __nombre, __id_empleado.

Métodos: mostrar_info().

Subclases Gerente y Tecnico

Heredan de Empleado.

Añaden atributos específicos (departamento, especialidad).

Sobrescriben mostrar_info() usando super().

Voluntario

Independiente de Empleado, con sus propios atributos.

Roles adicionales con composición

Clases Administrador y Mantenimiento representan funcionalidades adicionales.

Se agregan a empleados mediante herencia múltiple o composición interna.

Herencia múltiple

GerenteAdministrador hereda de Gerente y Administrador.

TecnicoMantenimiento hereda de Tecnico y Mantenimiento.

Se inicializan ambos padres explícitamente (ClasePadre.__init__) para asegurar que todos los atributos queden bien.

Encapsulamiento

Todos los atributos siguen privados (__atributo) y solo se accede mediante métodos o propiedades.