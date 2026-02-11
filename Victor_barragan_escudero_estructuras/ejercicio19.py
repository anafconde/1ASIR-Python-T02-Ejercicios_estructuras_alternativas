# Autora: Víctor Manuel
# Versión: 1.0
# ejercicio 15:
# Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
print("Calendario de meses 2026 dime un numero del 1-12 y te digo el numero de dias que tiene el mes")
a= int(input("dame el numero "))

if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print("31")
elif a == 2:
    print("28")
elif a == 4 or a == 6 or a == 9 or a == 11:
    print("30")

