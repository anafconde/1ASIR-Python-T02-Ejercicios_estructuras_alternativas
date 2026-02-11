# Autor: Honorio
# Version: 1.0
#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, 
# de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 
# 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 
# 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde,
# 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

tiempo=float(input("Ingresa el tiempo de llamada: "))
dia = input("Ingrese el día de la semana: ")

costo=0

if tiempo<=5:
    costo=1
else:
    costo=1
    tiempo -= 5

    if tiempo <= 3:
        costo += tiempo * 0.80
    else:
        costo += 3 * 0.80
        tiempo -= 3

        if tiempo <= 2:
            costo += tiempo * 0.70
        else:
            costo += 2 * 0.70
            tiempo -= 2
            costo += tiempo * 0.50
if dia == "domingo":
    impuesto=costo * 0.03
else:
    turno=input("Introduzca el turno (mañana o tarde): ")

    if turno == "mañana":
        impuesto=costo * 0.15
    elif turno == "tarde":
        impuesto=costo * 0.10
total=costo + impuesto

print("-----Cobro telefonico-----")
print("Costo base: ",costo)
print("Impuesto:",impuesto)
print("Total a pagar:",total)




    