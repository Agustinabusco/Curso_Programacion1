class Operacion:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def resultado(self):
        raise NotImplementedError("Este método debe ser sobrescrito en la subclase")
raise NotImplementedError(...) sirve para marcar un método como “abstracto” en la clase base.
Es decir, cuando escribimos una clase padre que va a ser heredada, a veces no queremos darle una implementación concreta a un método, porque cada subclase lo va a implementar de forma distinta. y si alguien intenta usar directamente ese método sin sobrescribirlo en una subclase, se lanza un error inmediatamente (NotImplementedError) para avisar que ese método debe ser implementado en la clase hija.

En este caso significa: "Operacion" no sabe cómo calcular el resultado, así que le dice a las subclases: “Ustedes deben decirme qué hacer aquí. Si intentan usarme sin definirlo, les voy a tirar un error.”

En esta parte del codigo con:
- __init__: guarda los números en el objeto (self.num1, self.num2).
-resultado: está declarado pero no implementado. El raise NotImplementedError obliga a las subclases a dar su propia versión. Si alguien llamara Operacion(5,3).resultado(), se lanza ese error.

Primero se crean las subclase que sobreescriben resultado:
class Suma(Operacion):
    def resultado(self):
        return self.num1 + self.num2
-Hereda de Operacion, por lo que ya tiene el __init__ y no hace falta reescribirlo.
-Sobrescribe resultado para devolver la suma.

En esta parte:
class Multiplicacion(Operacion):
    def resultado(self):
        return self.num1 * self.num2
Igual que arriba, pero resultado devuelve la multiplicación.

Luego aplicamos el polimorfismo a la practica, es decir en un ejercicio: 
operaciones = [
    Suma(5, 3),
    Multiplicacion(5, 3)
]

for operacion in operaciones:
    print(f"Resultado: {operacion.resultado()}")
-operaciones es una lista con objetos de tipos distintos (Suma y Multiplicacion) que comparten el método resultado().
-En el for, Python hace despacho dinámico:
-Toma el primer objeto: Suma(5,3).
-Llama resultado() → busca primero en Suma (encuentra la versión que suma) → calcula 5 + 3 → devuelve 8.
-Imprime: Resultado: 8.

-Toma el segundo objeto: Multiplicacion(5,3).
-Llama resultado() → busca primero en Multiplicacion (encuentra la versión que multiplica) → calcula 5 * 3 → devuelve 15.
-Imprime: Resultado: 15.






