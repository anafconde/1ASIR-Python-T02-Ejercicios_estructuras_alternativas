#Autor: Alberto Jiménez
#Version: 1.0
#Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

print ("""-----------------------CÁLCULO DE DÍAS-----------------------""")

mes = int(input("Introduce el número del mes (1-12): "))

if mes == 2:
    print("El mes",mes,"tiene 28 o 29 días.")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("El mes",mes,"tiene 30 días.")
elif 1 <= mes <= 12:
    print("El mes",mes,"tiene 31 días.")
else:
    print("Error!.El número debe estar entre 1 y 12.")