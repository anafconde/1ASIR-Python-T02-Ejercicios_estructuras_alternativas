# Autor: Julio Gómez Hoces
# Versión: 1.0
# Ejercicio 12
año = int(input("Dime un año: "))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print("Es bisiesto")
        else:
            print("No es bisiesto")
    else:
        print("Es bisiesto")
else:
    print("No es bisiessto")