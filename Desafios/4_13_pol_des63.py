# Clase base Autor
class Autor:
    def biografia(self):
        return "Biografía genérica de un autor."

# Subclase Escritor que sobrescribe el método biografia
class Escritor(Autor):
    def biografia(self):
        return "Este escritor se especializa en novelas y cuentos."

# Instanciamos un objeto de Escritor
e = Escritor()

# Mostramos el método biografia sobrescrito
print("Biografía desde Escritor:")
print(e.biografia())

# Acceder al método de la clase Autor usando super()
print("\nBiografía desde Autor (accedida con super()):")
print(super(Escritor, e).biografia())
