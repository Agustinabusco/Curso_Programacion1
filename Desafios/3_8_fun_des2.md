### Desafío 2
Diseña una función que tome una cadena y devuelva la misma cadena, pero con el primer carácter de cada palabra en mayúsculas.

Explicación del código:

Para este desafío voy a utilizar el método .title(), que es una función que ya tiene Python. Lo que queremos lograr es que cada palabra de la frase, es decir su primer letra sea en mayúscula, y el resto en minúscula, en nuestro caso vamos a utulizar la frase: programar es divertido, entonces llamamos a la función def capitalizar_cadena(texto):
return texto.title(), luego escribimos nuestra frase, repito en nuestro caso (Programar es diverido), luegro resultado = capitalizar_cadena(frase) y finalmente su print para que nos muestre el resultado en pantalla, el print en este caso es: print("Resultado:", resultado), y debería darnos como resultado: Programar Es Divertido.
Como modo de concepto .title() funciona para recorrer toda la cadena y busca espacios, y cuandon encuentra una nueva palabra, pone la primer letra en mayúscula que e slo que buscamos en este desafío.