# Autor: Julio Gómez Hoces
# Versión: 1.0
# Ejercicio 4

numero1 = int(input("Dime el primer número:"))
numero2 = int(input("Dime el primer número:"))

if numero2 <= 0:
    print("No se puede dividir entre 0")
    exit
else:
    division=numero1/numero2
    print("El resultado es:",division)