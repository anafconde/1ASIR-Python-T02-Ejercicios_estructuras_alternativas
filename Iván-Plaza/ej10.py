# Autor: Iván Plaza
# Versión: 1.0
# Primeros pasos con Python

# Ejercicio 10
# Algoritmo que pida los puntos centrales x1, y1, x2, y2
# y los radios r1, r2 de dos circunferencias y las clasifique en:
# exteriores, tangentes exteriores, secantes, tangentes interiores, interiores, concéntricas

import math


x1 = float(input("Introduce x1: "))
y1 = float(input("Introduce y1: "))
r1 = float(input("Introduce r1: "))

x2 = float(input("Introduce x2: "))
y2 = float(input("Introduce y2: "))
r2 = float(input("Introduce r2: "))


centros = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


if x1 == x2 and y1 == y2:
    if r1 == r2:
        print("Concéntricas (idénticas)")
    else:
        print("Concéntricas")
else:
    suma_radios = r1 + r2
    dif_radios = abs(r1 - r2)
    
    if centros > suma_radios:
        print("Exteriores")
    elif math.isclose(centros, suma_radios):
        print("Tangentes exteriores")
    elif dif_radios < centros < suma_radios:
        print("Secantes")
    elif math.isclose(centros, dif_radios) and centros != 0:
        print("Tangentes interiores")
    elif centros < dif_radios:
        print("Interiores")

