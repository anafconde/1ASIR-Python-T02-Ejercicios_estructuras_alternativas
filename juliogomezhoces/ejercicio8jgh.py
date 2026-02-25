# Autor: Julio Gómez Hoces
# Versión: 1.0
# Ejercicio 8
nota = float(input("Introduce  nota: "))
edad = int(input("Introduce  edad: "))
sexo = input("Introduce  sexo: ")

if nota >= 5 and edad >= 18 and sexo == "F":
    print("ACEPTADA")
elif nota >= 5 and edad >= 18 and sexo == "M":
    print("POSIBLE")
else:
    print("NO ACEPTADA")