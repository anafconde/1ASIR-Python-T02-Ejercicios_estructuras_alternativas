# Autor: David González Mora
# versión: 1.0
# Ejercicio 13 Relación de ejercicios
# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = int(input("Indica el día: "))
mes = int(input("Indica el mes: "))
año = int(input("Indica el año: "))

if dia >= 1 and dia <= 31:
    print("Es valido")
elif mes >= 1 and mes <= 12:
    print("Es valido")
else:
    print("No es valido")
