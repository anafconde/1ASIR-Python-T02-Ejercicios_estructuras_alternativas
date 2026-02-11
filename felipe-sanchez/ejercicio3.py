# Autor: Felipe
# Version: 1.0
import math
# Ejercicio 3
# Escribe un programa que lea un número e indique si es par o impar.

numero=int(input("Dame un numero: "))

par=numero%2

if par == 0 :
    print("El numero es par")
else:
    print("El numero es impar")