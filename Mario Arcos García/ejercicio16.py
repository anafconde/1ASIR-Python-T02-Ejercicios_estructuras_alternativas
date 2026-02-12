# autor: Mario Arcos
# version: 1.0
# ejercicio 16


minutos = int(input("duración de la llamada Minutos: "))
dia = input("¿Es domingo? (s/n): ")
turno = input("Turno de mañanas o tardes (m/t): ")

if minutos <= 5:
    coste = minutos * 1
elif minutos <= 8:
    coste = 5 + (minutos - 5) * 0.8
elif minutos <= 10:
    coste = 5 + 2.4 + (minutos - 8) * 0.7
else:
    coste = 5 + 2.4 + 1.4 + (minutos - 10) * 0.5

if dia == 's':
    impuesto = coste * 0.03
elif turno == 'm':
    impuesto = coste * 0.15
else:
    impuesto = coste * 0.10

print("Total a pagar:", coste + impuesto)