#Ejercicio 13
#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
dia= int(input("Pon un día: "))
mes= int(input("Pon un mes: "))
año= int(input("Pon un año: "))
fecha= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (año %4==0 and año %100!= 0) or (año %400==0):
    fecha[1]= 29
if 1<=mes<=12 and 1<=dia<=fecha[mes-1]:
    print("La fecha es correcta")
else:
    print("La fecha no es correcta, vuelve a intentarlo")
