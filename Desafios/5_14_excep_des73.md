Como primer paso se crea una lista original con los elementos que estan repetidos, guardados en la avriable numeros: numeros = [4, 7, 2, 7, 4, 9, 2, 10, 4]
En el segundo paso usamos set(numeros) para que convierta la lista en un conjunto, esto porque en python un conjunto no permite elementos repetidos entonces elimina los duplicaods. y list para volver a transformarlo en lista, porque se pretende usar el mismo formato.
Finalmente usar prints donde este: print("Lista original:", numeros)
muestra la lista tal cual estaba al principio, es decir, con sus elementos repetidos; y el segundo print: print("Lista sin duplicados:", sin_duplicados) va a mostrar la lista sin los elementos repetidos.
Fin del código.