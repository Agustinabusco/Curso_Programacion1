def es_palindromo(cadena):
   
    cadena = cadena.lower()
    
    cadena = cadena.replace(" ", "")
    
    return cadena == cadena[::-1]

texto = "Reconocer"
resultado = es_palindromo(texto)

print("¿Es palíndromo?", resultado)
print("\n")