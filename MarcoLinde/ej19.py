#Ejercicio 19
#Escribe un programa que pida un número entero entre uno y doce e imprima 
#el número de días que tiene el mes correspondiente.
mes= int(input("Introduce un número de mes (1-12): "))
dias = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
if mes in dias:
    print("El mes que has puesto tiene", dias[mes], "días")
else:
    print("El número del mes que has puesto no es correcto")
