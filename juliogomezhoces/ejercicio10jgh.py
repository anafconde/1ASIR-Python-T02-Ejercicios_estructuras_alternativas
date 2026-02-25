# Autor: Julio Gómez Hoces
# Versión: 1.0
# Ejercicio 10
# No funciona
x1 = float(input("x1: "))
y1 = float(input("y1: "))
r1 = float(input("r1: "))

x2 = float(input("x2: "))
y2 = float(input("y2: "))
r2 = float(input("r2: "))

d = (x2 - x1)**2 + (y2 - y1)**2

if d == 0 and r1 == r2:
     print("Concentricas")
elif d > r1 + r2:
     print("Exteriores")
elif d == r1 + r2:
     print("Tangentes exteriores")
elif d < r1 + r2 and d > abs(r1 - r2):
     print("Secantes")
elif d == abs(r1 - r2):
     print("Tangentes interiores")
elif d < abs(r1 - r2):
     print("Interiores")