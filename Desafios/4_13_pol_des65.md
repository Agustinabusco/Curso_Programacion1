Explicaicón paso a paso del código:

Primeor creamos la clase base: figura: 
class Figura:
    def area(self):
        return 0
- Define un método area() general, pero no calcula nada todavía.
- Sirve como modelo para las subclases.
- Este método será sobrescrito (override) en las figuras específicas.

Creamos la subclase: criculo:
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
- Hereda de Figura.
- Tiene su propio atributo: radio.

    def area(self):
        return math.pi * (self.radio ** 2)
- Sobrescribe el método area() para calcular el área de un círculo con la fórmula:
- Área = 𝜋 × radio al cuadrado

Creamos la subclase: cuadrado:
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
- También hereda de Figura.
- Calcula el área con la fórmula del cuadrado:
- Área = lado al cuadrado

Demostramos el polimorfismo:
figuras = [Circulo(5), Cuadrado(4), Circulo(2.5), Cuadrado(10)]
- Tenemos una lista con distintos tipos de figuras, pero todas heredan de la misma clase base.

for figura in figuras:
    print(f"Área de {figura.__class__.__name__}: {figura.area():.2f}")
- Recorremos la lista y llamamos al mismo método area() en todas.
- Cada clase responde de manera distinta según su tipo → eso es polimorfismo.