¿Qué es polimorfismo?
Que un mismo método o función se puede usar con diferentes tipos de objetos, y cada uno responde de forma diferente.

En este caso:
instrumento() existe en todas las clases, pero cada clase da su propia respuesta.

Explicación paso a paso del código:

Primero se crea la clase paadre: músico: 
class Musico:
    def instrumento(self):
        return "No especificado"
- Tiene un método llamado instrumento que devuelve un texto genérico.
- Esta clase sirve como base para los otros músicos.

Luego creamos la subclase: guitarrista:
class Guitarrista(Musico):
    def instrumento(self):
        return "Toca la guitarra"
- Hereda de Musico
- Sobrescribe el método instrumento → ahora devuelve un texto específico.

Luego creamos la otra subclase: baterista:
class Baterista(Musico):
    def instrumento(self):
        return "Toca la batería"
- Igual que la anterior, reemplaza el comportamiento de la clase padre.

Demostramos el polimorfismo:
def mostrar_instrumento(musico):
    print(musico.instrumento())
- Esta función recibe cualquier objeto que tenga el método instrumento.
- No importa si es Guitarrista o Baterista.

Posteriormente instanciamos los objetos:
g = Guitarrista()
b = Baterista()

La misma función se comporta diferente según el objeto
mostrar_instrumento(g)  # → "Toca la guitarra"
mostrar_instrumento(b)  # → "Toca la batería"
