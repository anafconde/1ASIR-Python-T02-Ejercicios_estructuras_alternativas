# Autor: Miguel Vilchez
# Versión: 1.0

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

# Verificación de triángulo rectángulo (Pitágoras)
es_rectangulo = (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)

if a == b == c:
    print("Es un triángulo equilátero.")
elif a == b or b == c or a == c:
    print("Es un triángulo isósceles.")
elif es_rectangulo:
    print("Es un triángulo rectángulo.")
else:
    print("Es un triángulo escaleno.")