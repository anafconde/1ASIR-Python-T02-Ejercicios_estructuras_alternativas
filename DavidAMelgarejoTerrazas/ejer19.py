"""
Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
"""
mes=int(input("numero de mes(1-12): "))
if mes in [4,6,9,11]:
    print("Tiene 30 dias")
elif mes in [1,3,5,7,8,10,12]:
    print("Tiene 31 dias")
elif mes==2:
    print("Tiene 28 o 29 dias")
else:
    print("Mes no válido")