# Autor: Iván Plaza
# Version: 1.0
# Primeros pasos con Python 

#Ejercicio 16
#  La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, 
#  de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos,
#  70 céntimos, y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día,
#  en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto
#  una persona que realiza una llamada.



duracion = int(input("Ingrese la duración de la llamada en minutos: "))
dia = input("Ingrese el día de la semana: ").lower()

if dia != "domingo":
    turno = input("Ingrese el turno (mañana/tarde): ").lower()


costo = 0
minutos_restantes = duracion


primeros = min(minutos_restantes, 5)
costo += 1  # tarifa fija
minutos_restantes -= primeros


if minutos_restantes > 0:
    siguiente = min(minutos_restantes, 3)
    costo += siguiente * 0.80
    minutos_restantes -= siguiente


if minutos_restantes > 0:
    siguiente = min(minutos_restantes, 2)
    costo += siguiente * 0.70
    minutos_restantes -= siguiente


if minutos_restantes > 0:
    costo += minutos_restantes * 0.50


if dia == "domingo":
    impuesto = costo * 0.03
else:
    if turno == "mañana":
        impuesto = costo * 0.15
    else:
        impuesto = costo * 0.10


total = costo + impuesto


print(f"Costo base: {costo:.2f} €")
print(f"Impuesto: {impuesto:.2f} €")
print(f"Total a pagar: {total:.2f} €")