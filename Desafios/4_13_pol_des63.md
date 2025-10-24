Explicación paso a paso del código:

Primero creamos la clase autor:
class Autor:
    def biografia(self):
        return "Biografía genérica de un autor."
- Tiene un método biografia() que describe de forma general a cualquier autor.

Luego creamos la subclase escritor:
class Escritor(Autor):
    def biografia(self):
        return "Este escritor se especializa en novelas y cuentos."
- Hereda de Autor.
- Sobrescribe (override) el método biografia() con información más específica.

Luego creamos una instanica de cescritor:
e = Escritor()

Mostramos la bibliograía propia del escritor:
e.biografia()
- Se ejecuta el método sobrescrito de Escritor.

Accedemos también al  método original de autor:
super(Escritor, e).biografia()
- Super() permite llamar al método de la clase padre ignorando el override.
