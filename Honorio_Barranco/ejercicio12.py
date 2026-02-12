# Autor: Honorio
# Version: 1.0
# Escribir un programa que lea un año e indique si es bisiesto.
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

anio=int(input("Introduzca un año: "))

if anio % 4 == 0 or anio % 400 == 0 :
    print("Es bisiesto")
elif anio % 100 != 0:
    print ("No es Bisiesto")