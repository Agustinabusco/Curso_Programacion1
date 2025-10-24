# Clase base
class Musico:
    def instrumento(self):
        return "No especificado"

# Subclase Guitarrista que sobrescribe el método instrumento
class Guitarrista(Musico):
    def instrumento(self):
        return "Toca la guitarra"

# Subclase Baterista que sobrescribe el método instrumento
class Baterista(Musico):
    def instrumento(self):
        return "Toca la batería"


# Demostración del polimorfismo
def mostrar_instrumento(musico):
    print(musico.instrumento())


# Crear instancias
g = Guitarrista()
b = Baterista()

# Uso del polimorfismo
mostrar_instrumento(g)
mostrar_instrumento(b)
