### Desafío 1 
Crea una función que tome una lista de números y devuelva la suma y el promedio de esos números.

Explicación del código:
El primero paso es guardar en una variable numeros, la lista en este caso elegí los números  [4, 8, 10], luego usamos la palabra clave def para crear la función, le vamos a poner como nombre represenativo, por ejemplo suma_y_promedio: def suma_y_promedio(lista):, esta función recibe una lista como parametro, como por ejemplo: [4, 8, 10], que es nuestro caso.
En el paso dos seria verificar que la lista no esté vacía, porque si esta vacía y tratamos de sacar promedio (dividiendo por cero), va a dar error, entonces cuando ponemos: if len(lista) == 0:
return 0, o, si no hay elementos, devolvemos 0 como suma y 0 comom promedio.
Como tercer paso: total = sum(lista): acá calculamos la suma de los elementos, es decir, usamos la función nativa de Python sum() que suma todos los elementos de una lista, por ejemplo, si la lista es [4, 8, 10], como es nuestro caso, el total va a ser 22.
Como cuarto paso: promedio = total / len(lista):  acá calculamos el promedio, el promedio es la suma dividida entre la cantidad de elementos. Para saber cuántos elementos hay, usamos len(lista), si la suma es 22 y hay 3 elementos, el promedio es 22 / 3 = 7.33.
El quinto paso: return total, promedio, aquí devolvemos los dos resultados, con return, devolvemos dos valores separados por coma y luego finalmente utilizamos los print para que nos devuelva los resultados en pantalla.