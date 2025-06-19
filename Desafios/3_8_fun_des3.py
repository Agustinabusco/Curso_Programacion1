def tienen_elemento_en_comun(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False

lista_1 = [1, 2, 3, 4]
lista_2 = [5, 6, 3]

print(tienen_elemento_en_comun(lista_1, lista_2))  
print("\n")