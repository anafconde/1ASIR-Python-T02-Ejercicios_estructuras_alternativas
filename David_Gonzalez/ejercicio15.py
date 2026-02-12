# Autor: David González Mora
# versión: 1.0
# Ejercicio 15 Relación de ejercicios
# El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

alumno = int(input("Indica el número de alumnos: "))

if alumno >=100:
    precio = 65
elif alumno >=50 :
    precio = 75
elif alumno >=30 :
    precio = 95
else:
    precio = 135

total = alumno * precio + 4000

print("El precio a pagar es", total,"€")
