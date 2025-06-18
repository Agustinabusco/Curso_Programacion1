numeros = [4, 8, 10]

def suma_y_promedio(lista):
    if len(lista) == 0:
        return 0, 0  
    
    total = sum(lista)         
    promedio = total / len(lista)  
    return total, promedio

suma, promedio = suma_y_promedio(numeros)

print("La suma es:", suma)
print("El promedio es:", promedio)

