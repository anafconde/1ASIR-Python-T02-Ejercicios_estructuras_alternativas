# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 19
# Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

mes = int(input("Introduce un numero del 1 al 12: "))

if mes < 1 or mes > 12:
    print("ERROR: numero incorrecto.")
elif mes == 1:
    print("El mes tiene 31 dias")
elif mes == 2:
    print("El mes tiene 28 dias")
elif mes == 3:
    print("El mes tiene 31 dias")
elif mes == 4:
    print("El mes tiene 30 dias")
elif mes == 5:
    print("El mes tiene 31 dias")
elif mes == 6:
    print("El mes tiene 30 dias")
elif mes == 7:
    print("El mes tiene 31 dias")
elif mes == 8:
    print("El mes tiene 31 dias")
elif mes == 9:
    print("El mes tiene 30 dias")
elif mes == 10:
    print("El mes tiene 31 dias")
elif mes == 11:
    print("El mes tiene 30 dias")
else:
    print("El mes tiene 31 dias")