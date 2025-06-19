def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Probar la función
numero1 = 48
numero2 = 18

resultado = mcd(numero1, numero2)
print("El MCD de", numero1, "y", numero2, "es:", resultado)
print("\n")