class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def construir_arbol(expresion):
    # Quitar espacios
    tokens = expresion.replace(" ", "")
    
    # Separar en lista de números y operadores
    elementos = []
    num = ""
    for c in tokens:
        if c.isdigit():
            num += c
        else:
            if num:
                elementos.append(num)
                num = ""
            elementos.append(c)
    if num:
        elementos.append(num)
    
    # Precedencia de operadores
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    # Convertir a notación postfija (Shunting Yard)
    salida = []
    operadores = []
    
    for token in elementos:
        if token.isdigit():  # es número
            salida.append(token)
        else:  # es operador
            while (operadores and 
                   operadores[-1] in precedencia and 
                   precedencia[operadores[-1]] >= precedencia[token]):
                salida.append(operadores.pop())
            operadores.append(token)
    
    while operadores:
        salida.append(operadores.pop())
    
    # Construir árbol desde notación postfija
    pila = []
    for token in salida:
        if token.isdigit():
            pila.append(Nodo(int(token)))
        else:
            nodo = Nodo(token)
            nodo.derecha = pila.pop()
            nodo.izquierda = pila.pop()
            pila.append(nodo)
    
    return pila[0]  # raíz del árbol


def evaluar_arbol(nodo):
    if isinstance(nodo.valor, int):  # es número
        return nodo.valor
    
    izq = evaluar_arbol(nodo.izquierda)
    der = evaluar_arbol(nodo.derecha)
    
    if nodo.valor == '+':
        return izq + der
    elif nodo.valor == '-':
        return izq - der
    elif nodo.valor == '*':
        return izq * der
    elif nodo.valor == '/':
        return izq / der


if __name__ == "__main__":
    expresion = "5 + 3 * 4"
    arbol = construir_arbol(expresion)
    resultado = evaluar_arbol(arbol)
    print("Expresión:", expresion)
    print("Resultado:", resultado)

