# autor: Mario Arcos
# version: 1.0
# ejercicio 10

x1, y1, r1 = float(input("x1: ")), float(input("y1: ")), float(input("r1: "))
x2, y2, r2 = float(input("x2: ")), float(input("y2: ")), float(input("r2: "))

dist = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


if dist > r1 + r2:
    print("Son exteriores")
elif dist == r1 + r2:
    print("Tangentes exteriores")
elif dist < r1 + r2 and dist > abs(r1 - r2):
    print("Secantes")
elif dist == abs(r1 - r2):
    print("Tangentes interiores")
elif dist > 0:
    print("Interiores")
else:
    print("Concentricas")