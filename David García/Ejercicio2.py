# Author: David García Pérez
# Version: 1.0

# Ejercicio 2
# Algoritmo que pida un número y diga si es positivo, negativo o 0.

print("#################### Comprobar número ######################")

num = int(input("Introduce un número: "))

if num < 0:
    print("El número", num, "es negativo")
elif num > 0:
    print("El número", num, "es positivo")
else:
    print("El número", num, "es igual a 0")

print("############################################################")