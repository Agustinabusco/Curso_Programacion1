# TAD: Arma
class Arma:
    def __init__(self, nombre, danio):
        self.nombre = nombre       # nombre del arma, por ejemplo: "Espada"
        self.danio = danio         # cuánto daño hace, por ejemplo: 20

    def __str__(self):
        return f"{self.nombre} (Daño: {self.danio})"


# TAD: Personaje
class Personaje:
    def __init__(self, nombre, clase, vida, arma):
        self.nombre = nombre       # nombre del personaje, por ejemplo: "Aragorn"
        self.clase = clase         # tipo de personaje, como "guerrero", "mago"
        self.vida = vida           # puntos de vida, por ejemplo: 100
        self.arma = arma           # un objeto de la clase Arma

    def atacar(self, enemigo):
        print(f"{self.nombre} ataca a {enemigo.nombre} con {self.arma.nombre}")
        enemigo.vida -= self.arma.danio
        if enemigo.vida <= 0:
            enemigo.vida = 0
            print(f"{enemigo.nombre} ha sido derrotado.")
        else:
            print(f"{enemigo.nombre} ahora tiene {enemigo.vida} de vida.")

    def __str__(self):
        return f"{self.nombre} el {self.clase}, Vida: {self.vida}, Arma: {self.arma}"


# Creamos algunas armas
espada = Arma("Espada", 20)
varita = Arma("Varita Mágica", 15)

# Creamos personajes
guerrero = Personaje("Aragorn", "Guerrero", 100, espada)
mago = Personaje("Gandalf", "Mago", 80, varita)

# Mostramos a los personajes
print(guerrero)
print(mago)

# Simulamos un ataque
guerrero.atacar(mago)
