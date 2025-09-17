Primeor se define la clase Nodo, igual que antes: cada nodo tiene un valor, un hijo izquierdo y un hijo derecho.
Como segundo paso se utiliza la función max_postorden, y en esta parte del codigo: if nodo is None:
    return float('-inf')
similar al anterior: caso bnase: si no hay nodo devuelve -infinito, esto permite que al comparar siempre gane cualquier número real del árbol.
Luego seguimos con el orden postorden:
- llamamos recursivamente al hijo izquierdo
- llamamos recursivamente al hijo derecho
- finalmente procesamos el nodo actual

Luego, al final, con: 
return max(max_izquierda, max_derecha, actual)
- comparamos el máximo del subárbol izquierdo, el máximo del derecho y el valor actual
y luego devolvemos el mayor de todos.

Se usa un árbol de ejemplo con los valores: 8, 3, 10, 1, 6, 14, 13. El mayor es 14. y el resultado en pantalla nos va  adecir: el valor máximo en el árbol es: 14.

#Nuevamente use recursión porque facilita el recorrido y la búsqueda.