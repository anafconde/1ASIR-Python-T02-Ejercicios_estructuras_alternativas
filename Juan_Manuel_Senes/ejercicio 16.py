#autor: juan manuel senes 
#version 1.0 
#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

tiempo_llamada=float(input("indicame el tiempo que ha estado en llamada"))

if tiempo_llamada <= 5:
    costo_llamada = tiempo_llamada * 1
elif tiempo_llamada <= 8:
    costo_llamada = 5 * 1 + (tiempo_llamada - 5) * 0.80
elif tiempo_llamada <= 10:
    costo_llamada = 5 * 1 + 3 * 0.80 + (tiempo_llamada - 8) * 0.70
else:
    costo_llamada = 5 * 1 + 3 * 0.80 + 2 * 0.70 + (tiempo_llamada - 10) * 0.50

total= costo_llamada +tiempo_llamada
    
print("el costo de la llamada es: ", costo_llamada)
print("el total a pagar es: ", total)