# Autor: Julio Gómez Hoces
# Versión: 1.1
# Ejercicio 16
minutos = int(input("Introduce los minutos de la llamada: "))
dia = input("Introduce el día: ")

costo = 0

if minutos <= 5:
    costo = minutos * 1
elif minutos <= 8:
    costo = 5 * 1 + (minutos - 5) * 0.80
elif minutos <= 10:
    costo = 5 * 1 + 3 * 0.80 + (minutos - 8) * 0.70
else:
    costo = 5 * 1 + 3 * 0.80 + 2 * 0.70 + (minutos - 10) * 0.50


if dia == "domingo":
    impuesto = costo * 0.03
else:
    turno = input("Introduce el turno: ")
    if turno == "mañana":
        impuesto = costo * 0.15
    else:
        impuesto = costo * 0.10

total = costo + impuesto

print("Costo de la llamada:", costo, "€")
print("Impuesto:",impuesto, "€")
print("Total a pagar:",total,  "€")
