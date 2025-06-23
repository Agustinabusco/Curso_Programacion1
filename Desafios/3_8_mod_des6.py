from datetime import datetime

fecha1_str = input("Ingrese la primera fecha (DD/MM/AAAA): ")
fecha2_str = input("Ingrese la segunda fecha (DD/MM/AAAA): ")

fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")

diferencia = abs(fecha2 - fecha1)

print(f"La diferencia entre las fechas es de {diferencia.days} días.")
print("\n")