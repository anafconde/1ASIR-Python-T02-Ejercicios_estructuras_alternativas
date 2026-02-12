# Autor: Felipe
# Version: 1.0
import math
# Ejercicio 19
# Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

numero= int(input("Introduce un numero entero entre (1-12): "))

if numero < 1 or numero > 12:
    print("El valor introducido no es correcto")
elif numero == 2:

    print("El mes tiene 28 días .")
elif numero in [4, 6, 9, 11]:
    print("El mes tiene 30 días.")
else:
    print("El mes tiene 31 días.")
