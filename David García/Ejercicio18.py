# Author: David García Pérez
# Version: 1.0

# Ejercicio 18
# Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.

print("#################### Comprobar día de la semana ######################")

dia = int(input("Introduce el día de la semana (1-7): "))

if dia == 1:
    print("El día", dia, "corresponde a Lunes")
elif dia == 2:
    print("El día", dia, "corresponde a Martes")
elif dia == 3:
    print("El día", dia, "corresponde a Miércoles")
elif dia == 4:
    print("El día", dia, "corresponde a Jueves")
elif dia == 5:
    print("El día", dia, "corresponde a Viernes")
elif dia == 6:
    print("El día", dia, "corresponde a Sábado")
elif dia == 7:
    print("El día", dia, "corresponde a Domingo")
else:
    print("Error. El día introducido es incorrecto")

print("############################################################")