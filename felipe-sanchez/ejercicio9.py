# Autor: Felipe
# Version: 1.0
import math
# Ejercicio 9
# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)

nume1 = int(input("Dame un numero: "))
nume2 = int(input("Dame otro numero: "))
nume3 = int(input("Dame el ultimo numero: "))

if nume1 >= nume2 and nume1 >= nume3:
    if nume2 >= nume3:
        print(nume1, nume2, nume3)
    else:
        print(nume1, nume3, nume2)


elif nume2 >= nume1 and nume2 >= nume3:
    if nume1 >= nume3:
        print(nume2, nume1, nume3)
    else:
        print(nume2, nume3, nume1)


else:
    if nume1 >= nume2:
        print(nume3, nume1, nume2)
    else:
        print(nume3, nume2, nume1)