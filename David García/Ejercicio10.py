# Author: David García Pérez
# Version: 1.0

# Ejercicio 10
# Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en uno de estos estados:

# exteriores
# tangentes exteriores
# secantes
# tangentes interiores
# interiores
# concéntricas

print("#################### Clasificación de circunferencias ######################")

import math

x1 = float(input("Introduce la medida del punto x1: "))
y1 = float(input("Introduce la medida del punto y1: "))

x2 = float(input("Introduce la medida del punto x2: "))
y2 = float(input("Introduce la medida del punto y2: "))

r1 = float(input("Introduce la medida del radio 1: "))
r2 = float(input("Introduce la medida del radio 2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if distancia > r1 + r2:
    print("Las circunferencias son exteriores")
elif distancia == r1 + r2:
    print("Las circunferencias son tangentes exteriores")
elif abs(r1 - r2) < distancia < r1 + r2:
    print("Las circunferencias son secantes")
elif distancia == abs(r1 - r2):
    print("Las circunferencias son tangentes interiores")
elif distancia < abs(r1 - r2):
    print("Las circunferencias son interiores")
elif distancia == 0 and r1 == r2:
    print("Las circunferencias son concéntricas")

print("############################################################")