# Autora: Víctor Manuel
# Versión: 1.0
# ejercicio 13:
# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

from datetime import date
hoy = date.today()
hoy_d= hoy.day
hoy_m= hoy.month
hoy_a= hoy.year

print("Introduzca el dia , mes y año de hoy")
d= int(input("Introduzca el dia "))
m= int(input("Introduzca el mes "))
a= int(input("Introduca el anyo "))

if d < hoy_d or d > hoy_d:
    print("fecha incorrecta")
elif m < hoy_m or m > hoy_m:
    print("fecha incorrecta")  
elif a < hoy_a or a > hoy_a:
    print("fecha incorrecta")
else:
    print ("Exacto hoy es " ,d,"-",m,"-",a)