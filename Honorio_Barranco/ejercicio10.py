# Autor: Honorio
# Version: 1.0
#Algoritmo que pida los puntos centrales x1, y1, x2, y2 y los radios r1, r2 de dos circunferencias y las clasifique en uno de estos estados:

#exteriores
#tangentes exteriores
#secantes
#tangentes interiores
#interiores
#concéntricas

import math

x1=int(input("Introduzca el punto x1: "))
y1=int(input("Introduzca el punto y1: "))
x2=int(input("Introduzca el punto x2: "))
y2=int(input("Introduzca el punto y2: "))
print("-----------------------------------")

r1=int(input("Introduzca el radio r1: "))
r2=int(input("Introduzca el radio r2: "))

distacia=math.sqrt((x2**2)-(x1**2)+(y2**2)-(y1**2))

print("La distancia es de", distacia)

print("########################################")

if distacia > (r1+r2):
    print("Exteriores")
elif distacia == (r1 + r2):
    print("Tangentes exteriores")
elif distacia > abs(r1 - r2) and distacia < (r1 + r2):
    print("Secantes")
elif distacia == abs(r1 - r2):
    print("Tangentes interiores")
elif distacia < abs(r1 - r2):
    print("Interiores")
elif distacia==0 :
    print("Concéntricas")
else:
    print("No es ninguno")


