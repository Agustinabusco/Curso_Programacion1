### Desafío 6 : Verificación y Cálculo de Números Primos

Crea dos funciones y un `main` que te permita trabajar con números primos, un concepto matemático fundamental. En este desafío, deberás:

1. Crear una función que verifique si un número es primo.
2. Crear otra función que cuente la cantidad de números primos dentro de una lista dada.
3. Implementar un `main` que integre estas funciones y muestre los resultados.

Asegúrate de que tu código esté bien documentado y que las funciones sean reutilizables.

Solución del ejercicio:

Primero que nada saber que es un número primo, un número primo es un número natural mayor que 1 que solo es divisible por 1 y por si mismo, como por ejemplo son primos: 2, 3, 4, 5, 7, 11, 13.
Y para que quede más claro, una función es un bloque de código reutilizable que realiza una tarea específica. Se define con def y puede recibir valores (parámetros) y devolver resultados con return.

Ahora vamos con el paso a paso de la resolución del código, como primer paso llamamos a la función: def es_primo(n), esta función toma un número: n como entrada, luego en el segundo paso: if n < 2:
return False, acá los números menores que 2 no son primos, así que por eso devolvemos False.
en la siguiente línea: for i range(2, int(n**0.5) + 1):, aquí usamos un bucle para revisar si n se puede dividir por otros números entre 2 y la raíz cuadrada de n. Esto es más eficiente que revisar todos los números hasta n. En la siguiente línea: if n % i == 0:
return False, acá nos dice que si n se puede dividir por i sin dejar resto, no es primo, continuando en la siguiente línea: return True, acá nos dice que si el bucle termina y no se encontró ningún divisor, entonces n es primo.

Ahora pasamos a la función, entonces llamamos a la función: def contar_primos(lista):, lo que hace e stomar una lista de números y cuenta cuántos son primos, en la siguientes líneas: contador = 0
for numero in lista:
if es_primo(numero):
contador += 1, acá por cada número, usamos la función: es_primo para verificar si es primo, y si lo es, aumentamos el contador con el +=1.
en la siguiente línea: return contador, devuelve la cantidad total de números primos encontrados.

Finalmente pasando a la función main(), como primer paso llamamos a la función: def main():, esta es la función principal donde se ejecuta todo el programa, en la siguiente línea escribimos<. numeros = [2, 4, 7, 9, 13, 15, 17, 21], es decir, creamos una lista de números para analizar, continuando en la otra línea: cantidad = contar_primos(numeros), con esto llamamos a la función que cuenta primos. en la siguiente línea: print("Cantidad de números primos en la lista:", cantidad), simplemente mostramos el resultado en pantalla.

Finalmente como cuarto paso ejecutamos el main: if __name__ == "__main__":
main(), esta línea hace que la función (main) se ejecute solo si el archivo se corre directamente, no si se importa desde otro módulo.

Si el codigo esta bien debería devolvernos los 4 numeros que si son primos (2, 7, 13, 17) esto porque para que un número sea primo, no puede tener otros divisores además de 1 y él mismo. Por eso 4 no es primo, porque se puede dividir también por 2, y 15 tampoco porque se divide también por 3 y 5.