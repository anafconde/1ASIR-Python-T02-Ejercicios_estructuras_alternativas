# Autor: Paco Fernandez
# Version: 1.0
#Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,
# r2 de dos circunferencias y las clasifique en uno de estos estados:

import math

x1 = float(input("Introduce x1: "))
y1 = float(input("Introduce y1: "))
r1 = float(input("Introduce r1: "))

x2 = float(input("Introduce x2: "))
y2 = float(input("Introduce y2: "))
r2 = float(input("Introduce r2: "))

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if d == 0 and r1 != r2:
    print("Concéntricas")
elif d > r1 + r2:
    print("Exteriores")
elif d == r1 + r2:
    print("Tangentes exteriores")
elif abs(r1 - r2) < d < r1 + r2:
    print("Secantes")
elif d == abs(r1 - r2):
    print("Tangentes interiores")
elif d < abs(r1 - r2):
    print("Interiores")
