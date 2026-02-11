# Author: David García Pérez
# Version: 1.0

# Ejercicio 16
# La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura,
# de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos,
# y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %,
# y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

print("#################### Cálculo precio de llamada telefónica ######################")

duracion_llamada = int(input("Introduce la duración de la llamada: "))
dia = input("Introduce el día de la semana: ")
turno = input("Introduce el turno del día (mañana/tarde): ")

# Cálculo del coste base
if duracion_llamada <= 5:
    costo = 1
elif duracion_llamada <= 8:
    costo = 1 + (duracion_llamada - 5) * 0.80
elif duracion_llamada <= 10:
    costo = 1 + 3 * 0.80 + (duracion_llamada - 8) * 0.70
else:
    costo = 1 + 3 * 0.80 + 2 * 0.70 + (duracion_llamada - 10) * 0.50

# Cálculo del impuesto
if dia == "domingo":
    impuesto = costo * 0.03
else:
    if turno == "mañana":
        impuesto = costo * 0.15
    else:
        impuesto = costo * 0.10

total = costo + impuesto

print("Coste base de la llamada:", costo, "€")
print("Impuesto aplicado:", impuesto, "€")
print("Total a pagar:", total, "€")

print("############################################################")