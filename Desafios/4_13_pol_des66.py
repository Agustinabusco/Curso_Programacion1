#Clase base
class Operacion:
 def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
    
def resultado(self):
 raise NotImplementedError("Este método debe ser sobre escrito en la subclase")
   
class Suma(Operacion):
   def resultado(self):
        return self.num1 + self.num2 


class Multiplicación(Operacion): 
 def resultado(self):
    return self.num1 * self.num2


operaciones = [
    Suma(5, 3),
    Multiplicación(5, 3)
]

for operacion in operaciones:
    print(f"Resultado: {operacion.resultado()}")
    
    
