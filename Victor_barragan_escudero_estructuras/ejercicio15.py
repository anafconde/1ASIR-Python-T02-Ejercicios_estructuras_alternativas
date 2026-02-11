# Autora: Víctor Manuel
# Versión: 1.0
# ejercicio 15:
# El director de una escuela está organizando un viaje de estudios, 
# y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 
# 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de 
# la renta del autobús es de 4000 euros,sin importar el número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe 
# pagar cada alumno por el viaje.

print("Dime cuantos alumnos son y te digo cuanto tienen que pagar cada uno")
a= int(input("dame el numero de alumnos "))

if a >= 100:
    print("Cada alumno tendra que pagar 65€")
elif a >= 50:
    print("Cada alumno tendra que pagar 70€")
elif a >= 30:
    print("Cada alumno tendra que pagar 95€")
elif a < 30:
    print("el costo de la renta del autobús es de 4000 euros")