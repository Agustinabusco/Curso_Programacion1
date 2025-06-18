# Función para verificar si un número es primo
def es_primo(n):
    """
    Devuelve True si n es un número primo, False en caso contrario.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Solo se verifica hasta la raíz cuadrada de n
        if n % i == 0:
            return False
    return True

# Función para contar cuántos números primos hay en una lista
def contar_primos(lista):
    """
    Cuenta y devuelve cuántos números primos hay en la lista.
    """
    contador = 0
    for numero in lista:
        if es_primo(numero):
            contador += 1
    return contador

# Función principal (main)
def main():
    """
    Función principal que ejecuta el programa.
    """
    numeros = [2, 4, 7, 9, 13, 15, 17, 21]
    print("Lista de números:", numeros)

    # Contamos cuántos son primos
    cantidad = contar_primos(numeros)

    print("Cantidad de números primos en la lista:", cantidad)

# Ejecutar el main
if __name__ == "__main__":
    main()
print("\n")