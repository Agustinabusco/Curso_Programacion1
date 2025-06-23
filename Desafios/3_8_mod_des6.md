### Desafío 6

Calculadora de Fechas
Objetivo:
Escribir un programa en Python que permita calcular la diferencia entre dos fechas, utilizando el módulo `datetime.`

Solución del ejercicio: 

Como primer paso en la primera línea escribibimos: from datetime import datetime, con esto importamos solo la clase -datetime- desde el módulo -datetime-, lo que nos va a permitir trabajar con fechas y horas completas.
luego, en las líneas 4 y 5, con: fecha1_str = input("Ingrese la primera fecha (DD/MM/AAAA): ")
fecha2_str = input("Ingrese la segunda fecha (DD/MM/AAAA): "), aca le pedimos al usuario que escriba dos fechas como texto, ejemplo la fecha actual, 22/06/2025 y otra, paras ber la diferencia de dias exactas. el formato "DD/MM/AAAA" ésto porque es mas familiar para nosotros que el formato inglés.
Luego en las lineas 8 y 9, usamos: fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y"), con strotime() convierte un string a un objto datetime, desglosando el formato "%d/%m/%Y", donde: 
-%:dia
-%m:mes
-%Y año con 4 cifras
por esto, ahora fecga1 y fecha 2 son fechas reales que Python puede comparar. 
en la línea 12: diferencia = abs(fecha2 - fecha1), acá restamos las dos fechas, el resultado es un objeto tipo -timedelta-, que tiene propiedad -.days- para saber cuántos días hay de diferencia, y usamos (abs()) para que no importe el orden en que ingresás las fechas, siempre da positivo.
finalmente en la linea 15: print(f"La diferencia entre las fechas es de {diferencia.days} días."), aca mostramos el resultado en pantalla, acceediendo a .days.
