El escenario será así:
Cada Personaje tiene un nombre, una clase (como mago, guerrero), vida y un arma, cada Arma tiene un nombre y un daño y podemos atacar con un personaje a otro, y esto reducirá la vida del personaje objetivo.
Estrategia: 
Creamos dos clases:
- Arma: encapsula los atributos de un arma (nombre y daño).
- Personaje: encapsula un personaje, incluyendo su arma, nombre, tipo y vida.
Esto nos permite cambiar o crear nuevas armas fácilmente y agregar nuevos tipos de personajes sin cambiar toda la lógica.
Explicación del código:
- Clase Arma: representa un arma, guarda el nombre y cuánto daño hace y tiene un método __str__ para mostrarlo como texto amigable.
- Clase Personaje: representa un personaje jugable, tiene nombre, tipo (mago, guerrero…), vida y un arma, el método atacar() le quita vida al enemigo según el daño del arma y también tiene __str__ para imprimirlo de forma clara.
- Objetos: Creamos armas y personajes usando las clases y cada personaje puede interactuar con otro a través del método atacar().

Es bueno hacer este desafío con usando TAD, porque cada clase representa un TAD: Arma y Personaje y está bien separado, si mañana agregamos un nuevo tipo de arma (como "Arco") o habilidad, solo agregamos una clase o un atributo nuevo.