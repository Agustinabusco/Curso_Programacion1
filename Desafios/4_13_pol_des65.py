import math

# Clase base
class Figura:
    def area(self):
        # Método genérico que luego será sobrescrito
        return 0

# Subclase Circulo que sobrescribe el método area
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

# Subclase Cuadrado que sobrescribe el método area
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


# Demostración del polimorfismo
figuras = [
    Circulo(5),
    Cuadrado(4),
    Circulo(2.5),
    Cuadrado(10)
]

# Recorremos la lista y mostramos el área de cada figura
for figura in figuras:
    print(f"Área de {figura.__class__.__name__}: {figura.area():.2f}")
