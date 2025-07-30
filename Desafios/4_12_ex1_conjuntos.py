class Numero:
    def __init__(self, valor):
        self.valor = valor

    def es_natural(self):
        return isinstance(self.valor, int) and self.valor > 0

    def es_entero(self):
        return isinstance(self.valor, int)

    def es_racional(self):
        return isinstance(self.valor, float) or self.es_entero()

    def mostrar_clases(self):
        print("Natural:", self.es_natural())
        print("Entero:", self.es_entero())
        print("Racional:", self.es_racional())

n = Numero(5)
n.mostrar_clases()
